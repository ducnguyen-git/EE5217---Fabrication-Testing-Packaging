import urllib.request
import urllib.error
import json
import time
import os

API_KEY = "LcoBwMK01wxuOfBu3ZnOryHBQrzqnXjq"
VOICE = "minhquang"

url = "https://api.fpt.ai/hmi/tts/v5"
headers = {
    'api-key': API_KEY,
    'speed': '',
    'voice': VOICE,
    'Content-Type': 'application/x-www-form-urlencoded'
}

text_1 = "Xin chào thầy Nguyễn Hoàng Trang và tất cả các bạn. Hôm nay, Nhóm 7 xin trình bày đề tài thiết kế hỗ trợ kiểm thử bằng kỹ thuật Xcan, hay còn gọi là Scan based D F T. Nhóm gồm có bốn thành viên là: thái thanh bình, tiến giang, minh đức, và huy thanh. Đề tài được thực hiện trong khuôn khổ môn Thiết kế phần cứng hệ thống số."

text_2 = "Kỹ thuật Full Scan sử dụng MUX DFF tạo thành chuỗi Shift Register. Kiến trúc này giúp cải thiện Test Time và bao phủ Fault Coverage tối đa."

for i, text in enumerate([text_1, text_2]):
    data = text.encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    
    print(f"Bắt đầu tải test {i+1}...")
    try:
        with urllib.request.urlopen(req) as response:
            res_json = json.loads(response.read().decode('utf-8'))
            audio_url = res_json["async"]
            
            for _ in range(30):
                time.sleep(2)
                try:
                    out_path = f"/Users/huythanh/Code/EE5217_Tue/audio/test_fpt_{i+1}.mp3"
                    q = urllib.request.Request(audio_url)
                    with urllib.request.urlopen(q) as r:
                        if r.status == 200:
                            with open(out_path, 'wb') as f:
                                f.write(r.read())
                            print(f"Xong {out_path}!")
                            break
                except Exception:
                    pass
    except Exception as e:
        print("Lỗi:", e)
