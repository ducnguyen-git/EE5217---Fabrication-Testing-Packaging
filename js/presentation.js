const slidesList = [
    'sections/00_cover.html',
    'sections/00_toc.html',
    'sections/01_00_chapter.html',
    'sections/01_01_khai_niem.html',
    'sections/01_02_background.html',
    'sections/01_03_objectives.html',
    'sections/02_00_chapter.html',
    'sections/02_01_intro.html',
    'sections/02_01_making_testable.html',
    'sections/02_01_tradeoffs.html',
    'sections/02_02_huffman.html',
    'sections/02_03_combinational_testability.html',
    'sections/02_03_logic_fault_models.html',
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
    'sections/05_01_adding_machine.html',
    'sections/05_02_shadow_register.html',
    'sections/05_03_partial_scan.html',
    'sections/05_04_multiple_scan_intro.html',
    'sections/05_05_other_scan.html',
    'sections/06_00_chapter.html',
    'sections/06_01_rtl_scan.html',
    'sections/06_02_rtl_full_scan.html',
    'sections/06_03_rtl_multiple_scan.html',
    'sections/07_00_chapter.html',
    'sections/07_01_comparison.html',
    'sections/07_02_casestudy.html',
    'sections/07_03_summary.html'
];

const wrapper = document.getElementById('slides_wrapper');
let currentSlide = 0;
let isPresenting = false;
let scaleObserver = null; // Biến lưu trữ ResizeObserver

// Khởi tạo ResizeObserver để theo dõi Tự động Kích thước
function initResizeObserver() {
    if (!scaleObserver) {
        scaleObserver = new ResizeObserver((entries) => {
            if (!isPresenting) return;
            // Chỉ tính toán khi có sự thay đổi thực sự trong khối lượng thẻ DOM
            for (let entry of entries) {
                if (entry.target.classList.contains('active')) {
                    recalculateScale(entry.target);
                    break;
                }
            }
        });
    }
}

// Hàm tính toán cốt lõi (Tách biệt khỏi sự kiện UI)
function recalculateScale(activeSlide) {
    let baseWidth = 1440;
    let baseHeight = 900;

    // Lấy kích thước thật của Slide bao gồm padding/margin
    if (activeSlide && activeSlide.scrollHeight > baseHeight) {
        baseHeight = activeSlide.scrollHeight + 40; // Safely buffer
    }

    const sx = window.innerWidth / baseWidth;
    const sy = window.innerHeight / baseHeight;
    const scale = Math.min(sx, sy);
    document.body.style.setProperty('--scale', scale);
}

// Dừng theo dõi nội dung cũ và cắm vào nội dung mới
function observeActiveSlide() {
    initResizeObserver();
    scaleObserver.disconnect(); // Gỡ các theo dõi cũ
    const activeSlide = document.querySelector('.slide-container.active');
    if (activeSlide) {
        scaleObserver.observe(activeSlide);
        // Chạy ép một lần đầu tiên để cover Layout tĩnh
        recalculateScale(activeSlide);
    }
}

// Auto-scale slides in overview mode to fit viewport width
function updateOverviewZoom() {
    if (isPresenting) return;
    const vw = window.innerWidth;
    const slideWidth = 1440;
    const zoom = Math.min(1, (vw * 0.9) / slideWidth);
    document.documentElement.style.setProperty('--slide-zoom', zoom);
}
updateOverviewZoom();

window.addEventListener('resize', () => {
    if (isPresenting) {
        const activeSlide = document.querySelector('.slide-container.active');
        recalculateScale(activeSlide);
    } else {
        updateOverviewZoom();
    }
});


// Load all slides
async function loadSlides() {
    try {
        const promises = slidesList.map(url => fetch(url).then(res => {
            if (!res.ok) throw new Error(`Could not load ${url}`);
            return res.text();
        }));

        const contents = await Promise.all(promises);

        let globalIndex = 0;
        contents.forEach((html) => {
            const div = document.createElement('div');
            div.innerHTML = html;
            // Cho phép 1 file HTML có chứa NHIỀU thẻ .slide-container (phục vụ tách hình)
            const subSlides = div.querySelectorAll('.slide-container');
            if (subSlides.length > 0) {
                subSlides.forEach(slide => {
                    slide.id = `slide-${globalIndex++}`;
                    wrapper.appendChild(slide);
                });
            } else if (div.firstElementChild) {
                div.firstElementChild.id = `slide-${globalIndex++}`;
                wrapper.appendChild(div.firstElementChild);
            }
        });

        document.getElementById('loading').style.display = 'none';
        updateCounter();

        // Gọi MathJax render lại toàn bộ trang sau khi đã nạp xong HTML
        if (window.MathJax && typeof MathJax.typesetPromise === 'function') {
            MathJax.typesetPromise().catch((err) => console.log('MathJax error: ', err));
        } else {
            console.log('MathJax not ready yet, will typeset when available.');
            // Retry after MathJax finishes loading
            document.getElementById('MathJax-script')?.addEventListener('load', () => {
                if (typeof MathJax.typesetPromise === 'function') {
                    MathJax.typesetPromise().catch((err) => console.log('MathJax error: ', err));
                }
            });
        }

        return Promise.resolve(); // Return success

    } catch (error) {
        console.error(error);
        document.getElementById('loading').innerHTML = `
            <div style="text-align: center; color: #ff6b6b; padding: 20px;">
                <h1>Lỗi tải dữ liệu Slide!</h1>
                <p>Chi tiết lỗi:</p>
                <div style="background: #333; padding: 20px; border-radius: 8px; margin-top: 20px; word-break: break-word;">
                    <code>${error.message}</code>
                </div>
            </div>
        `;
    }
}

function updateCounter() {
    const total = document.querySelectorAll('.slide-container').length;
    document.getElementById('counter').innerText = `${currentSlide + 1} / ${total}`;
}

function updateView() {
    const slides = document.querySelectorAll('.slide-container');
    updateCounter();

    if (isPresenting) {
        slides.forEach((s, i) => {
            s.classList.toggle('active', i === currentSlide);
        });
        // Gắn móc theo dõi thẻ active MỚI nhất (Rootfix)
        observeActiveSlide();
    } else {
        slides[currentSlide].scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}

function nextSlide() {
    const total = document.querySelectorAll('.slide-container').length;
    if (currentSlide < total - 1) {
        currentSlide++;
        updateView();
    }
}

function prevSlide() {
    if (currentSlide > 0) {
        currentSlide--;
        updateView();
    }
}

let wasFullscreenAchieved = false;

function togglePresentation() {
    const slides = document.querySelectorAll('.slide-container');
    isPresenting = !isPresenting;
    document.body.classList.toggle('presentation-mode', isPresenting);

    if (isPresenting) {
        // Try fullscreen but don't depend on it for presentation mode
        wasFullscreenAchieved = false;
        document.documentElement.requestFullscreen().then(() => {
            wasFullscreenAchieved = true;
        }).catch(e => {
            console.log('Fullscreen not available, presenting in windowed mode.');
            wasFullscreenAchieved = false;
        });
        updateView();
        // Change icon to Stop/Compress
        const btnIcon = document.querySelector('#controls button:nth-child(2) i');
        if (btnIcon) {
            btnIcon.classList.remove('fa-play');
            btnIcon.classList.add('fa-compress');
        }
    } else {
        wasFullscreenAchieved = false;
        if (document.fullscreenElement) {
            document.exitFullscreen().catch(e => { });
        }
        document.body.style.setProperty('--scale', 1);
        slides.forEach(s => s.classList.remove('active'));
        // Change icon back to Play
        const btnIcon = document.querySelector('#controls button:nth-child(2) i');
        if (btnIcon) {
            btnIcon.classList.remove('fa-compress');
            btnIcon.classList.add('fa-play');
        }
        // Cleanup presentation tools
        if (window.presentationTools) {
            window.presentationTools.cleanup();
        }
        // Sync scroll to current slide
        setTimeout(() => slides[currentSlide].scrollIntoView({ behavior: 'smooth', block: 'center' }), 100);
    }
}

// Only exit presentation if user intentionally exited fullscreen (e.g. ESC key)
document.addEventListener('fullscreenchange', () => {
    if (!document.fullscreenElement && isPresenting && wasFullscreenAchieved) {
        togglePresentation();
    }
});

// Keyboard nav
document.addEventListener('keydown', (e) => {
    // Skip if tools dialogs are handled by presentation-tools.js
    if (document.querySelector('#slide-jump-overlay.visible') || document.querySelector('#chapter-nav-overlay.visible')) return;
    if (document.querySelector('#blackout-overlay.visible')) return;

    if (e.key === 'ArrowRight' || e.key === ' ') {
        if (!document.body.classList.contains('drawing-mode')) nextSlide();
    }
    if (e.key === 'ArrowLeft') {
        if (!document.body.classList.contains('drawing-mode')) prevSlide();
    }
    if (e.key === 'f' || e.key === 'F' || e.key === 'p' || e.key === 'P') {
        if (e.key === 'f' || e.key === 'F') togglePresentation();
        // 'p' and 'P' only toggle if not in presentation mode (avoid conflict)
        if ((e.key === 'p' || e.key === 'P') && !isPresenting) togglePresentation();
    }
    if (e.key === 'Escape' && isPresenting && !wasFullscreenAchieved) {
        if (!document.body.classList.contains('drawing-mode')) togglePresentation();
    }
    // ESC during fullscreen is handled by fullscreenchange
});

// Mouse nav
document.addEventListener('click', (e) => {
    // Only trigger in presentation mode and not on buttons/overlays
    if (isPresenting && !e.target.closest('#controls') && !e.target.closest('#pres-toolbar')
        && !e.target.closest('#context-menu') && !e.target.closest('#drawing-toolbar')
        && !document.body.classList.contains('drawing-mode')
        && !document.body.classList.contains('laser-mode')
        && !document.querySelector('#slide-jump-overlay.visible')
        && !document.querySelector('#chapter-nav-overlay.visible')) {
        nextSlide();
    }
});

// Context menu is now handled by presentation-tools.js

// Scroll Observer for Overview Mode
const observer = new IntersectionObserver((entries) => {
    if (isPresenting) return; // Don't mess with tracking while presenting
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // Extract index from id "slide-X"
            const index = parseInt(entry.target.id.replace('slide-', ''));
            if (!isNaN(index)) {
                currentSlide = index;
                updateCounter();
            }
        }
    });
}, {
    threshold: 0.6 // Slide must be 60% visible to be considered "current"
});

// Init
loadSlides().then(() => {
    // Attach observer to all slides after they load
    document.querySelectorAll('.slide-container').forEach(slide => {
        observer.observe(slide);
    });
});
