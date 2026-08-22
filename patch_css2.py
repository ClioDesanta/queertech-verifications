import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace interactive-caption block
old_interactive = '''/* ═══════════════════════════════════════════ */
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
}'''

new_interactive = '''/* ═══════════════════════════════════════════ */
/* STATIC CAPTIONS (ALWAYS VISIBLE)            */
/* ═══════════════════════════════════════════ */
.interactive-caption {
    position: relative;
    border-radius: 4px;
    margin-bottom: 2.5rem;
}
.interactive-caption .hover-caption {
    background: transparent;
    padding: 1rem 0;
}
.interactive-caption .hover-caption p {
    margin: 0;
    color: var(--bone);
    font-size: 0.95rem;
    line-height: 1.5;
    opacity: 0.9;
}'''

css = css.replace(old_interactive, new_interactive)

# In case it was already replaced or missing, we can just append it or make sure it's correct.
if new_interactive not in css:
    print("Warning: CSS replacement didn't match. Adding at end.")
    css += "\\n" + new_interactive

# Also fix connector-line
old_connector = '''.draw-line {
    stroke-dasharray: 2000;
    stroke-dashoffset: 2000;
}'''
new_connector = '''.draw-line {
    stroke-dasharray: 2000;
    stroke-dashoffset: 0; /* Fully visible */
}'''
css = css.replace(old_connector, new_connector)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
