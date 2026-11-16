"""Build a pass/fail review sheet + empty labels.json for one advanced run, and score filled labels.

    .venv/bin/python src/adv_review_sheet.py advanced/results/test-<config>            # sheet + labels.json (never overwritten)
    .venv/bin/python src/adv_review_sheet.py advanced/results/test-<config> --score    # metrics.json from labels.json

Pass rule (ADVANCED.md §3): answerable → correct and complete (units, conditions, calculation),
citations locate the needed page/region and actually support the whole answer; partial, wrong
citation or abstention = fail. Unanswerable → abstains without unsupported claims. Errors = fail.
Labels are written after comparing with the original page images, not the extracted text.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADV = ROOT / 'advanced'
GROUPS = ['table', 'image', 'chart', 'multihop', 'text', 'unanswerable']


def sheet(run: Path) -> None:
    traces = json.loads((run / 'traces.json').read_text(encoding='utf-8'))
    bench = {q['id']: q for q in json.loads((ADV / 'benchmark/benchmark.json').read_text(encoding='utf-8'))['questions']}
    chunks = {c['id']: c for c in json.loads((ADV / 'index/chunks.json').read_text(encoding='utf-8'))}
    lines = [f'# Bảng chấm đạt/không đạt: `{run.name}`', '', f"Cấu hình: `{traces[0]['config']}`", '']
    for t in traces:
        q = bench[t['query_id']]
        lines += [f"## {t['query_id']} · {q['group']} · status `{t['status']}`", '', f"**Câu hỏi:** {q['question']}", '']
        if q['answerable']:
            lines.append(f"**Đáp án chuẩn:** {q['expected_answer']}")
            for ev in q['evidence']:
                lines.append(f"- Evidence gốc trang {ev['page']} ({ev['kind']}; {ev['locator']}): {ev['content']}")
            if q.get('calculation'):
                lines.append(f"- Phép tính: {q['calculation']}")
        else:
            lines.append(f"**Hành vi mong đợi:** tìm rồi từ chối. Kiểm tra trong tài liệu: {q['absence_check']}")
        tools = [f"search({e['query']!r})" if e['event'] == 'search' else f"view_page({e['page']})" for e in t['events'] if e['event'] in ('search', 'view_page')]
        lines += ['', f"**Tool:** {' → '.join(tools)}", '', f"**Câu trả lời:** {t['answer']}", '', '**Citation:**']
        views = {e['id']: e for e in t['events'] if e['event'] == 'view_page'}
        for cid in t['citations']:
            if cid in views:
                lines.append(f"- `{cid}` (ảnh trang {views[cid]['page']}, quan sát của vision model): {views[cid]['observation'][:1200]}")
            elif cid in chunks:
                c = chunks[cid]
                lines.append(f"- `{cid}` (trang {c['page']}, {c['metadata']['kind']}): {c['text'][:1200]}")
        if not t['citations']:
            lines.append('- (không có)')
        lines += ['', f"Gợi ý tự động: trang gold {t['auto_hint']['gold_pages']}, trang được trích {t['cited_pages']}", '', '---', '']
    (run / 'review_sheet.md').write_text('\n'.join(lines), encoding='utf-8')
    out = run / 'labels.json'
    if not out.exists():
        out.write_text(json.dumps([{'query_id': t['query_id'], 'group': bench[t['query_id']]['group'], 'pass': None, 'reason': ''} for t in traces],
                                  ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'wrote {run / "review_sheet.md"} (labels.json kept if it existed)')


def score(run: Path) -> None:
    labels = json.loads((run / 'labels.json').read_text(encoding='utf-8'))
    traces = {t['query_id']: t for t in json.loads((run / 'traces.json').read_text(encoding='utf-8'))}
    if any(l['pass'] is None for l in labels):
        raise SystemExit('labels.json còn câu chưa chấm')
    by = defaultdict(lambda: [0, 0])
    for l in labels:
        by[l['group']][0] += bool(l['pass'])
        by[l['group']][1] += 1
    n, N = sum(v[0] for v in by.values()), len(labels)
    ts = list(traces.values())
    metrics = {'pass': n, 'total': N, 'pass_rate': round(100 * n / N, 2), 'meets_90pct': n * 10 >= 9 * N,
               'by_group': {g: {'pass': by[g][0], 'total': by[g][1], 'rate': round(100 * by[g][0] / by[g][1], 1)} for g in GROUPS if g in by},
               'errors': sum(t['status'] == 'error' for t in ts),
               'tokens_total': {k: sum(t['tokens'][k] for t in ts) for k in ('prompt_tokens', 'completion_tokens')},
               'cost_usd_total': None if any(t['cost_usd'] is None for t in ts) else round(sum(t['cost_usd'] for t in ts), 6),
               'latency_s_total': round(sum(t['latency_s'] for t in ts), 1),
               'tool_calls': {k: sum(t['tool_counts'][k] for t in ts) for k in ('search', 'view_page')}}
    (run / 'metrics.json').write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(metrics, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    run = Path(sys.argv[1])
    score(run) if '--score' in sys.argv else sheet(run)
