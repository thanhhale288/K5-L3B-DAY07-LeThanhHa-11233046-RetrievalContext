"""Check what the advanced index captured, against values read by hand from the original pages.

    .venv/bin/python src/adv_check_index.py

For every answerable benchmark question it looks at the gold pages and reports which hand-read
values (numbers, names in `evidence[].content`) appear in (a) the text/table chunks and (b) the vision
chunks of those pages. This is an offline audit of extraction coverage only: it is never used by the
retriever or the agent, and it does not replace reading the page images.
"""
from __future__ import annotations

import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADV = ROOT / 'advanced'


def norm(s: str) -> str:
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFC', s)).lower()


def tokens(content: str) -> list[str]:
    """Numbers with Vietnamese separators (e.g. 19.507, 27,8) are the checkable atoms."""
    return sorted(set(re.findall(r'\d[\d.]*(?:,\d+)?', content)) - {'0', '1', '2', '3', '4', '5'})


def main() -> None:
    chunks = json.loads((ADV / 'index/chunks.json').read_text(encoding='utf-8'))
    by_page = defaultdict(lambda: {'textual': '', 'visual': ''})
    for c in chunks:
        key = 'visual' if c['metadata']['kind'] == 'visual' else 'textual'
        by_page[c['page']][key] += ' ' + norm(c['text'])
    bench = json.loads((ADV / 'benchmark/benchmark.json').read_text(encoding='utf-8'))['questions']
    rows, tot = [], defaultdict(int)
    for q in bench:
        for ev in q.get('evidence', []):
            toks = tokens(ev['content'])
            if not toks:
                continue
            page = by_page[ev['page']]
            in_text = [t for t in toks if t in page['textual']]
            in_vis = [t for t in toks if t in page['visual']]
            either = set(in_text) | set(in_vis)
            tot['values'] += len(toks)
            tot['text'] += len(in_text)
            tot['visual'] += len(in_vis)
            tot['either'] += len(either)
            rows.append({'id': q['id'], 'group': q['group'], 'page': ev['page'], 'kind': ev['kind'], 'values': len(toks),
                         'in_text_layer': len(in_text), 'in_vision': len(in_vis),
                         'missing_everywhere': sorted(set(toks) - either)})
    report = {'evidence_values_checked': tot['values'], 'found_in_text_layer': tot['text'], 'found_in_vision_chunks': tot['visual'],
              'found_in_either': tot['either'], 'rows': rows}
    (ADV / 'index/coverage_check.json').write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')
    print({k: v for k, v in report.items() if k != 'rows'})
    for r in rows:
        if r['missing_everywhere'] or r['in_vision'] < r['values']:
            print(r)


if __name__ == '__main__':
    main()
