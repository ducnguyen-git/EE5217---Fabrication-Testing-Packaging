# Kịch bản Thuyết trình - Chương 04: Kiến trúc Full Scan và Virtual Tester

## Slide 26: Mở đầu Chương 4 (04_00_chapter.html)
- **Hành động:** 
  Nhấn mạnh chữ "sự đơn giản" và "hiệu quả".
- **Lời thoại tham khảo:**
  "Bước vào Chương 4: Kỹ thuật Full Scan - Lõi của DFT.
  Hàng chục năm nghiên cứu DFT tựu chung lại bằng câu nói của Austin Freeman: *'Sự đơn giản chính là linh hồn của tính hiệu quả.'*"

***

## Slide 27: Khái quát Full Scan (04_01_fullscan_intro.html)
- **Hành động:** 
  Chỉ vào hoạt ảnh luân chuyển Test Enable và Normal Mode.
- **Lời thoại tham khảo:**
  "Ý tưởng đột phá của Full Scan là biến tất cả các Flip-Flops nội bộ đang kết nối ngẫu nhiên trong chip thành một sợi dây chuyền duy nhất. Bằng sự đơn giản đó, mọi thành phần nhớ lưu trữ đã bị ép vào khuôn khổ tuần tự dịch bit (Shift Register)."

***

## Slide 28: Cấu trúc Scan Flip-Flop (MUX-DFF) (04_02_ff_structures.html)
- **Hành động:** 
  Chỉ tay vào thành phần cổng Mux ghép trước cổng D.
- **Lời thoại tham khảo:**
  "Để uốn nắn một thanh Flip-Flop thông thường thành Scan Flip-Flop. Cấu trúc Muxed-DFF được sử dụng đại trà bằng cách chèn thiết bị ghép kênh MUX 2:1 vào cổng nhận dữ liệu Data In của Flip-Flop."

***

## Slide 29: Tuyến chuyển mạch lựa chọn (04_02_ff_structures.html)
- **Hành động:** 
  Chỉ vào tín hiệu Test Enable TE.
- **Lời thoại tham khảo:**
  "Tín hiệu công tắc TE (Test Enable) sẽ làm trọng tài điều hướng cho Cổng Mux: Nó cho phép Flip-Flop chốt lại kết quả điện toán bình thường nếu TE mức 0, hoặc ép nhận dữ liệu dồn dịch từ con Flip-Flop anh em sát bên nó qua ngõ SI nếu TE ở mức 1."

***

## Slide 30: Nút thắt Cổ chai Timing (04_02_ff_structures.html)
- **Hành động:** 
  Nhấn mạnh vào chữ Setup Time Delay mầu đỏ.
- **Lời thoại tham khảo:**
  "Gót A-sin của MUX-DFF là Timing Critical Delay. Vì con MUX chèn án ngữ giữa hệ thống, luồng dữ liệu sạch bắt buộc phải tốn thêm thời gian đi xuyên qua Mux, làm suy giảm tốc độ xung nhịp hoạt động tối đa mà mạch vốn có thể đạt được."

***

## Slide 31: Khái quát Level Sensitive Scan Design (LSSD) (04_02_ff_structures.html)
- **Hành động:** 
  Chỉ sự khác biệt của LSSD.
- **Lời thoại tham khảo:**
  "Để vượt qua nỗi sợ kẹt Delay, gã khổng lồ máy trạm IBM đã tạo ra con đường thứ 2 mang tên Level Sensitive Scan Design (LSSD), nổi tiếng với thiết kế không dùng cổng MUX mà sử dụng hệ thống mạch Latch nhạy mức (Dual-Clock Latch)."

***

## Slide 32: Hoạt động của hai Clock LSSD (04_02_ff_structures.html)
- **Hành động:** 
  Chỉ vào tín hiệu Clock A và Clock B rời rạc.
- **Lời thoại tham khảo:**
  "Thiết kế này vĩnh viễn không gây trễ chậm mạch luồng dữ liệu thật, bởi vì nó bơm Shift Data Test thông qua một cánh cửa dùng Clock A và Clock B lệch pha nhau, chịu mất thêm diện tích cực lớn trên Chip để đổi lấy sự an toàn tuyệt đối chống lỗi Race Condition."

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
  "Đỉnh cao của nghệ thuật Stitching là nét khâu mũi chỉ dây điện kéo từ Scan-In (Tin) trực tiếp vào chân SI của Flip-flop đầu tiên, đi ra chân Q, chọc vào chân SI của con Flip-flop thứ hai, và mượt mà tuôn thẳng ra tận đích Scan-Out (Tout)."

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
  "Vì quá nhỏ bé, vi mạch Silicon Die không thể cắm vào cổng USB, mà buộc chiếc máy ATE Tester phải chích dữ liệu Scan In truyền qua hệ thống xúc tu siêu vi (Probe Card) có đính mũi nhọn bằng chất liệu vàng tinh khiết ép vào Pad của IC."

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
  "Và để tối ưu KPI thời gian test, cơ chế ATE thực hiện quá trình tống những lỗi gặt được (Shift-Out) ra bộ nhớ máy chủ so sánh trùng lúc gối đầu trực tiếp với luồng Vector Data mới (Shift-In) ùa vào theo dạng Pipeline lặp đi lặp lại rất tiết kiệm chu kì Clock."
