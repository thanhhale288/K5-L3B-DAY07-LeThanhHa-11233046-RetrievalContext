"""Hybrid retrieval: dense (Day 6) + TF-IDF lexical, fused with RRF."""

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

from baseline import TfidfIndex, hit, pack_context, validate
from day6_store import Day6PgVectorStore
from dense import DenseRetriever
from embeddings import MyEmbedder

logger = logging.getLogger(__name__)
STARTER_DIR = Path(__file__).resolve().parent


def rrf_fuse(
    ranked_lists: list[list[dict[str, Any]]],
    *,
    k: int = 60,
    top_k: int = 3,
) -> list[dict[str, Any]]:
    """Reciprocal Rank Fusion over multiple ranked result lists."""
    scores: dict[str, float] = {}
    by_id: dict[str, dict[str, Any]] = {}
    for results in ranked_lists:
        for rank, item in enumerate(results, start=1):
            cid = item["id"]
            scores[cid] = scores.get(cid, 0.0) + 1.0 / (k + rank)
            if cid not in by_id:
                by_id[cid] = dict(item)
    fused = []
    for cid, score in sorted(scores.items(), key=lambda kv: (-kv[1], kv[0])):
        row = dict(by_id[cid])
        row["score"] = score
        row["strategy"] = "hybrid_rrf"
        fused.append(row)
        if len(fused) >= top_k:
            break
    return fused


class HybridRetriever:
    def __init__(
        self,
        dense: DenseRetriever,
        lexical: TfidfIndex,
        *,
        candidate_k: int = 10,
    ) -> None:
        self.dense = dense
        self.lexical = lexical
        self.candidate_k = candidate_k

    def search(
        self,
        query: str,
        *,
        filters: dict[str, Any] | None,
        top_k: int,
    ) -> list[dict[str, Any]]:
        dense_hits = self.dense.search(
            query, filters=filters, top_k=max(top_k, self.candidate_k)
        )
        # Lexical baseline has no metadata filter; fuse after dense filtering.
        lexical_hits = self.lexical.search(query, top_k=max(top_k, self.candidate_k))
        return rrf_fuse([dense_hits, lexical_hits], top_k=top_k)


def _filters_for_question(question: dict[str, Any]) -> dict[str, Any] | None:
    filt = question.get("filter")
    return dict(filt) if isinstance(filt, dict) else None


def evaluate_hybrid(
    retriever: HybridRetriever,
    questions: list[dict[str, Any]],
    *,
    top_k: int = 3,
    budget: int = 800,
) -> list[dict[str, Any]]:
    traces = []
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
                "strategy": "hybrid_rrf",
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
    parser = argparse.ArgumentParser(description="Hybrid RRF dense+TF-IDF retrieval")
    parser.add_argument("--chunks", required=True, type=Path)
    parser.add_argument("--questions", required=True, type=Path)
    parser.add_argument("--split", required=True, choices=("dev", "test"))
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--strategy", default=os.getenv("DAY6_STRATEGY") or "B")
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--budget", type=int, default=800)
    args = parser.parse_args()

    chunks = json.loads(args.chunks.read_text(encoding="utf-8"))
    questions = json.loads(args.questions.read_text(encoding="utf-8"))
    selected = [
        q
        for q in questions
        if q.get("split") == args.split and q.get("answerable", True) is not False
    ]
    validate(chunks, selected)

    embedder = MyEmbedder(local_files_only=True)
    store = Day6PgVectorStore(dimensions=embedder.dimensions)
    dense = DenseRetriever(store, embedder, strategy=args.strategy)
    lexical = TfidfIndex(chunks)
    retriever = HybridRetriever(dense, lexical)

    traces = evaluate_hybrid(
        retriever, selected, top_k=args.top_k, budget=args.budget
    )
    summary = {
        "strategy": "hybrid_rrf",
        "day6_strategy": args.strategy,
        "embedding_model": embedder.model_name,
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
