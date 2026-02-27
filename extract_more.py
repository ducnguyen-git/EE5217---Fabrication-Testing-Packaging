import PyPDF2
import os

pdf_path = "d:/Phd/EE5217_Tue/refs/3-Digital System Test and Testable Design_ Using HDL Models and Architectures.pdf"
reader = PyPDF2.PdfReader(pdf_path)
text = ""
start_page = 200
end_page = min(301, len(reader.pages))
for i in range(start_page, end_page):
    text += reader.pages[i].extract_text() + "\n"
with open("d:/Phd/EE5217_Tue/Chapter7_Pages200_300.txt", "w", encoding="utf-8") as f:
    f.write(text)
print(f"Extracted pages {start_page} to {end_page} successfully to Chapter7_Pages200_300.txt")
