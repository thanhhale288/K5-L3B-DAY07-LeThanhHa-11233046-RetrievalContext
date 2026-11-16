"""CLI to run the Day 7 agent loop against the Day 6 dense retriever."""

from __future__ import annotations

import argparse
import json
import logging
import os
from pathlib import Path

from dotenv import load_dotenv

from agentic import run_agent
from controller import build_controller
from day6_store import Day6PgVectorStore
from dense import DenseRetriever
from embeddings import MyEmbedder

logger = logging.getLogger(__name__)
STARTER_DIR = Path(__file__).resolve().parent


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
    load_dotenv(STARTER_DIR / ".env")

    parser = argparse.ArgumentParser(description="Run Day 7 agent on one question")
    parser.add_argument("--question", required=True)
    parser.add_argument("--strategy", default=os.getenv("DAY6_STRATEGY") or "B")
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--max-searches", type=int, default=4)
    # Day 6 strategy-B chunks are up to ~800 chars; headers need headroom.
    parser.add_argument("--budget", type=int, default=2400)
    parser.add_argument("--filter-pillar", default=None)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    embedder = MyEmbedder(local_files_only=True)
    store = Day6PgVectorStore(dimensions=embedder.dimensions)
    retriever = DenseRetriever(store, embedder, strategy=args.strategy)
    controller = build_controller()
    filters = {"pillar": args.filter_pillar} if args.filter_pillar else None

    result = run_agent(
        args.question,
        controller,
        retriever,
        filters=filters,
        max_searches=args.max_searches,
        top_k=args.top_k,
        budget=args.budget,
    )
    result["query"] = args.question
    result["controller"] = type(controller).__name__
    result["day6_strategy"] = args.strategy
    text = json.dumps(result, ensure_ascii=False, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
