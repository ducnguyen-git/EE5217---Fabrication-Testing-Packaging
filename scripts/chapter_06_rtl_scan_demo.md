# Kịch bản Thuyết trình - Chương 06: Thiết kế Scan Mức RTL và Demo

## Slide 52: Mở đầu Chương 6 (06_00_chapter.html)
- **Hành động:** 
  Dừng lại 1 nhịp sau khi đọc trích dẫn để tạo điểm nhấn.
- **Lời thoại tham khảo:**
  "Chương 6: Phát triển DFT thẳng vào Mã Nguồn mức RTL. W. Edwards Deming từng đúc kết: *'Chất lượng không thể đạt được qua việc kiểm thử sản phẩm ở khúc cuối; chất lượng phải được nhúng vào ngay từ nguyên bản...'*
  Và thay vì chờ máy tính ném thành tỷ cái logic Gate rối rắm rồi tool mới tự ráp Scan, Kỹ sư RTL thiết kế chuỗi Scan mạnh tay ngay từ mức Level Khối."

***

## Slide 53: Cấu trúc cấp cao RTL Design Full Scan (06_01_rtl_full_scan.html)
- **Hành động:** 
  Chỉ vào mô hình Single Scan kết nối mượt mà từ khối này qua khối khác.
- **Lời thoại tham khảo:**
  "Giống như việc xâu dính chuỗi, ở mức RTL, Full Scan xâu thẳng thừng các Module lớn làm một sợi cáp duy nhất đi qua Bộ đếm Counter, Arithmetic Logic v.v."

***

## Slide 54: Ví dụ định tuyến kết nối ngang RTL (06_02_rtl_full_scan_ex.html)
- **Hành động:** 
  Kích sang slide ví dụ hình mạch, chỉ đường đi theo chiều từ trái qua phải SI -> SO.
- **Lời thoại tham khảo:**
  "Ở vi xử lý này, Scan-In SI sẽ chạy dắt dọc qua thanh ghi AC, đẩy qua IR, qua PC logic và Controller rồi ra đầu SO. Nếu có 400 Flip-Flop tổng, thì mạch gánh 400 nhịp Clock để lấp đầy."

***

## Slide 55: Chia cắt Multiple Scan cấp cao (06_03_rtl_multiple_scan.html)
- **Hành động:** 
  Chỉ tay phân tích sự tách rẽ.
- **Lời thoại tham khảo:**
  "Dĩ nhiên để chống hiện tượng ùn tắc 400 Clock đó, kỹ sư áp dụng Multiple Scan rẽ nhánh trực tiếp từ mã nguồn RTL. Tính module hoá Verilog hỗ trợ cắt lát rất tiện dụng."

***

## Slide 56: Biểu đồ Bóc tách song song (06_04_rtl_multiple_scan_ex.html)
- **Hành động:** 
  Chỉ vào 3 mũi nhọn Scan nhánh nằm rải rác trên khối.
- **Lời thoại tham khảo:**
  "Kết quả ta có sự phân làn rõ rệt. Tuyến AC đi riêng. Tuyến thanh ghi lệnh IR đi riêng. Và Tuyến gánh team PC, Controller đi riêng. Hệ sinh thái này giúp hạ giảm Test-Time đi một nửa và đẩy năng suất cho nhà máy chẩn đoán wafer."

***

## Slide 57: Demonstration chạy thử phần mềm thương mại (06_99_demonstration.html)
- **Hành động:** 
  Kết hợp mời giáo viên và sinh viên hướng mắt lên công cụ demo.
- **Lời thoại tham khảo:**
  "Trăm nghe không bằng một xem trực tiếp. Sau đây tiếp nối chương trình, xin kính mời cố vấn và các bạn theo dõi phần Demo hoạt động tổng hợp vi mạch bằng bộ phần mềm độc quyền Design Compiler và trình xuất Test-Pattern từ ATPG TetraMAX của hệ sinh thái Synopsys!"

***

## Slide 58: So sánh Chế độ Normal và Test Mode (06_99a_demo_modes.html)
- **Hành động:** 
  Chỉ tay qua lại 2 bức ảnh bên trái và bên phải.
- **Lời thoại tham khảo:**
  "Đầu tiên là quan sát trích xuất đồ họa mạch ở 2 chế độ. Bên trái là Normal Mode khi mạch chạy bình thường. Bên phải là Test Mode khi ta cấp tín hiệu Scan, có thể thấy rõ các đường tín hiệu đỏ cho thấy dữ liệu đang chuyển luồng đi xuyên qua chân vòng vèo của các khối Scan Flip-Flop thay vì mạch gốc."

***

## Slide 59: Mô phỏng Dạng sóng không có Lỗi (06_99b_demo_non_stuck.html)
- **Hành động:** 
  Chỉ tay vào dãy sóng xanh lá mượt mà.
- **Lời thoại tham khảo:**
  "Phần mềm tiến hành xuất ra kết quả mô phỏng Waveform dạng sóng khi mạch ở điều kiện lý tưởng không có lỗi (Non-stuck-at). Các tín hiệu Logic chuyển trạng thái mượt mà đúng như thiết kế."

***

## Slide 60: Mô phỏng Dạng sóng bắt Lỗi Stuck-at (06_99c_demo_stuck_at.html)
- **Hành động:** 
  Chỉ tay nhận mạnh vào điểm khác biệt trên dãy sóng cảnh báo đỏ.
- **Lời thoại tham khảo:**
  "Khi tool TetraMAX giả lập tiêm một lỗi Kẹt Stuck-at vào đường kết nối mạch, ta quan sát được trên sóng mô phỏng xuất hiện các vệt cảnh báo, dữ liệu đầu ra bị sai lệch ngay lập tức. Nhờ tính năng này, Tool tự động tính toán để sinh ra mẫu Test phát hiện được chính lỗi đó trên dây chuyền sản xuất ngoài đời!"
