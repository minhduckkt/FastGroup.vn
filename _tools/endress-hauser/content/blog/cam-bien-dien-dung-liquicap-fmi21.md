---
title: "Liquicap FMI21: Cảm biến điện dung đo mức liên tục"
slug: cam-bien-dien-dung-liquicap-fmi21
meta_title: "Liquicap FMI21 điện dung"
meta_description: "Liquicap FMI21 cảm biến điện dung đo mức liên tục: khi nào chọn điện dung, xử lý bám dính que đo, hiệu chuẩn 2 điểm. Kinh nghiệm lắp đặt & báo giá FastGroup."
primary_keyword: "cảm biến điện dung đo mức FMI21"
secondary_keywords: ["Liquicap FMI21", "đo mức điện dung", "capacitance level", "đo mức bám dính", "hiệu chuẩn điện dung", "đo mức hóa chất", "Endress+Hauser"]
brand: "Endress+Hauser"
category: "Đo mức - Điện dung liên tục (Liquicap)"
source_docs: ["CP00023F00EN2126 (Level selection)", "endress.com – TI00393F Liquicap FMI21"]
---

# Liquicap FMI21: Cảm biến điện dung đo mức liên tục

Không phải bồn nào cũng hợp với radar. Trong những bình nhỏ, hẹp, có nhiều vật cản, hoặc chứa chất lỏng mà radar/GWR khó cấu hình, một công nghệ lâu đời vẫn rất hữu dụng: **đo mức điện dung**. **Liquicap FMI21** là cảm biến điện dung compact đo mức liên tục, dùng chính chất lỏng làm một phần của tụ điện — càng nhiều chất lỏng bao quanh que đo, điện dung càng lớn, và thiết bị quy đổi ra mức.

## Nguyên lý điện dung — khi nào là lựa chọn đúng

Que đo của FMI21 cùng thành bồn (hoặc điện cực đối) tạo thành một tụ điện; chất lỏng giữa chúng là điện môi. Khi mức dâng, phần que ngập trong chất lỏng làm điện dung thay đổi theo tuyến tính với mức. Điện dung là lựa chọn tốt khi:

- **Bình nhỏ/hẹp** mà radar khó lắp hoặc bị nhiễu thành bình.
- Cần một thiết bị **đơn giản, không bộ phận chuyển động**, gọn.
- Chất lỏng có hằng số điện môi ổn định (dẫn điện hoặc cách điện, tùy cấu hình que).

Điểm cần hiểu: vì đo dựa trên điện môi, **mọi thay đổi tính chất điện của môi chất đều ảnh hưởng** — đây vừa là nguyên lý vừa là giới hạn của công nghệ.

## Thông số kỹ thuật quan trọng (theo tài liệu)

| Hạng mục | Giá trị (theo catalog/TI) |
|---|---|
| Nguyên lý | Điện dung (capacitance), đo mức liên tục |
| Dải đo | Đến **2.5 m** |
| Độ chính xác | ±1% |
| Nhiệt độ quá trình | -40 đến +100 °C |
| Áp suất quá trình | -1 đến +10 bar |
| Kết nối quá trình | Ren 1½" |
| Vật liệu tiếp xúc | 316L, PP, sợi carbon |
| Tín hiệu / truyền thông | 4-20 mA / IO-Link |
| Cấu trúc | Compact |

> Lưu ý biên tập: dải đo, vật liệu que và khả năng bù bám dính **phụ thuộc phiên bản và cấu hình đặt hàng**. BẮT BUỘC đối chiếu TI00393F theo mã đặt hàng và xác minh tương thích môi chất (dẫn điện/cách điện) với loại que.

Hỗ trợ **IO-Link** là điểm hiện đại đáng chú ý: cấu hình số, chẩn đoán và tích hợp dễ vào hệ automation mới — ưu thế cho máy móc và OEM.

## Xử lý bám dính & hiệu chuẩn 2 điểm

Hai vấn đề thực tế quyết định thành bại khi dùng điện dung:

- **Bám dính (build-up) trên que:** lớp chất bám dẫn điện tạo điện dung ký sinh, gây đọc sai mức. Với môi chất bám dính, chọn phiên bản có **bù bám dính** (active build-up compensation) hoặc cấu hình que phù hợp. Đây là điểm cần xác minh kỹ khi chọn model.
- **Hiệu chuẩn 2 điểm:** điện dung cần hiệu chuẩn theo môi chất thực tế — thường lấy điểm cạn (empty) và điểm đầy (full) để thiết bị lập tương quan điện dung–mức đúng cho môi chất đó. Đổi môi chất (đổi điện môi) thì phải hiệu chuẩn lại.

## Kinh nghiệm lắp đặt & lỗi thường gặp

- **Chọn que theo môi chất:** dẫn điện vs cách điện dùng cấu hình que khác nhau (có/không lớp cách điện) — chọn sai là nguồn lỗi lớn nhất.
- **Tránh chạm vật cản:** que không được chạm thành bồn hay vật cản khác; giữ khoảng cách theo hướng dẫn.
- **Hiệu chuẩn với môi chất thật:** hiệu chuẩn khô/nước rồi chạy môi chất khác sẽ lệch — nên hiệu chuẩn theo điều kiện vận hành.
- **Theo dõi bám dính:** nếu đọc trôi dần theo thời gian vận hành, nghi ngờ bám dính que trước khi kết luận hỏng.

## Ưu điểm, hạn chế, khi nào KHÔNG dùng

**Ưu điểm:** compact, không bộ phận chuyển động, phù hợp bình nhỏ/hẹp; IO-Link hiện đại; chi phí hợp lý; đa dụng cho nhiều chất lỏng.

**Hạn chế / không phù hợp:** phụ thuộc hằng số điện môi — môi chất đổi tính chất điện gây sai số; nhạy bám dính nếu không chọn đúng phiên bản; dải đo và độ chính xác (±1%) khiêm tốn so với radar/GWR. Cần độ chính xác cao, môi chất biến thiên điện môi, hay bồn lớn → dùng radar/GWR (FMP51).

## Hiệu quả kinh tế (TCO)

Ở đúng ứng dụng — bình nhỏ, máy móc, môi chất ổn định — FMI21 là giải pháp rẻ, gọn, ít bảo trì. Chìa khóa TCO là **chọn đúng cấu hình que và bù bám dính ngay từ đầu**; chọn sai sẽ tốn công hiệu chuẩn lặp lại và mất tin cậy. IO-Link giúp giảm chi phí tích hợp và chẩn đoán về sau.

## FastGroup hỗ trợ gì

FastGroup cung cấp thiết bị Endress+Hauser chính hãng tại Việt Nam. Với Liquicap FMI21, chúng tôi hỗ trợ: tư vấn khi nào chọn điện dung vs radar/GWR, chọn cấu hình que theo môi chất dẫn điện/cách điện, tư vấn bù bám dính, đối chiếu datasheet TI theo mã đặt hàng, hỗ trợ nhập khẩu và cung cấp CO/CQ theo từng đơn hàng.

## Kết luận & liên hệ

Cho bình nhỏ và ứng dụng cần cảm biến mức gọn, không chuyển động, Liquicap FMI21 là giải pháp điện dung linh hoạt. Để chọn đúng que và cấu hình bù bám dính — cùng **báo giá chính hãng** — liên hệ FastGroup.

## Câu hỏi thường gặp (FAQ)

**1. Khi nào nên chọn điện dung thay radar?** Khi bồn nhỏ/hẹp, nhiều vật cản, hoặc cần thiết bị gọn đơn giản và môi chất có điện môi ổn định.

**2. Bám dính que có làm sai không?** Có — cần chọn phiên bản bù bám dính hoặc cấu hình que phù hợp cho môi chất dính.

**3. Vì sao phải hiệu chuẩn 2 điểm?** Vì điện dung phụ thuộc điện môi môi chất; hiệu chuẩn empty/full để lập đúng tương quan cho môi chất thực.

**4. Đổi môi chất có phải hiệu chuẩn lại?** Có, nếu hằng số điện môi khác đáng kể.

**5. Có hỗ trợ IO-Link không?** Có — cấu hình số và chẩn đoán, tích hợp dễ vào automation mới.

## Nguồn tham khảo
- Endress+Hauser – Level measurement selection (CP00023F00EN2126)
- Endress+Hauser – Technical Information TI00393F Liquicap FMI21, endress.com (đối chiếu theo mã đặt hàng)
