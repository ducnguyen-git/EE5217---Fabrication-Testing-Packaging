# Kịch bản Thuyết trình - Chương 07: Tổng hợp Phân tích, Đánh giá và Cảm ơn

## Slide 61: Mở đầu Chương 7 (07_00_chapter.html)
- **Hành động:** 
  Đứng thẳng, hướng mắt về toàn bộ căn phòng để chuẩn bị kết luận.
- **Lời thoại tham khảo:**
  "Bước sang phần cuối cùng: Tổng hợp Phân tích và Đánh giá. Kỹ sư hàng không vĩ đại Burt Rutan từng nói: *'Kiểm thử dẫn đến sự thất bại, và đi qua sự thất bại dẫn đến sự thấu hiểu sâu sắc.'* Chúng ta chèn DFT không phải dèm pha thiết kế ban đầu dở, mà để đo lường và loại trừ những góc khuất trong con Vi mạch phức tạp."

***

## Slide 62: Bảng so sánh (07_01_comparison.html)
- **Hành động:** 
  Chỉ tay lướt qua bảng phân tích đánh đổi (Trade-off) từ trái qua phải.
- **Lời thoại tham khảo:**
  "Nhìn vào Bảng đánh giá Trade-off tổng thể, ta có thể thấy Không phương pháp nào là hoàn hảo tuyệt đối.
  Điển hình như Full Scan dù ăn chắc mặc bền 100% Fault Coverage và dễ thiết kế, nhưng lại Rất chậm và tốn diện tích silicon (~20%).
  Trong khi Multiple Scan giải bài toán thì nhanh, độ phủ cao, nhưng lại rất tốn chân IO và bắt Mạch trắc trở. Shadow Register thì đạt Zero Delay nhưng nhồi nhét diện tích lên mức giới hạn kỷ lục."

***

## Slide 63: Case Study tại các Tập đoàn (07_02_casestudy.html)
- **Hành động:** 
  Chỉ vào logo ARM và Intel/IBM để làm dẫn chứng thực tế.
- **Lời thoại tham khảo:**
  "Bạn sẽ tự hỏi, thế Qualcomm Snapdragon, Apple A-series họ dùng cái gì trên chiếc điện thoại của bạn?
  Gần như 100% thiết kế vi mạch di động áp dụng Multiple Scan cộng thêm một vũ khí bí mật On-Chip Decompressor. Bằng cách nhồi giải nén ngay trên Chip, họ bóp Data test gửi xuống từ ATE gọn lại 100 lần, vừa rẻ tiền vừa cực nhanh.
  Ở thái cực khác, Intel hay IBM làm vi xử lý máy chủ tản nhiệt lớn xung nhịp 5GHz, họ bắt buộc ôm trọn chuẩn 2 Clock LSSD, tránh tuyệt đối làm trễ mạch."

***

## Slide 64: Tóm tắt và Kết luận (07_03_summary.html)
- **Hành động:** 
  Chia hai bàn tay ra 2 bên, cân nhắc Ưu và Nhược điểm.
- **Lời thoại tham khảo:**
  "Tổng hợp lại, Thiết kế DFT bằng kỹ thuật Scan Chain hiện đã là tiêu chuẩn Công nghiệp bắt buộc không thể thiếu (De facto). Nó biến 1 cỗ máy FSM tù mù thành hàm Logic Combinational trong suốt, bắt bớ mọi lỗi sản xuất.
  Nhưng Yếu điểm vĩnh viễn cần Đánh đổi (Trade-off) cho kiến trúc sư phần cứng: Bạn muốn Test tốt, bạn mất diện tích chip vật lý đi kèm với rủi ro suy giảm hiệu năng do dòng trễ Cổng Mux Delay."

***

## Slide 65: Tài liệu tham khảo (07_04_references.html)
- **Hành động:** 
  Không cần đọc từng dòng, chỉ giới thiệu nguồn tài liệu.
- **Lời thoại tham khảo:**
  "Trên đây là toàn bộ tài liệu nghiên cứu tham khảo từ các sách giáo khoa uy tín như cuốn Essentials of Electronic Testing của thầy Bushnell và VLSI Test Principles của thầy Wang, cùng các Whitepaper của hãng Synopsys mà nhóm đã đối chiếu."

***

## Slide 66: Lời Cảm ơn (07_99_thanks.html)
- **Hành động:** 
  Gật đầu nhẹ/cúi chào để cảm ơn thầy và các bạn.
- **Lời thoại tham khảo:**
  "Bài thuyết trình dài của nhóm xin phép được khép lại tại đây. Xin thay mặt nhóm chân thành cảm ơn Thầy và các bạn đã chú ý lắng nghe! Sau đây nhóm rất mong nhận được câu hỏi phản biện từ lớp nhằm làm rõ hơn vấn đề."
