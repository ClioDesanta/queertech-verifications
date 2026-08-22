import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

addition = '''

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
'''

js += addition

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
