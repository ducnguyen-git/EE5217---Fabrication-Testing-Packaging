import urllib.request
import urllib.error
import json
import time

API_KEY = "LcoBwMK01wxuOfBu3ZnOryHBQrzqnXjq"
VOICE = "minhquang"

url = "https://api.fpt.ai/hmi/tts/v5"
headers = {
    'api-key': API_KEY,
    'speed': '',
    'voice': VOICE,
    'Content-Type': 'application/x-www-form-urlencoded'
}

texts = [
    "Để giải quyết bế tắc, ý tưởng vĩ đại của Xờ can đi zai là bẻ gãy một phần của các mạch tuần tự đa trạng thái thành các khối tổ hợp rời rạc đơn giản hơn.",
    "Nó hoạt động như một tấm khiên bảo vệ, giúp giảm tải thuật toán sinh Tét Pát-tờn.",
    "Ý tưởng của Scan Design là bẻ gãy mạch tuần tự.",
]

for i, text in enumerate(texts):
    data = text.encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    
    print(f"Test {i+1}: {text}")
    try:
        with urllib.request.urlopen(req) as response:
            res_json = json.loads(response.read().decode('utf-8'))
            audio_url = res_json["async"]
            # Fast poll 10s
            success = False
            for _ in range(10):
                time.sleep(1)
                try:
                    q = urllib.request.Request(audio_url)
                    with urllib.request.urlopen(q) as r:
                        if r.status == 200:
                            print(f"  ✅ Thành công test {i+1}")
                            success = True
                            break
                except Exception:
                    pass
            if not success:
                print(f"  ❌ Timeout (Có lỗi nội bộ) Test {i+1}")
    except Exception as e:
        print("Lỗi:", e)
