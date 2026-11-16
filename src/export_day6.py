"""Export Day 6 chunks (pgvector) and benchmark into the Day 7 JSON contract.

Usage (from the Day 7 repo root, Day 6 Postgres container running):
    DATABASE_URL=... python src/export_day6.py \
        --benchmark "../Lab day 6/<day6-repo>/data/benchmark.json" \
        --strategy B --output starter/data/converted

Reads DATABASE_URL from the environment or from a `.env` file in the repo root.
Only reads the database; never writes to it. Gold evidence is used solely to
check the converted data, never passed to any retriever or agent.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'starter'))
from baseline import hit  # noqa: E402
from convert_day6 import convert_chunk, convert_question  # noqa: E402


def load_env(path: Path) -> None:
    """Minimal .env loader (no dependency); existing env vars win."""
    if not path.exists():
        return
    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def export_chunks(database_url: str, strategy: str) -> tuple[list[dict], dict]:
    import psycopg
    from psycopg.rows import dict_row

    with psycopg.connect(database_url, row_factory=dict_row) as conn, conn.cursor() as cur:
        cur.execute(
            """SELECT chunk_id, document_id, source, page, text, pillar, metadata
               FROM rag_chunks WHERE strategy = %s ORDER BY page, chunk_id""",
            (strategy,),
        )
        rows = cur.fetchall()
        cur.execute(
            """SELECT vector_dims(embedding) AS dim, count(*) AS n
               FROM rag_chunks WHERE strategy = %s GROUP BY 1""",
            (strategy,),
        )
        dims = cur.fetchall()
        cur.execute("SELECT extversion FROM pg_extension WHERE extname = 'vector'")
        ext = cur.fetchone()
    if not rows:
        raise RuntimeError(f'Không có chunk nào cho strategy={strategy!r}')
    raw = []
    for r in rows:
        metadata = dict(r['metadata'] or {})
        if r['pillar'] is not None:
            metadata.setdefault('pillar', r['pillar'])
        metadata.setdefault('strategy', strategy)
        raw.append({'chunk_id': r['chunk_id'], 'document_id': r['document_id'], 'source': r['source'],
                    'page': r['page'], 'text': r['text'], 'metadata': metadata})
    info = {'strategy': strategy, 'chunks': len(raw), 'pages': len({r['page'] for r in raw}),
            'embedding_dims': [d['dim'] for d in dims], 'pgvector_version': ext['extversion'] if ext else None}
    return raw, info


def load_questions(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding='utf-8'))
    questions = data['questions'] if isinstance(data, dict) else data
    if not isinstance(questions, list):
        raise ValueError('benchmark phải là JSON array hoặc dict có khóa "questions"')
    return questions


def apply_overrides(questions: list[dict], overrides: dict) -> list[dict]:
    """Apply Day 7 label fixes (question/expected_answer/evidence) by question ID."""
    by_id = {q['id']: q for q in questions}
    for qid, patch in overrides.get('question_overrides', {}).items():
        if qid not in by_id:
            raise ValueError(f'override cho câu không tồn tại: {qid}')
        q = by_id[qid]
        for key in ('question', 'expected_answer'):
            if key in patch:
                q[key] = patch[key]
        if 'evidence' in patch:
            q['gold'] = [{**g, 'evidence': patch['evidence']} for g in q['gold']]
        if 'add_gold' in patch:  # alternative valid evidence (any one entry counts as a hit)
            q['gold'] = q['gold'] + list(patch['add_gold'])
        q['day7_override'] = patch.get('reason', '')
    return questions


def check_gold(chunks: list[dict], questions: list[dict]) -> list[dict]:
    """Report answerable questions whose evidence is not fully inside one chunk."""
    problems = []
    for q in questions:
        for g in q.get('gold') or []:
            if not any(hit(c, [g]) for c in chunks):
                same_page = [c['id'] for c in chunks if c['source_id'] == g['source_id'] and c['page'] == g['page']]
                problems.append({'id': q['id'], 'split': q['split'], 'page': g['page'],
                                 'chunks_on_page': len(same_page), 'evidence': g['evidence']})
    return problems


def main() -> None:
    parser = argparse.ArgumentParser(description='Export Day 6 pgvector chunks + benchmark sang schema Day 7')
    parser.add_argument('--benchmark', required=True, type=Path)
    parser.add_argument('--strategy', default='B', help='Strategy Day 6 trong bảng rag_chunks (A/B/C)')
    parser.add_argument('--embedding-model', default='BAAI/bge-m3', help='Chỉ ghi vào metadata export')
    parser.add_argument('--overrides', default=ROOT / 'data/benchmark_day7.json', type=Path,
                        help='Sửa nhãn và câu thiếu evidence của Day 7')
    parser.add_argument('--output', default=ROOT / 'starter/data/converted', type=Path)
    args = parser.parse_args()

    load_env(ROOT / '.env')
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        raise SystemExit('Thiếu DATABASE_URL (đặt trong môi trường hoặc .env)')

    raw_chunks, info = export_chunks(database_url, args.strategy)
    raw_questions = load_questions(args.benchmark)
    chunks = [convert_chunk(c) for c in raw_chunks]
    questions = [convert_question(q) for q in raw_questions]
    overrides = json.loads(args.overrides.read_text(encoding='utf-8')) if args.overrides.exists() else {}
    questions = apply_overrides(questions, overrides)
    unanswerable = overrides.get('unanswerable', [])
    ids = [q['id'] for q in questions] + [u['id'] for u in unanswerable]
    if len(ids) != len(set(ids)):
        raise ValueError('ID câu hỏi bị trùng giữa câu có đáp án và câu thiếu evidence')
    # Contract for starter/agent_metrics.py; no gold, only answerability.
    cases = ([{'id': q['id'], 'split': q['split'], 'answerable': True} for q in questions]
             + [{'id': u['id'], 'split': u['split'], 'answerable': False} for u in unanswerable])

    args.output.mkdir(parents=True, exist_ok=True)
    raw_dir = args.output / 'raw'
    raw_dir.mkdir(exist_ok=True)
    problems = check_gold(chunks, questions)
    meta = {**info, 'embedding_model': args.embedding_model, 'benchmark': str(args.benchmark),
            'overrides': str(args.overrides), 'overridden_questions': sorted(overrides.get('question_overrides', {})),
            'answerable': {s: sum(q['split'] == s for q in questions) for s in ('dev', 'test')},
            'unanswerable': {s: sum(u['split'] == s for u in unanswerable) for s in ('dev', 'test')},
            'gold_not_in_single_chunk': problems}
    outputs = {raw_dir / 'day6_chunks.json': raw_chunks, raw_dir / 'day6_questions.json': raw_questions,
               args.output / 'chunks.json': chunks, args.output / 'questions.json': questions,
               args.output / 'unanswerable.json': unanswerable, args.output / 'cases.json': cases,
               args.output / 'export_meta.json': meta}
    for path, obj in outputs.items():
        path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    print(json.dumps({k: v for k, v in meta.items() if k != 'gold_not_in_single_chunk'}, ensure_ascii=False, indent=2))
    if problems:
        print(f'\n⚠ {len(problems)} evidence không nằm trọn trong một chunk (xem export_meta.json):')
        for p in problems:
            print(f"  {p['id']} ({p['split']}, p.{p['page']}): {p['evidence'][:70]}…")
    else:
        print('\nTất cả evidence nằm trọn trong một chunk đúng nguồn/trang.')


if __name__ == '__main__':
    main()
