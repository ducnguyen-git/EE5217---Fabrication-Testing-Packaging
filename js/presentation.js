const slidesList = [
    'sections/00_cover.html',
    'sections/00_toc.html',
    'sections/01_01_khai_niem.html',
    'sections/01_02_background.html',
    'sections/01_03_objectives.html',
    'sections/02_01_intro.html',
    'sections/02_01_making_testable.html',
    'sections/02_01_tradeoffs.html',
    'sections/02_02_huffman.html',
    'sections/02_03_combinational_testability.html',
    'sections/02_03_logic_fault_models.html',
    'sections/03_01_insertion.html',
    'sections/03_02_muxdemux.html',
    'sections/03_03_isolated_scan.html',
    'sections/03_04_basic_scan_concept.html',
    'sections/03_05_reduce_simul.html',
    'sections/04_01_fullscan_intro.html',
    'sections/04_02_ff_structures.html',
    'sections/04_03_residue5.html',
    'sections/04_04_virtual_tester.html',
    'sections/05_01_multiple_scan_intro.html',
    'sections/05_02_adding_machine.html',
    'sections/05_02_shadow_register.html',
    'sections/05_03_partial_scan.html',
    'sections/05_03_other_scan.html',
    'sections/06_01_rtl_scan.html',
    'sections/06_02_iddq_test.html',
    'sections/07_01_summary.html'
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

window.addEventListener('resize', () => {
    if (isPresenting) {
        const activeSlide = document.querySelector('.slide-container.active');
        recalculateScale(activeSlide);
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
        if (window.MathJax) {
            MathJax.typesetPromise().catch((err) => console.log('MathJax error: ', err));
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

function togglePresentation() {
    const slides = document.querySelectorAll('.slide-container');
    isPresenting = !isPresenting;
    document.body.classList.toggle('presentation-mode', isPresenting);

    if (isPresenting) {
        document.documentElement.requestFullscreen().catch(e => { });
        updateView(); // Update DOM active states first, which triggers handleResize via timeout
        // Change icon to Stop/Compress
        const btnIcon = document.querySelector('#controls button:nth-child(2) i');
        if (btnIcon) {
            btnIcon.classList.remove('fa-play');
            btnIcon.classList.add('fa-compress'); // Or fa-stop
        }
    } else {
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
        // Sync scroll to current slide
        setTimeout(() => slides[currentSlide].scrollIntoView({ behavior: 'smooth', block: 'center' }), 100);
    }
}

// Đảm bảo đồng bộ với trạng thái phím ESC (khi trình duyệt tự động tắt Fullscreen)
document.addEventListener('fullscreenchange', () => {
    if (!document.fullscreenElement && isPresenting) {
        togglePresentation();
    }
});

// Keyboard nav
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === ' ') nextSlide();
    if (e.key === 'ArrowLeft') prevSlide();
    if (e.key === 'f' || e.key === 'F' || e.key === 'p' || e.key === 'P') togglePresentation();
    // Phím Escape đã được xử lý bởi fullscreenchange
});

// Mouse nav
document.addEventListener('click', (e) => {
    // Only trigger in presentation mode and not on buttons
    if (isPresenting && !e.target.closest('#controls')) {
        nextSlide();
    }
});

document.addEventListener('contextmenu', (e) => {
    // Right-click = go back in presentation mode
    if (isPresenting) {
        e.preventDefault();
        prevSlide();
    }
});

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
