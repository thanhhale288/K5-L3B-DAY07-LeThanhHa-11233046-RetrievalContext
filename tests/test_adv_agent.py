"""Advanced agent loop with a fake LLM and a fake retriever (no network, no model)."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from adv_agent import ABSTAIN, Agent  # noqa: E402


class FakeLLM:
    def __init__(self, script):
        self.script = list(script)

    def complete(self, messages, tools=None, tool_choice=None):
        name, args = self.script.pop(0)
        tc = [{'id': f'c{len(messages)}', 'name': name, 'arguments': args}]
        raw = {'role': 'assistant', 'content': '', 'tool_calls': [{'id': tc[0]['id'], 'type': 'function', 'function': {'name': name, 'arguments': '{}'}}]}
        return {'content': '', 'tool_calls': tc, 'raw_message': raw, 'usage': {'prompt_tokens': 1, 'completion_tokens': 1},
                'latency_ms': 1.0, 'cost_usd': 0.0, 'model': 'fake'}


class FakeRetriever:
    def search(self, query, *, filters=None, top_k=5):
        return [{'id': 'ar_p11_v2', 'page': 11, 'text': 'ROA 2024 14,4%', 'metadata': {'kind': 'visual', 'visual_type': 'chart'},
                 'score': 1.0, 'rank': 1}]


class AdvAgentTests(unittest.TestCase):
    def run_agent(self, script):
        return Agent(FakeRetriever(), view_page=False, llm=FakeLLM(script)).run('ROA cao nhất?')

    def test_answer_with_valid_citation(self):
        r = self.run_agent([('search', {'query': 'ROA'}), ('answer', {'answer': '2024, 14,4% [ar_p11_v2]', 'citations': ['ar_p11_v2']})])
        self.assertEqual(r['status'], 'answered')
        self.assertEqual(r['cited_pages'], [11])

    def test_citation_outside_context_abstains(self):
        r = self.run_agent([('search', {'query': 'ROA'}), ('answer', {'answer': 'x [ar_p99_t0]', 'citations': ['ar_p99_t0']})])
        self.assertEqual(r['status'], 'abstain')

    def test_abstain_text_with_citations_is_abstention(self):
        r = self.run_agent([('search', {'query': 'ROA'}), ('answer', {'answer': ABSTAIN + ' Chỉ có ROA.', 'citations': ['ar_p11_v2']})])
        self.assertEqual(r['status'], 'abstain')
        self.assertEqual(r['citations'], [])
        self.assertEqual(r['abstain_support'], ['ar_p11_v2'])

    def test_step_limit_abstains(self):
        r = Agent(FakeRetriever(), view_page=False, max_steps=2, llm=FakeLLM([('search', {'query': 'a'})] * 2)).run('q')
        self.assertEqual(r['status'], 'abstain')
        self.assertEqual(r['events'][-1]['reason'], 'max_steps')


if __name__ == '__main__':
    unittest.main()
