---
title: "Micropilot NMR81: Radar đo lường hợp pháp cho kho bồn xăng dầu"
slug: cam-bien-radar-tank-gauging-nmr81
meta_title: "Radar custody NMR81 tank gauging"
meta_description: "Micropilot NMR81 radar đo lường hợp pháp (custody transfer) cho kho bồn xăng dầu: chuẩn đo lường, tích hợp hệ quản lý bồn, kinh nghiệm triển khai. Tư vấn FastGroup."
primary_keyword: "radar đo mức bồn xăng dầu NMR81"
secondary_keywords: ["Micropilot NMR81", "tank gauging", "custody transfer radar", "đo mức kho xăng dầu", "chuẩn OIML", "Tankvision", "đo mức terminal", "Endress+Hauser"]
brand: "Endress+Hauser"
category: "Đo mức - Radar tank gauging (Micropilot)"
source_docs: ["CP00023F00EN2126 (Level selection)", "endress.com – TI01252G Micropilot NMR81"]
---

# Micropilot NMR81: Radar đo lường hợp pháp cho kho bồn xăng dầu

Trong một kho bồn xăng dầu (tank farm) hay terminal, con số mức chất lỏng không chỉ là thông tin vận hành — nó là **cơ sở tính tiền**. Mỗi milimét sai lệch trên một bồn đường kính hàng chục mét quy đổi ra hàng nghìn lít, tức hàng chục triệu đồng mỗi lần giao nhận. Đây là lý do bài toán *tank gauging* (đo mức bồn chứa cho mục đích thương mại) đòi hỏi một lớp thiết bị riêng, có độ chính xác và chứng nhận đo lường hợp pháp. **Micropilot NMR81** là radar không tiếp xúc chuyên dụng cho phân khúc này.

## Vì sao đo bồn thương mại cần thiết bị riêng

Một radar quá trình thông thường (FMR51) đạt độ chính xác cỡ ±2 mm — quá đủ cho điều khiển, nhưng chưa đạt yêu cầu *custody transfer*. Trong giao nhận thương mại, phép đo phải truy xuất được theo chuẩn đo lường hợp pháp (OIML R85, API), được cơ quan đo lường phê duyệt, và có độ chính xác dưới milimét. NMR81 được thiết kế để đạt **±0.5 mm** trong không gian tự do, đủ điều kiện tham gia vào hệ thống quản lý bồn được công nhận cho mục đích thương mại.

## Thông số kỹ thuật quan trọng (theo tài liệu)

| Hạng mục | Giá trị (theo catalog/TI) |
|---|---|
| Nguyên lý | Radar không tiếp xúc – tank gauging (free space) |
| Dải đo | Đến **70 m** |
| Độ chính xác | **±0.5 mm** (custody transfer) |
| Nhiệt độ quá trình | -40 đến +200 °C |
| Áp suất quá trình | Chân không đến +16 bar |
| Kết nối quá trình | Mặt bích DN80–DN250 / 3–10" |
| Vật liệu tiếp xúc | 316L, PTFE |
| Tín hiệu / truyền thông | Modbus / HART (tank gauging) |
| Tính năng | Custody transfer, gastight standard |

> Lưu ý biên tập: độ chính xác ±0.5 mm và tính hợp lệ cho custody transfer **phụ thuộc phiên bản, cấu hình và chứng nhận đo lường tại từng quốc gia**. BẮT BUỘC đối chiếu TI01252G theo mã đặt hàng và xác minh phê duyệt OIML/API cùng quy định đo lường Việt Nam trước khi cam kết dùng cho mục đích thương mại.

Điểm khác biệt cốt lõi so với radar quá trình không nằm ở tần số hay nguyên lý, mà ở **chuỗi truy xuất đo lường**: NMR81 đi kèm bảng hiệu chuẩn, chứng nhận, và được tích hợp vào hệ thống inventory management được cơ quan chức năng công nhận.

## Tích hợp hệ thống quản lý bồn (inventory & Tankvision)

NMR81 hiếm khi hoạt động đơn lẻ. Nó thường là một node trong hệ **tank gauging** hoàn chỉnh: radar đo mức → cảm biến nhiệt độ nhiều điểm (spot/average) → cảm biến áp suất/nước đáy bồn → bộ tập trung dữ liệu và phần mềm quản lý tồn kho. Truyền thông Modbus giúp NMR81 ghép vào các hệ quản lý bồn theo chuẩn công nghiệp, tính toán thể tích đã bù nhiệt độ (Net Standard Volume) theo API. Khi thiết kế, cần xác định ngay từ đầu kiến trúc hệ thống để chọn đúng giao thức và phụ kiện đồng bộ.

## Kinh nghiệm lắp đặt & lỗi thường gặp

- **Still-pipe / stilling well:** trong bồn mái nổi hoặc bồn có xáo trộn bề mặt, NMR81 thường lắp trong ống dẫn sóng (still-pipe) để ổn định tín hiệu và loại nhiễu — cần chọn đúng đường kính ống và anten tương thích.
- **Bảng hiệu chuẩn (calibration table):** phép đo custody phụ thuộc bảng dung tích bồn (tank capacity table); phải nghiệm thu và nhập đúng.
- **Bù nhiệt độ:** thể tích thương mại luôn quy về nhiệt độ chuẩn — thiếu cảm biến nhiệt nhiều điểm sẽ làm sai kết quả tính tiền.
- **Niêm phong đo lường:** sau nghiệm thu, thiết bị và cấu hình thường phải được niêm phong; mọi thay đổi cần theo quy trình đo lường hợp pháp.

## Ưu điểm, hạn chế, khi nào KHÔNG dùng

**Ưu điểm:** độ chính xác dưới milimét, đủ điều kiện custody transfer, dải đo tới 70 m cho bồn lớn, không tiếp xúc nên bảo trì thấp, tích hợp hệ inventory chuẩn công nghiệp.

**Hạn chế / không phù hợp:** chi phí cao và quy trình chứng nhận phức tạp — không cần thiết cho bồn chỉ phục vụ điều khiển/tồn kho nội bộ (khi đó FMR51 kinh tế hơn nhiều). Với bồn cần đo thêm interface và mật độ có kiểm soát cơ khí, cân nhắc servo Proservo NMS81.

## Hiệu quả kinh tế (TCO)

Trong tank farm, sai số đo lường đi thẳng vào bảng cân đối thương mại. Một hệ gauging chính xác, được chứng nhận, giúp giảm tranh chấp giao nhận, kiểm soát hao hụt (loss control) và minh bạch tồn kho. Chi phí đầu tư NMR81 nhỏ so với giá trị hàng hóa luân chuyển qua bồn mỗi năm — đây là khoản đầu tư vào độ tin cậy thương mại, không phải chi phí thiết bị đơn thuần.

## FastGroup hỗ trợ gì

FastGroup cung cấp thiết bị Endress+Hauser chính hãng tại Việt Nam. Với Micropilot NMR81, chúng tôi hỗ trợ: tư vấn kiến trúc hệ tank gauging (radar + nhiệt + áp + phần mềm), đối chiếu datasheet TI theo mã đặt hàng, xác minh yêu cầu chứng nhận đo lường, hỗ trợ nhập khẩu và cung cấp CO/CQ theo từng đơn hàng, phối hợp commissioning và nghiệm thu.

## Kết luận & liên hệ

Cho kho bồn xăng dầu và terminal cần đo lường hợp pháp, Micropilot NMR81 là radar tank gauging chuẩn công nghiệp. Để thiết kế hệ thống đúng chuẩn và nhận **báo giá chính hãng**, liên hệ FastGroup.

## Câu hỏi thường gặp (FAQ)

**1. NMR81 khác radar FMR51 ở đâu?** Ở độ chính xác (±0.5 mm) và chứng nhận đo lường hợp pháp cho custody transfer, không chỉ ở nguyên lý.

**2. Có dùng ngay cho giao nhận thương mại được không?** Cần đúng phiên bản có phê duyệt đo lường và tuân thủ quy định tại Việt Nam — phải kiểm tra TI và chứng nhận theo đơn hàng.

**3. NMR81 hay servo NMS81?** Radar không tiếp xúc phù hợp đa số bồn; cần đo thêm interface/mật độ bằng cơ khí thì cân nhắc NMS81.

**4. Có cần cảm biến nhiệt kèm theo không?** Có — thể tích thương mại phải bù nhiệt độ, nên cần đo nhiệt nhiều điểm.

**5. Có đầy đủ CO/CQ và chứng nhận không?** FastGroup cung cấp hàng chính hãng kèm CO/CQ và hỗ trợ hồ sơ chứng nhận theo từng đơn hàng.

## Nguồn tham khảo
- Endress+Hauser – Level measurement selection (CP00023F00EN2126)
- Endress+Hauser – Technical Information TI01252G Micropilot NMR81, endress.com (đối chiếu theo mã đặt hàng và chứng nhận đo lường)
