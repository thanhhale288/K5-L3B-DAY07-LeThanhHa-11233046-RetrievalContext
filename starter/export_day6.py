"""Export Day 6 chunks from pgvector + convert Day 6 benchmark questions to Day 7 JSON."""

from __future__ import annotations

import argparse
import json
import logging
import os
from pathlib import Path

from dotenv import load_dotenv

from convert_day6 import convert_question
from day6_store import Day6PgVectorStore

logger = logging.getLogger(__name__)
STARTER_DIR = Path(__file__).resolve().parent

# Day 7 needs abstention cases Day 6 did not include. Kept out of questions.json
# (retrieval Hit metrics) and written to agent_cases.json for agent evaluation.
ABSTENTION_CASES = [
    {
        "id": "abs01",
        "split": "dev",
        "question": "FPT công bố giá cổ phiếu đóng cửa ngày 31/12/2025 trên sàn HOSE là bao nhiêu?",
        "answerable": False,
        "expected_behavior": "search_and_abstain",
        "absence_reason": "Báo cáo ESG không chứa bảng giá cổ phiếu / dữ liệu thị trường chứng khoán.",
    },
    {
        "id": "abs02",
        "split": "dev",
        "question": "Chi phí marketing sản phẩm FPT Shop quý IV/2025 là bao nhiêu tỷ đồng?",
        "answerable": False,
        "expected_behavior": "search_and_abstain",
        "absence_reason": "Không có số liệu marketing / FPT Shop trong báo cáo ESG.",
    },
    {
        "id": "abs03",
        "split": "test",
        "question": "FPT dự kiến mở bao nhiêu cửa hàng điện thoại mới tại châu Âu năm 2026?",
        "answerable": False,
        "expected_behavior": "search_and_abstain",
        "absence_reason": "Kế hoạch retail châu Âu không nằm trong báo cáo ESG 2025.",
    },
    {
        "id": "abs04",
        "split": "test",
        "question": "Ai là HLV trưởng đội bóng đá FPT năm 2025?",
        "answerable": False,
        "expected_behavior": "search_and_abstain",
        "absence_reason": "Không có nội dung thể thao / bóng đá trong corpus ESG.",
    },
]


def _default_day6_repo() -> Path | None:
    env = os.getenv("DAY6_REPO")
    if env:
        return Path(env)
    sibling = (
        STARTER_DIR.parents[1]
        / "k5-l3b-day06-lethanhha-2a202603901-dataingestion"
    )
    if sibling.is_dir():
        return sibling
    return None


def _load_day6_questions(path: Path) -> list[dict]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    questions = raw["questions"] if isinstance(raw, dict) else raw
    if not isinstance(questions, list):
        raise ValueError(f"Unexpected benchmark shape in {path}")
    return [convert_question(q) for q in questions]


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
    load_dotenv(STARTER_DIR / ".env")

    parser = argparse.ArgumentParser(description="Export Day 6 artifacts for Day 7")
    parser.add_argument(
        "--strategy",
        default=None,
        help="Single Day 6 strategy to export (A/B/C). Ignored if --strategies is set.",
    )
    parser.add_argument(
        "--strategies",
        default=None,
        help=(
            "Comma-separated strategies to union into chunks.json "
            "(default: A,B so long gold quotes still validate)."
        ),
    )
    parser.add_argument(
        "--day6-benchmark",
        type=Path,
        default=None,
        help="Path to Day 6 data/benchmark.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=STARTER_DIR / "data" / "converted",
    )
    parser.add_argument(
        "--dimensions",
        type=int,
        default=1024,
        help="Embedding dimensions of the Day 6 index (bge-m3 = 1024)",
    )
    parser.add_argument(
        "--include-abstention",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Append Day 7 abstention stubs (default: true)",
    )
    args = parser.parse_args()

    day6_repo = _default_day6_repo()
    benchmark = args.day6_benchmark
    if benchmark is None:
        if day6_repo is None:
            raise SystemExit(
                "Pass --day6-benchmark or set DAY6_REPO to the Day 6 checkout."
            )
        benchmark = day6_repo / "data" / "benchmark.json"
    if not benchmark.is_file():
        raise FileNotFoundError(f"Day 6 benchmark not found: {benchmark}")

    store = Day6PgVectorStore(dimensions=args.dimensions)
    if args.strategies:
        strategy_list = [s.strip() for s in args.strategies.split(",") if s.strip()]
    elif args.strategy:
        strategy_list = [args.strategy]
    else:
        strategy_list = ["A", "B"]

    by_id: dict[str, dict] = {}
    for strategy in strategy_list:
        for chunk in store.export_chunks(strategy):
            meta = dict(chunk.get("metadata") or {})
            meta.setdefault("day6_strategy", strategy)
            chunk = {**chunk, "metadata": meta}
            by_id.setdefault(chunk["id"], chunk)
    chunks = list(by_id.values())
    if not chunks:
        raise RuntimeError(
            f"No chunks exported for strategies={strategy_list}. "
            "Run Day 6 ingestion first."
        )

    questions = _load_day6_questions(benchmark)
    agent_cases = [
        {
            "id": q["id"],
            "split": q["split"],
            "question": q["question"],
            "answerable": True,
            "expected_behavior": "search_and_answer",
        }
        for q in questions
    ]
    if args.include_abstention:
        agent_cases = agent_cases + ABSTENTION_CASES

    args.output.mkdir(parents=True, exist_ok=True)
    chunks_path = args.output / "chunks.json"
    questions_path = args.output / "questions.json"
    cases_path = args.output / "agent_cases.json"
    meta_path = args.output / "export_meta.json"

    chunks_path.write_text(
        json.dumps(chunks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    # questions.json = answerable only (safe for baseline.validate / Hit metrics)
    questions_path.write_text(
        json.dumps(questions, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    cases_path.write_text(
        json.dumps(agent_cases, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    meta = {
        "strategies_exported": strategy_list,
        "dense_search_strategy": os.getenv("DAY6_STRATEGY") or "B",
        "n_chunks": len(chunks),
        "n_questions": len(questions),
        "n_agent_cases": len(agent_cases),
        "n_abstention": sum(1 for c in agent_cases if c.get("answerable") is False),
        "day6_benchmark": str(benchmark),
        "note": (
            "chunks.json may union strategies for gold coverage / TF-IDF; "
            "dense.py still searches DAY6_STRATEGY (default B) in pgvector. "
            "questions.json is answerable-only; agent_cases.json adds abstention stubs."
        ),
    }
    meta_path.write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    logger.info(
        "Exported %s chunks + %s questions + %s agent cases → %s",
        len(chunks),
        len(questions),
        len(agent_cases),
        args.output,
    )
    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
