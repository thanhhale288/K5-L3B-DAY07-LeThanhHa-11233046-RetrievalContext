# Bảng chấm: `agent-test-baseline-dense`

Cấu hình: method `dense`, top-k 3, budget 3200, max searches 3, fix citations `False`, model `deepseek-flash`.

## Cách chấm (BENCHMARK.md)

- `answer_grade` (câu có đáp án): 0 = sai hoặc không có evidence; 1 = đúng một phần; 2 = đúng và đủ. Câu bị từ chối chấm 0.
- `citation_support`: mỗi citation một giá trị `true`/`false`, theo thứ tự. `true` chỉ khi đoạn được trích thật sự hỗ trợ câu trả lời.
- `abstention_correct` (câu thiếu bằng chứng): `true` nếu agent từ chối và không thêm khẳng định thiếu căn cứ.
- `context_grade` (câu có đáp án): 0 = context không có evidence; 1 = có nhưng thiếu điều kiện hoặc nguồn; 2 = đủ evidence và nguồn.
- Ghi lý do ngắn vào `note`. Không dựa vào cột "gợi ý tự động": cột đó chỉ so chuỗi và có thể sai.

## q16 · có đáp án · status `abstain`

**Câu hỏi:** FPT đứng ở vị trí nào trong xếp hạng doanh nghiệp Việt Nam có chất lượng quản trị công ty tốt nhất ASEAN?

**Đáp án chuẩn:** Top 5
**Evidence gold (trang 9):** “Top 5 Doanh nghiệp Việt Nam có chất lượng quản trị công ty tốt nhất ASEAN, Top 8 Doanh nghiệp vốn hóa lớn có quản trị công ty tốt nhất”
**Gợi ý tự động:** evidence gold có trong context cuối = `False`

**Các query agent dùng:** ['xếp hạng quản trị công ty tốt nhất ASEAN vị trí FPT', 'quản trị công ty tốt nhất ASEAN xếp hạng', 'chất lượng quản trị công ty tốt nhất ASEAN xếp hạng']

**Câu trả lời của agent:** Không đủ bằng chứng để trả lời.

**Đoạn được trích:** không có

**Context cuối gửi model:** `fpt_esg_report_2025_p30_b_1`, `fpt_esg_report_2025_p32_b_1`, `fpt_esg_report_2025_p36_b_0`

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

**Context cuối gửi model:** `fpt_esg_report_2025_p41_b_0`, `fpt_esg_report_2025_p41_b_1`, `fpt_esg_report_2025_p43_b_3`

---

## q18 · có đáp án · status `answered`

**Câu hỏi:** FPT hợp tác với tổ chức nào để triển khai dự án “Bếp Xanh – Sống Lành”, và dự án được thực hiện tại đâu?

**Đáp án chuẩn:** World Vision; tại xã Sín Chải, tỉnh Điện Biên
**Evidence gold (trang 51):** “Tổ chức World Vision và FPT ký kết Biên bản ghi nhớ hợp tác triển khai Dự án “Bếp Xanh – Sống Lành” tại xã Sín Chải, tỉnh Điện Biên.”
**Gợi ý tự động:** evidence gold có trong context cuối = `True`

**Các query agent dùng:** ['Bếp Xanh Sống Lành hợp tác triển khai']

**Câu trả lời của agent:** FPT hợp tác với Tổ chức World Vision, ký kết Biên bản ghi nhớ hợp tác triển khai Dự án "Bếp Xanh – Sống Lành" tại xã Sín Chải, tỉnh Điện Biên [fpt_esg_report_2025_p51_b_0].

**Đoạn được trích:**
1. `fpt_esg_report_2025_p51_b_0` (trang 51): BÁO CÁO PHÁT TRIỂN BỀN VỮNG 2025 Thông điệp và định hướng ESG Quản trị hướng đến phát triển bền vững Môi trường làm việc đẳng cấp, hạnh phúc Hoạt động vì môi trường xanh Song hành vì sự phát triển cộng đồng BÁO CÁO PHÁT TRIỂN BỀN VỮNG 50 Tổ chức World Vision và FPT ký kết Biên bản ghi nhớ hợp tác triển khai Dự án “Bếp Xanh – Sống Lành” tại xã Sín Chải, tỉnh Điện Biên. Sự kiện đánh dấu bước tiến quan trọng trong nỗ lực thúc đẩy phát triển bền vững, cải thiện sức khỏe cộng đồng và tăng cường khả năng thích ứng với biến đổi khí hậu tại khu vực nông thôn Việt Nam. Dự án giúp hơn 1.000 người dân tiếp cận các giải pháp bếp cải tiến nhằm giảm ô nhiễm không khí trong nhà, cải thiện điều kiện sức khỏe và cắt giảm phát thải khí nhà kính. Việc thúc đẩy các giải pháp nấu ăn sạch góp phần bảo vệ tài ng

**Context cuối gửi model:** `fpt_esg_report_2025_p51_b_0`, `fpt_esg_report_2025_p33_b_4`, `fpt_esg_report_2025_p50_b_2`

---

## q19 · có đáp án · status `answered`

**Câu hỏi:** FPT có quy tắc nào về việc ký hợp đồng với nhà cung cấp liên quan đến sức khỏe, an toàn lao động và môi trường?

**Đáp án chuẩn:** Không ký hợp đồng với các nhà cung cấp có hoạt động ảnh hưởng đến sức khỏe, an toàn lao động và môi trường
**Evidence gold (trang 8):** “Không ký hợp đồng với các nhà cung cấp có các hoạt động ảnh hưởng đến sức khoẻ, an toàn lao động và môi trường.”
**Gợi ý tự động:** evidence gold có trong context cuối = `False`

**Các query agent dùng:** ['hợp đồng nhà cung cấp sức khỏe an toàn lao động môi trường']

**Câu trả lời của agent:** Có. FPT đưa điều khoản "Cam kết không thực hiện hành vi hối lộ" và tuân thủ nhân quyền, lao động, môi trường vào tất cả các hợp đồng mẫu [fpt_esg_report_2025_p21_b_3].

**Đoạn được trích:**
1. `fpt_esg_report_2025_p21_b_3` (trang 21): lao động, môi trường và quản trị. Song song, để đảm bảo công tác mua sắm bền vững, FPT tiếp tục duy trì: • Chính sách mua sắm bền vững với những nguyên tắc cơ bản nhằm tạo tác động tích cực nhất đến môi trường, kinh tế và xã hội, đồng thời đảm bảo sự công bằng, minh bạch và tuân thủ các quy định của pháp luật cũng như quy định nội bộ của Tập đoàn trong quá trình thực hiện mua sắm; • Các tiêu chí đảm bảo tính bền vững khi tìm kiếm, đánh giá, lựa chọn nhà cung cấp, trong đó tiêu chí đánh giá thông số năng lượng và thân thiện với môi trường chiếm tối đa 5% tổng số điểm đánh giá cho các phương án mua sắm thiết bị tiêu thụ điện; • Điều khoản “Cam kết không thực hiện hành vi hối lộ” và tuân thủ nhân quyền, lao động, môi trường trong tất cả các hợp đồng mẫu;

**Context cuối gửi model:** `fpt_esg_report_2025_p28_b_5`, `fpt_esg_report_2025_p44_b_0`, `fpt_esg_report_2025_p21_b_3`

---

## q20 · có đáp án · status `answered`

**Câu hỏi:** Năm 2025, FPT ghi nhận tổng số giờ đào tạo và số giờ học trung bình trên mỗi CBNV/năm là bao nhiêu?

**Đáp án chuẩn:** Trên 7,1 triệu giờ đào tạo; 151 giờ học trung bình/năm/CBNV
**Evidence gold (trang 11):** “Ghi nhận trên 7,1 triệu giờ đào tạo, đạt 151 giờ học trung bình/năm/CBNV”
**Gợi ý tự động:** evidence gold có trong context cuối = `True`

**Các query agent dùng:** ['tổng số giờ đào tạo năm 2025 giờ học trung bình mỗi CBNV']

**Câu trả lời của agent:** Năm 2025, FPT ghi nhận trên 7,1 triệu giờ đào tạo (tăng 12% so với cùng kỳ), đạt 151 giờ học trung bình/năm/CBNV [fpt_esg_report_2025_p11_b_2][fpt_esg_report_2025_p15_b_3].

**Đoạn được trích:**
1. `fpt_esg_report_2025_p11_b_2` (trang 11): • Khởi công xây dựng Khu công viên công nghệ số góp phần khẳng định vị thế Hà Nội là trung tâm khoa học công nghệ của cả nước, xa hơn là từng bước hiện thực hóa khát vọng về một “Thung lũng Silicon” của Việt Nam. Tổ chức học tập suốt đời Duy trì FPT luôn là tổ chức học tập, kiến tạo việc học tập suốt đời của CBNV. • Sử dụng công nghệ để cá thể hóa việc học của CBNV; • Đẩy mạnh và nâng cao số giờ học cho CBNV; • Nâng cao hiệu quả đào tạo bằng công nghệ tiên tiến: AI Mentor, Text-to-voice, chatbot… • Ứng dụng AI Mentoring, AI Knowledge Explore cá thể hóa lộ trình học cho CBNV; • Đầu tư sử dụng các nền tảng toàn cầu đáp ứng nhu cầu học tập chuyên nghiệp, đa dạng của CBNV như: Coursera, Udemy, Udacity; • Ghi nhận trên 7,1 triệu giờ đào tạo, đạt 151 giờ học trung bình/năm/CBNV;
2. `fpt_esg_report_2025_p15_b_3` (trang 15): • Các chương trình đào tạo được triển khai sâu rộng trên toàn Tập đoàn với tổng số hơn 7,1 triệu giờ học, tăng 12% so với cùng kỳ; • 98% CBNV được nâng cao kiến thức cơ bản về AI, tương ứng hơn 1,1 triệu giờ học; • Chú trọng nuôi dưỡng và phát triển nguồn lực ở tất cả các cấp với nhiều chương trình đào tạo chuyên biệt như: Chương trình Sư phụ – Đệ tử/Mentorship, chương trình quản trị trải nghiệm học tập kết hợp mô hình học – thi – trải nghiệm, chương trình MiniMBA, chương trình đào tạo cán bộ quản lý cấp trung, cán bộ kế cận. Thực hiện các chế độ bảo hiểm, các chế độ phúc lợi theo quy định

**Context cuối gửi model:** `fpt_esg_report_2025_p11_b_2`, `fpt_esg_report_2025_p15_b_3`, `fpt_esg_report_2025_p11_b_3`

---

## u03 · thiếu bằng chứng · status `abstain`

**Câu hỏi:** Năm 2025 FPT ghi nhận bao nhiêu vụ tai nạn lao động?

**Hành vi mong đợi:** tìm rồi từ chối. Lý do thiếu: Chỉ có chính sách liên quan: bảo hiểm tai nạn FPT Care (p34), ISO 45001 (p20), quan trắc môi trường lao động (p44); không có số vụ tai nạn. Kiểm tra: 'tai nạn' chỉ xuất hiện ở p34 (bảo hiểm); đọc các ngữ cảnh 'an toàn lao động' (p8, p20, p21, p44).

**Các query agent dùng:** ['tai nạn lao động 2025 số vụ', 'an toàn lao động tai nạn thương tích nhân viên', 'số vụ tai nạn lao động']

**Câu trả lời của agent:** Không đủ bằng chứng để trả lời.

**Đoạn được trích:** không có

**Context cuối gửi model:** `fpt_esg_report_2025_p31_b_2`, `fpt_esg_report_2025_p12_b_3`, `fpt_esg_report_2025_p26_b_2`, `fpt_esg_report_2025_p27_b_1`, `fpt_esg_report_2025_p43_b_3`, `fpt_esg_report_2025_p28_b_0`, `fpt_esg_report_2025_p4_b_0`

---

## u04 · thiếu bằng chứng · status `abstain`

**Câu hỏi:** Năm 2025 FPT tái chế hoặc tái sử dụng bao nhiêu phần trăm tổng lượng nước tiêu thụ?

**Hành vi mong đợi:** tìm rồi từ chối. Lý do thiếu: p42 có tổng lượng nước tiêu thụ (831.885 m3 năm 2025, +0,48%) và mô tả dùng nước mưa, xử lý/tái chế nước thải, nhưng không có tỷ lệ nước tái chế/tái sử dụng. Kiểm tra: tìm 'nước tái', 'tỷ lệ tái', 'tái chế nước', 'tái sử dụng' trên cả 52 trang; các kết quả (p38, p42, p43) không nêu tỷ lệ nước.

**Các query agent dùng:** ['tái chế tái sử dụng nước tỷ lệ phần trăm tổng lượng nước tiêu thụ', 'tỷ lệ nước tái chế tái sử dụng so với tổng lượng nước tiêu thụ']

**Câu trả lời của agent:** Không đủ bằng chứng để trả lời.

**Đoạn được trích:** không có

**Context cuối gửi model:** `fpt_esg_report_2025_p42_b_0`, `fpt_esg_report_2025_p40_b_3`, `fpt_esg_report_2025_p8_b_1`, `fpt_esg_report_2025_p42_b_3`

---
