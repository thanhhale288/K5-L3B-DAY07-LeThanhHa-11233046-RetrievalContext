"""Compare retrieval methods on one split with identical corpus, questions, labels and cutoffs.

    .venv/bin/python src/evaluate_retrieval.py --split dev --methods dense,bm25,hybrid \
        --top-k 3 --budget 800 --output starter/results/retrieval-dev

Metrics (answerable questions only, BENCHMARK.md §2):
  Hit@1, Evidence Hit@3 (always from the top-3), MRR@top_k, Context Evidence Rate
  (a gold-hit chunk survives pack_context into the final context), latency.
Only `question` and the user-provided `filter` reach the retriever; gold is used after retrieval to score.
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'starter'))
sys.path.insert(0, str(ROOT / 'src'))
from baseline import hit, pack_context, validate  # noqa: E402
from retrievers import BM25Retriever, DenseRetriever, HybridRetriever, timed_search  # noqa: E402

DATA = ROOT / 'starter/data/converted'


def build(methods: list[str], chunks: list[dict]) -> dict:
    """Lazily build only the requested retrievers; the dense model loads once and is shared."""
    cache: dict = {}

    def get(name: str):
        if name not in cache:
            if name == 'dense':
                cache[name] = DenseRetriever()
            elif name == 'bm25':
                cache[name] = BM25Retriever(chunks)
            elif name == 'bm25+bigram':
                cache[name] = BM25Retriever(chunks, bigrams=True)
            elif name == 'hybrid':
                cache[name] = HybridRetriever([get('dense'), get('bm25')])
            elif name == 'hybrid+bigram':
                cache[name] = HybridRetriever([get('dense'), get('bm25+bigram')])
            else:
                raise ValueError(f'method không hỗ trợ: {name}')
        return cache[name]

    return {m: get(m) for m in methods}


def evaluate(retriever, questions: list[dict], *, top_k: int, budget: int, use_filter: bool) -> tuple[list, dict]:
    traces = []
    for q in questions:
        filters = q.get('filter') if use_filter else None
        results, ms = timed_search(retriever, q['question'], filters=filters, top_k=max(top_k, 3))
        top3 = results[:3]
        used = results[:top_k]
        context, ids = pack_context(used, budget=budget)
        flags = [hit(c, q['gold']) for c in used]
        first = next((i + 1 for i, f in enumerate(flags) if f), None)
        traces.append({
            'query_id': q['id'], 'split': q['split'], 'question': q['question'], 'filter': filters,
            'method': retriever.name, 'top_k': top_k, 'budget_chars': budget,
            'results': [{k: v for k, v in {**c, 'hit': f}.items() if k != 'text'} | {'text_preview': c['text'][:160]}
                        for c, f in zip(used, flags)],
            'context_ids': ids, 'context_chars': len(context),
            'hit1': bool(top3 and hit(top3[0], q['gold'])),
            'hit3': any(hit(c, q['gold']) for c in top3),
            'first_hit_rank': first,
            'context_hit': any(f and c['id'] in ids for c, f in zip(used, flags)),
            'latency_ms': ms, 'gold': q['gold'],
        })
    n = len(traces)
    summary = {'method': retriever.name, 'n': n, 'top_k': top_k, 'budget_chars': budget, 'use_filter': use_filter,
               'hit1': sum(t['hit1'] for t in traces), 'hit3': sum(t['hit3'] for t in traces),
               'context_hit': sum(t['context_hit'] for t in traces),
               'mrr': sum(1 / t['first_hit_rank'] for t in traces if t['first_hit_rank']) / n,
               'avg_context_chars': statistics.mean(t['context_chars'] for t in traces),
               'avg_context_chunks': statistics.mean(len(t['context_ids']) for t in traces),
               'median_latency_ms': statistics.median(t['latency_ms'] for t in traces),
               'cost_usd': 0.0}
    return traces, summary


def table(summaries: list[dict]) -> str:
    lines = ['| Method | Hit@1 | Evidence Hit@3 | MRR | Context Evidence Rate | Avg context (chars / chunks) | Median latency |',
             '|---|---|---|---|---|---|---|']
    for s in summaries:
        n = s['n']
        lines.append(f"| {s['method']} | {s['hit1']}/{n} ({s['hit1']/n:.0%}) | {s['hit3']}/{n} ({s['hit3']/n:.0%}) | "
                     f"{s['mrr']:.3f} | {s['context_hit']}/{n} ({s['context_hit']/n:.0%}) | "
                     f"{s['avg_context_chars']:.0f} / {s['avg_context_chunks']:.1f} | {s['median_latency_ms']:.1f} ms |")
    return '\n'.join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description='So sánh các phương pháp retrieval trên một split')
    parser.add_argument('--split', required=True, choices=('dev', 'test'))
    parser.add_argument('--methods', default='dense,bm25,hybrid')
    parser.add_argument('--top-k', type=int, default=3)
    parser.add_argument('--budget', type=int, default=800, help='Context budget (ký tự, gồm header nguồn)')
    parser.add_argument('--no-filter', action='store_true', help='Bỏ filter do người dùng cung cấp')
    parser.add_argument('--chunks', type=Path, default=DATA / 'chunks.json')
    parser.add_argument('--questions', type=Path, default=DATA / 'questions.json')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()

    chunks = json.loads(args.chunks.read_text(encoding='utf-8'))
    questions = [q for q in json.loads(args.questions.read_text(encoding='utf-8')) if q['split'] == args.split]
    validate(chunks, questions)
    methods = [m.strip() for m in args.methods.split(',') if m.strip()]
    retrievers = build(methods, chunks)

    args.output.mkdir(parents=True, exist_ok=True)
    summaries = []
    for name, retriever in retrievers.items():
        traces, summary = evaluate(retriever, questions, top_k=args.top_k, budget=args.budget,
                                   use_filter=not args.no_filter)
        summaries.append(summary)
        safe = name.replace('+', '_').replace('(', '_').replace(')', '')
        (args.output / f'traces_{safe}.json').write_text(json.dumps(traces, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (args.output / 'summary.json').write_text(json.dumps({'split': args.split, 'methods': summaries}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    md = table(summaries)
    (args.output / 'summary.md').write_text(md + '\n', encoding='utf-8')
    print(md)


if __name__ == '__main__':
    main()
