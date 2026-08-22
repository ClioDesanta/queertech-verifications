/* ══════════════════════════════════════════════════════════════ */
/* THE QUEERTECH VERIFICATIONS v3 — Animation Orchestration      */
/* GSAP + ScrollTrigger                                          */
/* ══════════════════════════════════════════════════════════════ */

gsap.registerPlugin(ScrollTrigger);

/* ─── 0. SCROLL LOCK ─────────────────────────────────────────── */

function preventScroll(e) { e.preventDefault(); }
function lockScroll() {
    document.body.classList.add('scroll-locked');
    window.addEventListener('wheel', preventScroll, { passive: false });
    window.addEventListener('touchmove', preventScroll, { passive: false });
}
function unlockScroll() {
    document.body.classList.remove('scroll-locked');
    window.removeEventListener('wheel', preventScroll);
    window.removeEventListener('touchmove', preventScroll);
}

// Lock on load
lockScroll();

/* ─── 1. ENTRY DOOR ─────────────────────────────────────────── */

const entryOverlay = document.querySelector('.scene-entry-overlay');
const doorLine = document.querySelector('.door-line');
const doorLeft = document.querySelector('.door-panel--left');
const doorRight = document.querySelector('.door-panel--right');
const entryText = document.querySelector('.entry-text');
const heroVideo = document.querySelector('.hero-bg-video');
const enterBtn = document.getElementById('enter-btn');
let doorOpened = false;

function openDoor() {
    if (doorOpened) return;
    doorOpened = true;

    const tl = gsap.timeline({
        onComplete: () => {
            unlockScroll();
            entryOverlay.classList.add('hidden');
            ScrollTrigger.refresh();
        }
    });

    // Fade out text and button
    tl.to(entryText, {
        opacity: 0,
        y: -30,
        duration: 0.5,
        ease: 'power2.in'
    })
    // Open door
    .to(doorLine, {
        scaleX: 8,
        opacity: 0,
        duration: 0.6,
        ease: 'power2.inOut'
    })
    .to(doorLeft, {
        xPercent: -100,
        duration: 1.4,
        ease: 'power4.inOut'
    }, '-=0.3')
    .to(doorRight, {
        xPercent: 100,
        duration: 1.4,
        ease: 'power4.inOut'
    }, '<');

    if (heroVideo) heroVideo.play().catch(() => {});
}

// Open door on button click
if (enterBtn) {
    enterBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        openDoor();
    });
}

/* ─── 2. BACKGROUND COLOR INTERPOLATION ─────────────────────── */

ScrollTrigger.create({
    trigger: document.body,
    start: 'top top',
    end: 'bottom bottom',
    scrub: 0.5,
    onUpdate: (self) => {
        const p = self.progress;
        let bg, headingColor, bodyColor, surface;

        if (p <= 0.25) {
            const t = p / 0.25;
            bg = gsap.utils.interpolate('#0A0A0C', '#3D3D45', t);
            headingColor = '#F5F1E8';
            bodyColor = '#E0DCD5';
            surface = gsap.utils.interpolate('#1A1714', '#2A2722', t);
        } else if (p <= 0.6) {
            const t = (p - 0.25) / 0.35;
            bg = gsap.utils.interpolate('#3D3D45', '#F0EAD6', t);
            headingColor = gsap.utils.interpolate('#F5F1E8', '#1A1A1E', t);
            bodyColor = gsap.utils.interpolate('#E0DCD5', '#3A362F', t);
            surface = gsap.utils.interpolate('#2A2722', '#E4DCC8', t);
        } else {
            bg = '#F0EAD6';
            headingColor = '#1A1A1E';
            bodyColor = '#3A362F';
            surface = '#E4DCC8';
        }

        const root = document.documentElement.style;
        root.setProperty('--bg', bg);
        root.setProperty('--text-heading', headingColor);
        root.setProperty('--text-body', bodyColor);
        root.setProperty('--surface', surface);
        document.body.style.backgroundColor = bg;
        document.body.style.color = bodyColor;
    }
});

/* ─── 3. STORY MODE ─────────────────────────────────────────── */

let activeStory = 'meera';
let activePanel = 0;
const storyTabs = document.querySelectorAll('.story-tab');
const storyTracks = document.querySelectorAll('.story-track');
const counterCurrent = document.querySelector('.counter-current');
const counterTotal = document.querySelector('.counter-total');
const storyCaptions = document.querySelectorAll('.story-caption-box');
const storyPrev = document.querySelector('.story-nav--prev');
const storyNext = document.querySelector('.story-nav--next');

function getActiveTrack() {
    return document.querySelector(`.story-track[data-track="${activeStory}"]`);
}

function getStoryTotal() {
    const track = getActiveTrack();
    return track ? track.querySelectorAll('.story-slide').length : 0;
}

function updateStory() {
    storyTracks.forEach(t => t.classList.toggle('active', t.dataset.track === activeStory));
    const track = getActiveTrack();
    if (track) track.style.transform = `translateX(-${activePanel * 100}%)`;

    const total = getStoryTotal();
    if (counterCurrent) counterCurrent.textContent = activePanel + 1;
    if (counterTotal) counterTotal.textContent = total;

    storyCaptions.forEach(c => c.classList.toggle('active', c.dataset.caption === activeStory));
    storyTabs.forEach(t => t.classList.toggle('active', t.dataset.story === activeStory));

    if (storyPrev) storyPrev.style.opacity = activePanel === 0 ? '0.15' : '0.5';
    if (storyNext) storyNext.style.opacity = activePanel >= total - 1 ? '0.15' : '0.5';
}

storyTabs.forEach(tab => {
    tab.addEventListener('click', () => {
        activeStory = tab.dataset.story;
        activePanel = 0;
        updateStory();
    });
});

if (storyPrev) storyPrev.addEventListener('click', () => {
    if (activePanel > 0) { activePanel--; updateStory(); }
});
if (storyNext) storyNext.addEventListener('click', () => {
    if (activePanel < getStoryTotal() - 1) { activePanel++; updateStory(); }
});

document.addEventListener('keydown', (e) => {
    const storiesSection = document.getElementById('scene-stories');
    const rect = storiesSection ? storiesSection.getBoundingClientRect() : null;
    if (rect && rect.top < window.innerHeight && rect.bottom > 0) {
        if (e.key === 'ArrowLeft' && activePanel > 0) { activePanel--; updateStory(); }
        if (e.key === 'ArrowRight' && activePanel < getStoryTotal() - 1) { activePanel++; updateStory(); }
    }
});

updateStory();

/* ─── 4. SCALE CARDS — Interactive Globe ─────────────────────────── */

const globeNodes = document.querySelectorAll('.globe-node');
const scaleCards = document.querySelectorAll('.scale-card');

globeNodes.forEach(node => {
    node.addEventListener('click', (e) => {
        e.stopPropagation();
        const index = node.dataset.card;
        
        // Hide all cards
        scaleCards.forEach(card => card.classList.remove('active'));
        globeNodes.forEach(n => n.classList.remove('active'));
        
        // Show specific card
        node.classList.add('active');
        const targetCard = document.querySelector(`.scale-card[data-index="${index}"]`);
        if (targetCard) targetCard.classList.add('active');
    });
});

// Click anywhere else to close card
document.addEventListener('click', (e) => {
    if (!e.target.closest('.scale-card')) {
        scaleCards.forEach(card => card.classList.remove('active'));
        globeNodes.forEach(n => n.classList.remove('active'));
    }
});

/* ─── 5. SOLUTION CAROUSEL — Click Navigation ────────────────── */

const carouselTrack = document.querySelector('.carousel-track');
const carouselSlides = document.querySelectorAll('.carousel-slide');
const carPrev = document.querySelector('.carousel-nav--prev');
const carNext = document.querySelector('.carousel-nav--next');
const carCurrent = document.querySelector('.carousel-current');
const carTotal = document.querySelector('.carousel-total');
let carIndex = 0;

function updateCarousel() {
    if (!carouselTrack) return;
    const total = carouselSlides.length;
    carouselTrack.style.transform = `translateX(-${carIndex * 100}%)`;
    if (carCurrent) carCurrent.textContent = carIndex + 1;
    if (carTotal) carTotal.textContent = total;
    if (carPrev) carPrev.style.opacity = carIndex === 0 ? '0.15' : '0.5';
    if (carNext) carNext.style.opacity = carIndex >= total - 1 ? '0.15' : '0.5';
}

if (carPrev) carPrev.addEventListener('click', () => {
    if (carIndex > 0) { carIndex--; updateCarousel(); }
});
if (carNext) carNext.addEventListener('click', () => {
    if (carIndex < carouselSlides.length - 1) { carIndex++; updateCarousel(); }
});

updateCarousel();

/* ─── 6. SCROLL REVEALS ──────────────────────────────────────── */

gsap.utils.toArray('.reveal-up').forEach(el => {
    gsap.to(el, {
        opacity: 1,
        y: 0,
        duration: 0.9,
        ease: 'power3.out',
        scrollTrigger: {
            trigger: el,
            start: 'top 88%',
            once: true
        }
    });
});

/* ─── 7. JOURNEY ITEMS ───────────────────────────────────────── */

gsap.utils.toArray('.journey-item').forEach((item, i) => {
    gsap.to(item, {
        opacity: 1,
        y: 0,
        duration: 0.7,
        ease: 'power2.out',
        delay: i * 0.15,
        scrollTrigger: {
            trigger: item,
            start: 'top 88%',
            once: true
        }
    });
});

/* ─── 8. VIDEO LAZY-LOAD & AUTO-PLAY / PAUSE ─────────────────── */

document.querySelectorAll('video').forEach(video => {
    const isHero = video.classList.contains('hero-bg-video');
    
    // Hero video plays immediately, others lazy-load
    if (isHero) {
        video.play().catch(() => {});
        return;
    }

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Start loading when visible
                if (video.preload === 'none') {
                    video.preload = 'auto';
                    video.load();
                }
                video.loop = true;
                video.play().catch(() => {});
            } else {
                video.pause();
            }
        });
    }, { threshold: 0.2, rootMargin: '200px' });
    observer.observe(video);
});

/* ─── 9. REFRESH ─────────────────────────────────────────────── */

window.addEventListener('load', () => {
    ScrollTrigger.refresh();
});

setTimeout(() => ScrollTrigger.refresh(), 1500);


/* Draw Connector Line */
if (document.querySelector('.draw-line')) {
    gsap.to('.draw-line', {
        strokeDashoffset: 0,
        ease: "none",
        scrollTrigger: {
            trigger: ".dossier-connector",
            start: "top 70%",
            end: "bottom 30%",
            scrub: 1
        }
    });
}
