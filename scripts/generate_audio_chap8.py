import os
import re
import time
import json
import urllib.request
import urllib.error

API_KEY = "LcoBwMK01wxuOfBu3ZnOryHBQrzqnXjq"
VOICE = "minhquang"

def clean_markdown_text(text):
    text = text.strip()
    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1].strip()
    text = text.replace("*", "").replace("_", "").replace("$", "")
    text = text.replace("\n", " ").strip()
    text = re.sub(' +', ' ', text)
    return text

def parse_grouped_slides(slide_nums_str, full_text):
    nums = re.findall(r'\d+', slide_nums_str)
    return {n: full_text for n in nums}

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
            res_json = json.loads(response.read().decode('utf-8'))
            if "async" not in res_json: return False
            audio_url = res_json["async"]
            for _ in range(45):
                time.sleep(2)
                try:
                    audio_req = urllib.request.Request(audio_url)
                    with urllib.request.urlopen(audio_req) as audio_resp:
                        if audio_resp.status == 200:
                            content = audio_resp.read()
                            try:
                                json.loads(content.decode('utf-8'))
                                return False
                            except:
                                with open(output_file, 'wb') as f:
                                    f.write(content)
                                return True
                except urllib.error.HTTPError as e:
                    pass
            return False
    except:
        return False

def main():
    md_file = "/Users/huythanh/Code/EE5217_Tue/scripts/chapter_08_cicd_latex.md"
    output_dir = "/Users/huythanh/Code/EE5217_Tue/audio"
    
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    slides = re.split(r'\n## Slide ', content)
    for slide in slides[1:]:
        match = re.match(r'^([^:]+)', slide)
        if not match: continue
        slide_header_nums = match.group(1)
        
        parts = slide.split("- **Lời thoại tham khảo:**")
        if len(parts) > 1:
            text_part = re.split(r'\n\*\*\*|\n##', parts[1])[0]
            text_part = clean_markdown_text(text_part)
            
            slide_audio_map = parse_grouped_slides(slide_header_nums, text_part)
            for slide_n, t_part in slide_audio_map.items():
                t_part = t_part.replace("'", "").replace("(", ", ").replace(")", ", ").replace('"', '')
                t_part = t_part.replace("[", "").replace("]", "")
                
                mp3_file = os.path.join(output_dir, f"slide_{slide_n}.mp3")
                print(f"Generating audio for slide_{slide_n}...")
                for attempt in range(3):
                    if generate_fpt_audio(t_part, mp3_file):
                        print(f"  OK: {mp3_file}")
                        break
                    print("  Retry...")
                    time.sleep(3)

if __name__ == "__main__":
    main()
