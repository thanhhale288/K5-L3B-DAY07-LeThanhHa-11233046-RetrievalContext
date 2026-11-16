# Bảng chấm: `agent-test-chosen-bm25-fixcite`

Cấu hình: method `bm25`, top-k 3, budget 3200, max searches 3, fix citations `True`, model `deepseek-flash`.

## Cách chấm (BENCHMARK.md)

- `answer_grade` (câu có đáp án): 0 = sai hoặc không có evidence; 1 = đúng một phần; 2 = đúng và đủ. Câu bị từ chối chấm 0.
- `citation_support`: mỗi citation một giá trị `true`/`false`, theo thứ tự. `true` chỉ khi đoạn được trích thật sự hỗ trợ câu trả lời.
- `abstention_correct` (câu thiếu bằng chứng): `true` nếu agent từ chối và không thêm khẳng định thiếu căn cứ.
- `context_grade` (câu có đáp án): 0 = context không có evidence; 1 = có nhưng thiếu điều kiện hoặc nguồn; 2 = đủ evidence và nguồn.
- Ghi lý do ngắn vào `note`. Không dựa vào cột "gợi ý tự động": cột đó chỉ so chuỗi và có thể sai.

## q16 · có đáp án · status `answered`

**Câu hỏi:** FPT đứng ở vị trí nào trong xếp hạng doanh nghiệp Việt Nam có chất lượng quản trị công ty tốt nhất ASEAN?

**Đáp án chuẩn:** Top 5
**Evidence gold (trang 9):** “Top 5 Doanh nghiệp Việt Nam có chất lượng quản trị công ty tốt nhất ASEAN, Top 8 Doanh nghiệp vốn hóa lớn có quản trị công ty tốt nhất”
**Gợi ý tự động:** evidence gold có trong context cuối = `True`

**Các query agent dùng:** ['xếp hạng quản trị công ty tốt nhất ASEAN vị trí FPT']

**Câu trả lời của agent:** FPT nằm trong Top 5 Doanh nghiệp Việt Nam có chất lượng quản trị công ty tốt nhất ASEAN [fpt_esg_report_2025_p13_b_2][fpt_esg_report_2025_p9_b_0][fpt_esg_report_2025_p4_b_0]. Ngoài ra, FPT cũng thuộc Top 8 Doanh nghiệp quản trị công ty tốt nhất nhóm vốn hóa lớn [fpt_esg_report_2025_p13_b_2][fpt_esg_report_2025_p9_b_0].

**Đoạn được trích:**
1. `fpt_esg_report_2025_p13_b_2` (trang 13): • Tiếp tục khẳng định vị trí doanh nghiệp đầu ngành với những giải thưởng uy tín về quản trị, kinh doanh, công nghệ trên toàn cầu như: Top 40 Công ty Dịch vụ CNTT châu Á; Top 5 Doanh nghiệp Việt Nam có chất lượng quản trị công ty tốt nhất ASEAN; Top 8 Doanh nghiệp quản trị công ty tốt nhất nhóm vốn hóa lớn; Giá trị thương hiệu tăng 18%, đạt 1,2 tỷ USD; Top 10 Thương hiệu mạnh Việt Nam; Dẫn đầu Top 50 Công ty đại chúng uy tín nhất Việt Nam; Top 50 Công ty kinh doanh hiệu quả nhất Việt Nam…. BÁO CÁO PHÁT TRIỂN BỀN VỮNG 2025 Thông điệp và định hướng ESG Quản trị hướng đến phát triển bền vững Môi trường làm việc đẳng cấp, hạnh phúc Hoạt động vì môi trường xanh Song hành vì sự phát triển cộng đồng BÁO CÁO PHÁT TRIỂN BỀN VỮNG 12
2. `fpt_esg_report_2025_p9_b_0` (trang 9): QUẢN TRỊ XUẤT SẮC Cam kết Mục tiêuHoạt động trọng yếu Quản trị công ty Quản trị công ty xuất sắc hướng tới phát triển bền vững. Không ngừng nâng cao năng lực quản trị đáp ứng lợi ích của tất cả các bên liên quan. • Top 5 Doanh nghiệp Việt Nam có chất lượng quản trị công ty tốt nhất ASEAN, Top 8 Doanh nghiệp vốn hóa lớn có quản trị công ty tốt nhất; • Tiên phong nghiên cứu và ứng dụng AI trong quản lý tài chính, bán hàng – marketing và tối ưu hệ thống CRM nhằm nâng cao hiệu quả vận hành và kiểm soát rủi ro; • Ứng dụng AI trong quản trị, phát triển và triển khai phần mềm, từ thiết kế, lập trình, kiểm thử đến đảm bảo chất lượng sản phẩm;
3. `fpt_esg_report_2025_p4_b_0` (trang 4): Môi trường làm việc đẳng cấp Nơi làm việc tốt nhất Việt Nam Top 10 Việc làm ổn định 54.110 Nhân sự người nước ngoài (82 quốc tịch) 4.124 Dấu ấn nổi bật Cán bộ quản lý nữ 36,4% Giờ học nâng cao kiến thức kỹ năng AI 1,1 triệu Doanh nghiệp Việt Nam có chất lượng quản trị công ty tốt nhất ASEAN Top 5 ISO 27001:2013 Hệ thống quản lý an toàn thông tin ISO 14001:2015 Hệ thống quản lý môi trường ISO 45001:2018 Hệ thống an toàn sức khoẻ ISO 14064:2018 Tiêu chuẩn đo lường và quản lý phát thải khí nhà kính ISO/IEC 42001:2023 Tiêu chuẩn dành cho hệ thống quản lý trí tuệ nhân tạo (AIMS) Hoạt động vì môi trường xanh 02 Tổng sản lượng 842.749 kWh Cơ sở được giám sát phát thải khí nhà kính định kỳ 100% Hệ thống điện mặt trời mái nhà Trách nhiệm xã hội 15 năm Liên tiếp triển khai Ngày FPT vì cộng đồng 26 Đ

**Context cuối gửi model:** `fpt_esg_report_2025_p13_b_2`, `fpt_esg_report_2025_p9_b_0`, `fpt_esg_report_2025_p4_b_0`

---

## q17 · có đáp án · status `answered`

**Câu hỏi:** Các hoạt động trồng rừng của FPT tại Sóc Trăng (cũ), Tp.Huế và Thanh Hóa đã trồng bao nhiêu cây?

**Đáp án chuẩn:** 4.500 cây
**Evidence gold (trang 41):** “Tiên phong thực hiện thành công các hoạt động trồng rừng tại Sóc Trăng (cũ), Tp.Huế, Thanh Hóa với 4.500 cây được trồng tại các khu vực rừng ngập mặn, khu bảo tồn thiên nhiên”
**Gợi ý tự động:** evidence gold có trong context cuối = `True`

**Các query agent dùng:** ['trồng rừng Sóc Trăng Huế Thanh Hóa số cây']

**Câu trả lời của agent:** FPT đã triển khai các hoạt động trồng rừng tại Sóc Trăng (cũ), Tp.Huế và Thanh Hóa với tổng cộng 4.500 cây được trồng tại các khu vực rừng ngập mặn và khu bảo tồn thiên nhiên [fpt_esg_report_2025_p41_b_0].

**Đoạn được trích:**
1. `fpt_esg_report_2025_p41_b_0` (trang 41): Triển khai và duy trì mô hình làm việc kết hợp từ xa, góp phần tối ưu nhu cầu di chuyển và giảm phát thải khí nhà kính (Phạm vi 3). Tiên phong thực hiện thành công các hoạt động trồng rừng tại Sóc Trăng (cũ), Tp.Huế, Thanh Hóa với 4.500 cây được trồng tại các khu vực rừng ngập mặn, khu bảo tồn thiên nhiên góp phần tích cực chống biến đổi khí hậu, bảo vệ hệ sinh thái vì lợi ích của con người và thiên nhiên. Thông qua việc hạn chế các chuyến đi không cần thiết, ưu tiên họp trực tuyến, lựa chọn các chuyến bay thẳng khi phải di chuyển, đồng thời khuyến khích sử dụng các phương tiện giao thông thân thiện với môi trường và các giải pháp di chuyển xanh. Nhằm trung hoà/bù trừ lượng phát thải khí nhà kính. FPT đã tham vấn đơn vị tư vấn chuyên môn và tiến hành khảo sát tại một số địa phương như Quản

**Context cuối gửi model:** `fpt_esg_report_2025_p41_b_0`, `fpt_esg_report_2025_p41_b_1`, `fpt_esg_report_2025_p42_b_3`

---

## q18 · có đáp án · status `answered`

**Câu hỏi:** FPT hợp tác với tổ chức nào để triển khai dự án “Bếp Xanh – Sống Lành”, và dự án được thực hiện tại đâu?

**Đáp án chuẩn:** World Vision; tại xã Sín Chải, tỉnh Điện Biên
**Evidence gold (trang 51):** “Tổ chức World Vision và FPT ký kết Biên bản ghi nhớ hợp tác triển khai Dự án “Bếp Xanh – Sống Lành” tại xã Sín Chải, tỉnh Điện Biên.”
**Gợi ý tự động:** evidence gold có trong context cuối = `True`

**Các query agent dùng:** ['Bếp Xanh Sống Lành hợp tác']

**Câu trả lời của agent:** FPT hợp tác với Tổ chức World Vision, ký kết Biên bản ghi nhớ hợp tác triển khai Dự án "Bếp Xanh – Sống Lành" tại xã Sín Chải, tỉnh Điện Biên [fpt_esg_report_2025_p51_b_0].

**Đoạn được trích:**
1. `fpt_esg_report_2025_p51_b_0` (trang 51): BÁO CÁO PHÁT TRIỂN BỀN VỮNG 2025 Thông điệp và định hướng ESG Quản trị hướng đến phát triển bền vững Môi trường làm việc đẳng cấp, hạnh phúc Hoạt động vì môi trường xanh Song hành vì sự phát triển cộng đồng BÁO CÁO PHÁT TRIỂN BỀN VỮNG 50 Tổ chức World Vision và FPT ký kết Biên bản ghi nhớ hợp tác triển khai Dự án “Bếp Xanh – Sống Lành” tại xã Sín Chải, tỉnh Điện Biên. Sự kiện đánh dấu bước tiến quan trọng trong nỗ lực thúc đẩy phát triển bền vững, cải thiện sức khỏe cộng đồng và tăng cường khả năng thích ứng với biến đổi khí hậu tại khu vực nông thôn Việt Nam. Dự án giúp hơn 1.000 người dân tiếp cận các giải pháp bếp cải tiến nhằm giảm ô nhiễm không khí trong nhà, cải thiện điều kiện sức khỏe và cắt giảm phát thải khí nhà kính. Việc thúc đẩy các giải pháp nấu ăn sạch góp phần bảo vệ tài ng

**Context cuối gửi model:** `fpt_esg_report_2025_p51_b_0`, `fpt_esg_report_2025_p51_b_1`, `fpt_esg_report_2025_p12_b_0`

---

## q19 · có đáp án · status `answered`

**Câu hỏi:** FPT có quy tắc nào về việc ký hợp đồng với nhà cung cấp liên quan đến sức khỏe, an toàn lao động và môi trường?

**Đáp án chuẩn:** Không ký hợp đồng với các nhà cung cấp có hoạt động ảnh hưởng đến sức khỏe, an toàn lao động và môi trường
**Evidence gold (trang 8):** “Không ký hợp đồng với các nhà cung cấp có các hoạt động ảnh hưởng đến sức khoẻ, an toàn lao động và môi trường.”
**Gợi ý tự động:** evidence gold có trong context cuối = `False`

**Các query agent dùng:** ['hợp đồng nhà cung cấp sức khỏe an toàn lao động môi trường']

**Câu trả lời của agent:** FPT cam kết không hợp tác với các nhà cung cấp có hoạt động ảnh hưởng đến sức khỏe, an toàn lao động và môi trường; đồng thời Tập đoàn thiết lập và tuân thủ nghiêm ngặt các hướng dẫn nội bộ về mua sắm xanh, và ban hành quy trình đánh giá nhà cung cấp trọng yếu để đảm bảo nhà cung cấp không chỉ đáp ứng yêu cầu về chất lượng, chi phí mà còn tuân thủ tiêu chuẩn về đạo đức [fpt_esg_report_2025_p21_b_2].

**Đoạn được trích:**
1. `fpt_esg_report_2025_p21_b_2` (trang 21): m tập trung, đấu thầu online; nhà cung cấp tự báo giá online; tự động hóa các thao tác nội bộ; sử dụng AI hỗ trợ giao dịch mua sắm, hỏi đáp nhanh về mua sắm, gợi ý nhà cung cấp, kiểm soát chênh lệch giá giúp nâng cao sự minh bạch và đảm bảo công bằng cho nhà cung cấp. Nhằm góp phần đạt được các mục tiêu về tính bền vững của Tập đoàn trên quy mô toàn cầu, FPT hướng đến xây dựng chuỗi cung ứng bền vững thông qua việc: thiết lập và tuân thủ nghiêm ngặt các hướng dẫn nội bộ về mua sắm xanh. Đồng thời, Tập đoàn cam kết không hợp tác với các nhà cung cấp có hoạt động ảnh hưởng đến sức khỏe, an toàn lao động và môi trường. Tập đoàn đã ban hành quy trình đánh giá nhà cung cấp trọng yếu nhằm đảm bảo nhà cung cấp không chỉ đáp ứng yêu cầu về chất lượng, chi phí mà còn tuân thủ tiêu chuẩn về đạo đức,

**Context cuối gửi model:** `fpt_esg_report_2025_p21_b_2`, `fpt_esg_report_2025_p27_b_1`, `fpt_esg_report_2025_p44_b_0`

---

## q20 · có đáp án · status `answered`

**Câu hỏi:** Năm 2025, FPT ghi nhận tổng số giờ đào tạo và số giờ học trung bình trên mỗi CBNV/năm là bao nhiêu?

**Đáp án chuẩn:** Trên 7,1 triệu giờ đào tạo; 151 giờ học trung bình/năm/CBNV
**Evidence gold (trang 11):** “Ghi nhận trên 7,1 triệu giờ đào tạo, đạt 151 giờ học trung bình/năm/CBNV”
**Gợi ý tự động:** evidence gold có trong context cuối = `True`

**Các query agent dùng:** ['tổng số giờ đào tạo giờ học trung bình mỗi CBNV năm 2025']

**Câu trả lời của agent:** Năm 2025, FPT ghi nhận trên 7,1 triệu giờ đào tạo, đạt 151 giờ học trung bình/năm/CBNV [fpt_esg_report_2025_p11_b_2].

**Đoạn được trích:**
1. `fpt_esg_report_2025_p11_b_2` (trang 11): • Khởi công xây dựng Khu công viên công nghệ số góp phần khẳng định vị thế Hà Nội là trung tâm khoa học công nghệ của cả nước, xa hơn là từng bước hiện thực hóa khát vọng về một “Thung lũng Silicon” của Việt Nam. Tổ chức học tập suốt đời Duy trì FPT luôn là tổ chức học tập, kiến tạo việc học tập suốt đời của CBNV. • Sử dụng công nghệ để cá thể hóa việc học của CBNV; • Đẩy mạnh và nâng cao số giờ học cho CBNV; • Nâng cao hiệu quả đào tạo bằng công nghệ tiên tiến: AI Mentor, Text-to-voice, chatbot… • Ứng dụng AI Mentoring, AI Knowledge Explore cá thể hóa lộ trình học cho CBNV; • Đầu tư sử dụng các nền tảng toàn cầu đáp ứng nhu cầu học tập chuyên nghiệp, đa dạng của CBNV như: Coursera, Udemy, Udacity; • Ghi nhận trên 7,1 triệu giờ đào tạo, đạt 151 giờ học trung bình/năm/CBNV;

**Context cuối gửi model:** `fpt_esg_report_2025_p31_b_1`, `fpt_esg_report_2025_p11_b_2`, `fpt_esg_report_2025_p8_b_0`

---

## u03 · thiếu bằng chứng · status `abstain`

**Câu hỏi:** Năm 2025 FPT ghi nhận bao nhiêu vụ tai nạn lao động?

**Hành vi mong đợi:** tìm rồi từ chối. Lý do thiếu: Chỉ có chính sách liên quan: bảo hiểm tai nạn FPT Care (p34), ISO 45001 (p20), quan trắc môi trường lao động (p44); không có số vụ tai nạn. Kiểm tra: 'tai nạn' chỉ xuất hiện ở p34 (bảo hiểm); đọc các ngữ cảnh 'an toàn lao động' (p8, p20, p21, p44).

**Các query agent dùng:** ['tai nạn lao động 2025', 'số vụ tai nạn lao động', 'an toàn lao động số vụ tai nạn thương tích']

**Câu trả lời của agent:** Không đủ bằng chứng để trả lời.

**Đoạn được trích:** không có

**Context cuối gửi model:** `fpt_esg_report_2025_p27_b_0`, `fpt_esg_report_2025_p34_b_3`, `fpt_esg_report_2025_p26_b_2`, `fpt_esg_report_2025_p36_b_3`

---

## u04 · thiếu bằng chứng · status `abstain`

**Câu hỏi:** Năm 2025 FPT tái chế hoặc tái sử dụng bao nhiêu phần trăm tổng lượng nước tiêu thụ?

**Hành vi mong đợi:** tìm rồi từ chối. Lý do thiếu: p42 có tổng lượng nước tiêu thụ (831.885 m3 năm 2025, +0,48%) và mô tả dùng nước mưa, xử lý/tái chế nước thải, nhưng không có tỷ lệ nước tái chế/tái sử dụng. Kiểm tra: tìm 'nước tái', 'tỷ lệ tái', 'tái chế nước', 'tái sử dụng' trên cả 52 trang; các kết quả (p38, p42, p43) không nêu tỷ lệ nước.

**Các query agent dùng:** ['tái chế tái sử dụng nước tỷ lệ phần trăm tổng lượng nước tiêu thụ', 'tỷ lệ nước tái chế tái sử dụng']

**Câu trả lời của agent:** Không đủ bằng chứng để trả lời.

**Đoạn được trích:** không có

**Context cuối gửi model:** `fpt_esg_report_2025_p42_b_0`, `fpt_esg_report_2025_p46_b_1`, `fpt_esg_report_2025_p42_b_3`

---
