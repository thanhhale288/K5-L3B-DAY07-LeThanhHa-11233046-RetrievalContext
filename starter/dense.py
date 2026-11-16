"""Dense retrieval against the Day 6 pgvector index (same embedding model)."""

from __future__ import annotations

import argparse
import json
import logging
import os
import statistics
import time
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from baseline import hit, pack_context, validate
from day6_store import Day6PgVectorStore
from embeddings import MyEmbedder

logger = logging.getLogger(__name__)

STARTER_DIR = Path(__file__).resolve().parent


class DenseRetriever:
    """Retriever.search adapter for agentic.run_agent."""

    def __init__(
        self,
        store: Day6PgVectorStore,
        embedder: MyEmbedder,
        *,
        strategy: str = "B",
    ) -> None:
        self.store = store
        self.embedder = embedder
        self.strategy = strategy

    def search(
        self,
        query: str,
        *,
        filters: dict[str, Any] | None,
        top_k: int,
    ) -> list[dict[str, Any]]:
        vector = self.embedder.embed_query(query)
        return self.store.search(
            strategy=self.strategy,
            query_vector=vector,
            top_k=top_k,
            filters=filters,
        )


def _filters_for_question(question: dict[str, Any]) -> dict[str, Any] | None:
    filt = question.get("filter")
    if not filt:
        return None
    if not isinstance(filt, dict):
        raise ValueError(f"filter must be a JSON object, got {filt!r}")
    return dict(filt)


def evaluate_dense(
    retriever: DenseRetriever,
    questions: list[dict[str, Any]],
    *,
    top_k: int = 3,
    budget: int = 800,
) -> list[dict[str, Any]]:
    traces: list[dict[str, Any]] = []
    for q in questions:
        start = time.perf_counter()
        filters = _filters_for_question(q)
        results = retriever.search(q["question"], filters=filters, top_k=top_k)
        context, ids = pack_context(results, budget=budget)
        elapsed_ms = (time.perf_counter() - start) * 1000
        marked = [{**c, "hit": hit(c, q["gold"])} for c in results]
        traces.append(
            {
                "query_id": q["id"],
                "split": q["split"],
                "question": q["question"],
                "strategy": "dense",
                "day6_strategy": retriever.strategy,
                "top_k": top_k,
                "budget_chars": budget,
                "applied_filter": filters,
                "gold": q["gold"],
                "results": marked,
                "context": context,
                "context_ids": ids,
                "context_chars": len(context),
                "elapsed_ms": elapsed_ms,
                "hit1": bool(marked and marked[0]["hit"]),
                "hit3": any(c["hit"] for c in marked),
                "context_hit": any(c["hit"] and c["id"] in ids for c in marked),
            }
        )
    return traces


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%H:%M:%S",
    )
    load_dotenv(STARTER_DIR / ".env")

    parser = argparse.ArgumentParser(
        description="Dense retrieval eval on Day 6 pgvector index"
    )
    parser.add_argument("--chunks", required=True, type=Path)
    parser.add_argument("--questions", required=True, type=Path)
    parser.add_argument("--split", required=True, choices=("dev", "test"))
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--strategy",
        default=os.getenv("DAY6_STRATEGY") or "B",
        help="Day 6 strategy column: A | B | C (default B)",
    )
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--budget", type=int, default=800)
    args = parser.parse_args()

    chunks = json.loads(args.chunks.read_text(encoding="utf-8"))
    questions = json.loads(args.questions.read_text(encoding="utf-8"))
    selected = [q for q in questions if q.get("split") == args.split]
    # Dense eval only scores answerable questions with gold evidence.
    selected = [q for q in selected if q.get("answerable", True) is not False]
    validate(chunks, selected)

    embedder = MyEmbedder(local_files_only=True)
    store = Day6PgVectorStore(dimensions=embedder.dimensions)
    n = store.count(args.strategy)
    if n <= 0:
        raise RuntimeError(
            f"No chunks for strategy={args.strategy}. Re-run Day 6 ingestion first."
        )
    logger.info("Day 6 store strategy=%s rows=%s", args.strategy, n)

    retriever = DenseRetriever(store, embedder, strategy=args.strategy)
    traces = evaluate_dense(
        retriever, selected, top_k=args.top_k, budget=args.budget
    )
    summary = {
        "strategy": "dense",
        "day6_strategy": args.strategy,
        "embedding_model": embedder.model_name,
        "embedding_dimensions": embedder.dimensions,
        "split": args.split,
        "n": len(traces),
        "hit1": sum(t["hit1"] for t in traces),
        "hit3": sum(t["hit3"] for t in traces),
        "context_hit": sum(t["context_hit"] for t in traces),
        "avg_context_chars": statistics.mean(t["context_chars"] for t in traces)
        if traces
        else 0,
        "median_ms": statistics.median(t["elapsed_ms"] for t in traces)
        if traces
        else 0,
        "store_rows": n,
    }
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "traces.json").write_text(
        json.dumps(traces, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (args.output / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
