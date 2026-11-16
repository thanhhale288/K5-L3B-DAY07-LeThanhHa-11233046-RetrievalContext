# Bảng chấm đạt/không đạt: `test-full-hybrid`

Cấu hình: `{'name': 'full-hybrid', 'kinds': ['table', 'text', 'visual'], 'retriever': 'hybrid', 'view_page': False, 'top_k': 5, 'max_steps': 8, 'max_views': 3, 'model': 'deepseek-chat', 'vision_model': None, 'index_chunks': 965}`

## t01 · table · status `answered`

**Câu hỏi:** Nhóm cổ đông sở hữu từ 1.000.001 cổ phiếu trở lên có bao nhiêu cổ đông và nắm bao nhiêu phần trăm tổng số cổ phiếu đã phát hành?

**Đáp án chuẩn:** 254 cổ đông (0,20% tổng số cổ đông), nắm 1.241.598.059 cổ phiếu, tương đương 72,88%.
- Evidence gốc trang 32 (table; Bảng 'Cơ cấu cổ đông theo các mức cổ phiếu sở hữu', hàng '1.000.001 trở lên'): 254 | 0,20% | 1.241.598.059 | 72,88%

**Tool:** search('cơ cấu cổ đông sở hữu từ 1.000.001 cổ phiếu trở lên') → search('tỷ lệ sở hữu cổ đông lớn số lượng cổ đông phần trăm cổ phiếu đã phát hành')

**Câu trả lời:** Nhóm cổ đông sở hữu từ 1.000.001 cổ phiếu trở lên có 254 cổ đông (chiếm 0,20% tổng số cổ đông), nắm 1.241.598.059 cổ phiếu, tương đương 72,88% tổng số cổ phiếu đã phát hành [ar_p32_v1].

**Citation:**
- `ar_p32_v1` (trang 32, visual): [table] Cơ cấu cổ đông theo các mức cổ phiếu sở hữu
| Các mức cổ phiếu sở hữu | Số lượng cổ đông | Tỷ lệ/ Tổng số cổ đông | Số lượng cổ phiếu sở hữu | Tỷ lệ/Tổng số cổ phiếu đã phát hành |
|---|---:|---:|---:|---:|
| 01 – 999 | 89.786 | 70,43% | 19.527.027 | 1,15% |
| 1.000 – 10.000 | 32.023 | 25,12% | 94.203.628 | 5,53% |
| 10.001 – 1.000.000 | 5.425 | 4,26% | 348.178.407 | 20,44% |
| 1.000.001 trở lên | 254 | 0,20% | 1.241.598.059 | 72,88% |
| Tổng số | 127.488 | 100,00% | 1.703.507.121 | 100,00% |

Gợi ý tự động: trang gold [32], trang được trích [32]

---

## t02 · table · status `answered`

**Câu hỏi:** Theo cơ cấu cổ đông theo quốc tịch, cổ đông nước ngoài là tổ chức có bao nhiêu cổ đông và nắm bao nhiêu phần trăm cổ phiếu đã phát hành?

**Đáp án chuẩn:** 487 cổ đông, nắm 643.733.874 cổ phiếu, tương đương 37,79%.
- Evidence gốc trang 33 (table; Bảng 'Cơ cấu cổ đông theo quốc tịch', hàng 'Tổ chức' dưới nhóm 'Nước ngoài'): 487 | 0,4% | 643.733.874 | 37,79%

**Tool:** search('cơ cấu cổ đông theo quốc tịch cổ đông nước ngoài tổ chức') → search('cổ đông nước ngoài tổ chức số lượng cổ đông tỷ lệ sở hữu')

**Câu trả lời:** Theo cơ cấu cổ đông theo quốc tịch (trang 33), cổ đông nước ngoài là tổ chức có 487 cổ đông (chiếm 0,4% tổng số cổ đông), nắm 643.733.874 cổ phiếu, tương đương 37,79% tổng số cổ phiếu đã phát hành.

**Citation:**
- `ar_p33_v0` (trang 33, visual): [table] Cơ cấu cổ đông theo quốc tịch
| Đối tượng | Số lượng cổ đông | Tỷ lệ/Tổng số cổ đông | Số lượng cổ phiếu sở hữu | Tỷ lệ/Tổng số cổ phiếu đã phát hành |
|---|---:|---:|---:|---:|
| Việt Nam | 124.667 | 97,8% | 1.043.777.633 | 61,27% |
| Cá nhân | 124.385 | 97,6% | 744.568.681 | 43,71% |
| Tổ chức | 282 | 0,2% | 299.208.952 | 17,56% |
| Nước ngoài | 2.821 | 2,2% | 659.729.488 | 38,73% |
| Cá nhân | 2.334 | 1,8% | 15.995.614 | 0,94% |
| Tổ chức | 487 | 0,4% | 643.733.874 | 37,79% |
| Tổng số | 127.488 | 100,00% | 1.703.507.121 | 100,00% |

Gợi ý tự động: trang gold [33], trang được trích [33]

---

## t03 · table · status `answered`

**Câu hỏi:** Theo bảng chi tiêu cho AI giai đoạn 2025-2027, chi tiêu cho Phần mềm AI tăng bao nhiêu từ năm 2025 đến năm 2027?

**Đáp án chuẩn:** Tăng 353 tỷ USD, từ 283 tỷ USD (2025) lên 636 tỷ USD (2027).
- Evidence gốc trang 47 (table; Bảng 'Chi tiêu cho AI giai đoạn 2025-2027', hàng 'Phần mềm AI'): 2025 283 | 2026 452 | 2027 636 (tỷ USD)
- Phép tính: 636 − 283 = 353

**Tool:** search('chi tiêu cho AI giai đoạn 2025-2027') → search('Phần mềm AI chi tiêu')

**Câu trả lời:** Theo bảng "Chi tiêu cho AI giai đoạn 2025-2027" (đơn vị: Tỷ USD), chi tiêu cho Phần mềm AI là 283 tỷ USD năm 2025 và 636 tỷ USD năm 2027, tức tăng 353 tỷ USD (636 − 283 = 353), tương đương khoảng 2,25 lần (tăng ~124,7%) [ar_p47_v0].

**Citation:**
- `ar_p47_v0` (trang 47, visual): [table] Chỉ tiêu cho AI giai đoạn 2025-2027
Đơn vị: Tỷ USD

| Lĩnh vực | 2025 | 2026 | 2027 |
|---|---:|---:|---:|
| Dịch vụ AI | 439 | 588 | 761 |
| An ninh mạng AI | 26 | 51 | 86 |
| Phần mềm AI | 283 | 452 | 636 |
| Mô hình AI | 14 | 26 | 43 |
| Nền tảng AI cho khoa học dữ liệu và học máy | 22 | 31 | 44 |
| Nền tảng phát triển ứng dụng AI | 7 | 8 | 11 |
| Dữ liệu AI | 0,8 | 3 | 6 |
| Hạ tầng AI | 965 | 1.366 | 1.748 |
| Tổng chi tiêu AI | 1.757 | 2.525 | 3.335 |

Gợi ý tự động: trang gold [47], trang được trích [47]

---

## t04 · table · status `answered`

**Câu hỏi:** Lượng phát thải khí nhà kính Phạm vi 1 của FPT năm 2025 giảm bao nhiêu phần trăm so với năm 2023?

**Đáp án chuẩn:** Giảm khoảng 66,8%, từ 13.217 xuống 4.383 tấn CO2 tương đương.
- Evidence gốc trang 146 (table; Bảng 'Tổng hợp lượng phát thải khí nhà kính của FPT năm 2025', hàng 'Phạm vi 1'): 2023 13.217 | 2024 4.826 | 2025 4.383 (tấn CO2 tương đương)
- Phép tính: (4.383 − 13.217) / 13.217 = −66,8%

**Tool:** search('phát thải khí nhà kính Phạm vi 1') → search('Scope 1 phát thải tấn CO2e 2023 2025')

**Câu trả lời:** Phạm vi 1: năm 2023 là 13.217 tấn CO₂tđ, năm 2025 là 4.383 tấn CO₂tđ. Mức giảm = (13.217 − 4.383) / 13.217 ≈ 66,8% (giảm khoảng 8.834 tấn CO₂tđ).

**Citation:**
- `ar_p146_v0` (trang 146, visual): [table] Tổng hợp lượng phát thải khí nhà kính của FPT năm 2025
Đơn vị: tấn CO₂ tương đương

| Phạm vi | Năm 2023 | Năm 2024 | Năm 2025 |
|---|---:|---:|---:|
| Phạm vi 1 | 13.217 | 4.826 | 4.383 |
| Phạm vi 2 | 109.696 | 138.748 | 123.569 |
| Phạm vi 3 | Chưa triển khai | Triển khai thí điểm tại FPT Software | Triển khai tại FPT Software |
| Tổng | 122.913 | 143.574 | 127.952 |

Gợi ý tự động: trang gold [146], trang được trích [146]

---

## t05 · table · status `answered`

**Câu hỏi:** Theo bảng tình hình thay đổi vốn điều lệ, lần phát hành tháng 10/2003 đưa vốn điều lệ lên bao nhiêu và vì lý do gì?

**Đáp án chuẩn:** 150.000.000.000 VNĐ (150 tỷ), lý do: phát hành thêm cổ phần.
- Evidence gốc trang 33 (table; Bảng 'Tình hình thay đổi vốn điều lệ', lần 3): 3 | 10/2003 | 150.000.000.000 | Phát hành thêm cổ phần.

**Tool:** search('tình hình thay đổi vốn điều lệ phát hành tháng 10/2003') → search('bảng thay đổi vốn điều lệ qua các năm')

**Câu trả lời:** Theo bảng "Tình hình thay đổi vốn điều lệ", lần phát hành thứ 3 vào tháng 10/2003 đưa vốn điều lệ lên 150.000.000.000 VNĐ (150 tỷ đồng), với lý do "Phát hành thêm cổ phần" [ar_p33_v2].

**Citation:**
- `ar_p33_v2` (trang 33, visual): [table] Tình hình thay đổi vốn điều lệ
Đơn vị: VNĐ

| Lần | Thời điểm phát hành | Vốn điều lệ sau khi phát hành | Lý do |
|---:|---|---:|---|
| 1 | 04/2002 | 20.000.000.000 | Cổ phần hóa. |
| 2 | 04/2003 | 30.000.000.000 | Tăng vốn điều lệ từ kết quả kinh doanh năm 2002. |
| 3 | 10/2003 | 150.000.000.000 | Phát hành thêm cổ phần. |
| 4 | 05/2004 | 189.752.500.000 | Tăng vốn điều lệ từ kết quả kinh doanh năm 2003. |
| 5 | 01/2005 | 263.252.500.000 | Phát hành thêm cổ phần. |
| 6 | 08/2005 | 362.084.900.000 | Tăng vốn điều lệ từ kết quả kinh doanh năm 2004. |

Gợi ý tự động: trang gold [33], trang được trích [33]

---

## t06 · table · status `answered`

**Câu hỏi:** Theo báo cáo kết quả hoạt động kinh doanh hợp nhất, chi phí lãi vay năm 2025 là bao nhiêu và tăng bao nhiêu phần trăm so với năm 2024?

**Đáp án chuẩn:** 809.759.601.156 VNĐ, tăng khoảng 46,8% so với 551.639.361.786 VNĐ năm 2024.
- Evidence gốc trang 169 (table; Báo cáo kết quả hoạt động kinh doanh hợp nhất (Mẫu B 02-DN/HN), mã số 23 'Trong đó: Chi phí lãi vay'): 2025 809.759.601.156 | 2024 551.639.361.786 (VNĐ)
- Phép tính: 809.759.601.156 / 551.639.361.786 − 1 = 46,8%

**Tool:** search('chi phí lãi vay hợp nhất 2025') → search('kết quả hoạt động kinh doanh hợp nhất chi phí tài chính')

**Câu trả lời:** Theo Báo cáo kết quả hoạt động kinh doanh hợp nhất (Mẫu số B 02 – DN/HN), chi phí lãi vay năm 2025 là 809.759.601.156 VNĐ, năm 2024 là 551.639.361.786 VNĐ [ar_p169_v0]. Mức tăng: 809.759.601.156 − 551.639.361.786 = 258.120.239.370 VNĐ, tương đương khoảng 46,8% (258.120.239.370 / 551.639.361.786 ≈ 0,468) [ar_p169_v0]. Số liệu này cũng khớp với thuyết minh Chi phí tài chính (lãi tiền vay 809.759.601.156 VNĐ năm 2025 so với 551.639.361.786 VNĐ năm 2024) [ar_p209_v3].

**Citation:**
- `ar_p169_v0` (trang 169, visual): [table] BÁO CÁO KẾT QUẢ HOẠT ĐỘNG KINH DOANH HỢP NHẤT
Mẫu số B 02 – DN/HN
Đơn vị: VNĐ

| Mã số | Thuyết minh | Năm tài chính kết thúc ngày 31 tháng 12 năm 2025 | Năm tài chính kết thúc ngày 31 tháng 12 năm 2024 |
|---|---:|---:|---:|
| 01 | | 70.207.688.944.553 | 62.962.652.134.635 |
| 02 | | 94.863.843.843 | 113.857.783.268 |
| 10 | 26 | 70.112.825.100.710 | 62.848.794.351.367 |
| 11 | 27 | 44.224.295.588.297 | 39.150.445.981.451 |
| 20 | | 25.888.529.512.413 | 23.698.348.369.916 |
| 21 | 28 | 2.977.156.356.773 | 1.935.749.115.305 |
| 22 | 29 | 1.672.048.701.466 | 1.811.547.381.981 |
| 23 | | 809.759.601.156 | 551.639.361.786 |
| 24 | 5(b) | 658.024.835.314 | 392.531.256.272 |
| 25 | 30 | 7.562.660.640.454 | 6.115.961.971.783 |
| 26 | 31 | 7.337.325.397.804 | 7.074.038.614.774 |
| 30 | | 12.951.675.964.776 | 11.025.080.772.955 |
| 31 | | 142.892.570.480 | 175.450.599.740 |
| 32 | | 50.935.701.459 | 130.864.954.876 |
| 40 | | 91.956.869.021 | 44.585.644.864 |
| 50 | | 13.043.632.833.797 | 11.069.666.417.819 |
| 51 | 32(a) | 1.916.998.192.442 | 1.922.927.614.658 |
| 52 | 32(b) | (105.704.809.379) | (280.683.727.283) |

Ghi chú nội dung hàng:
- 01: Doanh thu bán hàng và cung cấp dịch
- `ar_p209_v3` (trang 209, visual): [table] 29. Chi phí tài chính
Đơn vị: VND

| Chỉ tiêu | 2025 | 2024 |
|---|---:|---:|
| Lãi tiền vay | 809.759.601.156 | 551.639.361.786 |
| Lỗ chênh lệch tỷ giá | 474.800.589.595 | 506.839.495.688 |
| Dự phòng giảm giá các khoản đầu tư và tổn thất đầu tư tài chính | 384.631.609.873 | 738.729.747.218 |
| Khác | 2.856.900.842 | 14.338.777.289 |
| **Cộng** | 1.672.048.701.466 | 1.811.547.381.981 |

Gợi ý tự động: trang gold [169], trang được trích [169, 209]

---

## t07 · image · status `answered`

**Câu hỏi:** Theo sơ đồ tổ chức, FPT Telecom thuộc khối nào, có vốn điều lệ bao nhiêu và FPT sở hữu bao nhiêu phần trăm?

**Đáp án chuẩn:** Khối Viễn thông; vốn điều lệ 7.387.634.630.000 VNĐ; tỷ lệ sở hữu 45,66%.
- Evidence gốc trang 31 (diagram; Sơ đồ tổ chức, ô 'FPT Telecom' nối với 'Khối Viễn thông'): FPT Telecom — Vốn điều lệ 7.387.634.630.000 VNĐ — Tỷ lệ sở hữu: 45,66%

**Tool:** search('sơ đồ tổ chức FPT Telecom khối') → search('FPT Telecom vốn điều lệ tỷ lệ sở hữu')

**Câu trả lời:** Theo sơ đồ tổ chức (trang 31), FPT Telecom thuộc KHỐI VIỄN THÔNG (nằm trong nhóm Công ty con), với vốn điều lệ 7.387.634.630.000 VNĐ và tỷ lệ sở hữu của FPT là 45,66%.

**Citation:**
- `ar_p31_v0` (trang 31, visual): [diagram] Sơ đồ tổ chức
Sơ đồ tổ chức gồm các nút và quan hệ:
- ĐẠI HỘI ĐỒNG CỔ ĐÔNG
 + nối xuống HỘI ĐỒNG QUẢN TRỊ
 + nối sang BAN KIỂM SOÁT
- HỘI ĐỒNG QUẢN TRỊ
 + nối xuống TỔNG GIÁM ĐỐC VÀ BAN ĐIỀU HÀNH
 + nối sang nhóm gồm: ỦY BAN NHÂN SỰ VÀ LƯƠNG THƯỞNG; ỦY BAN CHÍNH SÁCH PHÁT TRIỂN; VĂN PHÒNG CHỦ TỊCH HĐQT; BỘ PHẬN KIỂM TOÁN NỘI BỘ
- TỔNG GIÁM ĐỐC VÀ BAN ĐIỀU HÀNH
 + nối đến TẬP ĐOÀN
 + nối đến CÔNG TY CON
 + nối đến CÔNG TY LIÊN KẾT
- TẬP ĐOÀN
 + nối đến các đơn vị: Ban Công nghệ; Ban Công nghệ thông tin; Văn phòng Chuyển đổi số; Ban Nhân sự; Ban Đảm bảo chất lượng; Ban Tài chính Kế hoạch; Ban Giám sát Tuân thủ; Ban Truyền thông; Ban Mua sắm; Ban Văn hóa Doanh nghiệp; Văn phòng; Bộ phận phát triển các dự án chiến lược; Chi nhánh Tp.HCM
- CÔNG TY CON
 + nối đến KHỐI CÔNG NGHỆ; KHỐI VIỄN THÔNG; KHỐI GIÁO DỤC, ĐẦU TƯ VÀ KHÁC
- KHỐI CÔNG NGHỆ gồm/liên kết đến:
 + FPT Software — Vốn điều lệ: 7.750.000.000.000 VNĐ; Tỷ lệ sở hữu: 100%
 + FPT IS — Vốn điều lệ: 1.500.000.000.000 VNĐ; Tỷ lệ sở hữu: 100%
 + FPT Digital — Vốn điều lệ: 60.000.000.000 VNĐ; Tỷ lệ sở hữu: 100%
 + FPT Smart Cloud — Vốn điều lệ: 1.000.000.000.000 VNĐ; Tỷ lệ sở hữu: 100%
- KHỐI VIỄN THÔNG gồm/liên kết đến:
 + 
- `ar_p31_t1` (trang 31, text): Ban Giám sát Tuân thủ
Ban Truyền thông
KHỐI CÔNG NGHỆ
Ban Mua sắm
FPT Smart Cloud
FPT Digital
FPT Software FPT IS
Synnex FPT
Ban Văn hóa Đoàn thể
Vốn điều lệ 1.000.000.000.000 VNĐ Tỷ lệ sở hữu: 100%
Vốn điều lệ 1.188.400.000.000 VNĐ Tỷ lệ sở hữu: 48,00%
Vốn điều lệ 7.750.000.000.000 VNĐ Tỷ lệ sở hữu: 100%
Vốn điều lệ 1.500.000.000.000 VNĐ Tỷ lệ sở hữu: 100%
Vốn điều lệ 60.000.000.000 VNĐ Tỷ lệ sở hữu: 100%
Văn phòng
KHỐI VIỄN THÔNG
FPT Retail
FPT Telecom
FPT Online
Bộ phận phát triển các dự án chiến lược
Vốn điều lệ 184.712.750.000 VNĐ Tỷ lệ sở hữu: 49,52%
Vốn điều lệ 7.387.634.630.000 VNĐ Tỷ lệ sở hữu: 45,66%
Vốn điều lệ 1.703.017.850.000 VNĐ Tỷ lệ sở hữu: 46,54%
Chi nhánh Tp.HCM
KHỐI GIÁO DỤC, ĐẦU TƯ VÀ KHÁC
FPT Education
FPT Investment
Vốn điều lệ 1.000.000.000.000 VNĐ Tỷ lệ sở hữu: 100%
Vốn điều lệ 4.500.000.000.000 VNĐ Tỷ lệ sở hữu: 100%

Gợi ý tự động: trang gold [31], trang được trích [31]

---

## t08 · image · status `answered`

**Câu hỏi:** Sơ đồ tổ chức thể hiện những công ty liên kết nào của FPT và tỷ lệ sở hữu tương ứng?

**Đáp án chuẩn:** Synnex FPT (vốn điều lệ 1.188.400.000.000 VNĐ, tỷ lệ sở hữu 48,00%) và FPT Retail (vốn điều lệ 1.703.017.850.000 VNĐ, tỷ lệ sở hữu 46,54%).
- Evidence gốc trang 31 (diagram; Sơ đồ tổ chức, nhánh 'Công ty liên kết' bên phải): Synnex FPT 48,00%; FPT Retail 46,54%

**Tool:** search('sơ đồ tổ chức công ty liên kết tỷ lệ sở hữu') → search('công ty liên kết tỷ lệ sở hữu FPT')

**Câu trả lời:** Theo Sơ đồ tổ chức (trang 31), nhánh "CÔNG TY LIÊN KẾT" gồm 2 công ty:
- Synnex FPT: vốn điều lệ 1.188.400.000.000 VNĐ, tỷ lệ sở hữu 48,00%
- FPT Retail: vốn điều lệ 1.703.017.850.000 VNĐ, tỷ lệ sở hữu 46,54%

(Lưu ý: sơ đồ cũng ghi FPT Online 49,52% và FPT Telecom 45,66% nhưng nằm trong nhánh "Khối Viễn thông" thuộc Công ty con.) [ar_p31_v0]

**Citation:**
- `ar_p31_v0` (trang 31, visual): [diagram] Sơ đồ tổ chức
Sơ đồ tổ chức gồm các nút và quan hệ:
- ĐẠI HỘI ĐỒNG CỔ ĐÔNG
 + nối xuống HỘI ĐỒNG QUẢN TRỊ
 + nối sang BAN KIỂM SOÁT
- HỘI ĐỒNG QUẢN TRỊ
 + nối xuống TỔNG GIÁM ĐỐC VÀ BAN ĐIỀU HÀNH
 + nối sang nhóm gồm: ỦY BAN NHÂN SỰ VÀ LƯƠNG THƯỞNG; ỦY BAN CHÍNH SÁCH PHÁT TRIỂN; VĂN PHÒNG CHỦ TỊCH HĐQT; BỘ PHẬN KIỂM TOÁN NỘI BỘ
- TỔNG GIÁM ĐỐC VÀ BAN ĐIỀU HÀNH
 + nối đến TẬP ĐOÀN
 + nối đến CÔNG TY CON
 + nối đến CÔNG TY LIÊN KẾT
- TẬP ĐOÀN
 + nối đến các đơn vị: Ban Công nghệ; Ban Công nghệ thông tin; Văn phòng Chuyển đổi số; Ban Nhân sự; Ban Đảm bảo chất lượng; Ban Tài chính Kế hoạch; Ban Giám sát Tuân thủ; Ban Truyền thông; Ban Mua sắm; Ban Văn hóa Doanh nghiệp; Văn phòng; Bộ phận phát triển các dự án chiến lược; Chi nhánh Tp.HCM
- CÔNG TY CON
 + nối đến KHỐI CÔNG NGHỆ; KHỐI VIỄN THÔNG; KHỐI GIÁO DỤC, ĐẦU TƯ VÀ KHÁC
- KHỐI CÔNG NGHỆ gồm/liên kết đến:
 + FPT Software — Vốn điều lệ: 7.750.000.000.000 VNĐ; Tỷ lệ sở hữu: 100%
 + FPT IS — Vốn điều lệ: 1.500.000.000.000 VNĐ; Tỷ lệ sở hữu: 100%
 + FPT Digital — Vốn điều lệ: 60.000.000.000 VNĐ; Tỷ lệ sở hữu: 100%
 + FPT Smart Cloud — Vốn điều lệ: 1.000.000.000.000 VNĐ; Tỷ lệ sở hữu: 100%
- KHỐI VIỄN THÔNG gồm/liên kết đến:
 + 

Gợi ý tự động: trang gold [31], trang được trích [31]

---

## t09 · image · status `answered`

**Câu hỏi:** Trên bản đồ hiện diện toàn cầu ở trang 'Vị thế và quy mô', FPT có mặt ở những quốc gia nào thuộc khu vực Mỹ Latinh?

**Đáp án chuẩn:** Mexico, Costa Rica và Colombia.
- Evidence gốc trang 27 (image; Bản đồ thế giới với các ghim vị trí, khu vực Trung và Nam Mỹ): Mexico, Costa Rica, Colombia (Bắc Mỹ còn có Canada, USA)

**Tool:** search('Vị thế và quy mô bản đồ hiện diện toàn cầu') → search('Mỹ Latinh quốc gia FPT có mặt')

**Câu trả lời:** Trên bản đồ hiện diện toàn cầu ở trang "Vị thế và quy mô" (trang 27), các quốc gia thuộc khu vực Mỹ Latinh có mặt là: Mexico, Costa Rica và Colombia [ar_p27_v1].

**Citation:**
- `ar_p27_v1` (trang 27, visual): [infographic] VỊ THẾ VÀ QUY MÔ
Bản đồ thế giới với các điểm đánh dấu màu cam và nhãn quốc gia/vùng lãnh thổ: Canada; USA; Mexico; Costa Rica; Colombia; Thụy Điển; Đan Mạch; Anh; Đức; Pháp; Cộng hòa Séc; Slovakia; Romania; Thổ Nhĩ Kỳ; Israel; Ả Rập thống nhất; Ả-rập Xê-út; Ấn Độ; Trung Quốc; Hàn Quốc; Nhật Bản; Đài Loan; Hồng Kông; Việt Nam; Campuchia; Philippines; Malaysia; Singapore; Indonesia; Thái Lan; Myanmar; Úc.

Gợi ý tự động: trang gold [27], trang được trích [27]

---

## t10 · image · status `answered`

**Câu hỏi:** Sơ đồ nền tảng AI linh hoạt FleziPT gồm những vòng nào, kể từ trong ra ngoài?

**Đáp án chuẩn:** Flezi Foundation (trong cùng), Flezi Crew (giữa), Flezi Verse (ngoài).
- Evidence gốc trang 63 (diagram; Sơ đồ vòng tròn 'Nền tảng AI linh hoạt FleziPT...', cột phải): Tâm: FLEZI FOUNDATION; vòng cam: FLEZI CREW; vòng xanh lá: FLEZI VERSE

**Tool:** search('FleziPT nền tảng AI linh hoạt sơ đồ') → search('FleziPT các vòng')

**Câu trả lời:** Theo sơ đồ đồng tâm về nền tảng AI linh hoạt FleziPT (trang 63), các vòng từ trong ra ngoài gồm:

1. **Lõi trung tâm: FLEZI FOUNDATION** (lõi xanh).
2. **Vòng cam phía trong: FLEZI CREW** — gồm các nhãn: Flezi Pulse; Flezi Crew; Chuyển đổi AI; AI Agents; AI Foundation; Đội tàu AI toàn cầu; Customer; Nhân viên số.
3. **Vòng xanh phía trong: FLEZI VERSE** — gồm các nhãn: Giải pháp chuyển đổi số; Maaz One; Flezi Loop; Flezi Lift; Flezi MS; Flezi DX; Flezi Q; Flezi Agents.
4. **Vòng ngoài cùng: các kết quả/tiêu chí** — NHANH HƠN; MẠNH HƠN; HIỆU QUẢ HƠN; BẢO MẬT HƠN; LINH HOẠT HƠN.

Quan hệ giữa các lớp: FLEZI FOUNDATION là nền tảng, bao quanh bởi FLEZI CREW, tiếp đến FLEZI VERSE và các kết quả/tiêu chí ở vòng ngoài [ar_p63_v1].

**Citation:**
- `ar_p63_v1` (trang 63, visual): [infographic] Nền tảng AI linh hoạt FleziPT với phương pháp, quy trình và giải pháp đã được kiểm chứng hiệu quả
Sơ đồ đồng tâm. Vòng ngoài cùng gồm các nhãn: NHANH HƠN; MẠNH HƠN; HIỆU QUẢ HƠN; BẢO MẬT HƠN; LINH HOẠT HƠN. Vòng xanh phía trong có tiêu đề FLEZI VERSE, gồm các nút/nhãn: Giải pháp chuyển đổi số; Maaz One; Flezi Loop; Flezi Lift; Flezi MS; Flezi DX; Flezi Q; Flezi Agents. Vòng cam phía trong có tiêu đề FLEZI CREW, gồm các nút/nhãn: Flezi Pulse; Flezi Crew; Chuyển đổi AI; AI Agents; AI Foundation; Đội tàu AI toàn cầu; Customer; Nhân viên số. Lõi xanh trung tâm: FLEZI FOUNDATION. Quan hệ: các lớp đồng tâm từ trong ra ngoài thể hiện FLEZI FOUNDATION là nền tảng, bao quanh bởi FLEZI CREW, tiếp đến FLEZI VERSE và các kết quả/tiêu chí ở vòng ngoài.

Gợi ý tự động: trang gold [63], trang được trích [63]

---

## t11 · image · status `answered`

**Câu hỏi:** Trong sơ đồ quy trình xác định các vấn đề trọng yếu, Bước 02 là gì?

**Đáp án chuẩn:** Phân tích và xác định các vấn đề trọng yếu được các bên quan tâm (dựa trên tham vấn các bên liên quan và đánh giá mức độ tác động đến chiến lược tăng trưởng dài hạn).
- Evidence gốc trang 125 (diagram; Sơ đồ 'Quy trình xác định các vấn đề trọng yếu', khối 'Bước 02'): Bước 02: Phân tích và xác định các vấn đề trọng yếu được các bên quan tâm.

**Tool:** search('quy trình xác định vấn đề trọng yếu Bước 02') → search('sơ đồ các bước xác định vấn đề trọng yếu')

**Câu trả lời:** Bước 02 trong sơ đồ "Quy trình xác định các vấn đề trọng yếu" (trang 125) là: **Phân tích và xác định các vấn đề trọng yếu được các bên quan tâm.**

Nội dung: Xác định các vấn đề trọng yếu dựa trên cơ sở tham vấn các bên liên quan và đánh giá mức độ tác động đến chiến lược tăng trưởng dài hạn. Các vấn đề trọng yếu được xác định tập trung vào quản trị minh bạch, an toàn dữ liệu, cam kết chuyển đổi xanh, phát triển nguồn nhân lực chất lượng cao và quản trị chuỗi cung ứng bền vững.

**Citation:**
- `ar_p125_v1` (trang 125, visual): [diagram] Quy trình xác định các vấn đề trọng yếu
Quan hệ: Bước 01 → Bước 02 → Bước 03 (quy trình tuần tự).

Bước 01 — Xác định các vấn đề chính có ảnh hưởng lớn đến hoạt động kinh doanh của Tập đoàn và lợi ích của các bên quan tâm.
• Bám sát các diễn biến kinh tế, chính trị, xã hội, môi trường của Việt Nam và thế giới;
• Nghiên cứu thông tin từ các báo cáo kinh tế-xã hội, báo cáo thị trường, báo cáo ngành do các tổ chức uy tín đưa ra;
• Phân tích các báo cáo đánh giá, khảo sát khách hàng của Tập đoàn;
• Phân tích đặc thù kinh doanh của ngành và các lĩnh vực hoạt động của Tập đoàn;
• Ghi nhận phản hồi từ cổ đông, nhà đầu tư và các bên liên quan khác;
• Tìm hiểu các hướng dẫn xây dựng báo cáo phát triển bền vững.

Bước 02 — Phân tích và xác định các vấn đề trọng yếu được các bên quan tâm.
• Xác định các vấn đề trọng yếu dựa trên cơ sở tham vấn các bên liên quan và đánh giá mức độ tác động đến chiến lược tăng trưởng dài hạn. Các vấn đề trọng yếu được xác định tập trung vào quản trị minh bạch, an toàn dữ liệu, cam kết chuyển đổi xanh, phát triển nguồn nhân lực chất lượng cao và quản trị chuỗi cung ứng bền vững.

Bước 03 — Phân tích các vấn đề trọng yếu trong mối quan hệ với các bên li
- `ar_p125_t1` (trang 125, text): HĐQT • Phê duyệt, ban hành chiến lược và định hướng phát triển bền vững trong toàn Tập đoàn.
• Tìm hiểu các hướng dẫn về xây dựng báo cáo phát triển bền vững.
Ban Điều hành
Bước 02
Đảm bảo việc triển khai chiến lược phát triển bền vững thông qua các hoạt động:
Thông điệp và định hướng ESG
Quản trị hướng đến phát triển bền vững
Phân tích và xác định các vấn đề trọng yếu được các bên quan tâm.
• Xây dựng mục tiêu phát triển bền vững cụ thể cho Tập đoàn và công ty thành viên;
Môi trường làm việc đẳng cấp, hạnh phúc
• Chỉ đạo triển khai các chương trình hiện thực hóa chiến lược phát triển bền vững của Tập đoàn;
Hoạt động vì môi trường xanh
Song hành vì sự phát triển cộng đồng
• Giám sát kết quả thực hiện mục tiêu phát triển bền vững của Tập đoàn và công ty thành viên.
- `ar_p125_t2` (trang 125, text): • Xác định các vấn đề trọng yếu dựa trên cơ sở tham vấn các bên liên quan và đánh giá mức độ tác động đến chiến lược tăng trưởng dài hạn. Các vấn đề trọng yếu được xác định tập trung vào quản trị minh bạch, an toàn dữ liệu, cam kết chuyển đổi xanh, phát triển nguồn nhân lực chất lượng cao và quản trị chuỗi cung ứng bền vững.
Công ty thành viên
• Đảm bảo hiện thực hóa các mục tiêu phát triển bền vững theo định hướng và chiến lược chung của Tập đoàn;
Bước 03
• Thực hiện báo cáo định kỳ về tình hình triển khai chiến lược phát triển bền vững của đơn vị.
Phân tích các vấn đề trọng yếu trong mối quan hệ với các bên liên quan.
• Xây dựng ma trận các vấn đề trọng yếu; • Lựa chọn các vấn đề trọng yếu.
Dựa trên nguyên tắc và quy trình xác định các vấn đề trọng yếu nêu trên, FPT lựa chọn 04 vấn đề trọng yếu gồm: (1) Quản trị hướng đến phát triển bền vững; (2) Xây dựng môi trường làm việc đẳng cấp, hạnh phúc; (3) Hoạt động vì môi trường xanh; (4) Song hành vì sự phát triển cộng đồng.

Gợi ý tự động: trang gold [125], trang được trích [125]

---

## t12 · chart · status `answered`

**Câu hỏi:** Theo biểu đồ ROE và ROA giai đoạn 2021-2025, ROA đạt cao nhất vào năm nào và bằng bao nhiêu?

**Đáp án chuẩn:** Năm 2024, ROA 14,4%.
- Evidence gốc trang 11 (chart; Biểu đồ đường ROE/ROA, đường màu cam (ROA theo chú giải)): ROA: 2021 11,4% | 2022 11,9% | 2023 13,6% | 2024 14,4% | 2025 14,1%

**Tool:** search('biểu đồ ROE ROA giai đoạn 2021-2025') → search('ROA cao nhất')

**Câu trả lời:** Theo biểu đồ ROE/ROA giai đoạn 2021-2025 (trang 11), ROA đạt cao nhất vào năm 2024, bằng 14,4% (các năm: 2021: 11,4%; 2022: 11,9%; 2023: 13,6%; 2024: 14,4%; 2025: 14,1%).

**Citation:**
- `ar_p11_v2` (trang 11, visual): [chart] Tỷ suất sinh lợi trên vốn chủ sở hữu (ROE) / Tỷ suất sinh lợi trên tổng tài sản (ROA)
Biểu đồ đường với hai đường ROE và ROA. Giá trị hiển thị: ROE 28,1%; ROA 14,1%. Trục tung: 0; 10; 20; 30 (%). Trục hoành/năm: 2021, 2022, 2023, 2024, 2025. Chú giải: ROE (%); ROA (%). Giá trị ROE theo năm: 2021: 26,7%; 2022: 27,7%; 2023: 27,9%; 2024: 28,5%; 2025: 28,1%. Giá trị ROA theo năm: 2021: 11,4%; 2022: 11,9%; 2023: 13,6%; 2024: 14,4%; 2025: 14,1%.
- `ar_p11_t0` (trang 11, text): Đảm bảo tăng trưởng ổn định (Tiếp theo)
Con số nổi bật
1.697 2.011 2.374 2.741 3.185
Cổ tức bằng tiền mặt
5.750 7.112 8.167 10.117 11.078
Đóng góp Ngân sách Nhà nước
Giải thưởng tiêu biểu
12.000
Hoạt động nổi bật
3.500
10.000
Dự án AI nổi bật
Tỷ VNĐ 3.185
Tỷ VNĐ 11.078
3.000
8.000
2.500
so với cùng kỳ 16,2%
so với cùng kỳ 9,5%
2.000
6.000
1.500
4.000
1.000
2.000
Đơn vị: Tỷ VNĐ
Đơn vị: Tỷ VNĐ
BÁO CÁO TÀI CHÍNH HỢP NHẤT
26,7% 27,7% 27,9% 28,5% 28,1%
Tỷ suất sinh lời trên vốn chủ sở hữu (ROE) 28,1%
11,4% 11,9% 13,6% 14,4% 14,1%
Tỷ suất sinh lời trên tổng tài sản (ROA) 14,1%
ROE (%)
ROA (%)

Gợi ý tự động: trang gold [11], trang được trích [11]

---

## t13 · chart · status `answered`

**Câu hỏi:** Theo biểu đồ doanh thu theo khu vực địa lý, thị trường nước ngoài nào chiếm tỷ trọng doanh thu lớn nhất và bao nhiêu phần trăm?

**Đáp án chuẩn:** Nhật Bản, 22,8%.
- Evidence gốc trang 27 (chart; Biểu đồ vành khuyên 'Doanh thu theo khu vực địa lý', lát màu cam (Nhật Bản theo chú giải)): Việt Nam 48,9% | Nhật Bản 22,8% | Châu Mỹ 11,6% | Châu Á-Thái Bình Dương 11,1% | Châu Âu 5,6%

**Tool:** search('doanh thu theo khu vực địa lý') → search('thị trường nước ngoài tỷ trọng doanh thu')

**Câu trả lời:** Theo biểu đồ "Doanh thu theo khu vực địa lý" (trang 27), trong các thị trường nước ngoài, Nhật Bản chiếm tỷ trọng lớn nhất: 22,8%. Các thị trường nước ngoài còn lại: Châu Mỹ 11,6%; Châu Á – Thái Bình Dương 11,1%; Châu Âu 5,6% (Việt Nam 48,9%).

**Citation:**
- `ar_p27_v2` (trang 27, visual): [chart] Doanh thu theo khu vực địa lý
Biểu đồ tròn dạng vành khuyên, đơn vị: %. Các lát: Việt Nam 48,9%; Châu Mỹ 11,6%; Châu Âu 5,6%; Nhật Bản 22,8%; Châu Á-Thái Bình Dương 11,1%. Chú giải màu: Việt Nam; Châu Mỹ; Châu Âu; Nhật Bản; Châu Á-Thái Bình Dương. Chú giải vòng: Việt Nam; Nước ngoài.

Gợi ý tự động: trang gold [27], trang được trích [27]

---

## t14 · chart · status `answered`

**Câu hỏi:** Theo biểu đồ kế hoạch năm 2026, doanh thu khối Giáo dục, Đầu tư và Khác dự kiến thay đổi thế nào so với năm 2025?

**Đáp án chuẩn:** Giảm 3,3%, từ 6.132 tỷ VNĐ (2025) xuống 5.930 tỷ VNĐ (2026).
- Evidence gốc trang 55 (chart; Biểu đồ cột 'Doanh thu' trong 'Kế hoạch năm 2026', nhóm cột 'Khối Giáo dục, Đầu tư và Khác'): Năm 2025 6.132 | Năm 2026 5.930 | mũi tên giảm 3,3%

**Tool:** search('kế hoạch năm 2026 doanh thu khối Giáo dục, Đầu tư và Khác') → search('biểu đồ kế hoạch 2026 doanh thu')

**Câu trả lời:** Theo biểu đồ Doanh thu trong phần "Kế hoạch năm 2026" (trang 55), Khối Giáo dục, Đầu tư và Khác dự kiến doanh thu năm 2026 là 5.930 tỷ VNĐ, so với 6.132 tỷ VNĐ năm 2025 — tức giảm 3,3% so với cùng kỳ (giảm 202 tỷ VNĐ). Lưu ý: số liệu năm 2025 đã được điều chỉnh theo phương pháp hợp nhất FPT Telecom theo vốn chủ sở hữu để đảm bảo so sánh được.

**Citation:**
- `ar_p55_v0` (trang 55, visual): [chart] Doanh thu
Loại biểu đồ: Biểu đồ cột nhóm.
Tổng Doanh thu năm 2026: 58.580 Tỷ VNĐ; tăng 15,8% so với cùng kỳ.
Trục tung: 0–60.000, bước 10.000 (nhãn: 0; 10.000; 20.000; 30.000; 40.000; 50.000; 60.000).
Trục hoành: Khối Công nghệ; Khối Giáo dục, Đầu tư và Khác.
Đơn vị: Tỷ VNĐ.
Chú giải: Năm 2026 (xanh đậm); Năm 2025 (xanh nhạt).
Khối Công nghệ: Năm 2026 = 52.650; Năm 2025 = 44.475; tăng 18,4%.
Khối Giáo dục, Đầu tư và Khác: Năm 2026 = 5.930; Năm 2025 = 6.132; giảm 3,3%.
Ghi chú: (Đối với số liệu năm 2026, Tập đoàn hợp nhất Công ty Cổ phần Viễn thông FPT (FPT Telecom) theo phương pháp vốn chủ sở hữu, số liệu năm 2025 đã được điều chỉnh theo cùng phương pháp nhằm đảm bảo tính nhất quán và khả năng so sánh.)
- `ar_p55_t0` (trang 55, text): KẾ HOẠCH NĂM 2026
Các mục tiêu chủ yếu
52.650
5.930
7.350
4.279
Doanh thu
Lợi nhuận trước thuế
44.475
6.132
5.907
4.206
60.000
Tỷ VNĐ 58.580
Tỷ VNĐ 11.629
18,4%
24,4%
50.000
so với cùng kỳ 15,8%
so với cùng kỳ 15,0%
Bối cảnh chung
40.000
1,7%
30.000
Chiến lược phát triển giai đoạn 2026 - 2028
20.000
10.000
3,3%
Năm 2026
Năm 2026
Năm 2025
Năm 2025
Khối Công nghệ
Khối Công nghệ
Khối Giáo dục, Đầu tư và Khác Đơn vị: Tỷ VNĐ
Khối Giáo dục, Đầu tư và Khác Đơn vị: Tỷ VNĐ
(Đối với số liệu năm 2026, Tập đoàn hợp nhất Công ty Cổ phần Viễn thông FPT (FPT Telecom) theo phương pháp vốn chủ sở hữu, số liệu năm 2025 đã được điều chỉnh theo cùng phương pháp nhằm đảm bảo tính nhất quán và khả năng so sánh.)
Kế hoạch đầu tư dự kiến
Đơn vị: Tỷ VNĐ
Khối Ngân sách đầu tư Chú thích
4.200
Khối Công nghệ
Đầu tư mở rộng các khu tổ hợp văn phòng tại các thành phố lớn như: Hà Nội, Tp.Hồ Chí Minh, Bình Định.
3.000
Khối Giáo dục, Đầu tư và Khác

Gợi ý tự động: trang gold [55], trang được trích [55]

---

## t15 · chart · status `answered`

**Câu hỏi:** Theo biểu đồ cơ cấu lợi nhuận trước thuế theo khối năm 2025, khối nào có tốc độ tăng trưởng lợi nhuận trước thuế cao nhất và đạt bao nhiêu?

**Đáp án chuẩn:** Khối Giáo dục, Đầu tư và Khác: 2.773 tỷ VNĐ (21,2%), tăng 23,1%.
- Evidence gốc trang 60 (chart; Biểu đồ tròn 'Cơ cấu lợi nhuận trước thuế theo khối', lát xanh lá): Khối Giáo dục, Đầu tư và Khác 2.773 (21,2%) tăng 23,1% | Viễn thông 4.364 (33,5%) tăng 21,6% | Công nghệ 5.907 (45,3%) tăng 12,9%

**Tool:** search('cơ cấu lợi nhuận trước thuế theo khối 2025') → search('tăng trưởng lợi nhuận trước thuế theo khối')

**Câu trả lời:** Theo biểu đồ cơ cấu lợi nhuận trước thuế theo khối năm 2025 (trang 60), khối Giáo dục, Đầu tư và Khác có tốc độ tăng trưởng lợi nhuận trước thuế cao nhất: tăng 23,1% (đạt 2.773 tỷ VND, chiếm 21,2% cơ cấu). So sánh: Khối Viễn thông tăng 21,6% (4.364 tỷ VND, 33,5%) và Khối Công nghệ tăng 12,9% (5.907 tỷ VND, 45,3%); tổng lợi nhuận trước thuế đạt 13.044 tỷ VND, tăng 17,8%.

**Citation:**
- `ar_p60_v1` (trang 60, visual): [chart] Cơ cấu lợi nhuận trước thuế theo khối
Biểu đồ vòng tròn (donut) thể hiện cơ cấu lợi nhuận trước thuế theo khối. Không có trục; đơn vị: Tỷ VND. Tổng/trung tâm: 13.044 (mũi tên tăng 17,8%). Chú giải: Khối Công nghệ (cam); Khối Viễn thông (xanh dương); Khối Giáo dục, Đầu tư và Khác (xanh lá). Số liệu: Khối Công nghệ: 5.907, 45,3% (mũi tên tăng 12,9%); Khối Viễn thông: 4.364, 33,5% (mũi tên tăng 21,6%); Khối Giáo dục, Đầu tư và Khác: 2.773, 21,2% (mũi tên tăng 23,1%). Số liệu thuộc trang Báo cáo thường niên FPT 2025.
- `ar_p60_t0` (trang 60, text): Phân tích kết quả kinh doanh theo khối
Để phản ánh đúng mô hình hoạt động của Tập đoàn, kết quả kinh doanh được phân tích theo từng khối và phân tách theo từng lĩnh vực cụ thể. Cách tiếp cận này giúp đánh giá chính xác, hiệu quả vận hành và đóng góp của từng lĩnh vực hoạt động vào tăng trưởng chung của Tập đoàn. Cụ thể, hoạt động kinh doanh của Tập đoàn được chia thành ba khối chính, bao gồm: khối Công nghệ với hai lĩnh vực là Dịch vụ CNTT cho thị trường nước ngoài và Dịch vụ CNTT cho thị trường trong nước; khối Viễn thông với hai lĩnh vực Dịch vụ Viễn thông và Dịch vụ Nội dung số; khối Giáo dục, Đầu tư và Khác.
Cơ cấu doanh thu theo khối
Cơ cấu lợi nhuận trước thuế theo khối
6.132 8,8%
2.773 21,2%
0,05%
23,1%
Báo cáo của Ban Điều hành về kết quả kinh doanh 2025 và nhận định 2026
Đánh giá của HĐQT về hoạt động của Tập đoàn
70.113
13.044
11,6%
17,8%
44.475 63,4% 19.507 27,8%
5.907 45,3%
4.364 33,5%
10,8%
13,7%
21,6%
12,9%
Khối Công nghệ Khối Viễn thông Khối Giáo dục, Đầu tư và Khác
Đơn vị: Tỷ VNĐ

Gợi ý tự động: trang gold [60], trang được trích [60]

---

## t16 · chart · status `answered`

**Câu hỏi:** Theo biểu đồ doanh thu Dịch vụ Chuyển đổi số giai đoạn 2021-2025, doanh thu Dịch vụ Chuyển đổi số năm 2023 là bao nhiêu?

**Đáp án chuẩn:** 10.425 tỷ VNĐ.
- Evidence gốc trang 63 (chart; Biểu đồ cột 'Doanh thu Dịch vụ Chuyển đổi số giai đoạn 2021-2025', cột xanh năm 2023): Chuyển đổi số: 5.522 | 7.349 | 10.425 | 14.340 | 16.751; CNTT nước ngoài: 14.541 | 18.915 | 24.288 | 30.953 | 35.382 (tỷ VNĐ)

**Tool:** search('doanh thu Dịch vụ Chuyển đổi số 2021-2025 biểu đồ') → search('Dịch vụ Chuyển đổi số doanh thu 2023')

**Câu trả lời:** Theo biểu đồ "Doanh thu Dịch vụ Chuyển đổi số giai đoạn 2021-2025" (trang 63), doanh thu Dịch vụ Chuyển đổi số năm 2023 là 10.425 tỷ VNĐ (cột xanh; cột cam tương ứng là 24.288 tỷ VNĐ - doanh thu dịch vụ CNTT cho thị trường nước ngoài).

**Citation:**
- `ar_p63_v0` (trang 63, visual): [chart] Doanh thu Dịch vụ Chuyển đổi số giai đoạn 2021-2025
Biểu đồ cột nhóm. Trục tung: 0; 5.000; 10.000; 15.000; 20.000; 25.000; 30.000; 35.000; 40.000. Đơn vị: Tỷ VNĐ. Trục hoành: 2021, 2022, 2023, 2024, 2025. Chú giải: cột cam = Doanh thu dịch vụ CNTT cho thị trường nước ngoài; cột xanh = Doanh thu dịch vụ Chuyển đổi số. Giá trị theo năm: 2021: 14.541 và 5.522; 2022: 18.915 và 7.349; 2023: 24.288 và 10.425; 2024: 30.953 và 14.340; 2025: 35.382 và 16.751.
- `ar_p63_t1` (trang 63, text): Việc kết hợp hiệu quả giữa năng lực công nghệ, hiểu biết theo ngành và lực lượng kỹ sư được đào tạo bài bản giúp FPT từng bước khẳng định vai trò là đối tác chuyển đổi số chiến lược, đồng hành cùng khách hàng trong các chương trình chuyển đổi dài hạn. Trên nền tảng đó, Việt Nam và FPT ngày càng trở thành mắt xích quan trọng trong chuỗi giá trị dịch vụ CNTT toàn cầu, có khả năng cạnh tranh với các tập đoàn lớn trong cùng ngành.
Doanh thu Dịch vụ Chuyển đổi số giai đoạn 2021-2025
Nền tảng AI linh hoạt FleziPT với phương pháp, quy trình và giải pháp đã được kiểm chứng hiệu quả
14.541
18.915
24.288
30.953
35.382
40.000
5.522
7.349
10.425
14.340
16.751
35.000
30.000
25.000
20.000
Báo cáo của Ban Điều hành về kết quả kinh doanh 2025 và nhận định 2026
15.000
10.000
Đánh giá của HĐQT về hoạt động của Tập đoàn
5.000
Đơn vị: Tỷ VNĐ
Doanh thu dịch vụ Chuyển đổi số
Doanh thu dịch vụ CNTT cho thị trường nước ngoài

Gợi ý tự động: trang gold [63], trang được trích [63]

---

## t17 · multihop · status `abstain`

**Câu hỏi:** Doanh thu kế hoạch năm 2026 thấp hơn doanh thu thực hiện năm 2025 bao nhiêu tỷ đồng, và vì sao số kế hoạch lại thấp hơn?

**Đáp án chuẩn:** Thấp hơn 11.533 tỷ VNĐ (70.113 − 58.580). Nguyên nhân: từ năm 2026 FPT hợp nhất FPT Telecom theo phương pháp vốn chủ sở hữu (số liệu 2025 đã điều chỉnh theo cùng phương pháp để so sánh, nên kế hoạch vẫn tăng 15,8%).
- Evidence gốc trang 12 (table; Bảng 2021-2025, hàng 'Tổng doanh thu', 2025): 70.113
- Evidence gốc trang 55 (chart; Kế hoạch năm 2026: 'Doanh thu 58.580 tỷ VNĐ, 15,8% so với cùng kỳ' và chú thích dưới biểu đồ): Đối với số liệu năm 2026, Tập đoàn hợp nhất Công ty Cổ phần Viễn thông FPT (FPT Telecom) theo phương pháp vốn chủ sở hữu, số liệu năm 2025 đã được điều chỉnh theo cùng phương pháp
- Phép tính: 70.113 − 58.580 = 11.533

**Tool:** search('kế hoạch doanh thu 2026') → search('doanh thu thực hiện 2025') → search('vì sao kế hoạch doanh thu 2026 thấp hơn 2025 hợp nhất FPT Telecom vốn chủ sở hữu') → search('nhận định 2026 kế hoạch kinh doanh doanh thu 58.580')

**Câu trả lời:** Không đủ bằng chứng để trả lời.

Tài liệu cho thấy kế hoạch doanh thu 2026 là 58.580 tỷ đồng, tăng 15,8% so với cùng kỳ [ar_p55_v0], trong khi doanh thu hợp nhất thực hiện năm 2025 là 70.113 tỷ đồng [ar_p107_t0]. Tuy nhiên, số kế hoạch 2026 được lập trên cơ sở hợp nhất FPT Telecom theo phương pháp vốn chủ sở hữu, và số liệu 2025 trong biểu đồ kế hoạch đã được điều chỉnh lại theo cùng phương pháp (tổng doanh thu 2025 điều chỉnh = 44.475 + 6.132 = 50.607 tỷ đồng) [ar_p55_v0][ar_p55_t0]. Báo cáo không nêu trực tiếp việc so sánh kế hoạch 2026 với doanh thu thực hiện 2025 (70.113 tỷ đồng) hay lý do kế hoạch thấp hơn con số này, nên không có bằng chứng để kết luận mức chênh lệch và nguyên nhân theo đúng cách đặt câu hỏi.

**Citation:**
- (không có)

Gợi ý tự động: trang gold [12, 55], trang được trích []

---

## t18 · multihop · status `answered`

**Câu hỏi:** Cổ đông cá nhân lớn nhất của FPT nắm bao nhiêu phần trăm cổ phần và người đó giữ vai trò gì tại FPT?

**Đáp án chuẩn:** Ông Trương Gia Bình, 117.347.966 cổ phần (6,89%); thành viên sáng lập, Chủ tịch HĐQT.
- Evidence gốc trang 33 (table; Bảng 'Top 10 cổ đông lớn', STT 1): Ông Trương Gia Bình | 117.347.966 | 6,89%
- Evidence gốc trang 37 (text; Giới thiệu Ban lãnh đạo, mục Ông Trương Gia Bình): Thành viên sáng lập, Chủ tịch HĐQT

**Tool:** search('cổ đông cá nhân lớn nhất nắm giữ cổ phần') → search('cơ cấu cổ đông tỷ lệ sở hữu cá nhân') → search('Trương Gia Bình Chủ tịch HĐQT')

**Câu trả lời:** Cổ đông cá nhân lớn nhất của FPT là ông Trương Gia Bình, nắm 117.347.966 cổ phần, tương đương 6,89% tổng số cổ phiếu đã phát hành [ar_p33_t0]. Ông giữ vai trò Chủ tịch HĐQT FPT (nhiệm kỳ 2022–2027, tái bầu cử 07/04/2022) [ar_p86_t0][ar_p90_v0].

**Citation:**
- `ar_p33_t0` (trang 33, text): • Cơ cấu cổ đông theo quốc tịch
• Top 10 cổ đông lớn
Đối tượng STT Số cổ phần Tỷ lệ
Đối tượng Số lượng cổ đông Tỷ lệ/ Tổng số cổ đông
Tỷ lệ/Tổng số cổ phiếu đã phát hành
Số lượng cổ phiếu sở hữu
6,89%
Ông Trương Gia Bình
117.347.966
124.667
97,8%
1.043.777.633
61,27%
5,67%
Việt Nam
96.585.637
Tổng Công ty Đầu tư và Kinh doanh vốn Nhà nước – Công ty TNHH
Cá nhân
124.385
97,6%
744.568.681
43,71%
3,67%
Công ty TNHH QT
62.449.511
Tổ chức
0,2%
299.208.952
17,56%
1,76%
PYN ELITE FUND (NON-UCITS)
30.044.600
Thông tin chung
2.821
2,2%
659.729.488
38,73%
Nước ngoài
Sứ mệnh, giá trị cốt lõi
1,48%
Ông Bùi Quang Ngọc
25.255.715
Cá nhân
2.334
1,8%
15.995.614
0,94%
Ngành nghề kinh doanh
1,47%
Bà Trương Thị Thanh Thanh
25.095.835
Vị thế và quy mô
Tổ chức
0,4%
643.733.874
37,79%
1,35%
Quỹ ETF DCVFMVN DIAMOND
22.966.161
Hành trình khẳng định năng lực và vị thế
Tổng số
127.488
100,00%
1.703.507.121
100,00%
Cơ cấu quản trị và bộ máy quản lý
1,31%
NTASIAN DISCOVERY MASTER FUND
22.250.000
Ban Lãnh đạo
1,17%
EMPLOYEES PROVIDENT FUND BOARD
20.000.000
1,03%
17.597.379
- `ar_p86_t0` (trang 86, text): Danh sách Thành viên HĐQT nhiệm kỳ 2022-2027 và số cuộc họp tham dự trong năm 2025
Thành viên HĐQT Chức vụ tại FPT và các công ty khác Kinh nghiệm chuyên môn Tỷ lệ sở hữu Ngày bắt đầu là thành viên HĐQT Số buổi họp HĐQT tham dự Tỷ lệ tham dự họp
Ông Trương Gia Bình Chủ tịch HĐQT FPT
CNTT 6,89% 07/04/2022 Tái bầu cử 07/07 100%
Thành viên HĐQT FPT Telecom
Chủ tịch HĐTV FPT Education
Thành viên Hội đồng Trường Đại học FPT
Ông Bùi Quang Ngọc Phó chủ tịch HĐQT FPT
CNTT 1,48% 07/04/2022 Tái bầu cử 06/07 86%
Chủ sở hữu Công ty TNHH BĐS BQ
Mô hình quản trị và vai trò của các bên liên quan
Thành viên Hội đồng Trường Đại học FPT
Quản trị công ty năm 2025
Báo cáo của HĐQT
Ông Đỗ Cao Bảo Ủy viên HĐQT FPT
Báo cáo của Ban Kiểm soát
CNTT 0,93% 07/04/2022 Tái bầu cử 07/07 100%
Cổ đông lớn Công ty CP Đầu tư và Thương mại BDM
Ủy viên HĐQT Công ty Cổ phần Đô thị FPT Đà Nẵng
Thành viên góp vốn Công ty TNHH BDMD Aumoria Đà Nẵng
Ông Jean-Charles Belliol Ủy viên HĐQT độc lập Tài chính 0,00% 07/04/2022 Tái bầu cử 07/07 100%
- `ar_p90_v0` (trang 90, visual): [table] Chi tiết thù lao của từng thành viên HĐQT năm 2025
Đơn vị: VNĐ

| Thành viên HĐQT | Chức danh | Thù lao |
|---|---|---:|
| Ông Trương Gia Bình | Chủ tịch HĐQT | 0 |
| Ông Bùi Quang Ngọc | Phó chủ tịch HĐQT | 0 |
| Ông Đỗ Cao Bảo | Ủy viên HĐQT | 0 |
| Ông Jean-Charles Belliol | Ủy viên HĐQT | 960.000.000 |
| Ông Hiroshi Yokotsuka | Ủy viên HĐQT | 2.613.975.000 |
| Ông Hampapur Rangadore Binod | Ủy viên HĐQT | 2.613.975.000 |
| Bà Trần Thị Hồng Linh | Ủy viên HĐQT | 360.000.000 |

Gợi ý tự động: trang gold [33, 37], trang được trích [33, 86, 90]

---

## t19 · multihop · status `answered`

**Câu hỏi:** Năm 2025, doanh thu Dịch vụ CNTT cho thị trường nước ngoài gấp khoảng bao nhiêu lần doanh thu khối Viễn thông?

**Đáp án chuẩn:** Khoảng 1,81 lần (35.382 / 19.507 tỷ VNĐ).
- Evidence gốc trang 63 (chart; Biểu đồ 'Doanh thu Dịch vụ Chuyển đổi số giai đoạn 2021-2025', cột cam 2025): Doanh thu dịch vụ CNTT cho thị trường nước ngoài 2025: 35.382
- Evidence gốc trang 60 (chart; Biểu đồ 'Cơ cấu doanh thu theo khối', lát Khối Viễn thông): 19.507
- Phép tính: 35.382 / 19.507 = 1,81

**Tool:** search('doanh thu dịch vụ CNTT thị trường nước ngoài 2025') → search('doanh thu khối Viễn thông 2025')

**Câu trả lời:** Khoảng 1,8 lần. Doanh thu Dịch vụ CNTT cho thị trường nước ngoài năm 2025 đạt 35.382 tỷ đồng [ar_p62_t0], trong khi doanh thu Khối Viễn thông là 19.507 tỷ đồng [ar_p60_v0]. Tỷ lệ: 35.382 / 19.507 ≈ 1,81 lần.

**Citation:**
- `ar_p62_t0` (trang 62, text): Năm 2025, lĩnh vực Dịch vụ CNTT cho thị trường nước ngoài tiếp tục giữ vai trò trụ cột trong chiến lược tăng trưởng của Tập đoàn với doanh thu đạt 35.382 tỷ đồng, tăng 14,3%; lợi nhuận trước thuế đạt 5.467 tỷ đồng, tăng 14,6%. Kết quả này đạt được trong bối cảnh ngành dịch vụ CNTT toàn cầu tiếp tục đối mặt với nhiều thách thức, bao gồm bất ổn địa chính trị kéo dài, chính sách tiền tệ thắt chặt tại các nền kinh tế lớn, xu hướng doanh nghiệp kiểm soát chặt chẽ ngân sách CNTT và kéo dài chu kỳ ra quyết định đầu tư.
- `ar_p60_v0` (trang 60, visual): [chart] Cơ cấu doanh thu theo khối
Biểu đồ vòng tròn (donut) thể hiện cơ cấu doanh thu theo khối. Không có trục; đơn vị: Tỷ VND. Tổng/trung tâm: 70.113 (mũi tên tăng 11,6%). Chú giải: Khối Công nghệ (cam); Khối Viễn thông (xanh dương); Khối Giáo dục, Đầu tư và Khác (xanh lá). Số liệu: Khối Công nghệ: 44.475, 63,4% (mũi tên tăng 13,7%); Khối Viễn thông: 19.507, 27,8% (mũi tên tăng 10,8%); Khối Giáo dục, Đầu tư và Khác: 6.132, 8,8% (mũi tên tăng 0,05%). Số liệu thuộc trang Báo cáo thường niên FPT 2025.

Gợi ý tự động: trang gold [60, 63], trang được trích [60, 62]

---

## t20 · multihop · status `answered`

**Câu hỏi:** Nếu áp tỷ trọng doanh thu của thị trường Nhật Bản lên tổng doanh thu năm 2025, doanh thu từ Nhật Bản ước khoảng bao nhiêu tỷ đồng?

**Đáp án chuẩn:** Khoảng 15.986 tỷ VNĐ (22,8% × 70.113 tỷ VNĐ).
- Evidence gốc trang 27 (chart; Biểu đồ 'Doanh thu theo khu vực địa lý', lát Nhật Bản): 22,8%
- Evidence gốc trang 12 (table; Bảng 2021-2025, hàng 'Tổng doanh thu', 2025): 70.113
- Phép tính: 0,228 × 70.113 = 15.985,8 ≈ 15.986. Chấp nhận làm tròn 15.985–15.986 hoặc ≈16 nghìn tỷ nếu nêu phép tính.

**Tool:** search('doanh thu thị trường Nhật Bản tỷ trọng') → search('tổng doanh thu năm 2025')

**Câu trả lời:** Theo biểu đồ doanh thu theo khu vực địa lý, Nhật Bản chiếm 22,8% doanh thu [ar_p27_v2]. Tổng doanh thu năm 2025 là 70.113 tỷ đồng [ar_p10_v0]. Áp tỷ trọng này: 70.113 × 22,8% ≈ 15.986 tỷ đồng (khoảng 15.986 tỷ đồng).

**Citation:**
- `ar_p27_v2` (trang 27, visual): [chart] Doanh thu theo khu vực địa lý
Biểu đồ tròn dạng vành khuyên, đơn vị: %. Các lát: Việt Nam 48,9%; Châu Mỹ 11,6%; Châu Âu 5,6%; Nhật Bản 22,8%; Châu Á-Thái Bình Dương 11,1%. Chú giải màu: Việt Nam; Châu Mỹ; Châu Âu; Nhật Bản; Châu Á-Thái Bình Dương. Chú giải vòng: Việt Nam; Nước ngoài.
- `ar_p10_v0` (trang 10, visual): [chart] Tổng doanh thu
Biểu đồ cột. Trục hoành: năm 2021, 2022, 2023, 2024, 2025. Trục tung: 0; 15.000; 30.000; 45.000; 60.000; 75.000. Chú giải: mỗi cột tương ứng một năm. Đơn vị: Tỷ VND. Giá trị theo năm: 2021: 35.657; 2022: 44.010; 2023: 52.618; 2024: 62.849; 2025: 70.113. Số liệu nổi bật: 70.113 Tỷ VND; tăng 11,6% so với cùng kỳ.

Gợi ý tự động: trang gold [12, 27], trang được trích [10, 27]

---

## t21 · text · status `answered`

**Câu hỏi:** Năm 2025 tỷ lệ nghỉ việc chủ động của FPT là bao nhiêu?

**Đáp án chuẩn:** 15,4%, nằm trong ngưỡng kiểm soát an toàn.
- Evidence gốc trang 137 (text; Mục 'Sự đa dạng về văn hóa...', đoạn 2): FPT vẫn duy trì sự ổn định về nhân sự với tỷ lệ nghỉ việc chủ động ở mức 15,4%, nằm trong ngưỡng kiểm soát an toàn

**Tool:** search('tỷ lệ nghỉ việc chủ động') → search('nghỉ việc chủ động 2025')

**Câu trả lời:** Năm 2025, tỷ lệ nghỉ việc chủ động của FPT là 15,4% — nằm trong ngưỡng kiểm soát an toàn [ar_p137_t3]. Theo bảng chỉ tiêu ESG cam kết, chỉ tiêu "tỷ lệ nghỉ việc thấp hơn mức trung bình thị trường (Khối Công nghệ)" có cam kết 2025 là dưới 14%, kết quả 2025 thực tế 15,4% (cao hơn cam kết), cam kết 2026 là dưới 15% [ar_p115_v0].

**Citation:**
- `ar_p137_t3` (trang 137, text): Trong bối cảnh thị trường lao động có nhiều biến động, FPT vẫn duy trì sự ổn định về nhân sự với tỷ lệ nghỉ việc chủ động ở mức 15,4%, nằm trong ngưỡng kiểm soát an toàn, bảo đảm tính liên tục của hoạt động kinh doanh. Cơ cấu nhân sự cho thấy sự cân bằng và kế thừa bền vững, với 43,9% nhân sự dưới 30 tuổi, 13,0% trên 40 tuổi, 53,2% cán bộ quản lý dưới 40 tuổi. Nhân sự có trình độ đại học và sau đại học chiếm trên 84% tổng số nhân sự toàn Tập đoàn.
20.000
15.000
10.000
5.000
Cán bộ quản lý dưới 40 tuổi 53,2%
Nhân sự dưới 30 tuổi 43,9%
- `ar_p115_v0` (trang 115, visual): [table] CÁC CHỈ TIÊU ESG CAM KẾT
| TT | Cam kết | Chỉ tiêu | Cam kết 2025 | Kết quả 2025 | Cam kết 2026 |
|---|---|---|---|---|---|
| **QUẢN TRỊ XUẤT SẮC** | | | | | |
| 1 | Quản trị an toàn thông tin | Số lượng sự cố an toàn thông tin ảnh hưởng đến danh tiếng Tập đoàn bằng 0. | 0 | 0 | 0 |
| | | 100% CBNV trải qua đào tạo/diễn tập an toàn bảo mật thông tin. | 100% | 100% | 100% |
| 2 | Quản trị mua sắm bền vững | 100% cán bộ mua sắm được đào tạo về mua sắm bền vững. | 100% | 100% | 100% |
| | | Không ký hợp đồng với các nhà cung cấp có các hoạt động ảnh hưởng đến sức khỏe, an toàn lao động và môi trường. | 100% | 100% | 100% |
| **MÔI TRƯỜNG LÀM VIỆC ĐẲNG CẤP, HẠNH PHÚC** | | | | | |
| 3 | Nơi làm việc hạnh phúc | Tỷ lệ nghỉ việc thấp hơn so với mức trung bình thị trường (Khối Công nghệ). | Dưới 14% | 15,4% | Dưới 15% |
| | | Hỗ trợ CBNV mua nhà, mua xe. | 5.000 | 3.904 | 4.250 |
| 4 | Tổ chức học tập suốt đời | Đẩy mạnh và nâng cao số giờ học trung bình CBNV/năm (giờ). | 150 | 151 | 162 |
| 5 | Bình đẳng và đa dạng | Tỷ lệ nữ giới trong tổng số nhân sự. | Trên 1/3 | 37,7% | Trên 1/3 |
| | | Tỷ lệ nữ giới là quản lý trong tổng số nhân sự quản lý. | 1/3 | 36,4% | 1/3 |
| **HOẠT ĐỘN

Gợi ý tự động: trang gold [137], trang được trích [115, 137]

---

## t22 · text · status `answered`

**Câu hỏi:** Năm 2025, mô hình Mentor – Mentee của FPT thu hút bao nhiêu Mentor, Mentee và bao nhiêu giờ sinh hoạt?

**Đáp án chuẩn:** 1.581 Mentor, 10.606 Mentee, 209.138 giờ sinh hoạt (cao hơn 2,1 lần so với năm 2024).
- Evidence gốc trang 138 (text; Mục 'Đào tạo phát triển', đoạn 2): thu hút 1.581 Mentor và 10.606 Mentee tham gia với 209.138 giờ sinh hoạt, cao hơn 2,1 lần so với năm 2024

**Tool:** search('Mentor Mentee') → search('chương trình Mentor - Mentee giờ sinh hoạt')

**Câu trả lời:** Năm 2025, mô hình Mentor – Mentee thu hút 1.581 Mentor và 10.606 Mentee tham gia, với 209.138 giờ sinh hoạt (cao hơn 2,1 lần so với năm 2024) [ar_p138_t3].

**Citation:**
- `ar_p138_t3` (trang 138, text): Bên cạnh đó, mô hình Mentor – Mentee tiếp tục được mở rộng, thu hút 1.581 Mentor và 10.606 Mentee tham gia với 209.138 giờ sinh hoạt, cao hơn 2,1 lần so với năm 2024, góp phần lan tỏa tri thức và kinh nghiệm quản lý trong nội bộ. Công tác phát triển đội ngũ quản lý được đẩy mạnh thông qua các chương trình MiniMBA và đào tạo cán bộ quản lý cấp trung với hơn 47.000 giờ học trong năm 2025 tập trung nâng cao năng lực quản trị, điều hành và xây dựng đội ngũ lãnh đạo kế cận.
Một số chương trình đào tạo tiêu biểu dành cho sinh viên và người mới tốt nghiệp (Fresher):
Thông điệp và định hướng ESG
Quản trị hướng đến phát triển bền vững
• Chương trình thực tập từ 02-03 tháng tại FPT và công ty thành viên nhằm giúp củng cố kiến thức và kinh nghiệm làm việc thực tế thông qua sự hướng dẫn của các chuyên gia và lãnh đạo quản lý đã đón hơn 3.000 sinh viên thực tập trong năm 2025;
Môi trường làm việc đẳng cấp, hạnh phúc
Hoạt động vì môi trường xanh

Gợi ý tự động: trang gold [138], trang được trích [138]

---

## t23 · text · status `answered`

**Câu hỏi:** Theo báo cáo, giá trị thị trường Agentic AI năm 2025 là bao nhiêu và được dự báo đạt bao nhiêu vào năm 2034?

**Đáp án chuẩn:** 7,3 tỷ USD năm 2025, dự báo tăng lên 139,2 tỷ USD vào năm 2034 (9,1 tỷ USD năm 2026).
- Evidence gốc trang 47 (text; Cột trái, đoạn 2): Agentic AI nổi lên như một động lực tăng trưởng mới của thị trường với giá trị đạt 7,3 tỷ USD trong năm 2025 và được dự báo tăng từ 9,1 tỷ USD năm 2026 lên 139,2 tỷ USD vào năm 2034

**Tool:** search('giá trị thị trường Agentic AI 2025 dự báo 2034') → search('Agentic AI market size forecast')

**Câu trả lời:** Theo báo cáo (trang 47), Agentic AI đạt giá trị 7,3 tỷ USD trong năm 2025 và được dự báo tăng từ 9,1 tỷ USD năm 2026 lên 139,2 tỷ USD vào năm 2034 [ar_p47_t1].

**Citation:**
- `ar_p47_t1` (trang 47, text): Bối cảnh chung
Song song với xu hướng tối ưu hạ tầng và triển khai AI linh hoạt, Agentic AI nổi lên như một động lực tăng trưởng mới của thị trường với giá trị đạt 7,3 tỷ USD trong năm 2025 và được dự báo tăng từ 9,1 tỷ USD năm 2026 lên 139,2 tỷ USD vào năm 2034. Xu hướng này cho thấy sự chuyển dịch mạnh mẽ sang các hệ thống tự động thực thi nhiệm vụ với sự can thiệp của con người ở mức tối thiểu, qua đó tái định hình cách doanh nghiệp vận hành, từ tự động hóa quy trình đến hỗ trợ ra quyết định thông minh.

Gợi ý tự động: trang gold [47], trang được trích [47]

---

## t24 · text · status `answered`

**Câu hỏi:** Theo báo cáo, Ấn Độ triển khai chương trình nào để xây dựng năng lực tính toán trong nước và trị giá bao nhiêu?

**Đáp án chuẩn:** Chương trình IndiaAI Mission trị giá 1,25 tỷ USD.
- Evidence gốc trang 48 (text; Cột phải, mục 'Xung đột địa chính trị và chiến tranh thương mại...', đoạn 3): Ấn Độ triển khai chương trình IndiaAI Mission trị giá 1,25 tỷ USD để xây dựng năng lực tính toán trong nước

**Tool:** search('Ấn Độ chương trình năng lực tính toán') → search('Ấn Độ đầu tư AI tính toán quốc gia')

**Câu trả lời:** Ấn Độ triển khai chương trình **IndiaAI Mission** trị giá **1,25 tỷ USD** để xây dựng năng lực tính toán trong nước [ar_p48_t3].

**Citation:**
- `ar_p48_t3` (trang 48, text): AI trở thành sức mạnh quốc gia. Các nước đang đầu tư mạnh để xây dựng hạ tầng tính toán riêng và mô hình AI dựa trên dữ liệu bản địa. Hàn Quốc ra mắt AI Champions trị giá 530 tỷ Won để phát triển LLM bản địa như: HyperCLOVA X của Naver và Exaone của LG nhằm giảm sự phụ thuộc vào OpenAI và Google. Canada cam kết đầu tư 02 tỷ USD cho chiến lược tính toán AI chủ quyền. Chính phủ Nhật Bản hỗ trợ phát triển LLM tập trung vào tiếng Nhật và dữ liệu công nghiệp đặc thù để bảo vệ văn hóa và an ninh dữ liệu. Ấn Độ triển khai chương trình IndiaAI Mission trị giá 1,25 tỷ USD để xây dựng năng lực tính toán trong nước.
Đơn vị: Tỷ USD
Quy mô thị trường AI doanh nghiệp
37,0 3,2x

Gợi ý tự động: trang gold [48], trang được trích [48]

---

## tu1 · unanswerable · status `abstain`

**Câu hỏi:** Lượng phát thải khí nhà kính Phạm vi 3 của FPT năm 2025 là bao nhiêu tấn CO2 tương đương?

**Hành vi mong đợi:** tìm rồi từ chối. Kiểm tra trong tài liệu: Bảng trang 146 chỉ ghi Phạm vi 3 năm 2025 là 'Triển khai tại FPT Software', không có số; tổng 127.952 chỉ gồm Phạm vi 1 và 2. Trang 148 chỉ mô tả hoạt động giảm phát thải Phạm vi 3.

**Tool:** search('phát thải khí nhà kính Phạm vi 3') → search('Scope 3 tấn CO2 tương đương 2025')

**Câu trả lời:** Không đủ bằng chứng để trả lời. Bảng tổng hợp phát thải khí nhà kính năm 2025 của FPT chỉ nêu định tính đối với Phạm vi 3: "Triển khai tại FPT Software" (năm 2024: triển khai thí điểm tại FPT Software; năm 2023: chưa triển khai), không công bố con số tấn CO2 tương đương cho Phạm vi 3. Tổng phát thải năm 2025 là 127.952 tấn CO2 tương đương, trong đó Phạm vi 1 là 4.383 và Phạm vi 2 là 123.569 tấn.

**Citation:**
- (không có)

Gợi ý tự động: trang gold [], trang được trích []

---

## tu2 · unanswerable · status `abstain`

**Câu hỏi:** Kế hoạch lợi nhuận sau thuế năm 2026 của FPT là bao nhiêu?

**Hành vi mong đợi:** tìm rồi từ chối. Kiểm tra trong tài liệu: Kế hoạch 2026 (trang 55) chỉ có doanh thu 58.580 và lợi nhuận trước thuế 11.629 tỷ VNĐ. Tìm 'LNST'/'lợi nhuận sau thuế' gần '2026' trên toàn bộ tài liệu: không có.

**Tool:** search('kế hoạch lợi nhuận sau thuế năm 2026') → search('mục tiêu kế hoạch kinh doanh 2026') → search('lợi nhuận sau thuế cổ đông công ty mẹ kế hoạch 2026') → search('chỉ tiêu kế hoạch 2026 LNST EPS cổ tức') → search('nghị quyết HĐQT kế hoạch doanh thu lợi nhuận 2026 trình Đại hội đồng cổ đông') → search('mục tiêu 2026 doanh thu 75.000 lợi nhuận sau thuế') → search('Kế hoạch năm 2026 các mục tiêu chủ yếu doanh thu lợi nhuận trước thuế 58.580 11.629') → search('dự báo 2026 lợi nhuận sau thuế thuộc về cổ đông công ty mẹ') → search('kế hoạch 2026 LNST sau thuế 10.000 tỷ EPS cổ tức dự kiến') → search('Đại hội đồng cổ đông 2026 thông qua kế hoạch kinh doanh')

**Câu trả lời:** Không đủ bằng chứng để trả lời. Tài liệu (trang 55 – "Kế hoạch năm 2026") chỉ nêu kế hoạch doanh thu 58.580 tỷ VNĐ (tăng 15,8%) và lợi nhuận trước thuế 11.629 tỷ VNĐ (tăng 15,0%) [ar_p55_t0, ar_p55_v1]; không có chỉ tiêu kế hoạch lợi nhuận sau thuế năm 2026.

**Citation:**
- (không có)

Gợi ý tự động: trang gold [], trang được trích []

---

## tu3 · unanswerable · status `abstain`

**Câu hỏi:** Kế hoạch doanh thu năm 2026 của khối Viễn thông là bao nhiêu?

**Hành vi mong đợi:** tìm rồi từ chối. Kiểm tra trong tài liệu: Biểu đồ kế hoạch 2026 (trang 55) chỉ có khối Công nghệ và khối Giáo dục, Đầu tư và Khác vì FPT Telecom được hợp nhất theo phương pháp vốn chủ sở hữu từ 2026. Trang 69-71 (Khối Viễn thông) chỉ nêu định hướng 2026-2028, không có số.

**Tool:** search('kế hoạch doanh thu 2026 khối Viễn thông') → search('mục tiêu doanh thu 2026 Viễn thông FPT Telecom') → search('kế hoạch 2026 khối Viễn thông doanh thu lợi nhuận mục tiêu') → search('FPT Telecom kế hoạch doanh thu 2026 tỷ đồng') → search('kế hoạch kinh doanh 2026 FPT Telecom doanh thu lợi nhuận trước thuế') → search('nhận định 2026 khối Viễn thông mục tiêu tăng trưởng')

**Câu trả lời:** Không đủ bằng chứng để trả lời. Trang kế hoạch năm 2026 (tr.55) chỉ trình bày kế hoạch doanh thu/lợi nhuận trước thuế theo hai nhóm "Khối Công nghệ" và "Khối Giáo dục, Đầu tư và Khác" (do từ năm 2026 Tập đoàn hợp nhất FPT Telecom theo phương pháp vốn chủ sở hữu), không có số kế hoạch doanh thu riêng cho khối Viễn thông [ar_p55_t0][ar_p55_v0]. Các nội dung về khối Viễn thông chỉ nêu định hướng 2026-2028 và kết quả 2025, không nêu con số doanh thu kế hoạch 2026 [ar_p69_t0][ar_p58_t4].

**Citation:**
- (không có)

Gợi ý tự động: trang gold [], trang được trích []

---

## tu4 · unanswerable · status `abstain`

**Câu hỏi:** Tỷ lệ chi trả cổ tức bằng tiền mặt dự kiến cho năm 2026 là bao nhiêu?

**Hành vi mong đợi:** tìm rồi từ chối. Kiểm tra trong tài liệu: Chỉ có số liệu cổ tức đã trả (trang 11, 12) và tỷ lệ lợi nhuận trả cổ tức 2024/2025 (34,9%/34,0%, trang 58). Tìm 'cổ tức' gần '2026': không có.

**Tool:** search('cổ tức tiền mặt dự kiến năm 2026') → search('tỷ lệ chi trả cổ tức') → search('kế hoạch cổ tức năm 2026') → search('ĐHĐCĐ 2026 phương án phân phối lợi nhuận') → search('chính sách chi trả cổ tức tiền mặt năm 2026 tỷ lệ mệnh giá') → search('cổ tức dự kiến 2026 20% mệnh giá') → search('phương án phân phối lợi nhuận năm 2025 trình ĐHĐCĐ 2026 cổ tức') → search('tỷ lệ lợi nhuận trả cổ tức kế hoạch 2026') → search('chính sách cổ tức chi trả cổ tức bằng tiền mặt tỷ lệ dự kiến các năm tới') → search('thù lao HĐQT ngân sách 2026 tờ trình ĐHĐCĐ') → search('cổ tức năm 2026 dự kiến 20% tiền mặt cổ phiếu') → search('định hướng phân phối lợi nhuận cổ tức năm sau')

**Câu trả lời:** Không đủ bằng chứng để trả lời. Báo cáo chỉ nêu chính sách chi trả cổ tức tiền mặt năm 2025 (tạm ứng đợt 1 năm 2025 tỷ lệ 10%/mệnh giá, trả cổ tức còn lại năm 2024 bằng tiền mặt 10%/mệnh giá) [ar_p92_t1][ar_p207_t1] và kế hoạch kinh doanh năm 2026 (doanh thu, lợi nhuận trước thuế) [ar_p55_t0], không có số liệu về tỷ lệ chi trả cổ tức bằng tiền mặt dự kiến cho năm 2026.

**Citation:**
- (không có)

Gợi ý tự động: trang gold [], trang được trích []

---

## tu5 · unanswerable · status `abstain`

**Câu hỏi:** Năm 2025 FPT ghi nhận bao nhiêu vụ tai nạn lao động?

**Hành vi mong đợi:** tìm rồi từ chối. Kiểm tra trong tài liệu: 'tai nạn' chỉ xuất hiện ở trang 141 (bảo hiểm tai nạn cho CBNV); không có thống kê số vụ.

**Tool:** search('tai nạn lao động') → search('an toàn lao động số vụ tai nạn') → search('số vụ tai nạn lao động năm 2025') → search('sức khỏe an toàn lao động chỉ tiêu tai nạn') → search('tai nạn lao động số vụ xảy ra trong năm') → search('thương tật tai nạn CBNV thống kê')

**Câu trả lời:** Không đủ bằng chứng để trả lời.

**Citation:**
- (không có)

Gợi ý tự động: trang gold [], trang được trích []

---

## tu6 · unanswerable · status `abstain`

**Câu hỏi:** Doanh thu Dịch vụ Chuyển đổi số của FPT năm 2020 là bao nhiêu?

**Hành vi mong đợi:** tìm rồi từ chối. Kiểm tra trong tài liệu: Biểu đồ doanh thu Dịch vụ Chuyển đổi số (trang 63) chỉ có 2021-2025. Tìm '2020' gần 'chuyển đổi số': không có.

**Tool:** search('doanh thu dịch vụ chuyển đổi số 2020') → search('chuyển đổi số doanh thu qua các năm')

**Câu trả lời:** Không đủ bằng chứng để trả lời. Tài liệu chỉ cung cấp doanh thu Dịch vụ Chuyển đổi số giai đoạn 2021–2025 (2021: 5.522 tỷ đồng; 2022: 7.349; 2023: 10.425; 2024: 14.340; 2025: 16.751 tỷ đồng), không có số liệu năm 2020.

**Citation:**
- (không có)

Gợi ý tự động: trang gold [], trang được trích []

---
