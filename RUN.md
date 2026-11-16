# Hướng dẫn chạy lại: Lê Thanh Hà (2A202603901)

Agentic RAG trên Báo cáo Phát triển Bền vững FPT 2025. Agent dùng vector store của Day 6 và model DeepSeek với tool calling thật. Báo cáo nằm ở [report/individual/2A202603901_LeThanhHa.md](report/individual/2A202603901_LeThanhHa.md). Quá trình chọn cấu hình nằm ở [docs/config_selection.md](docs/config_selection.md).

Mọi lệnh dưới đây chạy từ thư mục gốc của repo.

## 1. Cài đặt

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt   # torch / sentence-transformers / transformers khớp phiên bản venv Day 6
cp .env.example .env                         # điền DATABASE_URL, DEEPSEEK_API_KEY; giá token tùy chọn
```

Các biến trong `.env`. Không commit file này.
- `DATABASE_URL`: Postgres của Day 6, ví dụ `postgresql://…@127.0.0.1:55433/day6_lab`.
- `LLM_PROVIDER`: `deepseek` (mặc định), `openai` hoặc `openrouter`.
- `DEEPSEEK_API_KEY`, `DEEPSEEK_MODEL` (mặc định `deepseek-chat`) và `DEEPSEEK_BASE_URL`.
- `DEEPSEEK_PRICE_INPUT_PER_M` / `DEEPSEEK_PRICE_OUTPUT_PER_M`: giá USD cho mỗi 1 triệu token. Nếu để trống, `cost_usd = null`.

Model embedding `BAAI/bge-m3` phải có sẵn trong cache Hugging Face local; code nạp nó với `local_files_only`. Nếu chưa có, tải một lần bằng `huggingface-cli download BAAI/bge-m3`.

## 2. Dữ liệu từ Day 6

Repo đã commit sẵn bản export `starter/data/converted/`, nên có thể bỏ qua bước này nếu chỉ chạy BM25, test hoặc chấm. Dense cần vector store Day 6 (repo: https://github.com/thanhhale288/K5-L3B-DAY06-LeThanhHa-2A202603901-DataIngestion).

Chạy vector store Day 6 (PostgreSQL 16 + pgvector 0.8.7, bảng `rag_chunks`, strategy B gồm 198 chunk):

```bash
D6="../Lab day 6/K5-L3B-DAY06-LeThanhHa-2A202603901-DataIngestion"
(cd "$D6/starter" && docker compose -p day6_student_starter up -d --wait)   # lần đầu: chạy `python -m src.run` trong Day 6 để ingest
.venv/bin/python src/export_day6.py --benchmark "$D6/data/benchmark.json" --strategy B
```

`export_day6.py` chỉ đọc DB. Nó áp dụng các sửa nhãn trong `data/benchmark_day7.json` (q06, q01 và 4 câu thiếu bằng chứng u01–u04). Kết quả được ghi vào `starter/data/converted/`: `chunks.json`, `questions.json`, `unanswerable.json`, `cases.json` và `export_meta.json`. Nếu có evidence không nằm gọn trong một chunk, script sẽ báo.

## 3. Kiểm tra code và kết nối

```bash
.venv/bin/python -m unittest discover -s tests -v   # 27 test, dùng mock, chỉ kiểm tra code
.venv/bin/python src/llm.py --ping                  # 1 lần gọi model thật có tool calling
```

## 4. Thử nghiệm trên dev

```bash
# Retrieval: dense (Day 6), BM25, hybrid RRF (+ biến thể bigram); budget 800 và 3200
.venv/bin/python src/evaluate_retrieval.py --split dev --methods dense,bm25,hybrid,bm25+bigram,hybrid+bigram --budget 800  --output starter/results/retrieval-dev-v2-b800
.venv/bin/python src/evaluate_retrieval.py --split dev --methods dense,bm25,hybrid,bm25+bigram,hybrid+bigram --budget 3200 --output starter/results/retrieval-dev-v2-b3200

# Agent: mỗi method chạy có và không có --fix-citations
for m in dense bm25 hybrid; do
  .venv/bin/python src/run_agent_eval.py --split dev --method $m --top-k 3 --budget 3200 --max-searches 3 --output starter/results/agent-dev-v2-$m
  .venv/bin/python src/run_agent_eval.py --split dev --method $m --top-k 3 --budget 3200 --max-searches 3 --fix-citations --output starter/results/agent-dev-v2-$m-fixcite
done
```

## 5. Test

Chỉ chạy test sau khi đã chốt cấu hình. Kết quả trong repo là của lần chạy duy nhất, ngày 2026-11-16.

```bash
.venv/bin/python src/run_agent_eval.py --split test --method dense --top-k 3 --budget 3200 --max-searches 3 --output starter/results/agent-test-baseline-dense
.venv/bin/python src/run_agent_eval.py --split test --method bm25  --top-k 3 --budget 3200 --max-searches 3 --fix-citations --output starter/results/agent-test-chosen-bm25-fixcite
.venv/bin/python src/evaluate_retrieval.py --split test --methods dense,bm25 --budget 3200 --output starter/results/retrieval-test-b3200
```

## 6. Chấm tay và tổng hợp

```bash
R=starter/results/agent-test-chosen-bm25-fixcite        # làm tương tự với agent-test-baseline-dense
.venv/bin/python src/make_review_sheet.py $R            # tạo review_sheet.md và reviews.json rỗng (không ghi đè nhãn đã có)
# đọc review_sheet.md rồi điền reviews.json: answer_grade, citation_support, abstention_correct, context_grade, note
.venv/bin/python starter/agent_metrics.py --cases starter/results/cases-test.json --traces $R/traces.json --reviews $R/reviews.json --split test --output $R/metrics.json
```

## Cấu trúc kết quả

Mỗi thư mục `starter/results/agent-*` chứa:
- `traces.json`: mỗi câu có tool call, query, kết quả kèm score/rank, context cuối, câu trả lời, citation, lỗi, token, độ trễ và chi phí.
- `summary.json`: các số đếm tự động.
- `reviews.json`: nhãn chấm tay.
- `metrics.json`: số liệu tổng hợp.

Mỗi thư mục `retrieval-*` chứa `summary.md`/`summary.json` và `traces_<method>.json`.

## Code

| File | Vai trò |
|---|---|
| `src/export_day6.py` | Chuyển dữ liệu từ Day 6 sang schema Day 7, áp dụng các sửa nhãn |
| `src/retrievers.py` | `DenseRetriever` (pgvector), `BM25Retriever` và `HybridRetriever` (RRF) |
| `src/llm.py` | `ChatProvider`: chat completions tương thích OpenAI, có tool calling, token, độ trễ và chi phí |
| `src/agent.py` | `LLMController` với tool `search` và `answer`, tùy chọn sửa citation |
| `src/evaluate_retrieval.py` | Tính Hit@1, Hit@3, MRR và Context Evidence Rate cho từng method |
| `src/run_agent_eval.py` | Chạy agent trên một split, ghi trace và template nhãn |
| `src/make_review_sheet.py` | Tạo bảng chấm tay |
| `starter/` | Starter của đề bài: `baseline.py` (thêm `norm_ws` cho phép so khớp evidence), `agentic.py` và `agent_metrics.py` |

## Thử thách nâng cao (Báo cáo thường niên FPT 2025, 232 trang)

```bash
curl -L -o advanced/source/fpt_annual_report_2025.pdf https://bctn2025.fpt.com/wp-content/uploads/2026/04/BCTN-2025.pdf   # SHA-256 trong advanced/source/SOURCE.md
.venv/bin/python src/adv_ingest.py                 # render trang, text + bảng PyMuPDF, vision deepseek-flash (đã cache trong advanced/index/vision/)
.venv/bin/python src/adv_check_index.py            # kiểm tra độ phủ evidence (offline)
export HF_HUB_OFFLINE=1
for c in text-bm25 full-bm25 full-hybrid full-hybrid-view; do
  .venv/bin/python src/adv_agent.py --split dev --config $c --output advanced/results/dev-$c
done
.venv/bin/python src/adv_agent.py --split test --config full-hybrid --output advanced/results/test-full-hybrid   # cấu hình đã chốt; chỉ chạy một lần
.venv/bin/python src/adv_review_sheet.py advanced/results/test-full-hybrid          # review_sheet.md + labels.json rỗng (không ghi đè)
.venv/bin/python src/adv_review_sheet.py advanced/results/test-full-hybrid --score  # metrics.json theo nhóm
```

Benchmark: `advanced/benchmark/benchmark.json`. Chọn cấu hình: `advanced/config_selection.md`. Các thư mục dev trước bản sửa nhãn từ chối là `dev-full-*`; bản chốt chạy trên dev là `dev-full-hybrid-v2`.
