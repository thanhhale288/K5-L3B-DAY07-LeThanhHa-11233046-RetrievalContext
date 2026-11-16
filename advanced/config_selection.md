# Thử thách nâng cao: chọn cấu hình trên dev

**Trạng thái: ĐÃ CHỐT lúc 2026-11-17 02:17 +07, trước khi chạy test.** Test chỉ chạy một lần với cấu hình dưới đây.

## Tiêu chí (theo thứ tự ưu tiên)

1. Tỷ lệ đạt trên dev (chấm tay theo luật của ADVANCED.md §3).
2. Không có câu thiếu bằng chứng nào bị trả lời bằng khẳng định không có căn cứ.
3. Chi phí và độ trễ.
4. Nếu vẫn hòa: chọn cấu hình ít phụ thuộc vào cách diễn đạt câu hỏi, vì câu test khác câu dev.

## Kết quả dev (18 câu: 15 có đáp án + 3 thiếu bằng chứng)

| Cấu hình | Index | Retriever | Tool | Đạt | Lỗi | Token vào / ra | Chi phí | Độ trễ trung vị |
|---|---|---|---|---|---|---|---|---|
| text-bm25 | text + bảng PyMuPDF (667 chunk) | BM25 | search, answer | 15/18 | d05, d08 từ chối nhầm; d10 tính sai (16,2%: lấy nhầm cột +/-) | 521k / 9,0k | 0,0070 USD | 4,2 s |
| full-bm25 | + 298 chunk vision (965 chunk) | BM25 | search, answer | 18/18* | du1 bị ghi `answered` dù đã từ chối | 354k / 6,9k | 0,0052 USD | 3,0 s |
| full-hybrid | 965 chunk | RRF (bge-m3 + BM25) | search, answer | 18/18* | du2 bị ghi `answered` dù đã từ chối | 284k / 6,7k | 0,0049 USD | 4,0 s |
| full-hybrid-view | 965 chunk | RRF | + `view_page` (đọc lại ảnh trang gốc) | 18/18* | du1 bị ghi `answered` | 361k / 32,2k | 0,0204 USD | 10,9 s |
| **full-hybrid + sửa nhãn từ chối (v2)** | 965 chunk | RRF | search, answer | **18/18** | không có | 332k / 6,7k | 0,0050 USD | 3,1 s |

\* Câu trả lời của du1/du2 mở đầu bằng "Không đủ bằng chứng để trả lời." và chỉ kèm dữ kiện liên quan có citation. Theo luật chấm thì vẫn đạt, nhưng trạng thái tự động ghi sai.

**Cải thiện 1, thêm chunk vision vào index:**
- Giả thuyết: lớp chữ PDF làm xáo trộn bảng và biểu đồ, nên agent không ghép được số với năm hoặc với cột.
- Kết quả: tỷ lệ đạt tăng từ 15/18 lên 18/18; câu có đáp án trích đúng trang gold tăng từ 14/15 lên 15/15.
- Lợi ích phụ: token giảm khoảng 32%, vì agent tìm được ngay chunk có cấu trúc.

**Cải thiện 2, ghi trạng thái từ chối theo nội dung câu trả lời:**
- Câu trả lời mở đầu bằng câu từ chối được ghi `abstain`.
- Các id liên quan mà model đã liệt kê được giữ lại trong trường `abstain_support`.
- Sửa này chỉ đổi cách ghi trạng thái, không đổi nội dung câu trả lời.

## Cấu hình chốt

`full-hybrid` (`src/adv_agent.py --config full-hybrid`) cùng bản sửa nhãn từ chối:
- Index 965 chunk: text, bảng PyMuPDF và vùng trực quan đọc bằng vision `deepseek-flash`.
- Retriever: hybrid RRF (k = 60, mỗi retriever đóng góp 20 ứng viên), top-5 mỗi lần search.
- Model: `deepseek-chat`, temperature 0.
- Giới hạn: tối đa 8 bước, mỗi bước bắt buộc gọi tool.

Lý do chọn:
- Hòa 18/18 với full-bm25 và full-hybrid-view.
- Rẻ và nhanh hơn full-hybrid-view khoảng 4 lần.
- So với full-bm25, phần dense giúp với câu diễn đạt khác tài liệu (tiêu chí 4).

`view_page` không được chọn: trên dev nó không tăng điểm nhưng tăng chi phí 4 lần và độ trễ 3 lần.

Lệnh test (chạy đúng một lần):

```bash
HF_HUB_OFFLINE=1 .venv/bin/python src/adv_agent.py --split test --config full-hybrid --output advanced/results/test-full-hybrid
```
