# Kịch bản Thuyết trình - Chương 07: Tổng hợp Phân tích, Đánh giá và Cảm ơn

## Slide 49: Mở đầu Chương 7 (07_00_chapter.html)
- **Hành động:** 
  Đứng thẳng, hướng mắt về toàn bộ căn phòng để chuẩn bị kết luận.
- **Lời thoại tham khảo:**
  "Bước sang phần cuối cùng: Tổng hợp Phân tích và Đánh giá."

***

## Slide 50: Bảng so sánh (07_01_comparison.html)
- **Hành động:** 
  Chỉ tay lướt qua bảng phân tích đánh đổi (Trade-off) từ trái qua phải.
- **Lời thoại tham khảo:**
  "Nhìn vào Bảng đánh giá Trade off tổng thể, ta có thể thấy Không phương pháp nào là hoàn hảo tuyệt đối.
  Điển hình như Full Scan ăn chắc mặc bền 100% độ phủ. Nhưng nó lại cực kỳ chậm và tốn thêm 20% thẻ silicon.
  Trong khi Multiple Scan giải bài toán rất nhanh. Tuy nhiên, nó tốn chân IO và khiến bo mạch trắc trở. Shadow Register đạt Zero Delay nhưng nhồi nhét diện tích lên mức giới hạn kỷ lục."

***

## Slide 51: Case Study tại các Tập đoàn (07_02_casestudy.html)
- **Hành động:** 
  Chỉ vào logo ARM và Intel/IBM để làm dẫn chứng thực tế.
- **Lời thoại tham khảo:**
  "Bạn sẽ tự hỏi, thế Qualcomm Snapdragon, Apple A-series họ dùng cái gì trên chiếc điện thoại của bạn?
  Gần như 100% thiết kế vi mạch di động áp dụng Multiple Scan cộng thêm một vũ khí bí mật On-Chip Decompressor. Bằng cách nhồi giải nén ngay trên Chip, họ bóp Data test gửi xuống từ ATE gọn lại 100 lần, vừa rẻ tiền vừa cực nhanh.
  Ở thái cực khác, Intel hay IBM làm vi xử lý máy chủ tản nhiệt lớn xung nhịp 5GHz, họ bắt buộc ôm trọn chuẩn 2 Clock LSSD, tránh tuyệt đối làm trễ mạch."

***

## Slide 52: Tóm tắt và Kết luận (07_03_summary.html)
- **Hành động:** 
  Chia hai bàn tay ra 2 bên, cân nhắc Ưu và Nhược điểm.
- **Lời thoại tham khảo:**
  "Tổng hợp lại, Thiết kế khả kiểm bằng Scan Chain hiện đã là tiêu chuẩn Công nghiệp bắt buộc. Nó biến hệ thống máy trạng thái mù mờ thành hàm logic có thể nhìn thấu. 
  Nhưng có một Yếu điểm vĩnh viễn cần Đánh đổi cho kiến trúc sư. Nếu bạn muốn kiểm thử tốt, bạn mất đi diện tích phần cứng vật lý. Đi kèm theo đó là rủi ro suy giảm hiệu năng do dòng trễ của Cổng ghép kênh."

***

## Slide 53: Tài liệu tham khảo (07_04_references.html)
- **Hành động:** 
  Không cần đọc từng dòng, chỉ giới thiệu nguồn tài liệu.
- **Lời thoại tham khảo:**
  "Trên đây là toàn bộ tài liệu nghiên cứu tham khảo từ các sách giáo khoa uy tín. Tiêu biểu như cuốn Essentials of Electronic Testing của giáo sư Bushnell. Hoặc tác phẩm VLSI Test Principles của thầy Wang. Cuối cùng không thể thiếu các Whitepaper của hãng Synopsys mà nhóm đã đối chiếu."

***

## Slide 54: Lời Cảm ơn (07_99_thanks.html)
- **Hành động:** 
  Gật đầu nhẹ/cúi chào để cảm ơn thầy và các bạn.
- **Lời thoại tham khảo:**
  "Bài thuyết trình dài của nhóm xin phép được khép lại tại đây. Xin thay mặt toàn bộ thành viên nhóm chân thành cảm ơn Thầy và các bạn đã chú ý lắng nghe! Sau đây nhóm rất mong nhận được câu hỏi phản biện từ lớp nhằm làm rõ hơn vấn đề."
