"""Advanced challenge: index the FPT Annual Report 2025 (232 pages) from text, tables and visuals.

    .venv/bin/python src/adv_ingest.py                  # all steps (vision results are cached)
    .venv/bin/python src/adv_ingest.py --skip-vision    # text + tables only

Each page yields three kinds of chunks, all with `source_id`, `page` (PDF page, 1-based),
`metadata.kind` and a locator so the original region can be found again:
  * text   (`ar_p{page}_t{n}`): PyMuPDF text blocks merged in reading order up to ~1000 chars.
           Repeated layout text (left navigation menu, running header) is removed.
  * table  (`ar_p{page}_tab{n}`): PyMuPDF `find_tables()` rendered as Markdown, with the bbox.
  * visual (`ar_p{page}_v{n}`): a vision model (DeepSeek `deepseek-flash`, image input) reads the
           rendered page and returns one entry per chart / table / diagram / informative image with
           its title, position and every readable value. Results are cached per page in
           advanced/index/vision/pNNN.json, so re-running costs nothing.
Visual chunks are model output: they are spot-checked against the page images (see the report)
and are never treated as ground truth for the benchmark.
"""
from __future__ import annotations

import argparse
import base64
import json
import re
import sys
import time
import unicodedata
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))

ADV = ROOT / 'advanced'
PDF = ADV / 'source/fpt_annual_report_2025.pdf'
PAGES = ADV / 'pages'
INDEX = ADV / 'index'
VISION = INDEX / 'vision'
SOURCE_ID = 'fpt_annual_report_2025'
SIDEBAR_X = 95          # pt; the left navigation menu sits in x < ~90 on every content page
MAX_CHARS = 1000
VISION_MODEL = 'deepseek-flash'

VISION_PROMPT = """Bạn là công cụ trích xuất nội dung trực quan từ một trang Báo cáo thường niên FPT 2025 (trang PDF số {page}).
Liệt kê MỌI biểu đồ, bảng, sơ đồ/infographic và ảnh có chứa thông tin trên trang. Bỏ qua ảnh chân dung, ảnh trang trí, logo và menu điều hướng bên trái.
Với mỗi vùng, ghi:
- type: "chart" | "table" | "diagram" | "infographic" | "image"
- title: tiêu đề hoặc chú thích gần nhất (giữ nguyên tiếng Việt)
- position: vị trí trên trang (ví dụ "nửa trái, phía trên")
- content: nội dung ĐẦY ĐỦ, chép chính xác số liệu như in trên trang (giữ dấu chấm/phẩy kiểu Việt Nam), kèm đơn vị và năm.
  * Biểu đồ: loại biểu đồ, trục, chú giải, đơn vị, giá trị của từng cột/điểm/lát theo từng năm hoặc nhóm, ghi chú.
  * Bảng: chép thành bảng Markdown, đủ hàng, cột và đơn vị.
  * Sơ đồ: các nút, nhãn và quan hệ/mũi tên giữa chúng.
  * Ảnh: mô tả thông tin nhìn thấy được (chữ trên ảnh, sự kiện, chú thích).
Không suy đoán số không nhìn thấy. Nếu trang không có vùng nào như vậy, trả về danh sách rỗng.
Chỉ trả về JSON: {{"regions": [{{"type": ..., "title": ..., "position": ..., "content": ...}}]}}"""


def norm(text: str) -> str:
    return re.sub(r'[ \t]+', ' ', unicodedata.normalize('NFC', text)).strip()


def render_pages(doc, dpi: int = 110) -> None:
    PAGES.mkdir(parents=True, exist_ok=True)
    for page in doc:
        out = PAGES / f'p{page.number + 1:03d}.png'
        if not out.exists():
            page.get_pixmap(dpi=dpi).save(out)


def repeated_lines(doc, min_share: float = 0.3) -> set[str]:
    counts: Counter = Counter()
    for page in doc:
        counts.update({norm(l) for l in page.get_text().splitlines() if norm(l)})
    return {line for line, n in counts.items() if n >= min_share * len(doc)}


def text_chunks(doc, boiler: set[str]) -> list[dict]:
    chunks = []
    for page in doc:
        pno = page.number + 1
        blocks = []
        for x0, y0, x1, y1, text, *_ in page.get_text('blocks', sort=True):
            if x1 <= SIDEBAR_X:
                continue
            lines = [norm(l) for l in text.splitlines() if norm(l) and norm(l) not in boiler]
            if not lines or re.fullmatch(r'[\d\s◀▶]+', ' '.join(lines)):
                continue
            blocks.append((' '.join(lines), (x0, y0, x1, y1)))
        buf, boxes, n = [], [], 0

        def flush():
            nonlocal buf, boxes, n
            if buf:
                bbox = [min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes)]
                chunks.append({'id': f'ar_p{pno}_t{n}', 'text': '\n'.join(buf), 'source_id': SOURCE_ID,
                               'source': str(PDF.relative_to(ROOT)), 'page': pno,
                               'metadata': {'kind': 'text', 'bbox': [round(v, 1) for v in bbox]}})
                n += 1
            buf, boxes = [], []

        for text, box in blocks:
            if buf and sum(len(t) for t in buf) + len(text) > MAX_CHARS:
                flush()
            buf.append(text)
            boxes.append(box)
        flush()
    return chunks


def table_chunks(doc) -> list[dict]:
    chunks = []
    for page in doc:
        pno = page.number + 1
        try:
            tables = page.find_tables().tables
        except Exception as exc:  # noqa: BLE001 - record and keep going
            print(f'p{pno}: find_tables failed: {exc}', file=sys.stderr)
            continue
        for n, tab in enumerate(tables):
            if tab.bbox[2] <= SIDEBAR_X:
                continue
            md = norm(tab.to_markdown() or '')
            if len(md) < 40:
                continue
            chunks.append({'id': f'ar_p{pno}_tab{n}', 'text': md, 'source_id': SOURCE_ID,
                           'source': str(PDF.relative_to(ROOT)), 'page': pno,
                           'metadata': {'kind': 'table', 'bbox': [round(v, 1) for v in tab.bbox],
                                        'rows': tab.row_count, 'cols': tab.col_count}})
    return chunks


def parse_json(text: str) -> dict:
    text = text.strip()
    m = re.search(r'\{.*\}', text, re.S)
    return json.loads(m.group(0) if m else text)


def vision_page(llm, pno: int) -> dict:
    out = VISION / f'p{pno:03d}.json'
    if out.exists():
        return json.loads(out.read_text(encoding='utf-8'))
    img = base64.b64encode((PAGES / f'p{pno:03d}.png').read_bytes()).decode()
    messages = [{'role': 'user', 'content': [
        {'type': 'text', 'text': VISION_PROMPT.format(page=pno)},
        {'type': 'image_url', 'image_url': {'url': 'data:image/png;base64,' + img}}]}]
    record = {'page': pno, 'model': None, 'regions': [], 'error': None}
    for attempt in range(3):
        try:
            r = llm.complete(messages)
            record.update(model=r['model'], usage=r['usage'], cost_usd=r['cost_usd'], latency_ms=r['latency_ms'])
            record['regions'] = parse_json(r['content'] or '{}').get('regions', [])
            record['error'] = None
            break
        except Exception as exc:  # noqa: BLE001 - errors are recorded, never replaced by fake output
            record['error'] = f'{type(exc).__name__}: {exc}'
            time.sleep(2 * (attempt + 1))
    if record['error'] is None:
        out.write_text(json.dumps(record, ensure_ascii=False, indent=1), encoding='utf-8')
    return record


def visual_chunks(records: list[dict]) -> list[dict]:
    chunks = []
    for rec in records:
        for n, reg in enumerate(rec.get('regions') or []):
            content = norm(str(reg.get('content', '')))
            if not content:
                continue
            title = norm(str(reg.get('title', '')))
            kind = str(reg.get('type', 'image'))
            chunks.append({'id': f"ar_p{rec['page']}_v{n}",
                           'text': f'[{kind}] {title}\n{content}', 'source_id': SOURCE_ID,
                           'source': str(PDF.relative_to(ROOT)), 'page': rec['page'],
                           'metadata': {'kind': 'visual', 'visual_type': kind, 'title': title,
                                        'position': reg.get('position', ''),
                                        'page_image': f"advanced/pages/p{rec['page']:03d}.png",
                                        'extracted_by': rec.get('model')}})
    return chunks


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--skip-vision', action='store_true')
    ap.add_argument('--workers', type=int, default=8)
    args = ap.parse_args()

    doc = pymupdf.open(PDF)
    INDEX.mkdir(parents=True, exist_ok=True)
    render_pages(doc)
    boiler = repeated_lines(doc)
    texts, tables = text_chunks(doc, boiler), table_chunks(doc)
    print(f'text chunks {len(texts)}, table chunks {len(tables)}, boilerplate lines removed {len(boiler)}')

    records, errors = [], []
    if not args.skip_vision:
        from llm import ChatProvider
        llm = ChatProvider('deepseek', model=VISION_MODEL, timeout=180)
        VISION.mkdir(parents=True, exist_ok=True)
        with ThreadPoolExecutor(args.workers) as pool:
            futs = {pool.submit(vision_page, llm, p): p for p in range(1, len(doc) + 1)}
            for i, fut in enumerate(as_completed(futs), 1):
                rec = fut.result()
                records.append(rec)
                if rec.get('error'):
                    errors.append({'page': rec['page'], 'error': rec['error']})
                if i % 20 == 0:
                    print(f'vision {i}/{len(doc)}', flush=True)
        records.sort(key=lambda r: r['page'])
    visuals = visual_chunks(records)

    chunks = texts + tables + visuals
    (INDEX / 'chunks.json').write_text(json.dumps(chunks, ensure_ascii=False, indent=1), encoding='utf-8')
    kinds = Counter(c['metadata']['kind'] for c in chunks)
    vtypes = Counter(c['metadata'].get('visual_type') for c in visuals)
    pages_with_text = len({c['page'] for c in texts})
    meta = {'source_pdf': str(PDF.relative_to(ROOT)), 'pages': len(doc), 'chunks': len(chunks), 'by_kind': kinds,
            'visual_types': vtypes, 'pages_with_text_chunks': pages_with_text,
            'pages_without_text_chunks': sorted(set(range(1, len(doc) + 1)) - {c['page'] for c in texts}),
            'vision_model': VISION_MODEL if records else None, 'vision_errors': errors,
            'vision_cost_usd': round(sum(r.get('cost_usd') or 0 for r in records), 6),
            'vision_tokens': {k: sum((r.get('usage') or {}).get(k, 0) for r in records) for k in ('prompt_tokens', 'completion_tokens')},
            'boilerplate_lines_removed': sorted(boiler)}
    (INDEX / 'index_meta.json').write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding='utf-8')
    print(json.dumps({k: v for k, v in meta.items() if k != 'boilerplate_lines_removed'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
