"""Run the real LLM agent on one split and save traces for review + starter/agent_metrics.py.

    .venv/bin/python src/run_agent_eval.py --split dev --method bm25 --top-k 3 --budget 3200 \
        --max-searches 3 --output starter/results/agent-dev-bm25

Only {id, question, filter} reach the agent. Gold is used afterwards for the automatic
Context Evidence Rate only. Answer quality, citation support and abstention correctness
must be labelled by hand in reviews.json (a template is written next to the traces).
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
import time
import traceback
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'starter'))
sys.path.insert(0, str(ROOT / 'src'))
from agentic import run_agent  # noqa: E402
from baseline import hit  # noqa: E402
from agent import LLMController  # noqa: E402
from evaluate_retrieval import DATA, build  # noqa: E402


def load_cases(split: str) -> list[dict]:
    answerable = [q for q in json.loads((DATA / 'questions.json').read_text(encoding='utf-8')) if q['split'] == split]
    unanswerable = [u for u in json.loads((DATA / 'unanswerable.json').read_text(encoding='utf-8')) if u['split'] == split]
    return ([{**q, 'answerable': True} for q in answerable] + [{**u, 'answerable': False} for u in unanswerable])


def main() -> None:
    parser = argparse.ArgumentParser(description='Chạy agent thật trên một split')
    parser.add_argument('--split', required=True, choices=('dev', 'test'))
    parser.add_argument('--method', default='bm25')
    parser.add_argument('--top-k', type=int, default=3)
    parser.add_argument('--budget', type=int, default=3200)
    parser.add_argument('--max-searches', type=int, default=3)
    parser.add_argument('--fix-citations', action='store_true',
                        help='Cải thiện 2: chèn [id] cho citation model đã khai báo nhưng quên ghi trong câu trả lời')
    parser.add_argument('--ids', default='', help='Chỉ chạy các ID này (phân tách bằng dấu phẩy), để thử nhanh')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()

    chunks = json.loads((DATA / 'chunks.json').read_text(encoding='utf-8'))
    retriever = build([args.method], chunks)[args.method]
    controller = LLMController(max_searches=args.max_searches, fix_citation_markers=args.fix_citations)
    cases = load_cases(args.split)
    if args.ids:
        wanted = {i.strip() for i in args.ids.split(',')}
        cases = [c for c in cases if c['id'] in wanted]

    config = {'split': args.split, 'method': retriever.name, 'top_k': args.top_k, 'budget_chars': args.budget,
              'max_searches': args.max_searches, 'fix_citations': args.fix_citations, 'provider': controller.llm.provider,
              'model_requested': controller.llm.model, 'temperature': controller.llm.temperature}
    traces = []
    for case in cases:
        controller.reset()
        filters = case.get('filter')  # user-provided field only
        start = time.perf_counter()
        try:
            out = run_agent(case['question'], controller, retriever, filters=filters,
                            max_searches=args.max_searches, top_k=args.top_k, budget=args.budget)
            error = None
        except Exception as exc:  # recorded, never replaced with a fake answer
            out = {'status': 'error', 'answer': None, 'citations': [], 'events': []}
            error = f'{type(exc).__name__}: {exc}\n{traceback.format_exc(limit=3)}'
        elapsed = time.perf_counter() - start
        searches = [e for e in out['events'] if e['event'] == 'search']
        final_ids = searches[-1]['context_ids'] if searches else []
        usage = Counter()
        for c in controller.calls:
            usage.update(c['usage'])
        costs = [c['cost_usd'] for c in controller.calls]
        trace = {
            'query_id': case['id'], 'split': case['split'], 'answerable': case['answerable'],
            'question': case['question'], 'filter': filters, 'config': config,
            'status': out['status'], 'answer': out['answer'], 'citations': out['citations'],
            'events': out['events'], 'llm_calls': controller.calls, 'error': error,
            'n_searches': len(searches), 'n_llm_calls': len(controller.calls),
            'tokens': dict(usage), 'cost_usd': sum(costs) if costs and None not in costs else None,
            'latency_s': elapsed, 'models': sorted({c['model'] for c in controller.calls}),
            'final_context_ids': final_ids,
        }
        if case['answerable']:  # evaluation only, after the run
            by_id = {r['id']: r for e in searches for r in e['results']}
            trace['auto_context_hit'] = any(hit(by_id[i], case['gold']) for i in final_ids if i in by_id)
        traces.append(trace)
        print(f"{case['id']:4s} {out['status']:8s} searches={len(searches)} {elapsed:5.1f}s  "
              f"{(out['answer'] or error or '')[:90]!r}")

    ok = [t for t in traces if t['status'] != 'error']
    ans = [t for t in ok if t['answerable']]
    una = [t for t in ok if not t['answerable']]
    costs = [t['cost_usd'] for t in traces]
    summary = {
        **config, 'cases': len(traces), 'status': dict(Counter(t['status'] for t in traces)),
        'errors': len(traces) - len(ok),
        'tool_use': f"{sum(t['n_searches'] > 0 for t in ok)}/{len(ok)}",
        'searches_distribution': dict(sorted(Counter(t['n_searches'] for t in ok).items())),
        'auto_context_evidence_rate': f"{sum(t['auto_context_hit'] for t in ans)}/{len(ans)}",
        'auto_answered_on_answerable': f"{sum(t['status'] == 'answered' for t in ans)}/{len(ans)}",
        'auto_abstained_on_unanswerable': f"{sum(t['status'] == 'abstain' for t in una)}/{len(una)}",
        'tokens_total': dict(sum((Counter(t['tokens']) for t in traces), Counter())),
        'cost_usd_total': sum(costs) if costs and None not in costs else None,
        'latency_s_median': statistics.median(t['latency_s'] for t in traces) if traces else None,
        'note': 'auto_* counts come from status/gold only; grounded answer, citation support and abstention need human labels in reviews.json.',
    }
    reviews = [{'query_id': t['query_id'], 'answerable': t['answerable'], 'status': t['status'],
                'question': t['question'], 'answer': t['answer'], 'citations': t['citations'],
                'answer_grade': None,
                'citation_support': [None] * len(t['citations']),
                'abstention_correct': None, 'note': ''}
               for t in traces if t['status'] != 'error']
    args.output.mkdir(parents=True, exist_ok=True)
    for name, obj in (('traces.json', traces), ('summary.json', summary), ('reviews_template.json', reviews)):
        (args.output / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
