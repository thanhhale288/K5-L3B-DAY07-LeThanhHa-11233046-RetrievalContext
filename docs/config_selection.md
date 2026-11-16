# Chọn cấu hình (dev) — trạng thái: ĐÃ CHỐT (2026-11-16 18:34 +07, người dùng duyệt, trước khi chạy test)

Ngày 2026-11-16. Mọi số liệu dưới đây là **dev** (15 câu có đáp án, 2 câu thiếu bằng chứng), nhãn bản v2: q06 đã thu hẹp, q01 có thêm evidence thay thế. Test chưa được chạy.

## Tiêu chí (theo thứ tự ưu tiên; chốt trước khi chạy test)

1. **Ràng buộc cứng:** từ chối đúng 2/2 câu thiếu bằng chứng trên dev.
2. **Chất lượng câu trả lời:** số câu có đáp án được trả lời, có đủ con số của đáp án chuẩn, và có ít nhất một citation trỏ đúng chunk evidence. Đây là kiểm tra tự động sơ bộ; nhãn cuối cùng là chấm tay.
3. **Context Evidence Rate** của agent.
4. Phân định khi hòa: Hit@3, rồi MRR của retrieval một lượt.
5. Độ trễ và chi phí.

## Retrieval (một lượt, top-3, budget 3200 ký tự, có filter người dùng)

| Phương pháp | Hit@1 | Hit@3 | MRR | Context Evidence Rate | Độ trễ trung vị |
|---|---|---|---|---|---|
| Dense (Day 6) | 10/15 | 13/15 | 0,756 | 13/15 | ~48 ms |
| BM25 | 12/15 | 14/15 | 0,856 | 14/15 | ~1 ms |
| Hybrid RRF | 12/15 | 13/15 | 0,833 | 13/15 | ~48 ms |

Cải thiện 1 (budget 800 → 3200), với BM25: Context Evidence Rate 4/15 → 14/15 (`starter/results/retrieval-dev-v2-b800` và `-b3200`).

## Agent (DeepSeek `deepseek-chat`, API trả về `deepseek-flash`, temperature 0, top-3, budget 3200, tối đa 3 lần search)

| Cấu hình | Trả lời / 15 | Đủ con số / 15 | Citation đúng chunk / 15 | Từ chối đúng / 2 | Context Evidence Rate | Token vào / ra | Độ trễ trung vị |
|---|---|---|---|---|---|---|---|
| Dense | 13 | 12 | 11 | 2 | 13/15 | 55,6k / 3,8k | 2,42 s |
| Dense + sửa citation | 15 | 14 | 13 | 2 | 13/15 | 55,6k / 3,8k | 2,34 s |
| BM25 | 11 | 11 | 11 | 2 | 15/15 | 53,7k / 3,9k | 2,38 s |
| **BM25 + sửa citation** | **15** | **15** | **15** | **2** | **15/15** | 55,9k / 4,0k | 2,25 s |
| Hybrid | 12 | 12 | 12 | 2 | 15/15 | 55,9k / 3,9k | 2,27 s |
| Hybrid + sửa citation | 15 | 15 | 15 | 2 | 15/15 | 55,8k / 3,9k | 2,50 s |

Cải thiện 2, sửa citation (`--fix-citations`):
- **Giả thuyết:** các câu có đáp án bị từ chối là do model liệt kê ID trong `citations` mà không ghi `[id]` vào câu trả lời, chứ không phải do thiếu bằng chứng.
- **Kết quả:** sau khi sửa, cả 3 retriever đều trả lời 15/15, và abstention vẫn 2/2.
- **Lưu ý về độ dao động giữa các lần chạy:** dù temperature = 0, số câu bị từ chối vì lỗi định dạng thay đổi giữa các lần chạy (BM25: 3 câu ở lần chạy đầu, 4 câu ở lần chạy v2). Mỗi run "+ sửa citation" chỉ thực sự chèn ID cho 2–3 câu; các câu còn lại tự có `[id]` ngay trong lần chạy đó. Vì vậy chênh lệch của một câu (≈7%) nằm trong mức dao động.

Chi phí tính theo giá token trong `.env`: khoảng 0,0025 USD cho mỗi run dev 17 câu, như nhau ở mọi cấu hình (`cost_usd_total` trong `summary.json`).

## Đề xuất

- **Cấu hình chọn:** BM25 + sửa citation, top-3, budget 3200, tối đa 3 lần search.
  - Hòa với Hybrid + sửa citation ở tiêu chí 1–3. BM25 thắng ở tiêu chí 4 (Hit@3 14 so với 13, MRR 0,856 so với 0,833) và tiêu chí 5 (retrieval ~1 ms so với ~48 ms, không cần nạp model embedding).
- **Baseline cho test:** Dense (vector store Day 6), không sửa citation, top-3, budget 3200, tối đa 3 lần search.

Lệnh test (chỉ chạy sau khi đề xuất được duyệt):

```bash
.venv/bin/python src/run_agent_eval.py --split test --method dense --top-k 3 --budget 3200 --max-searches 3 --output starter/results/agent-test-baseline-dense
.venv/bin/python src/run_agent_eval.py --split test --method bm25 --top-k 3 --budget 3200 --max-searches 3 --fix-citations --output starter/results/agent-test-chosen-bm25-fixcite
.venv/bin/python src/evaluate_retrieval.py --split test --methods dense,bm25 --budget 3200 --output starter/results/retrieval-test-b3200
```

## Giới hạn

- Dev chỉ có 15 câu, nên một câu tương đương ≈7%.
- Kiểm tra "đủ con số" chỉ so chuỗi số. Nó không phát hiện được câu trả lời thừa ý, sai điều kiện, hay sai đơn vị.
- BM25 mạnh ở bộ câu này một phần vì câu hỏi dùng lại nhiều từ khóa của tài liệu. Với câu diễn đạt khác hẳn tài liệu, dense có thể tốt hơn.
