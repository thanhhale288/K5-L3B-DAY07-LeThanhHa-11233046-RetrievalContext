# Bảng chấm đạt/không đạt: `dev-full-hybrid-v2`

Cấu hình: `{'name': 'full-hybrid', 'kinds': ['table', 'text', 'visual'], 'retriever': 'hybrid', 'view_page': False, 'top_k': 5, 'max_steps': 8, 'max_views': 3, 'model': 'deepseek-chat', 'vision_model': None, 'index_chunks': 965}`

## d01 · table · status `answered`

**Câu hỏi:** Theo bảng tình hình tài chính giai đoạn 2021-2025, tổng tài sản của FPT năm 2022 là bao nhiêu và thay đổi thế nào so với năm 2021?

**Đáp án chuẩn:** 51.650 tỷ VNĐ, giảm 3,8% so với 2021 (53.698 tỷ VNĐ).
- Evidence gốc trang 12 (table; Bảng 'Tình hình tài chính và kết quả kinh doanh nổi bật giai đoạn 2021-2025', hàng 2 'Tổng tài sản', cột 2022 và +/-): 2021: 53.698 | 2022: 51.650 | +/-: -3,8% (đơn vị tỷ VNĐ)

**Tool:** search('tình hình tài chính 2021-2025 tổng tài sản') → search('tổng tài sản năm 2022')

**Câu trả lời:** Theo bảng "Tình hình tài chính và kết quả kinh doanh nổi bật giai đoạn 2021-2025" (đơn vị: Tỷ VNĐ), tổng tài sản năm 2022 là 51.650 tỷ VNĐ, giảm 3,8% so với năm 2021 (53.698 tỷ VNĐ), tức giảm khoảng 2.048 tỷ VNĐ.

**Citation:**
- `ar_p12_v0` (trang 12, visual): [table] Tình hình tài chính và kết quả kinh doanh nổi bật giai đoạn 2021-2025
Đơn vị: Tỷ VND

| STT | Chỉ tiêu | 2021 | +/- | 2022 | +/- | 2023 | +/- | 2024 | +/- | 2025 | +/- |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Vốn chủ sở hữu | 21.418 | 15,1% | 25.356 | 18,4% | 29.933 | 18,1% | 35.728 | 19,4% | 43.748 | 22,4% |
| 2 | Tổng tài sản | 53.698 | 28,7% | 51.650 | -3,8% | 60.283 | 16,7% | 72.000 | 19,4% | 88.142 | 22,4% |
| 3 | Tổng doanh thu | 35.657 | 19,5% | 44.010 | 23,4% | 52.618 | 19,6% | 62.849 | 19,4% | 70.113 | 11,6% |
| 4 | Lợi nhuận thuần từ hoạt động kinh doanh | 6.228 | 20,0% | 7.589 | 21,8% | 9.112 | 20,1% | 11.025 | 21,0% | 12.952 | 17,5% |
| 5 | Lợi nhuận trước thuế, lãi vay và khấu hao | 7.981 | 18,2% | 9.495 | 19,0% | 11.490 | 21,0% | 13.605 | 18,4% | 15.958 | 17,3% |
| 6 | Lợi nhuận trước thuế và lãi vay | 6.337 | 20,4% | 7.662 | 20,9% | 9.203 | 20,1% | 11.070 | 20,3% | 13.044 | 17,8% |
| 7 | Lợi nhuận trước thuế | 6.337 | 20,4% | 7.662 | 20,9% | 9.203 | 20,1% | 11.070 | 20,3% | 13.044 | 17,8% |
| 8 | Lợi nhuận sau thuế | 5.349 | 20,9% | 6.491 | 21,3% | 7.788 | 20,0% | 9.427 | 21,0% | 11.232 | 19,1% |
| 9 | Lợi nhuận sau thuế thuộc về cổ
- `ar_p12_t0` (trang 12, text): Tình hình tài chính và kết quả kinh doanh nổi bật giai đoạn 2021-2025
Số liệu tài chính trong Báo cáo này được trích xuất từ Báo cáo tài chính hợp nhất đã kiểm toán bao gồm Báo cáo tài chính Công ty mẹ, Báo cáo tài chính của các công ty do Tập đoàn nắm quyền kiểm soát (Công ty con) và kết quả kinh doanh hợp nhất của các công ty liên kết theo phương pháp vốn chủ.
Đơn vị: Tỷ VNĐ
STT Chỉ tiêu 2021 +/- 2022 +/- 2023 +/- 2024 +/- 2025 +/-
21.418
25.356
15,1%
18,4%
18,1%
29.933
35.728
19,4%
43.748
22,4%
Vốn chủ sở hữu
Con số nổi bật
Giải thưởng tiêu biểu
53.698
51.650
28,7%
-3,8%
16,7%
60.283
72.000
19,4%
88.142
22,4%
Tổng tài sản
Hoạt động nổi bật
35.657
44.010
19,5%
23,4%
19,6%
52.618
62.849
19,4%
70.113
11,6%
Tổng doanh thu
Dự án AI nổi bật
6.228
7.589
20,0%
21,8%
20,1%
9.112
11.025
21,0%
12.952
17,5%
Lợi nhuận thuần từ hoạt động kinh doanh
7.981
9.495
18,2%
19,0%
21,0%
11.490
13.605
18,4%
15.958
17,3%
Lợi nhuận trước thuế, lãi vay và khấu hao
6.337
7.662
20,4%
20,9%
20,1%
9.203
11.070
20,3%
13.044
17,8%
Lợi nhuận trước thuế và lãi vay
6.337
7.662
20,4%
20,9%
20,1%

Gợi ý tự động: trang gold [12], trang được trích [12]

---

## d02 · table · status `answered`

**Câu hỏi:** Cổ đông lớn thứ ba trong danh sách Top 10 cổ đông lớn của FPT là ai, nắm bao nhiêu cổ phần và tỷ lệ bao nhiêu?

**Đáp án chuẩn:** Công ty TNHH QT, 62.449.511 cổ phần, 3,67%.
- Evidence gốc trang 33 (table; Bảng 'Top 10 cổ đông lớn', STT 3): Công ty TNHH QT | 62.449.511 | 3,67%

**Tool:** search('Top 10 cổ đông lớn FPT') → search('cổ đông lớn tỷ lệ sở hữu cổ phần')

**Câu trả lời:** Cổ đông lớn thứ ba trong Top 10 cổ đông lớn của FPT là Công ty TNHH QT, nắm 62.449.511 cổ phần, tương đương 3,67% [ar_p33_v1].

**Citation:**
- `ar_p33_v1` (trang 33, visual): [table] Top 10 cổ đông lớn
| STT | Đối tượng | Số cổ phần | Tỷ lệ |
|---:|---|---:|---:|
| 1 | Ông Trương Gia Bình | 117.347.966 | 6,89% |
| 2 | Tổng Công ty Đầu tư và Kinh doanh vốn Nhà nước – Công ty TNHH | 96.585.637 | 5,67% |
| 3 | Công ty TNHH QT | 62.449.511 | 3,67% |
| 4 | PYN ELITE FUND (NON-UCITS) | 30.044.600 | 1,76% |
| 5 | Ông Bùi Quang Ngọc | 25.255.715 | 1,48% |
| 6 | Bà Trương Thị Thanh Thanh | 25.095.835 | 1,47% |
| 7 | Quỹ ETF DCVFMVN DIAMOND | 22.966.161 | 1,35% |
| 8 | NTASIAN DISCOVERY MASTER FUND | 22.250.000 | 1,31% |
| 9 | EMPLOYEES PROVIDENT FUND BOARD | 20.000.000 | 1,17% |
| 10 | FIRST SENTIER INVESTORS GLOBAL UMBRELLA FUND PLC – FSSA ASIAN EQUITY PLUS FUND | 17.597.379 | 1,03% |

Gợi ý tự động: trang gold [33], trang được trích [33]

---

## d03 · table · status `answered`

**Câu hỏi:** Trong kế hoạch đầu tư dự kiến năm 2026, khối Giáo dục, Đầu tư và Khác có ngân sách bao nhiêu và dùng để làm gì?

**Đáp án chuẩn:** 3.000 tỷ VNĐ, để mở rộng các khuôn viên Đại học tại Hà Nội, Tp.Hồ Chí Minh và Đà Nẵng, đồng thời mở rộng thêm cơ sở đào tạo mới tại các tỉnh, thành trên toàn quốc.
- Evidence gốc trang 55 (table; Bảng 'Kế hoạch đầu tư dự kiến', hàng 'Khối Giáo dục, Đầu tư và Khác'): Ngân sách đầu tư 3.000 (tỷ VNĐ); Chú thích: Đầu tư mở rộng các khuôn viên Đại học tại Hà Nội, Tp.Hồ Chí Minh và Đà Nẵng, đồng thời mở rộng thêm cơ sở đào tạo mới tại các tỉnh, thành trên toàn quốc.

**Tool:** search('kế hoạch đầu tư năm 2026 khối Giáo dục, Đầu tư và Khác') → search('ngân sách đầu tư 2026 Giáo dục Đầu tư Khác')

**Câu trả lời:** Trong Kế hoạch đầu tư dự kiến năm 2026 (trang 55), Khối Giáo dục, Đầu tư và Khác có ngân sách đầu tư 3.000 tỷ VNĐ. Mục đích: đầu tư mở rộng các khuôn viên Đại học tại Hà Nội, Tp.Hồ Chí Minh và Đà Nẵng, đồng thời mở rộng thêm cơ sở đào tạo mới tại các tỉnh, thành trên toàn quốc. (Tổng ngân sách đầu tư dự kiến của Tập đoàn là 7.200 tỷ VNĐ, trong đó Khối Công nghệ 4.200 tỷ VNĐ.)

**Citation:**
- `ar_p55_v2` (trang 55, visual): [table] Kế hoạch đầu tư dự kiến
Đơn vị: Tỷ VNĐ

| Khối | Ngân sách đầu tư | Chú thích |
|---|---:|---|
| Khối Công nghệ | 4.200 | Đầu tư mở rộng các khu tổ hợp văn phòng tại các thành phố lớn như: Hà Nội, Tp.Hồ Chí Minh, Bình Dương. |
| Khối Giáo dục, Đầu tư và Khác | 3.000 | Đầu tư mở rộng các khuôn viên Đại học tại Hà Nội, Tp.Hồ Chí Minh và Đà Nẵng, đồng thời mở rộng thêm cơ sở đào tạo mới tại các tỉnh, thành trên toàn quốc. |
| Tổng cộng | 7.200 | |

Gợi ý tự động: trang gold [55], trang được trích [55]

---

## d04 · chart · status `answered`

**Câu hỏi:** Theo biểu đồ, đóng góp ngân sách Nhà nước của FPT năm 2023 là bao nhiêu?

**Đáp án chuẩn:** 8.167 tỷ VNĐ.
- Evidence gốc trang 11 (chart; Biểu đồ cột 'Đóng góp Ngân sách Nhà nước', góc trên bên phải, cột 2023): 2021 5.750 | 2022 7.112 | 2023 8.167 | 2024 10.117 | 2025 11.078 (tỷ VNĐ)

**Tool:** search('đóng góp ngân sách Nhà nước FPT 2023') → search('nộp ngân sách nhà nước qua các năm biểu đồ')

**Câu trả lời:** Theo biểu đồ "Đóng góp Ngân sách Nhà nước" (trang 11), năm 2023 FPT đóng góp 8.167 tỷ VNĐ (chuỗi: 2021: 5.750; 2022: 7.112; 2023: 8.167; 2024: 10.117; 2025: 11.078 tỷ VNĐ).

**Citation:**
- `ar_p11_v1` (trang 11, visual): [chart] Đóng góp Ngân sách Nhà nước
Biểu đồ cột. Giá trị hiển thị: 11.078 Tỷ VNĐ; tăng 9,5% so với cùng kỳ. Trục tung: 0; 2.000; 4.000; 6.000; 8.000; 10.000; 12.000 (Tỷ VNĐ). Trục hoành/năm: 2021, 2022, 2023, 2024, 2025. Giá trị từng năm: 2021: 5.750; 2022: 7.112; 2023: 8.167; 2024: 10.117; 2025: 11.078 (Tỷ VNĐ). Ghi chú: Đơn vị: Tỷ VNĐ.
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

## d05 · chart · status `answered`

**Câu hỏi:** Theo biểu đồ quy mô thị trường AI doanh nghiệp, quy mô năm 2023 là bao nhiêu?

**Đáp án chuẩn:** 1,7 tỷ USD.
- Evidence gốc trang 48 (chart; Biểu đồ đường 'Quy mô thị trường AI doanh nghiệp', điểm 2023): 2022 0 | 2023 1,7 | 2024 11,5 | 2025 37,0 (tỷ USD); 6,8x; 3,2x

**Tool:** search('quy mô thị trường AI doanh nghiệp biểu đồ') → search('thị trường AI doanh nghiệp 2023 quy mô tỷ USD')

**Câu trả lời:** Theo biểu đồ "Quy mô thị trường AI doanh nghiệp" (đơn vị: Tỷ USD), quy mô năm 2023 là 1,7 tỷ USD (các năm khác: 2022: 0; 2024: 11,5; 2025: 37,0) [ar_p48_v0].

**Citation:**
- `ar_p48_v0` (trang 48, visual): [chart] Quy mô thị trường AI doanh nghiệp
Biểu đồ đường. Tiêu đề: Quy mô thị trường AI doanh nghiệp. Đơn vị: Tỷ USD. Trục hoành: các năm 2022, 2023, 2024, 2025. Trục tung: 0, 10, 20, 30, 40. Giá trị theo từng năm: 2022: 0; 2023: 1,7; 2024: 11,5; 2025: 37,0. Chú thích tăng trưởng: 6,8x gần đoạn 2023–2024 và 3,2x gần đoạn 2024–2025, kèm mũi tên tăng màu xanh. Đường biểu diễn màu cam, các điểm dữ liệu có nhãn số liệu.

Gợi ý tự động: trang gold [48], trang được trích [48]

---

## d06 · chart · status `answered`

**Câu hỏi:** Theo biểu đồ cơ cấu doanh thu theo khối năm 2025, khối Viễn thông đạt bao nhiêu doanh thu và chiếm tỷ trọng bao nhiêu?

**Đáp án chuẩn:** 19.507 tỷ VNĐ, chiếm 27,8% (tăng 10,8%).
- Evidence gốc trang 60 (chart; Biểu đồ tròn 'Cơ cấu doanh thu theo khối', lát màu xanh dương (Khối Viễn thông theo chú giải)): 19.507 | 27,8% | tăng 10,8%

**Tool:** search('cơ cấu doanh thu theo khối 2025 Viễn thông tỷ trọng') → search('doanh thu khối Viễn thông 2025')

**Câu trả lời:** Theo biểu đồ "Cơ cấu doanh thu theo khối" (trang 60), năm 2025 khối Viễn thông đạt doanh thu 19.507 tỷ VNĐ, chiếm 27,8% tổng doanh thu (tổng 70.113 tỷ VNĐ), tăng 10,8% so với cùng kỳ [ar_p60_v0][ar_p60_t0].

**Citation:**
- `ar_p60_v0` (trang 60, visual): [chart] Cơ cấu doanh thu theo khối
Biểu đồ vòng tròn (donut) thể hiện cơ cấu doanh thu theo khối. Không có trục; đơn vị: Tỷ VND. Tổng/trung tâm: 70.113 (mũi tên tăng 11,6%). Chú giải: Khối Công nghệ (cam); Khối Viễn thông (xanh dương); Khối Giáo dục, Đầu tư và Khác (xanh lá). Số liệu: Khối Công nghệ: 44.475, 63,4% (mũi tên tăng 13,7%); Khối Viễn thông: 19.507, 27,8% (mũi tên tăng 10,8%); Khối Giáo dục, Đầu tư và Khác: 6.132, 8,8% (mũi tên tăng 0,05%). Số liệu thuộc trang Báo cáo thường niên FPT 2025.
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

## d07 · image · status `answered`

**Câu hỏi:** Theo sơ đồ tổ chức của FPT, những ủy ban/bộ phận nào được vẽ trực thuộc Hội đồng quản trị?

**Đáp án chuẩn:** Ủy ban Nhân sự và Lương thưởng; Ủy ban Chính sách phát triển; Văn phòng Chủ tịch HĐQT; Bộ phận Kiểm toán nội bộ.
- Evidence gốc trang 31 (diagram; Sơ đồ tổ chức, 4 ô xanh bên trái nối vào ô 'Hội đồng quản trị'): Ủy ban Nhân sự và Lương thưởng; Ủy ban Chính sách phát triển; Văn phòng Chủ tịch HĐQT; Bộ phận Kiểm toán nội bộ

**Tool:** search('sơ đồ tổ chức FPT Hội đồng quản trị ủy ban') → search('cơ cấu tổ chức bộ máy quản lý')

**Câu trả lời:** Theo sơ đồ tổ chức (trang 31), Hội đồng quản trị nối trực tiếp tới 4 đơn vị: Ủy ban Nhân sự và Lương thưởng; Ủy ban Chính sách Phát triển; Văn phòng Chủ tịch HĐQT; Bộ phận Kiểm toán Nội bộ [ar_p31_v0]. Sơ đồ mô hình quản trị (trang 80) cũng thể hiện HĐQT nối với 4 đơn vị tương ứng: Ủy ban Nhân sự và Lương thưởng, Ủy ban Chiến lược Phát triển, Văn phòng Chủ tịch HĐQT, Kiểm toán Nội bộ [ar_p80_v0]. (Ban Kiểm soát không trực thuộc HĐQT mà do ĐHĐCĐ bầu/nối sang [ar_p31_v0].)

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
- `ar_p80_v0` (trang 80, visual): [diagram] MÔ HÌNH QUẢN TRỊ VÀ VAI TRÒ CỦA CÁC BÊN
Loại sơ đồ: sơ đồ tổ chức/quản trị dạng cây.
Các nút và nội dung:
- ĐẠI HỘI ĐỒNG CỔ ĐÔNG: Đại hội đồng Cổ đông: Cơ quan có thẩm quyền cao nhất thực hiện các chức năng cùng các quyền và nghĩa vụ theo quy định tại Điều lệ Công ty và pháp luật có liên quan.
- BAN KIỂM SOÁT: Thực hiện giám sát HĐQT, TGĐ trong việc quản lý, điều hành Tập đoàn và chịu trách nhiệm trước ĐHĐCĐ trong việc thực hiện các nhiệm vụ được giao.
- HỘI ĐỒNG QUẢN TRỊ: Cơ quan quản trị cao nhất có quyền nhân danh Tập đoàn để quyết định, thực hiện các quyền và nghĩa vụ của Tập đoàn không thuộc thẩm quyền của ĐHĐCĐ theo quy định của Điều lệ Công ty và pháp luật có liên quan.
- CHỦ TỊCH HỘI ĐỒNG QUẢN TRỊ: Người đại diện theo pháp luật của Tập đoàn chịu trách nhiệm điều hành hoạt động công tác của HĐQT, xem xét và quyết định các công tác quản trị của Tập đoàn theo các quy định của pháp luật có liên quan và Điều lệ công ty, quy chế nội bộ.
- TỔNG GIÁM ĐỐC VÀ BAN ĐIỀU HÀNH: TGĐ là người đại diện theo pháp luật của Tập đoàn. Với sự trợ giúp của Ban Điều hành, TGĐ chịu trách nhiệm điều hành hoạt động kinh doanh hàng ngày của Tập đoàn trên cơ sở tuân thủ quyết định, nghị quyết

Gợi ý tự động: trang gold [31], trang được trích [31, 80]

---

## d08 · image · status `answered`

**Câu hỏi:** Trong sơ đồ lộ trình Net Zero 2040 gồm 5 bước, bước 04 là gì?

**Đáp án chuẩn:** Xác định các giải pháp ưu tiên (ví dụ tòa nhà văn phòng lắp đèn LED, cảm biến; trung tâm dữ liệu tối ưu làm mát bằng Liquid Cooling, AI-driven Thermal Management...).
- Evidence gốc trang 114 (diagram; Sơ đồ 5 bước '01–05' dưới khung 'Lộ trình Net Zero 2040', cột 04): 04 Xác định các giải pháp ưu tiên

**Tool:** search('lộ trình Net Zero 2040 5 bước') → search('bước 04 Net Zero')

**Câu trả lời:** Bước 04 trong sơ đồ lộ trình Net Zero 2040 là "Xác định các giải pháp ưu tiên", gồm:
- Tòa nhà văn phòng: lắp đặt đèn LED, hệ thống cảm biến thông minh; tích hợp cảm biến nhiệt độ và độ ẩm để điều khiển hệ thống điều hòa tự động.
- Trung tâm dữ liệu: tối ưu hệ thống làm mát thông qua các giải pháp Liquid Cooling, AI-driven Thermal Management; sử dụng môi chất lạnh có chỉ số GWP thấp; áp dụng cơ chế vận hành tiết kiệm năng lượng cho hệ thống máy chủ, áp dụng tiêu chuẩn xanh cho hạ tầng.

**Citation:**
- `ar_p114_v0` (trang 114, visual): [infographic] Lộ trình Net Zero 2040
Infographic dạng 5 cột đánh số 01-05, xếp từ trái sang phải; không thấy mũi tên kết nối, thứ tự thể hiện bằng số thứ tự.
Banner: Tập đoàn triển khai xây dựng lộ trình giảm phát thải khí nhà kính dựa trên việc tự tính toán và xác nhận đường cơ sở phát thải, đặt mục tiêu đến năm 2030 giảm 15,8% tổng lượng phát thải khí nhà kính và hướng tới mục tiêu Net Zero vào năm 2040.
01. Xác định lĩnh vực trọng tâm giảm phát thải
- Tiêu thụ điện trong Phạm vi 2.
02. Xác định mục tiêu giảm phát thải cho từng lĩnh vực
- Chuyển đổi sang sử dụng năng lượng sạch, song song với triển khai các giải pháp nâng cao hiệu quả năng lượng tại các cơ sở vận hành, bao gồm: Tòa nhà văn phòng; Trung tâm dữ liệu.
03. Thiết lập các giải pháp giảm phát thải khả thi và hiệu quả
- Tối ưu hệ thống điện và ứng dụng các giải pháp quản lý năng lượng thông minh;
- Đẩy mạnh sử dụng điện từ nguồn năng lượng tái tạo như năng lượng mặt trời;
- Cân nhắc mua chứng chỉ năng lượng tái tạo (REC).
04. Xác định các giải pháp ưu tiên
- Tòa nhà văn phòng: Lắp đặt đèn LED, hệ thống cảm biến thông minh; tích hợp cảm biến nhiệt độ và độ ẩm để điều khiển hệ thống điều hòa tự động;
- Trung tâm dữ liệu: T

Gợi ý tự động: trang gold [114], trang được trích [114]

---

## d09 · image · status `answered`

**Câu hỏi:** Theo infographic của lĩnh vực Dịch vụ Viễn thông, FPT Telecom có bao nhiêu trung tâm dữ liệu đạt chuẩn Uptime Tier III và dung lượng hạ tầng kết nối quốc tế là bao nhiêu?

**Đáp án chuẩn:** 04 trung tâm dữ liệu đạt chuẩn Uptime Tier III quốc tế; dung lượng hạ tầng kết nối quốc tế 6.800 Gbps.
- Evidence gốc trang 69 (infographic; Infographic 'Lĩnh vực dịch vụ viễn thông', hai ô dưới cùng): 04 Trung tâm dữ liệu đạt chuẩn Uptime Tier III quốc tế | 6.800 Gbps Dung lượng hạ tầng kết nối quốc tế

**Tool:** search('FPT Telecom trung tâm dữ liệu Uptime Tier III') → search('dung lượng hạ tầng kết nối quốc tế FPT Telecom')

**Câu trả lời:** Theo infographic lĩnh vực Dịch vụ Viễn thông (trang 69): FPT Telecom có **04 trung tâm dữ liệu đạt chuẩn Uptime Tier III quốc tế** và **dung lượng hạ tầng kết nối quốc tế là 6.800 Gbps**.

**Citation:**
- `ar_p69_v2` (trang 69, visual): [infographic] 04 Trung tâm dữ liệu đạt chuẩn Uptime Tier III quốc tế; 6.800 Gbps Dung lượng hạ tầng kết nối quốc tế
Hai ô số liệu: (1) '04' – 'Trung tâm dữ liệu đạt chuẩn Uptime Tier III quốc tế'; (2) '6.800 Gbps' – 'Dung lượng hạ tầng kết nối quốc tế'.
- `ar_p69_t1` (trang 69, text): Dung lượng hạ tầng kết nối quốc tế 6.800Gbps
Trung tâm dữ liệu đạt chuẩn Uptime Tier III quốc tế

Gợi ý tự động: trang gold [69], trang được trích [69]

---

## d10 · multihop · status `answered`

**Câu hỏi:** Cổ tức bằng tiền mặt chi trả năm 2025 bằng khoảng bao nhiêu phần trăm lợi nhuận sau thuế thuộc về cổ đông công ty mẹ năm 2025?

**Đáp án chuẩn:** Khoảng 34,0% (3.185 / 9.376 tỷ VNĐ).
- Evidence gốc trang 11 (chart; Biểu đồ 'Cổ tức bằng tiền mặt', 2025): 3.185 tỷ VNĐ
- Evidence gốc trang 12 (table; Bảng 2021-2025, hàng 9 'Lợi nhuận sau thuế thuộc về cổ đông công ty mẹ', cột 2025): 9.376
- Phép tính: 3.185 / 9.376 = 33,97% ≈ 34,0%. Trang 58 (bảng chỉ tiêu, 'Tỷ lệ lợi nhuận trả cổ tức' 34,0%) là evidence thay thế.

**Tool:** search('cổ tức tiền mặt 2025 tỷ lệ lợi nhuận sau thuế cổ đông công ty mẹ') → search('chi trả cổ tức bằng tiền năm 2025')

**Câu trả lời:** Khoảng 34,0%. Năm 2025, cổ tức tiền mặt chi trả trong năm là 3.185 tỷ đồng, lợi nhuận sau thuế thuộc về cổ đông công ty mẹ là 9.376 tỷ đồng; tài liệu ghi tỷ lệ lợi nhuận trả cổ tức năm 2025 là 34,0% (năm 2024: 34,9%, giảm 90 bps). (Kiểm tra: 3.185/9.376 ≈ 34,0%.) Lưu ý: tiền mặt chi trả trong năm bao gồm cổ tức tiền mặt còn lại của năm liền trước và tạm ứng cổ tức tiền mặt của năm hiện tại nếu có.

**Citation:**
- `ar_p58_v0` (trang 58, visual): [table] Một số chỉ tiêu hoạt động kinh doanh chính trong năm 2025
Đơn vị: Tỷ VNĐ
Ghi chú: (*) Riêng Lãi cơ bản trên cổ phiếu đơn vị là: VNĐ

| Chi tiêu | 2024 | 2025 | Tăng/Giảm |
|---|---:|---:|---:|
| Tổng tài sản | 72.000 | 88.142 | 22,4% |
| Doanh thu | 62.849 | 70.113 | 11,6% |
| Lợi nhuận từ hoạt động kinh doanh | 11.025 | 12.952 | 17,5% |
| LNTT, lãi vay và khấu hao (EBITDA) | 13.605 | 15.958 | 17,3% |
| LNTT | 11.070 | 13.044 | 17,8% |
| LNST | 9.427 | 11.232 | 19,1% |
| Lãi cơ bản trên cổ phiếu (*) | 4.292 | 5.216 | 21,5% |
| Cổ tức tiền mặt trả trong năm | 2.741 | 3.185 | 16,2% |
| Tỷ lệ lợi nhuận trả cổ tức | 34,9% | 34,0% | -90 bps |
- `ar_p12_v0` (trang 12, visual): [table] Tình hình tài chính và kết quả kinh doanh nổi bật giai đoạn 2021-2025
Đơn vị: Tỷ VND

| STT | Chỉ tiêu | 2021 | +/- | 2022 | +/- | 2023 | +/- | 2024 | +/- | 2025 | +/- |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Vốn chủ sở hữu | 21.418 | 15,1% | 25.356 | 18,4% | 29.933 | 18,1% | 35.728 | 19,4% | 43.748 | 22,4% |
| 2 | Tổng tài sản | 53.698 | 28,7% | 51.650 | -3,8% | 60.283 | 16,7% | 72.000 | 19,4% | 88.142 | 22,4% |
| 3 | Tổng doanh thu | 35.657 | 19,5% | 44.010 | 23,4% | 52.618 | 19,6% | 62.849 | 19,4% | 70.113 | 11,6% |
| 4 | Lợi nhuận thuần từ hoạt động kinh doanh | 6.228 | 20,0% | 7.589 | 21,8% | 9.112 | 20,1% | 11.025 | 21,0% | 12.952 | 17,5% |
| 5 | Lợi nhuận trước thuế, lãi vay và khấu hao | 7.981 | 18,2% | 9.495 | 19,0% | 11.490 | 21,0% | 13.605 | 18,4% | 15.958 | 17,3% |
| 6 | Lợi nhuận trước thuế và lãi vay | 6.337 | 20,4% | 7.662 | 20,9% | 9.203 | 20,1% | 11.070 | 20,3% | 13.044 | 17,8% |
| 7 | Lợi nhuận trước thuế | 6.337 | 20,4% | 7.662 | 20,9% | 9.203 | 20,1% | 11.070 | 20,3% | 13.044 | 17,8% |
| 8 | Lợi nhuận sau thuế | 5.349 | 20,9% | 6.491 | 21,3% | 7.788 | 20,0% | 9.427 | 21,0% | 11.232 | 19,1% |
| 9 | Lợi nhuận sau thuế thuộc về cổ
- `ar_p12_t1` (trang 12, text): 9.203
11.070
20,3%
13.044
17,8%
Lợi nhuận trước thuế
5.349
6.491
20,9%
21,3%
20,0%
7.788
9.427
21,0%
11.232
19,1%
Lợi nhuận sau thuế
4.337
5.310
22,6%
22,4%
21,8%
6.465
7.857
21,5%
9.376
19,3%
Lợi nhuận sau thuế thuộc về cổ đông công ty mẹ
1.697
2.011
15,8%
18,5%
18,1%
2.374
2.741
15,4%
3.185
16,2%
Chi trả cổ tức bằng tiền mặt (*)
BÁO CÁO TÀI CHÍNH HỢP NHẤT
(*): Tiền mặt chi trả trong năm bao gồm cổ tức tiền mặt còn lại của năm liền trước và tạm ứng cổ tức tiền mặt của năm hiện tại nếu có.

Gợi ý tự động: trang gold [11, 12], trang được trích [12, 58]

---

## d11 · multihop · status `answered`

**Câu hỏi:** Vốn điều lệ của FPT có khớp với tổng số cổ phiếu đang lưu hành nhân mệnh giá cổ phiếu không? Nêu các con số.

**Đáp án chuẩn:** Có. 1.703.507.121 cổ phiếu × 10.000 VNĐ = 17.035.071.210.000 VNĐ, đúng bằng vốn điều lệ.
- Evidence gốc trang 23 (text; Khối 'Thông tin chung', mục Vốn điều lệ): Vốn điều lệ 17.035.071.210.000 VNĐ
- Evidence gốc trang 32 (table; Bảng 'Thông tin về cổ phiếu'): Mệnh giá cổ phiếu 10.000 VNĐ; Tổng số cổ phiếu đang lưu hành 1.703.507.121 cổ phiếu
- Phép tính: 1.703.507.121 × 10.000 = 17.035.071.210.000

**Tool:** search('vốn điều lệ FPT') → search('số lượng cổ phiếu đang lưu hành mệnh giá')

**Câu trả lời:** Có, khớp. Vốn điều lệ 17.035.071.210.000 VNĐ [ar_p23_v0] đúng bằng tổng số cổ phiếu đang lưu hành 1.703.507.121 cổ phiếu [ar_p32_v0] nhân mệnh giá 10.000 VNĐ/cổ phiếu [ar_p32_v0]: 1.703.507.121 × 10.000 = 17.035.071.210.000 VNĐ. Số cổ phiếu đã phát hành cũng là 1.703.507.121 và cổ phiếu quỹ bằng 0 [ar_p204_v2], [ar_p32_v0].

**Citation:**
- `ar_p23_v0` (trang 23, visual): [table] THÔNG TIN CHUNG
| Mục | Giá trị |
|---|---|
| Tên công ty | Công ty Cổ phần FPT |
| Tên tiếng Anh | FPT Corporation |
| Tên viết tắt | FPT |
| Mã chứng khoán | FPT |
| Ngày thành lập | 13/09/1988 |
| Giấy chứng nhận đăng ký kinh doanh | 0101248141 |
| Vốn điều lệ | 17.035.071.210.000 VNĐ |
| Vốn chủ sở hữu | 43.748.040.747.539 VNĐ |
| Giá trị vốn hóa | 163.195.982.191.800 VNĐ (Tính tại thời điểm 31/12/2025) |
| Trụ sở chính | Số 10 phố Phạm Văn Bạch, phường Cầu Giấy, TP.Hà Nội, Việt Nam |
| Điện thoại | (+84) 24 7300 7300 |
| Fax | (+84) 24 3768 7410 |
| Website | https://fpt.com |
- `ar_p32_v0` (trang 32, visual): [table] Thông tin về cổ phiếu
Trong năm 2025, Tập đoàn không thực hiện giao dịch cổ phiếu quỹ

| Chỉ tiêu | Giá trị |
|---|---|
| Tên cổ phiếu | Cổ phiếu Công ty Cổ phần FPT |
| Loại cổ phiếu | Cổ phiếu phổ thông |
| Mã chứng khoán | FPT |
| Mệnh giá cổ phiếu | 10.000 VNĐ |
| Ngày bắt đầu niêm yết/đăng ký giao dịch | 13/12/2006 |
| Tổng số cổ phiếu đang lưu hành | 1.703.507.121 cổ phiếu |
| Tổng số cổ phiếu quỹ | 0 cổ phiếu |
| Số lượng cổ phiếu tự do chuyển nhượng | 1.671.922.715 cổ phiếu |
| Số lượng cổ phiếu hạn chế chuyển nhượng | 31.584.406 cổ phiếu |
| Tỷ lệ sở hữu tối đa của cổ đông nước ngoài | 49% |
- `ar_p204_v2` (trang 204, visual): [table] 23. Vốn góp của chủ sở hữu – (a) Số lượng cổ phiếu
Đơn vị: VND

| Chỉ tiêu | 31/12/2025 - Cổ phiếu phổ thông | 31/12/2024 - Cổ phiếu phổ thông |
|---|---:|---:|
| Số lượng cổ phiếu đăng ký | 1.703.507.121 | 1.471.069.183 |
| Số lượng cổ phiếu đã phát hành | 1.703.507.121 | 1.471.069.183 |
| Cổ phiếu phổ thông | 1.703.507.121 | 1.471.069.183 |
| * Trong đó: cổ phiếu bị hạn chế quyền chuyển nhượng quyền sở hữu | 31.584.406 | 25.943.108 |
| Số lượng cổ phiếu đang lưu hành | 1.703.507.121 | 1.471.069.183 |
| Cổ phiếu phổ thông | 1.703.507.121 | 1.471.069.183 |
| * Trong đó: cổ phiếu bị hạn chế quyền chuyển nhượng quyền sở hữu | 31.584.406 | 25.943.108 |

Gợi ý tự động: trang gold [23, 32], trang được trích [23, 32, 204]

---

## d12 · multihop · status `answered`

**Câu hỏi:** Ông Hoàng Việt Anh giữ chức vụ gì, và công ty ông phụ trách thuộc khối nào và FPT sở hữu bao nhiêu phần trăm theo sơ đồ tổ chức?

**Đáp án chuẩn:** Chủ tịch FPT Telecom; FPT Telecom thuộc Khối Viễn thông, tỷ lệ sở hữu 45,66%.
- Evidence gốc trang 69 (text; Phần Khối Viễn thông, tên và chức danh cạnh ảnh chân dung): Ông HOÀNG VIỆT ANH — Chủ tịch FPT Telecom
- Evidence gốc trang 31 (diagram; Sơ đồ tổ chức, nhánh 'Khối Viễn thông'): FPT Telecom — Vốn điều lệ 7.387.634.630.000 VNĐ — Tỷ lệ sở hữu 45,66%

**Tool:** search('Hoàng Việt Anh chức vụ') → search('sơ đồ tổ chức khối công ty thành viên tỷ lệ sở hữu')

**Câu trả lời:** Ông Hoàng Việt Anh là Chủ tịch FPT Telecom [ar_p69_t0] (trước đây từng là Phó Tổng Giám đốc FPT đến ngày 13/3/2024 [ar_p215_v0]). FPT Telecom thuộc KHỐI VIỄN THÔNG, với tỷ lệ sở hữu của FPT là 45,66% (vốn điều lệ 7.387.634.630.000 VNĐ) theo sơ đồ tổ chức [ar_p31_v0].

**Citation:**
- `ar_p69_t0` (trang 69, text): Khối Viễn thông
LĨNH VỰC DỊCH VỤ VIỄN THÔNG
Ông HOÀNG VIỆT ANH
Chủ tịch FPT Telecom
Top 3
Nhà cung cấp dịch vụ Internet băng thông rộng; trung tâm dữ liệu và dịch vụ tên miền; dịch vụ trực tuyến và cho thuê; dịch vụ truyền hình trả tiền
Báo cáo của Ban Điều hành về kết quả kinh doanh 2025 và nhận định 2026
Đánh giá của HĐQT về hoạt động của Tập đoàn
Tỉnh, thành trên toàn quốc có hạ tầng viễn thông và mạng lưới cung cấp dịch vụ 34
Công ty đã hoàn thành các mục tiêu thách thức về tăng trưởng khách hàng, khẳng định vị thế là nhà cung cấp dịch vụ Internet hàng đầu, nền tảng hàng đầu về giải trí thể thao, đặc biệt là thể thao bóng đá.
Giai đoạn 2026-2028, Công ty hướng đến trở thành doanh nghiệp tiên phong với ba nhiệm vụ trọng tâm: trở thành trụ cột trong các dự án trọng điểm an ninh quốc gia; thúc đẩy kinh doanh, mở rộng thị phần, tiên phong ứng dụng công nghệ Internet mới nhất tại Việt Nam; nghiên cứu, sáng tạo, làm chủ công nghệ lõi, hướng tới xuất khẩu.
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
- `ar_p215_v0` (trang 215, visual): [table] (iii) Thù lao Hội đồng Quản trị, Ban Kiểm soát và tiền lương của Tổng Giám đốc và người quản lý chủ chốt khác
Đơn vị: VNĐ

| STT | Họ và tên | Chức danh | 2025 | 2024 |
|---|---|---|---:|---:|
| | **Thù lao thành viên Hội đồng Quản trị** | | | |
| 1 | Ông Trương Gia Bình | Chủ tịch | - | - |
| 2 | Ông Bùi Quang Ngọc | Phó Chủ tịch | - | - |
| 3 | Ông Đỗ Cao Bảo | Ủy viên | - | - |
| 4 | Ông Jean Charles Belliol | Ủy viên | 960.000.000 | 960.000.000 |
| 5 | Bà Trần Thị Hồng Lĩnh | Ủy viên | 360.000.000 | 360.000.000 |
| 6 | Ông Hiroshi Yokotsuka | Ủy viên | 2.613.975.000 | 2.532.650.000 |
| 7 | Ông Hampapur Rangadore Binod | Ủy viên | 2.613.975.000 | 2.532.650.000 |
| | | | 6.547.950.000 | 6.385.300.000 |
| | **Thù lao thành viên Ban Kiểm soát** | | | |
| 1 | Ông Nguyễn Việt Thắng | Trưởng ban | 716.800.000 | 716.800.000 |
| 2 | Ông Nguyễn Khải Hoàn | Thành viên | 369.600.000 | 369.600.000 |
| 3 | Bà Dương Thùy Dương | Thành viên | 369.600.000 | 369.600.000 |
| | | | 1.456.000.000 | 1.456.000.000 |
| | **Tiền lương của Tổng Giám đốc và người quản lý chủ chốt khác** | | | |
| 1 | Ông Nguyễn Văn Khoa | Tổng Giám đốc | 4.420.000.000 | 4.420.000.000 |
| 2 | Ông Nguyễn Thế Phương

Gợi ý tự động: trang gold [31, 69], trang được trích [31, 69, 215]

---

## d13 · text · status `answered`

**Câu hỏi:** Trong năm 2025 FPT có thực hiện giao dịch cổ phiếu quỹ không, và tổng số cổ phiếu quỹ là bao nhiêu?

**Đáp án chuẩn:** Không thực hiện giao dịch cổ phiếu quỹ; tổng số cổ phiếu quỹ là 0.
- Evidence gốc trang 32 (text; Mục 'Thông tin về cổ phiếu'): Trong năm 2025, Tập đoàn không thực hiện giao dịch cổ phiếu quỹ; Tổng số cổ phiếu quỹ 0 cổ phiếu

**Tool:** search('cổ phiếu quỹ giao dịch năm 2025') → search('tổng số cổ phiếu quỹ')

**Câu trả lời:** Trong năm 2025, Tập đoàn không thực hiện giao dịch cổ phiếu quỹ. Tổng số cổ phiếu quỹ là 0 cổ phiếu (tổng số cổ phiếu đang lưu hành: 1.703.507.121 cổ phiếu) [ar_p32_v0][ar_p32_t0].

**Citation:**
- `ar_p32_v0` (trang 32, visual): [table] Thông tin về cổ phiếu
Trong năm 2025, Tập đoàn không thực hiện giao dịch cổ phiếu quỹ

| Chỉ tiêu | Giá trị |
|---|---|
| Tên cổ phiếu | Cổ phiếu Công ty Cổ phần FPT |
| Loại cổ phiếu | Cổ phiếu phổ thông |
| Mã chứng khoán | FPT |
| Mệnh giá cổ phiếu | 10.000 VNĐ |
| Ngày bắt đầu niêm yết/đăng ký giao dịch | 13/12/2006 |
| Tổng số cổ phiếu đang lưu hành | 1.703.507.121 cổ phiếu |
| Tổng số cổ phiếu quỹ | 0 cổ phiếu |
| Số lượng cổ phiếu tự do chuyển nhượng | 1.671.922.715 cổ phiếu |
| Số lượng cổ phiếu hạn chế chuyển nhượng | 31.584.406 cổ phiếu |
| Tỷ lệ sở hữu tối đa của cổ đông nước ngoài | 49% |
- `ar_p32_t0` (trang 32, text): Cơ cấu cổ đông
• Cơ cấu cổ đông theo các mức cổ phiếu sở hữu
• Thông tin về cổ phiếu
Trong năm 2025, Tập đoàn không thực hiện giao dịch cổ phiếu quỹ
Cổ phiếu Công ty Cổ phần FPT
Tên cổ phiếu
Các mức cổ phiếu sở hữu Số lượng cổ đông Tỷ lệ/ Tổng số cổ đông
Tỷ lệ/Tổng số cổ phiếu đã phát hành
Số lượng cổ phiếu sở hữu
Cổ phiếu phổ thông
Loại cổ phiếu
01 – 999
89.786
70,43%
19.527.027
1,15%
FPT
Mã chứng khoán
1.000 – 10.000
32.023
25,12%
94.203.628
5,53%
Thông tin chung
10.000 VNĐ
Mệnh giá cổ phiếu
Sứ mệnh, giá trị cốt lõi
10.001 – 1.000.000
5.425
4,26%
348.178.407
20,44%
13/12/2006
Ngày bắt đầu niêm yết/đăng ký giao dịch
Ngành nghề kinh doanh
1.000.001 trở lên
0,20%
1.241.598.059
72,88%
Vị thế và quy mô
1.703.507.121 cổ phiếu
Tổng số cổ phiếu đang lưu hành
Tổng số
127.488
100,00%
1.703.507.121
100,00%
Hành trình khẳng định năng lực và vị thế
0 cổ phiếu
Tổng số cổ phiếu quỹ
Cơ cấu quản trị và bộ máy quản lý
1.671.922.715 cổ phiếu
Số lượng cổ phiếu tự do chuyển nhượng
Ban Lãnh đạo
31.584.406 cổ phiếu
Số lượng cổ phiếu hạn chế chuyển nhượng
49%

Gợi ý tự động: trang gold [32], trang được trích [32]

---

## d14 · text · status `answered`

**Câu hỏi:** Dựa trên quy trình xác định vấn đề trọng yếu, FPT lựa chọn những vấn đề trọng yếu nào?

**Đáp án chuẩn:** 04 vấn đề: (1) Quản trị hướng đến phát triển bền vững; (2) Xây dựng môi trường làm việc đẳng cấp, hạnh phúc; (3) Hoạt động vì môi trường xanh; (4) Song hành vì sự phát triển cộng đồng.
- Evidence gốc trang 125 (text; Đoạn cuối cột phải): FPT lựa chọn 04 vấn đề trọng yếu gồm: (1) Quản trị hướng đến phát triển bền vững; (2) Xây dựng môi trường làm việc đẳng cấp, hạnh phúc; (3) Hoạt động vì môi trường xanh; (4) Song hành vì sự phát triển cộng đồng.

**Tool:** search('quy trình xác định vấn đề trọng yếu') → search('vấn đề trọng yếu lựa chọn')

**Câu trả lời:** Dựa trên nguyên tắc và quy trình xác định vấn đề trọng yếu (Bước 01: xác định các vấn đề chính; Bước 02: phân tích, xác định vấn đề trọng yếu được các bên quan tâm; Bước 03: xây dựng ma trận và lựa chọn vấn đề trọng yếu), FPT lựa chọn 04 vấn đề trọng yếu:
(1) Quản trị hướng đến phát triển bền vững;
(2) Xây dựng môi trường làm việc đẳng cấp, hạnh phúc;
(3) Hoạt động vì môi trường xanh;
(4) Song hành/Sống hạnh phúc vì sự phát triển cộng đồng.

Các vấn đề này được lồng ghép vào chiến lược kinh doanh, quản trị rủi ro, kế hoạch đầu tư trung và dài hạn của Tập đoàn.

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
- `ar_p125_t2` (trang 125, text): • Xác định các vấn đề trọng yếu dựa trên cơ sở tham vấn các bên liên quan và đánh giá mức độ tác động đến chiến lược tăng trưởng dài hạn. Các vấn đề trọng yếu được xác định tập trung vào quản trị minh bạch, an toàn dữ liệu, cam kết chuyển đổi xanh, phát triển nguồn nhân lực chất lượng cao và quản trị chuỗi cung ứng bền vững.
Công ty thành viên
• Đảm bảo hiện thực hóa các mục tiêu phát triển bền vững theo định hướng và chiến lược chung của Tập đoàn;
Bước 03
• Thực hiện báo cáo định kỳ về tình hình triển khai chiến lược phát triển bền vững của đơn vị.
Phân tích các vấn đề trọng yếu trong mối quan hệ với các bên liên quan.
• Xây dựng ma trận các vấn đề trọng yếu; • Lựa chọn các vấn đề trọng yếu.
Dựa trên nguyên tắc và quy trình xác định các vấn đề trọng yếu nêu trên, FPT lựa chọn 04 vấn đề trọng yếu gồm: (1) Quản trị hướng đến phát triển bền vững; (2) Xây dựng môi trường làm việc đẳng cấp, hạnh phúc; (3) Hoạt động vì môi trường xanh; (4) Song hành vì sự phát triển cộng đồng.
- `ar_p75_t0` (trang 75, text): Hoạt động ESG
Tình hình thực hiện các dự án đầu tư
Đơn vị: Tỷ VNĐ
Khối Kế hoạch 2025 Giải ngân 2025 So với kế hoạch
Công nghệ
6.000
47,1%
Viễn thông
2.500
70,0%
Cùng với việc đảm bảo sự tăng trưởng vững chắc về kinh tế, định hướng và những ưu tiên về ESG được xem là một phần quan trọng trong chiến lược phát triển. Theo đó, FPT lựa chọn bốn vấn đề trọng yếu trong phát triển bền vững bao gồm: Quản trị hướng đến phát triển bền vững; Xây dựng môi trường làm việc đẳng cấp, hạnh phúc; Hoạt động vì môi trường xanh và Song hành vì sự phát triển của cộng đồng. Các hoạt động ESG được lồng ghép vào chiến lược kinh doanh, quản trị rủi ro, kế hoạch đầu tư trung và dài hạn của Tập đoàn.
Giáo dục
2.500
2.823 1.751 749
30,0%

Gợi ý tự động: trang gold [125], trang được trích [75, 125]

---

## d15 · text · status `answered`

**Câu hỏi:** FPT thực hiện kiểm kê khí nhà kính theo những chuẩn mực nào?

**Đáp án chuẩn:** Nghị định thư Khí nhà kính (GHG Protocol) của Viện Tài nguyên thế giới (WRI) và tiêu chuẩn ISO 14040/14044.
- Evidence gốc trang 146 (text; Mục 'Phạm vi và phương pháp thu thập dữ liệu', đoạn 1): theo các chuẩn mực quốc tế được công nhận, bao gồm Nghị định thư Khí nhà kính (GHG Protocol) của Viện Tài nguyên thế giới (WRI) và tiêu chuẩn ISO 14040/14044

**Tool:** search('kiểm kê khí nhà kính chuẩn mực') → search('phát thải khí nhà kính GHG Protocol ISO 14064')

**Câu trả lời:** FPT thực hiện kiểm kê và quản lý dấu chân carbon theo các chuẩn mực quốc tế được công nhận, bao gồm: Nghị định thư Khí nhà kính (GHG Protocol) của Viện Tài nguyên thế giới (WRI) và tiêu chuẩn ISO 14040/14044 [ar_p146_t0]. Phạm vi xác định dấu chân carbon của FPT được xây dựng phù hợp với khuôn khổ GHG Protocol [ar_p146_t1]. Ngoài ra, trong phần dấu ấn nổi bật, FPT nêu tiêu chuẩn ISO 14064:2018 – Tiêu chuẩn đo lường và quản lý phát thải khí nhà kính [ar_p111_t0].

**Citation:**
- `ar_p146_t0` (trang 146, text): Quản lý hiệu quả tiêu thụ năng lượng và kiểm kê khí nhà kính
• Kết quả thực hiện kiểm kê khí nhà kính
• Phạm vi và phương pháp thu thập dữ liệu
FPT thực hiện kiểm kê và quản lý dấu chân carbon theo các chuẩn mực quốc tế được công nhận, bao gồm Nghị định thư Khí nhà kính (GHG Protocol) của Viện Tài nguyên thế giới (WRI) và tiêu chuẩn ISO 14040/14044.
Năm 2025, lượng phát thải khí nhà kính của FPT là 127.952 tấn CO2. Hai nguồn phát thải khí nhà kính phát sinh chủ yếu là xăng dầu dùng cho xe, máy phát điện (Phạm vi 1) và điện năng phục vụ cho sản xuất, vận hành máy móc thiết bị (Phạm vi 2) thuộc sở hữu của FPT.
Tổng hợp lượng phát thải khí nhà kính của FPT năm 2025
Năm 2025 Năm 2024 Năm 2023 Phạm vi
- `ar_p146_t1` (trang 146, text): Việc nâng cao độ chính xác của dữ liệu phát thải được Tập đoàn xác định là một quá trình cải tiến liên tục. Trên cơ sở mở rộng nguồn dữ liệu, hoàn thiện phương pháp tính toán và nâng cao năng lực phân tích, FPT định kỳ rà soát, cập nhật mô hình và điều chỉnh lộ trình giảm phát thải phù hợp với từng giai đoạn phát triển và mức độ sẵn sàng của dữ liệu.
Phạm vi 1 13.217 4.826 4.383
Phạm vi 2 109.696 138.748 123.569
Phạm vi 3
FPT chủ động thực hiện kiểm kê phát thải khí nhà kính tại trụ sở chính, các toà nhà, địa điểm kinh doanh tại Việt Nam của 08 công ty thành viên. Phạm vi xác định dấu chân carbon của FPT được xây dựng phù hợp với khuôn khổ GHG Protocol và các nguồn phát thải trọng yếu, có liên quan trực tiếp đến hoạt động của Tập đoàn, trên cơ sở mức độ sẵn có và độ tin cậy của dữ liệu.
Chưa triển khai Triển khai thí điểm tại FPT Software Triển khai tại FPT Software
Thông điệp và định hướng ESG
Quản trị hướng đến phát triển bền vững
Tổng
122.913 143.574 127.952
- `ar_p111_t0` (trang 111, text): Dấu ấn nổi bật
Môi trường làm việc đẳng cấp
Hoạt động vì môi trường xanh
Trách nhiệm xã hội
Quản trị bền vững
15 năm
Top 5
Liên tiếp triển khai Ngày FPT vì cộng đồng
Hệ thống điện mặt trời mái nhà
Nơi làm việc tốt nhất Việt Nam Top 10
Doanh nghiệp Việt Nam có chất lượng quản trị công ty tốt nhất ASEAN
Tổng sản lượng 842.749 kWh
ISO 27001:2013 Hệ thống quản lý an toàn thông tin
Việc làm ổn định 54.110
Điểm trường thiệt hại nặng được tái thiết sau lũ
Thông điệp và định hướng ESG
Quản trị hướng đến phát triển bền vững
ISO 14001:2015 Hệ thống quản lý môi trường
Môi trường làm việc đẳng cấp, hạnh phúc
Hoạt động vì môi trường xanh
Cơ sở được giám sát phát thải khí nhà kính định kỳ 100%
Song hành vì sự phát triển cộng đồng
Trường Hy Vọng nhận giải thưởng Hành động vì cộng đồng ở hạng mục Dự án kịp thời
Nhân sự người nước ngoài (82 quốc tịch) 4.124
ISO 45001:2018 Hệ thống an toàn sức khoẻ
Cán bộ quản lý nữ 36,4%
ISO 14064:2018 Tiêu chuẩn đo lường và quản lý phát thải khí nhà kính

Gợi ý tự động: trang gold [146], trang được trích [111, 146]

---

## du1 · unanswerable · status `abstain`

**Câu hỏi:** Doanh thu năm 2025 của FPT tại thị trường Hàn Quốc là bao nhiêu tỷ đồng?

**Hành vi mong đợi:** tìm rồi từ chối. Kiểm tra trong tài liệu: Báo cáo chỉ chia doanh thu theo khu vực (Việt Nam, Nhật Bản, Châu Mỹ, Châu Âu, Châu Á-Thái Bình Dương; biểu đồ trang 27). 'Hàn Quốc' xuất hiện ở trang 27 (bản đồ), 48, 64, 123 (mở rộng hiện diện, M&A), 218, 226 (danh sách công ty con/liên kết) nhưng không có doanh thu.

**Tool:** search('doanh thu thị trường Hàn Quốc') → search('Hàn Quốc doanh thu 2025 tỷ đồng') → search('thị trường nước ngoài doanh thu theo quốc gia Hàn Quốc Nhật Bản Mỹ') → search('doanh thu dịch vụ CNTT nước ngoài theo thị trường chi tiết') → search('Hàn Quốc thị trường mới thành lập văn phòng') → search('doanh thu theo khu vực địa lý bảng quốc gia chi tiết thuyết minh') → search('FPT Korea doanh thu thị trường Hàn Quốc mở rộng') → search('Châu Á - Thái Bình Dương doanh thu 8.173 thị trường')

**Câu trả lời:** Không đủ bằng chứng để trả lời. Báo cáo chỉ công bố doanh thu dịch vụ CNTT cho thị trường nước ngoài theo các khu vực lớn (Nhật Bản 15.452 tỷ đồng; Mỹ 8.163 tỷ đồng; Châu Âu 3.593 tỷ đồng; Châu Á - Thái Bình Dương 8.173 tỷ đồng; tổng 35.382 tỷ đồng) [ar_p62_v0], và doanh thu theo khu vực địa lý ở cấp Tập đoàn chỉ tách Việt Nam/Nước ngoài [ar_p214_v0]. Hàn Quốc chỉ xuất hiện trong danh sách quốc gia có hiện diện/văn phòng [ar_p27_t1], không có số liệu doanh thu riêng cho thị trường Hàn Quốc năm 2025.

**Citation:**
- (không có)

Gợi ý tự động: trang gold [], trang được trích []

---

## du2 · unanswerable · status `abstain`

**Câu hỏi:** Mức lương bình quân hàng tháng của CBNV FPT năm 2025 là bao nhiêu?

**Hành vi mong đợi:** tìm rồi từ chối. Kiểm tra trong tài liệu: Tìm 'lương bình quân', 'thu nhập bình quân', 'lương trung bình' trên toàn bộ 232 trang: không có. Phần nhân sự (trang 137-142) nêu chính sách thu nhập, phúc lợi nhưng không có số.

**Tool:** search('lương bình quân hàng tháng CBNV') → search('thu nhập bình quân người lao động 2025') → search('thu nhập bình quân CBNV triệu đồng/tháng') → search('chi phí lương nhân viên bình quân tháng') → search('lương bình quân người lao động FPT 2025 triệu đồng') → search('chỉ tiêu nhân sự thu nhập bình quân 2025 so với 2024') → search('"lương bình quân" FPT') → search('thu nhập bình quân tháng CBNV tăng so với năm trước') → search('thu nhập bình quân CBNV năm 2025 đạt') → search('báo cáo phát triển bền vững chỉ tiêu lao động lương thưởng') → search('GRI 202-1 mức lương khởi điểm so với lương tối thiểu') → search('chi phí nhân viên tổng doanh thu tỷ lệ thu nhập người lao động')

**Câu trả lời:** Không đủ bằng chứng để trả lời. Báo cáo thường niên FPT 2025 không nêu trực tiếp mức lương bình quân hàng tháng của CBNV năm 2025. Các nội dung liên quan chỉ gồm: chính sách lương, thưởng và phúc lợi (lương theo chức danh, lương theo hiệu quả kinh doanh, tháng lương thứ 13, khoán thu nhập) [ar_p141_t0, ar_p141_t2, ar_p141_t3]; kết quả nổi bật về môi trường làm việc như 151 giờ học trung bình/năm/CBNV, 37,7% nhân sự nữ [ar_p118_v0]; và năng suất lao động của lĩnh vực Dịch vụ CNTT thị trường nước ngoài (doanh thu/người 1.116 triệu VNĐ năm 2025) [ar_p65_v1] — không phải chỉ tiêu lương bình quân tháng.

**Citation:**
- (không có)

Gợi ý tự động: trang gold [], trang được trích []

---

## du3 · unanswerable · status `abstain`

**Câu hỏi:** Tổng chi phí nghiên cứu và phát triển (R&D) của FPT năm 2025 là bao nhiêu tỷ đồng?

**Hành vi mong đợi:** tìm rồi từ chối. Kiểm tra trong tài liệu: 'R&D' xuất hiện ở trang 17, 28, 30, 49, 54, 61, 68 (trung tâm R&D 3.000 m², văn phòng R&D...) và 'nghiên cứu và phát triển' ở trang 49, 67, 68, 120, 138 nhưng không có số tiền chi cho R&D; báo cáo tài chính không có khoản mục chi phí R&D riêng.

**Tool:** search('chi phí nghiên cứu và phát triển R&D năm 2025') → search('đầu tư R&D tỷ đồng') → search('chi phí R&D năm 2025 tỷ đồng đầu tư nghiên cứu phát triển') → search('ngân sách khoa học công nghệ đổi mới sáng tạo FPT 2025') → search('chi phí nghiên cứu phát triển hợp nhất thuyết minh') → search('FPT đầu tư cho R&D AI chip bán dẫn số tiền') → search('"R&D" chi phí năm 2025 Tập đoàn') → search('chi phí trả trước dài hạn R&D phân bổ') → search('tổng chi phí nghiên cứu và phát triển năm 2025') → search('chi cho nghiên cứu phát triển chiếm % doanh thu') → search('chi phí nghiên cứu phát triển 2025 con số nổi bật') → search('đầu tư công nghệ AI Factory chi phí R&D 2025 tỷ') → search('chi phí nghiên cứu phát triển FPT 2025 báo cáo phát triển bền vững') → search('đầu tư cho hoạt động nghiên cứu phát triển sáng kiến giá trị')

**Câu trả lời:** Không đủ bằng chứng để trả lời.

**Citation:**
- (không có)

Gợi ý tự động: trang gold [], trang được trích []

---
