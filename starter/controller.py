"""Controllers for agentic.run_agent — heuristic (offline) or OpenAI-compatible LLM."""

from __future__ import annotations

import json
import os
import re
from typing import Any


class HeuristicController:
    """Deterministic offline controller for smoke tests without an LLM API key.

    First call → search with the user question.
    Later calls → answer from context IDs if present, else abstain-shaped answer
    (run_agent still validates citations against retrieved chunks).
    """

    def decide(self, question: str, history: list[dict[str, Any]]) -> dict[str, Any]:
        if not history:
            return {"action": "search", "query": question.strip()}

        context = history[-1].get("context") or ""
        context_ids = history[-1].get("context_ids") or []
        if not context_ids or not context.strip():
            return {
                "action": "answer",
                "answer": "Không đủ bằng chứng để trả lời.",
                "citations": [],
            }

        cid = context_ids[0]
        # Pull a short snippet after the header line for a grounded-looking answer.
        block = context.split("\n\n")[0]
        lines = block.split("\n", 1)
        snippet = (lines[1] if len(lines) > 1 else block).strip()
        snippet = re.sub(r"\s+", " ", snippet)[:240]
        answer = f"{snippet} [{cid}]"
        return {"action": "answer", "answer": answer, "citations": [cid]}


class OpenAICompatibleController:
    """Tool-calling controller via OpenAI / OpenRouter (requires API key)."""

    def __init__(
        self,
        *,
        model: str | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
    ) -> None:
        try:
            from openai import OpenAI
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError(
                "Install openai package to use OpenAICompatibleController"
            ) from exc

        api_key = (
            api_key
            or os.getenv("OPENROUTER_API_KEY")
            or os.getenv("OPENAI_API_KEY")
        )
        if not api_key:
            raise ValueError(
                "Set OPENROUTER_API_KEY or OPENAI_API_KEY for the LLM controller"
            )

        base_url = base_url or os.getenv("OPENAI_BASE_URL")
        if not base_url and os.getenv("OPENROUTER_API_KEY"):
            base_url = "https://openrouter.ai/api/v1"

        self.model = model or os.getenv("LLM_MODEL") or "openai/gpt-4o-mini"
        self.client = OpenAI(api_key=api_key, base_url=base_url) if base_url else OpenAI(api_key=api_key)
        self.tools = [
            {
                "type": "function",
                "function": {
                    "name": "search",
                    "description": "Search the document corpus for evidence.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Search query in natural language",
                            }
                        },
                        "required": ["query"],
                    },
                },
            }
        ]

    def decide(self, question: str, history: list[dict[str, Any]]) -> dict[str, Any]:
        system = (
            "You are a grounded RAG agent. Use the search tool to find evidence. "
            "When answering, cite chunk IDs that appear in the provided context using "
            "[chunk-id] in the answer text and list them in citations. "
            "If evidence is insufficient, still return action=answer with an empty "
            "citations list so the harness can abstain."
        )
        user_parts = [f"Question: {question}"]
        if history:
            last = history[-1]
            user_parts.append(f"Context IDs: {last.get('context_ids')}")
            user_parts.append(f"Context:\n{last.get('context')}")
            user_parts.append(f"Prior search queries: {last.get('queries')}")
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": "\n\n".join(user_parts)},
        ]

        # Prefer tool call when we have no context yet; allow free-form JSON otherwise.
        kwargs: dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "tools": self.tools,
        }
        if not history:
            kwargs["tool_choice"] = {"type": "function", "function": {"name": "search"}}
        else:
            kwargs["response_format"] = {"type": "json_object"}
            messages[0]["content"] += (
                ' Reply JSON: {"action":"search","query":"..."} or '
                '{"action":"answer","answer":"... [id]","citations":["id"]}.'
            )

        resp = self.client.chat.completions.create(**kwargs)
        msg = resp.choices[0].message
        if msg.tool_calls:
            call = msg.tool_calls[0]
            args = json.loads(call.function.arguments or "{}")
            query = args.get("query") or question
            return {"action": "search", "query": query}

        content = msg.content or "{}"
        data = json.loads(content)
        if data.get("action") == "search":
            return {"action": "search", "query": data.get("query") or question}
        return {
            "action": "answer",
            "answer": data.get("answer") or "Không đủ bằng chứng để trả lời.",
            "citations": list(data.get("citations") or []),
        }


def build_controller() -> HeuristicController | OpenAICompatibleController:
    """Prefer LLM when a key is present; otherwise heuristic for local boots."""
    if os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY"):
        return OpenAICompatibleController()
    return HeuristicController()
