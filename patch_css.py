import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

addition = '''

/* ═══════════════════════════════════════════ */
/* 4+4 GRID INTERACTIVE CAPTIONS               */
/* ═══════════════════════════════════════════ */
.interactive-caption {
    position: relative;
    overflow: hidden;
    cursor: pointer;
    border-radius: 4px;
}
.interactive-caption .hover-caption {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    background: rgba(11, 11, 13, 0.95);
    padding: 1.5rem 1rem;
    transform: translateY(100%);
    transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.4s ease;
    opacity: 0;
    border-top: 2px solid var(--verified-brass);
    margin: 0 !important;
}
.interactive-caption:hover .hover-caption,
.interactive-caption:focus-within .hover-caption,
.interactive-caption.active .hover-caption {
    transform: translateY(0);
    opacity: 1;
}

/* ═══════════════════════════════════════════ */
/* CONNECTOR LINE                              */
/* ═══════════════════════════════════════════ */
.draw-line {
    stroke-dasharray: 2000;
    stroke-dashoffset: 2000;
}
'''

css += addition

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
