import os
import glob
import re

def renumber_slides():
    scripts_dir = "/Users/huythanh/Code/EE5217_Tue/scripts"
    md_files = sorted(glob.glob(os.path.join(scripts_dir, "chapter_*.md")))
    
    global_index = 1
    
    for filename in md_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract lines
        lines = content.split('\n')
        new_lines = []
        
        for line in lines:
            if re.match(r'^## Slide \d+:', line):
                # Replace the digit with global_index
                new_line = re.sub(r'## Slide \d+:', f'## Slide {global_index}:', line)
                new_lines.append(new_line)
                global_index += 1
            else:
                new_lines.append(line)
                
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))

if __name__ == '__main__':
    renumber_slides()
    print("Renumbering complete.")
