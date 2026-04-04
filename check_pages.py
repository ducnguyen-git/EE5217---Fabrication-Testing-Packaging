import os

slides = [
    'sections/00_00_cover.html',
    'sections/00_01_toc.html',
    'sections/01_00_chapter.html',
    'sections/01_01_khai_niem.html',
    'sections/01_02_background.html',
    'sections/01_03_objectives.html',
    'sections/01_04_physical_defects.html',
    'sections/02_00_chapter.html',
    'sections/02_01_huffman.html',
    'sections/02_02_combinational_testability.html',
    'sections/02_03_why_scan_design.html',
    'sections/02_04_tradeoffs.html',
    'sections/02_05_logic_fault_models.html',
    'sections/03_00_chapter.html',
    'sections/03_01_insertion.html',
    'sections/03_02_muxdemux.html',
    'sections/03_03_isolated_scan.html',
    'sections/03_04_reduce_simul.html',
    'sections/03_05_basic_scan_concept.html',
    'sections/04_00_chapter.html',
    'sections/04_01_fullscan_intro.html',
    'sections/04_02_ff_structures.html',
    'sections/04_03_residue5.html',
    'sections/04_04_virtual_tester.html',
    'sections/05_00_chapter.html',
    'sections/05_01_full_scan_architecture.html',
    'sections/05_02_shadow_register.html',
    'sections/05_03_partial_scan.html',
    'sections/05_04_multiple_scan_intro.html',
    'sections/05_05_other_scan.html',
    'sections/06_00_chapter.html',
    'sections/06_01_rtl_full_scan.html',
    'sections/06_02_rtl_full_scan_ex.html',
    'sections/06_03_rtl_multiple_scan.html',
    'sections/06_04_rtl_multiple_scan_ex.html',
    'sections/07_00_chapter.html',
    'sections/07_01_comparison.html',
    'sections/07_02_casestudy.html',
    'sections/07_03_summary.html'
]
slide_count = 1
for s in slides:
    with open('e:/EE5217_Tue/' + s, 'r', encoding='utf-8') as f:
        content = f.read()
    c = content.count('class="slide-container"')
    if c == 0 and len(content.strip()) > 0:
        c = 1 
    for i in range(c):
        print(f'Page {slide_count}: {s}')
        slide_count += 1
