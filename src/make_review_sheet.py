"""Build a human review sheet (Markdown) + an empty reviews.json for one agent run.

    .venv/bin/python src/make_review_sheet.py starter/results/agent-test-chosen-bm25-fixcite

The sheet puts the question, expected answer, gold evidence, the agent's answer and the
full text of every cited chunk side by side. It writes NO labels: a person fills
reviews.json (answer_grade 0/1/2, citation_support per citation, abstention_correct,
context_grade 0/1/2) after reading. Never overwrites an existing reviews.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'starter'))
from baseline import norm_ws  # noqa: E402

DATA = ROOT / 'starter/data/converted'

GUIDE = """## Cách chấm (BENCHMARK.md)

- `answer_grade` (câu có đáp án): 0 = sai hoặc không có evidence; 1 = đúng một phần; 2 = đúng và đủ. Câu bị từ chối chấm 0.
- `citation_support`: mỗi citation một giá trị `true`/`false`, theo thứ tự. `true` chỉ khi đoạn được trích thật sự hỗ trợ câu trả lời.
- `abstention_correct` (câu thiếu bằng chứng): `true` nếu agent từ chối và không thêm khẳng định thiếu căn cứ.
- `context_grade` (câu có đáp án): 0 = context không có evidence; 1 = có nhưng thiếu điều kiện hoặc nguồn; 2 = đủ evidence và nguồn.
- Ghi lý do ngắn vào `note`. Không dựa vào cột "gợi ý tự động": cột đó chỉ so chuỗi và có thể sai.
"""


def main() -> None:
    run = Path(sys.argv[1])
    traces = json.loads((run / 'traces.json').read_text(encoding='utf-8'))
    questions = {q['id']: q for q in json.loads((DATA / 'questions.json').read_text(encoding='utf-8'))}
    unanswerable = {u['id']: u for u in json.loads((DATA / 'unanswerable.json').read_text(encoding='utf-8'))}
    chunks = {c['id']: c for c in json.loads((DATA / 'chunks.json').read_text(encoding='utf-8'))}

    cfg = traces[0]['config']
    lines = [f'# Bảng chấm: `{run.name}`', '',
             f"Cấu hình: method `{cfg['method']}`, top-k {cfg['top_k']}, budget {cfg['budget_chars']}, "
             f"max searches {cfg['max_searches']}, fix citations `{cfg.get('fix_citations', False)}`, "
             f"model `{', '.join(sorted({m for t in traces for m in t['models']}))}`.", '', GUIDE]
    for t in traces:
        qid = t['query_id']
        lines += [f"## {qid} · {'có đáp án' if t['answerable'] else 'thiếu bằng chứng'} · status `{t['status']}`", '',
                  f"**Câu hỏi:** {t['question']}", '']
        if t['answerable']:
            q = questions[qid]
            lines.append(f"**Đáp án chuẩn:** {q['expected_answer']}")
            for g in q['gold']:
                lines.append(f"**Evidence gold (trang {g['page']}):** “{g['evidence']}”")
            lines.append(f"**Gợi ý tự động:** evidence gold có trong context cuối = `{t.get('auto_context_hit')}`")
        else:
            lines.append(f"**Hành vi mong đợi:** tìm rồi từ chối. Lý do thiếu: {unanswerable[qid]['absence_reason']}")
        queries = [e['query'] for e in t['events'] if e['event'] == 'search']
        lines += ['', f"**Các query agent dùng:** {queries}", '', f"**Câu trả lời của agent:** {t['answer']}", '']
        if t['citations']:
            lines.append('**Đoạn được trích:**')
            for i, cid in enumerate(t['citations'], 1):
                c = chunks.get(cid)
                text = norm_ws(c['text']) if c else '(ID không có trong corpus)'
                lines.append(f"{i}. `{cid}` (trang {c['page'] if c else '?'}): {text}")
        else:
            lines.append('**Đoạn được trích:** không có')
        lines += ['', f"**Context cuối gửi model:** {', '.join(f'`{i}`' for i in t['final_context_ids']) or '(rỗng)'}", '', '---', '']
    (run / 'review_sheet.md').write_text('\n'.join(lines), encoding='utf-8')

    out = run / 'reviews.json'
    if out.exists():
        print(f'Giữ nguyên {out} (đã có, không ghi đè)')
    else:
        reviews = [{'query_id': t['query_id'], 'answerable': t['answerable'], 'status': t['status'],
                    'answer_grade': None, 'citation_support': [None] * len(t['citations']),
                    'abstention_correct': None, 'context_grade': None, 'note': ''}
                   for t in traces if t['status'] != 'error']
        out.write_text(json.dumps(reviews, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Đã tạo {run / "review_sheet.md"} và {out}')


if __name__ == '__main__':
    main()
