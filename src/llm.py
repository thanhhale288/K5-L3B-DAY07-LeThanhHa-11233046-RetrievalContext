"""LLM provider layer for the Day 7 agent (OpenAI-compatible chat + tool calling).

Providers are configured in PROVIDERS; DeepSeek is the default. Select with
LLM_PROVIDER in `.env`. Keys are read only from the environment / `.env` and
never logged. No mock fallback: a missing key or API error raises.

Smoke test (makes one real, cheap API call):
    .venv/bin/python src/llm.py --ping
"""
from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class ProviderSpec:
    key_env: str
    base_url_env: str
    default_base_url: str
    model_env: str
    default_model: str


PROVIDERS: dict[str, ProviderSpec] = {
    # https://api-docs.deepseek.com — OpenAI-compatible; deepseek-chat supports tool calling.
    'deepseek': ProviderSpec('DEEPSEEK_API_KEY', 'DEEPSEEK_BASE_URL', 'https://api.deepseek.com',
                             'DEEPSEEK_MODEL', 'deepseek-chat'),
    'openai': ProviderSpec('OPENAI_API_KEY', 'OPENAI_BASE_URL', 'https://api.openai.com/v1',
                           'OPENAI_MODEL', 'gpt-4o-mini'),
    'openrouter': ProviderSpec('OPENROUTER_API_KEY', 'OPENROUTER_BASE_URL', 'https://openrouter.ai/api/v1',
                               'OPENROUTER_MODEL', 'deepseek/deepseek-chat'),
}


def load_env(path: Path = ROOT / '.env') -> None:
    """Minimal .env loader (no dependency); existing env vars win."""
    if not path.exists():
        return
    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def _price(name: str) -> float | None:
    raw = os.environ.get(name, '').strip()
    return float(raw) if raw else None


class ChatProvider:
    """Thin wrapper: one chat completion per call, returns message + usage + latency + cost."""

    def __init__(self, provider: str | None = None, *, model: str | None = None,
                 temperature: float = 0.0, timeout: float = 60.0, client: Any = None) -> None:
        load_env()
        self.provider = (provider or os.environ.get('LLM_PROVIDER') or 'deepseek').strip().lower()
        if self.provider not in PROVIDERS:
            raise ValueError(f'LLM_PROVIDER không hỗ trợ: {self.provider!r} (chọn {sorted(PROVIDERS)})')
        spec = PROVIDERS[self.provider]
        self.model = model or os.environ.get(spec.model_env) or spec.default_model
        self.base_url = os.environ.get(spec.base_url_env) or spec.default_base_url
        self.temperature = temperature
        # Optional USD per 1M tokens, so cost is reported only when you set real prices.
        prefix = self.provider.upper()
        self.price_in = _price(f'{prefix}_PRICE_INPUT_PER_M')
        self.price_out = _price(f'{prefix}_PRICE_OUTPUT_PER_M')
        if client is not None:
            self.client = client
            return
        api_key = os.environ.get(spec.key_env, '').strip()
        if not api_key:
            raise RuntimeError(f'Thiếu {spec.key_env} trong .env (provider={self.provider})')
        from openai import OpenAI
        self.client = OpenAI(api_key=api_key, base_url=self.base_url, timeout=timeout)

    def complete(self, messages: list[dict[str, Any]], tools: list[dict[str, Any]] | None = None,
                 tool_choice: str | None = None) -> dict[str, Any]:
        """Return {'content', 'tool_calls': [{id, name, arguments(dict)}], 'raw_message', 'usage', 'latency_ms', 'cost_usd'}."""
        kwargs: dict[str, Any] = {'model': self.model, 'messages': messages, 'temperature': self.temperature}
        if tools:
            kwargs['tools'] = tools
            if tool_choice:
                kwargs['tool_choice'] = tool_choice
        start = time.perf_counter()
        resp = self.client.chat.completions.create(**kwargs)
        latency_ms = (time.perf_counter() - start) * 1000
        msg = resp.choices[0].message
        tool_calls = []
        for tc in msg.tool_calls or []:
            try:
                args = json.loads(tc.function.arguments or '{}')
            except json.JSONDecodeError as exc:
                raise ValueError(f'Model trả arguments không phải JSON: {tc.function.arguments!r}') from exc
            tool_calls.append({'id': tc.id, 'name': tc.function.name, 'arguments': args})
        usage = {'prompt_tokens': getattr(resp.usage, 'prompt_tokens', 0) or 0,
                 'completion_tokens': getattr(resp.usage, 'completion_tokens', 0) or 0}
        cost = None
        if self.price_in is not None and self.price_out is not None:
            cost = (usage['prompt_tokens'] * self.price_in + usage['completion_tokens'] * self.price_out) / 1e6
        # Assistant message in a form that can be appended back to `messages` for the next turn.
        raw_message: dict[str, Any] = {'role': 'assistant', 'content': msg.content or ''}
        if msg.tool_calls:
            raw_message['tool_calls'] = [{'id': tc.id, 'type': 'function',
                                          'function': {'name': tc.function.name, 'arguments': tc.function.arguments}}
                                         for tc in msg.tool_calls]
        return {'content': msg.content or '', 'tool_calls': tool_calls, 'raw_message': raw_message,
                'usage': usage, 'latency_ms': latency_ms, 'cost_usd': cost,
                'model': getattr(resp, 'model', self.model), 'provider': self.provider}


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description='Kiểm tra kết nối LLM provider')
    parser.add_argument('--ping', action='store_true', help='Gọi API thật một lần với tool calling')
    parser.add_argument('--provider', default=None)
    args = parser.parse_args()
    llm = ChatProvider(args.provider)
    print(f'provider={llm.provider} model={llm.model} base_url={llm.base_url}')
    if not args.ping:
        return
    tool = {'type': 'function', 'function': {
        'name': 'search', 'description': 'Search the document store.',
        'parameters': {'type': 'object', 'properties': {'query': {'type': 'string'}}, 'required': ['query']}}}
    out = llm.complete([{'role': 'user', 'content': 'Gọi tool search với query "Net Zero FPT".'}],
                       tools=[tool], tool_choice='auto')
    print(json.dumps({k: out[k] for k in ('tool_calls', 'content', 'usage', 'latency_ms', 'cost_usd', 'model')},
                     ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
