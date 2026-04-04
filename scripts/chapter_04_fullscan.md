# Kịch bản Thuyết trình - Chương 04: Kiến trúc Full Scan và Virtual Tester

## Slide 26: Mở đầu Chương 4 (04_00_chapter.html)
- **Hành động:** 
  Nhấn mạnh chữ "sự đơn giản" và "hiệu quả".
- **Lời thoại tham khảo:**
  "Bước sang Chương 4: Cốt lõi của kiến trúc Full Scan."

***

## Slide 27: Khái quát Full Scan (04_01_fullscan_intro.html)
- **Hành động:** 
  Chỉ vào hoạt ảnh luân chuyển Test Enable và Normal Mode.
- **Lời thoại tham khảo:**
  "Ý tưởng đột phá của Full Scan là biến tất cả các Flip-Flops nội bộ thành một sợi dây chuyền duy nhất. Bằng sự đơn giản đó, mọi thành phần lưu trữ đã bị ép vào khuôn khổ dịch bit."

***

## Slide 28: Cấu trúc Scan Flip-Flop (MUX-DFF) (04_02_ff_structures.html)
- **Hành động:** 
  Chỉ tay vào thành phần cổng Mux ghép trước cổng D.
- **Lời thoại tham khảo:**
  "Chuyển một thanh Flip-Flop thông thường thành Scan Flip-Flop rất dễ. Cấu trúc Muxed-DFF được sử dụng đại trà bằng cách chèn bộ ghép kênh MUX hai một vào cổng nhận dữ liệu của Flip-Flop."

***

## Slide 29: Tuyến chuyển mạch lựa chọn (04_02_ff_structures.html)
- **Hành động:** 
  Chỉ vào tín hiệu Test Enable TE.
- **Lời thoại tham khảo:**
  "Tín hiệu công tắc Test Enable sẽ làm trọng tài điều hướng cho Cổng Mux. Nó cho phép Flip-Flop điện toán bình thường nếu bằng 0. Ngược lại, nó ép nhận dữ liệu dồn dịch từ Flip-Flop anh em sát bên cạnh nếu bằng 1."

***

## Slide 30: Nút thắt Cổ chai Timing (04_02_ff_structures.html)
- **Hành động:** 
  Nhấn mạnh vào chữ Setup Time Delay mầu đỏ.
- **Lời thoại tham khảo:**
  "Gót A-sin của MUX-DFF là Timing Critical Delay. Vì con MUX án ngữ giữa hệ thống, luồng dữ liệu bị chậm lại. Điều này làm suy giảm tốc độ xung nhịp hoạt động tối đa mà mạch có thể đạt được."

***

## Slide 31: Khái quát Level Sensitive Scan Design (LSSD) (04_02_ff_structures.html)
- **Hành động:** 
  Chỉ sự khác biệt của LSSD.
- **Lời thoại tham khảo:**
  "Để vượt qua nỗi sợ kẹt Delay, hệ thống đã tạo ra công nghệ thứ 2 mang tên Level Sensitive Scan Design. Công nghệ này nổi tiếng với thiết kế không dùng cổng ghép kênh MUX. Thay vào đó, nó sử dụng hệ thống mạch Latch nhạy mức bằng 2 xung nhịp riêng."

***

## Slide 32: Hoạt động của hai Clock LSSD (04_02_ff_structures.html)
- **Hành động:** 
  Chỉ vào tín hiệu Clock A và Clock B rời rạc.
- **Lời thoại tham khảo:**
  "Thiết kế này vĩnh viễn không gây trễ chậm luồng dữ liệu thật. Bởi vì nó truyền dữ liệu thông qua xung Nhịp A và xung Nhịp B lệch pha nhau. Phương pháp này chịu hao tốn diện tích cực lớn trên Chip để đổi lấy sự an toàn tuyệt đối chống lỗi Race Condition."

***

## Slide 33: Phân tích Case Study (04_03_residue5.html)
- **Hành động:** 
  Chỉ vào FSM Residue vòng tuần hoàn.
- **Lời thoại tham khảo:**
  "Để theo dõi chi tiết phép thuật Scan này biến hình vi mạch thế nào, ta lấy 1 tiểu cảnh Case Study: Bộ máy FSM hệ đếm Modulo 5 tịnh tiến hoạt động theo vòng tròn tuần hoàn."

***

## Slide 34: Hiện trạng chưa thiết kế Test (04_03_residue5.html)
- **Hành động:** 
  Chỉ vào khối 3 con DFFF màu xám.
- **Lời thoại tham khảo:**
  "Trong nguyên bản Pre-synthesis, bản thiết kế Gate-level của ta sở hữu 3 khối Flip-Flop lưu trữ trạng thái nằm rãi rác xen kẽ nhau với một loạt các vòng lặp hồi tiếp khép kín cực kỳ tù túng để Test rà lỗi."

***

## Slide 35: Quá trình Scan Stitching ghép nối (04_03_residue5.html)
- **Hành động:** 
  Chỉ vào các SD-FF đã thay thế D-FF thông thường.
- **Lời thoại tham khảo:**
  "Ngay khi công cụ Compiler được trao quyền thực thi Scan Stitching (Quá trình khâu vá vi mạch). Nó tàn nhẫn bới móc 3 Flip-flops nguyên thủy lên và trồng thay thế vào 3 MUX-DFF (Scan FF)."

***

## Slide 36: Sợi dây nối Chain (04_03_residue5.html)
- **Hành động:** 
  Vuốt theo đường chỉ đỏ kết nối Scan-In sang chân Q, đưa vào MUX của tầng tiếp theo.
- **Lời thoại tham khảo:**
  "Đỉnh cao của kỹ thuật này là nét khâu mũi chỉ dây điện trơn tru. Dòng điện đi từ Scan In trực tiếp vào chân SI của phần tử đầu tiên. Sau đó nó đi ra chân Q và chọc vào chân SI của phần tử kế tiếp. Cuối cùng, dòng máu này mượt mà tuôn ra tận đích Scan Out."

***

## Slide 37: Cao tốc Vector Kiểm thử (04_03_residue5.html)
- **Hành động:** 
  Chỉ mô hình chiếc xe Test Vector chay qua chuỗi.
- **Lời thoại tham khảo:**
  "Nhờ đường chỉ đỏ chuyên biệt không hề đụng chạm logic hệ thống ấy, Vector Test chớp nhoáng chạy băng qua cấu trúc mạch một cách độc lập không vướng bận trở ngại nào từ vòng lặp."

***

## Slide 38: Môi trường Virtual Tester (04_04_virtual_tester.html)
- **Hành động:** 
  Chỉ vào ATE Server Logic phía bên trái.
- **Lời thoại tham khảo:**
  "Nhưng công nghệ dây chuyền Scan In / Scan Out nói trên sẽ chỉ là sắt vụn nếu không có sự tiếp ứng tại xưởng từ cỗ máy ATE Test Tester cực lớn cung cấp xung Clock và Test Vector tương ứng."

***

## Slide 39: Giao tiếp qua chấu Kim (04_04_virtual_tester.html)
- **Hành động:** 
  Chỉ vào thẻ Kim Probe đang chọc lên bề mặt Silicon.
- **Lời thoại tham khảo:**
  "Vi mạch Silicon siêu nhỏ không thể cắm vào cổng giao tiếp bình thường. Máy Tester khổng lồ phải chích dữ liệu truyền qua hệ thống xúc tu siêu vi. Những xúc tu này có đính hàng nghìn mũi kim nhọn bằng chất liệu vàng tinh khiết ép vào chân con IC."

***

## Slide 40: Chu kỳ đẩy Shift-In (04_04_virtual_tester.html)
- **Hành động:** 
  Chỉ vào mũi tên đẩy trạng thái Dịch (Shift Mode).
- **Lời thoại tham khảo:**
  "Vậy quy trình nhịp Clock diễn ra sau đó ra thế nào? Cây kim ATE sẽ bơm đều đặn từng Bit, đẩy đẩy liên tục vào ống Shift Register cho đến khi toàn bộ mảng dữ liệu Tester yên vị tại hàng ghế Flip-flops."

***

## Slide 41: Khóa Capture Logic Kết Quả (04_04_virtual_tester.html)
- **Hành động:** 
  Sập trạng thái TE chuyển sang 0 (Normal).
- **Lời thoại tham khảo:**
  "Ngay khi Vector đã nạp đủ, ATE điều phối tín hiệu TE về mức Normal, và bắn 1 phát xung Clock nhanh gọi là nhịp Capture. Nhịp sập này chụp nhanh (Snapshot) cái kết quả tổ hợp do lỗi của IC gây ra rồi chốt gọn vào lại bộ ống Shift Register."

***

## Slide 42: Quá trình gối đầu đường song song (04_04_virtual_tester.html)
- **Hành động:** 
  Minh họa hành động lấy hàng mới và đẩy hàng cũ ra trên biểu đồ Timing.
- **Lời thoại tham khảo:**
  "Để tối ưu KPI thời gian, cơ chế này thực hiện hành trình gối đầu. Máy Tester tống những lỗi gặt được ra bộ nhớ máy chủ để so sánh. Quá trình này chạy song song trực tiếp với luồng dữ liệu mới đang tuôn vào. Sự lặp đi lặp lại theo kiểu đường ống này rất tiết kiệm thời gian tổng."
