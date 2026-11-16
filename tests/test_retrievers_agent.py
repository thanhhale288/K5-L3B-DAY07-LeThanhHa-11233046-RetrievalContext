"""Code checks for src/retrievers.py and src/agent.py with fakes; not benchmark results."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'starter'))
sys.path.insert(0, str(ROOT / 'src'))
from agentic import run_agent  # noqa: E402
from agent import LLMController  # noqa: E402
from retrievers import BM25Retriever, HybridRetriever, tokenize_vi  # noqa: E402


def chunk(id, text, pillar='Social', page=1):
    return {'id': id, 'source_id': 'doc', 'source': 'doc.pdf', 'page': page, 'text': text,
            'metadata': {'pillar': pillar}}


CHUNKS = [chunk('c1', 'Tỷ lệ lao động nữ đạt 37,7%.'),
          chunk('c2', 'Mục tiêu Net Zero vào năm 2040.', 'Environment', 7),
          chunk('c3', 'Điện mặt trời mái nhà tại Đà Nẵng.', 'Environment', 12)]


class FakeRetriever:
    def __init__(self, name, ids):
        self.name, self.ids = name, ids

    def search(self, query, *, filters=None, top_k=3):
        return [{**next(c for c in CHUNKS if c['id'] == i), 'score': 1.0, 'rank': r + 1}
                for r, i in enumerate(self.ids[:top_k])]


class FakeLLM:
    provider, model, temperature = 'fake', 'fake', 0.0

    def __init__(self, replies):
        self.replies = list(replies)

    def complete(self, messages, tools=None, tool_choice=None):
        tool_calls, content = self.replies.pop(0)
        return {'tool_calls': tool_calls, 'content': content, 'usage': {'prompt_tokens': 1, 'completion_tokens': 1},
                'latency_ms': 0.0, 'cost_usd': None, 'model': 'fake'}


class RetrieverTests(unittest.TestCase):
    def test_tokenize_bigrams(self):
        self.assertIn('lao_động', tokenize_vi('Lao động nữ', bigrams=True))
        self.assertEqual(tokenize_vi('Lao động'), ['lao', 'động'])

    def test_bm25_rank_and_filter(self):
        bm25 = BM25Retriever(CHUNKS)
        self.assertEqual(bm25.search('Net Zero năm nào', top_k=1)[0]['id'], 'c2')
        res = bm25.search('lao động nữ', filters={'pillar': 'Environment'}, top_k=3)
        self.assertNotIn('c1', [r['id'] for r in res])
        with self.assertRaises(ValueError):
            bm25.search('x', filters={'gold': 1})

    def test_rrf_fusion(self):
        hybrid = HybridRetriever([FakeRetriever('a', ['c1', 'c2']), FakeRetriever('b', ['c2', 'c3'])], k=60)
        res = hybrid.search('q', top_k=3)
        self.assertEqual(res[0]['id'], 'c2')  # in both lists
        self.assertEqual(set(res[0]['components']), {'a', 'b'})
        self.assertEqual([r['rank'] for r in res], [1, 2, 3])


class ControllerTests(unittest.TestCase):
    def test_search_then_cited_answer(self):
        llm = FakeLLM([
            ([{'id': '1', 'name': 'search', 'arguments': {'query': 'Net Zero'}}], ''),
            ([{'id': '2', 'name': 'answer', 'arguments': {'answer': 'Năm 2040 [c2]', 'citations': ['c2']}}], ''),
        ])
        ctrl = LLMController(llm, max_searches=2)
        out = run_agent('Net Zero năm nào?', ctrl, FakeRetriever('f', ['c2']), max_searches=2, budget=2000)
        self.assertEqual(out['status'], 'answered')
        self.assertEqual(out['citations'], ['c2'])
        self.assertEqual(len(ctrl.calls), 2)

    def test_empty_citations_abstain(self):
        llm = FakeLLM([
            ([{'id': '1', 'name': 'search', 'arguments': {'query': 'doanh thu'}}], ''),
            ([{'id': '2', 'name': 'answer', 'arguments': {'answer': 'Không đủ bằng chứng để trả lời.', 'citations': []}}], ''),
        ])
        out = run_agent('Doanh thu?', LLMController(llm), FakeRetriever('f', ['c1']), budget=2000)
        self.assertEqual(out['status'], 'abstain')

    def test_missing_markers_rejected_without_fix_and_repaired_with_fix(self):
        def replies():
            return [([{'id': '1', 'name': 'search', 'arguments': {'query': 'Net Zero'}}], ''),
                    ([{'id': '2', 'name': 'answer', 'arguments': {'answer': 'Năm 2040.', 'citations': ['c2']}}], '')]
        base = run_agent('q', LLMController(FakeLLM(replies())), FakeRetriever('f', ['c2']), budget=2000)
        self.assertEqual(base['status'], 'abstain')
        ctrl = LLMController(FakeLLM(replies()), fix_citation_markers=True)
        fixed = run_agent('q', ctrl, FakeRetriever('f', ['c2']), budget=2000)
        self.assertEqual(fixed['status'], 'answered')
        self.assertEqual(fixed['answer'], 'Năm 2040. [c2]')
        self.assertEqual(ctrl.calls[-1]['citation_markers_added'], ['c2'])

    def test_fix_does_not_validate_ids_outside_context(self):
        llm = FakeLLM([([{'id': '1', 'name': 'search', 'arguments': {'query': 'x'}}], ''),
                       ([{'id': '2', 'name': 'answer', 'arguments': {'answer': 'Bịa.', 'citations': ['c9']}}], '')])
        out = run_agent('q', LLMController(llm, fix_citation_markers=True), FakeRetriever('f', ['c2']), budget=2000)
        self.assertEqual(out['status'], 'abstain')

    def test_plain_text_answer_parses_citations(self):
        llm = FakeLLM([([], 'Năm 2040 [c2].')])
        action = LLMController(llm).decide('q', [{'queries': ['x'], 'context': '...', 'context_ids': ['c2']}])
        self.assertEqual(action, {'action': 'answer', 'answer': 'Năm 2040 [c2].', 'citations': ['c2']})


if __name__ == '__main__':
    unittest.main()
