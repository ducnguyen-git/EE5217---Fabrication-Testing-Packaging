import os
import re
import subprocess
import glob

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
    
    # Split text based on (Slide XX) or (Slide XX-YY)
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
            if i == 0:
                mapping[n] = full_text
            else:
                mapping[n] = full_text # if there's no Slide explicit split, just assign the same text so at least it plays, or user can skip it.

    # Ensure all extracted nums in the header get an assignment
    for n in nums:
        if n not in mapping:
            mapping[n] = "Nội dung tiếp nối slide trước."
            
    return {n: mapping.get(n) for n in nums}

def main():
    scripts_dir = "/Users/huythanh/Code/EE5217_Tue/scripts"
    output_dir = "/Users/huythanh/Code/EE5217_Tue/audio"
    
    # Remove old malformed files like slide_7_8.mp3
    for f in glob.glob(os.path.join(output_dir, "*_*_*.mp3")) + glob.glob(os.path.join(output_dir, "slide_*_*.mp3")):
        try:
            os.remove(f)
        except:
            pass
            
    md_files = sorted(glob.glob(os.path.join(scripts_dir, "chapter_*.md")))
    edge_tts_bin = "/Users/huythanh/Library/Python/3.9/bin/edge-tts"
    
    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        slides = re.split(r'\n## Slide ', content)
        
        for slide in slides[1:]:
            # Get slide header numbers
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
                            t_part = "Nội dung tiếp nối."
                            
                        # Clean out any remaining "(Slide ...)" tags so audio doesn't read them out loud
                        t_part = re.sub(r'\(Slide\s*[\d,\-\s&]+\)', '', t_part, flags=re.IGNORECASE).strip()
                            
                        mp3_file = os.path.join(output_dir, f"slide_{slide_n}.mp3")
                        print(f"Generating {mp3_file} ...")
                        
                        subprocess.run([
                            edge_tts_bin, 
                            "--voice", "vi-VN-NamMinhNeural", 
                            "--text", t_part, 
                            "--write-media", mp3_file
                        ], capture_output=True, text=True)

if __name__ == "__main__":
    main()
