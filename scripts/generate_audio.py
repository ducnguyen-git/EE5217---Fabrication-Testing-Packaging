import os
import re
import glob
import json
import time
import urllib.request
import urllib.error

API_KEY = "LcoBwMK01wxuOfBu3ZnOryHBQrzqnXjq"
VOICE = "minhquang" # Giọng Nam Miền Nam rất vang và sáng

def clean_markdown_text(text):
    text = text.strip()
    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1]
        text = text.strip()
        
    text = text.replace("*", "").replace("_", "").replace("$", "")
    text = text.replace("\n", " ").strip()
    text = re.sub(' +', ' ', text)
    return text

def parse_grouped_slides(slide_nums_str, full_text):
    nums = re.findall(r'\d+', slide_nums_str)
    pieces = re.split(r'\(Slide\s*([\d,\-\s&]+)\)', full_text, flags=re.IGNORECASE)
    
    mapping = {}
    if len(pieces) > 1:
        for i in range(1, len(pieces), 2):
            matched_nums_str = pieces[i]
            matched_text = pieces[i+1].strip()
            for n in re.findall(r'\d+', matched_nums_str):
                mapping[n] = matched_text
                
    if not mapping:
        for i, n in enumerate(nums):
            mapping[n] = full_text

    for n in nums:
        if n not in mapping:
            mapping[n] = "Nội dung slide gốc bị trống."
            
    return {n: mapping.get(n) for n in nums}

def generate_fpt_audio(text, output_file):
    url = "https://api.fpt.ai/hmi/tts/v5"
    headers = {
        'api-key': API_KEY,
        'speed': '',
        'voice': VOICE,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    data = text.encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    
    try:
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode('utf-8')
            res_json = json.loads(res_body)
            if "async" not in res_json:
                print(f"  ❌ Error từ API: {res_json}")
                return False
                
            audio_url = res_json["async"]
            print(f"  ⏳ Đang đợi xử lý trên server FPT...")
            
            # Polling the audio url until ready
            for _ in range(30): # max 60s
                time.sleep(2)
                try:
                    audio_req = urllib.request.Request(audio_url)
                    with urllib.request.urlopen(audio_req) as audio_resp:
                        if audio_resp.status == 200:
                            content = audio_resp.read()
                            # Đôi khi FPT trả về JSON chứa Exception thay vì file MP3 dù mã là 200 OK
                            try:
                                json_err = json.loads(content.decode('utf-8'))
                                print(f"  ❌ FPT trả về thông báo lỗi nội bộ: {json_err}")
                                return False
                            except:
                                pass # Content là Binary Audio chuẩn
                                
                            # Lưu file mp3
                            with open(output_file, 'wb') as f:
                                f.write(content)
                            return True
                except urllib.error.HTTPError as e:
                    # 404 là trạng thái bình thường khi Audio đang render chưa xong
                    if e.code != 404:
                        print(f"  ⚠️ HTTP Error {e.code} khi fetch audio: {e.read().decode('utf-8', errors='ignore')}")
                except Exception as e:
                    print(f"  ⚠️ Lỗi Request khi fetch audio: {e}")
                    
            print(f"  ❌ Timeout: Quá thời gian tải {output_file}")
            return False
            
    except Exception as e:
        print(f"  ❌ Yêu cầu API bị từ chối: {e}")
        return False

def main():
    scripts_dir = "/Users/huythanh/Code/EE5217_Tue/scripts"
    output_dir = "/Users/huythanh/Code/EE5217_Tue/audio"
    
    os.makedirs(output_dir, exist_ok=True)
    
    md_files = sorted(glob.glob(os.path.join(scripts_dir, "chapter_*.md")))
    
    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        slides = re.split(r'\n## Slide ', content)
        
        for slide in slides[1:]:
            match = re.match(r'^([^:]+)', slide)
            if not match:
                continue
                
            slide_header_nums = match.group(1)
            parts = slide.split("- **Lời thoại tham khảo:**")
            if len(parts) > 1:
                text_part = re.split(r'\n\*\*\*|\n##', parts[1])[0]
                text_part = clean_markdown_text(text_part)
                
                if text_part:
                    slide_audio_map = parse_grouped_slides(slide_header_nums, text_part)
                    
                    for slide_n, t_part in slide_audio_map.items():
                        if not t_part or not t_part.strip():
                            t_part = "Nội dung đang trống."
                            
                        # Remove Slide tags
                        t_part = re.sub(r'\(Slide\s*[\d,\-\s&]+\)', '', t_part, flags=re.IGNORECASE).strip()
                        
                        # Strip unsafe punctuation that crashes FPT AI silently
                        t_part = t_part.replace("'", "").replace("(", ", ").replace(")", ", ").replace('"', '')
                        t_part = t_part.replace("[", "").replace("]", "")
                        
                        # Giữ lại tiếng Anh nguyên bản cho FPT đọc tự nhiên
                        mp3_file = os.path.join(output_dir, f"slide_{slide_n}.mp3")
                        
                        # Smart Cache Logic: skip if mp3 exists, is > 1KB, and is newer than its markdown script
                        if os.path.exists(mp3_file):
                            mp3_mtime = os.path.getmtime(mp3_file)
                            md_mtime = os.path.getmtime(md_file)
                            if mp3_mtime >= md_mtime and os.path.getsize(mp3_file) > 1000:
                                print(f"⏭️ Bỏ qua slide_{slide_n} (File đã cập nhật mới nhất)")
                                continue
                                
                        print(f"▶️ Bắt đầu gọi FPT cho slide_{slide_n}...")
                        
                        success = False
                        for attempt in range(3):
                            success = generate_fpt_audio(t_part, mp3_file)
                            if success:
                                print(f"  ✅ Đã thành công sinh API: {mp3_file}\n")
                                break
                            print(f"  ⚠️ Lỗi hoặc Timeout. Thử lại lần {attempt+2}...")
                            time.sleep(3)
                            
                        if not success:
                            print(f"  🚨 Failed hoàn toàn slide_{slide_n} sau 3 lần thử.\n")

if __name__ == "__main__":
    main()
