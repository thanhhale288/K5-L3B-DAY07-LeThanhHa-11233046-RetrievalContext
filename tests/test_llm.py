"""Provider wiring checks with a fake client; never used for benchmark numbers."""
import os
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from llm import ChatProvider  # noqa: E402


def fake_client(tool_calls=None, content=''):
    msg = SimpleNamespace(content=content, tool_calls=tool_calls)
    resp = SimpleNamespace(choices=[SimpleNamespace(message=msg)], model='deepseek-chat',
                           usage=SimpleNamespace(prompt_tokens=100, completion_tokens=20))
    create = mock.Mock(return_value=resp)
    return SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create))), create


class ChatProviderTests(unittest.TestCase):
    def test_missing_key_raises(self):
        with mock.patch.dict(os.environ, {'DEEPSEEK_API_KEY': ''}, clear=False), \
                mock.patch('llm.load_env'):
            with self.assertRaises(RuntimeError):
                ChatProvider('deepseek')

    def test_unknown_provider(self):
        with self.assertRaises(ValueError):
            ChatProvider('nope', client=object())

    def test_parses_tool_call_and_cost(self):
        tc = SimpleNamespace(id='c1', function=SimpleNamespace(name='search', arguments='{"query": "net zero"}'))
        client, create = fake_client([tc])
        with mock.patch.dict(os.environ, {'DEEPSEEK_PRICE_INPUT_PER_M': '1', 'DEEPSEEK_PRICE_OUTPUT_PER_M': '2'}):
            llm = ChatProvider('deepseek', client=client)
        out = llm.complete([{'role': 'user', 'content': 'x'}], tools=[{'type': 'function'}])
        self.assertEqual(out['tool_calls'], [{'id': 'c1', 'name': 'search', 'arguments': {'query': 'net zero'}}])
        self.assertAlmostEqual(out['cost_usd'], (100 * 1 + 20 * 2) / 1e6)
        self.assertEqual(out['raw_message']['tool_calls'][0]['function']['name'], 'search')
        self.assertEqual(create.call_args.kwargs['temperature'], 0.0)

    def test_cost_none_without_prices(self):
        client, _ = fake_client(content='hi')
        with mock.patch.dict(os.environ, {'DEEPSEEK_PRICE_INPUT_PER_M': '', 'DEEPSEEK_PRICE_OUTPUT_PER_M': ''}):
            out = ChatProvider('deepseek', client=client).complete([{'role': 'user', 'content': 'x'}])
        self.assertIsNone(out['cost_usd'])
        self.assertEqual(out['tool_calls'], [])


if __name__ == '__main__':
    unittest.main()
