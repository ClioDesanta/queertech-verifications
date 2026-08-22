import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Task 3 replacement
target3 = '''            <div class="dossier-box reveal-up">
                <h2 class="playfair">The restaurant industry solved a version of this a century ago.</h2>
                <p class="inter">Michelin inspectors visit anonymously. No restaurant can buy a star, and none can self-report one. The QueerTech Verifications borrows that discipline and points it at human safety.</p>
            </div>'''

replacement3 = '''            <div class="dossier-box reveal-up">
                <h2 class="playfair">The restaurant industry solved a version of this a century ago.</h2>
                <p class="inter">Michelin inspectors visit anonymously. No restaurant can buy a star, and none can self-report one. The QueerTech Verifications borrows that discipline and points it at human safety.</p>
            </div>
            
            <div class="dossier-box reveal-up" style="margin-top: 3rem; max-width: 800px; margin-left: auto; margin-right: auto; text-align: left;">
                <h3 class="fraunces">Why anonymity is the whole mechanism.</h3>
                <p class="inter body-regular" style="margin-top: 1rem;">A Michelin star works because the restaurant never knows which table is the inspector's. There's no version of the meal to perform for a judge and a different version for everyone else — so the only way to earn the star is to be that good, every night, for every table.</p>
                <div class="frame frame--wide" style="margin: 2rem 0;"><img src="./images-2/img2-e1-unmarked-guest.webp" alt="The unmarked guest" loading="lazy"></div>
                <p class="inter body-regular" style="margin-top: 1rem;">Self-reported badges fail for the opposite reason: the property knows exactly when it's being graded, because it's the one filling out the form. The QueerTech Verifications borrows the one design decision that makes Michelin's system hard to game — the property doesn't know when the visit is happening, and doesn't get to choose who shows up.</p>
                <p class="inter body-regular" style="margin-top: 1rem;">And accountability doesn't end at the visit. A Michelin star can be pulled the following year if standards slip. QueerTech's certification is time-stamped, geo-tagged, and re-audited on a fixed six-month cycle — verified isn't a badge earned once and kept forever. It's a standard that has to keep being met.</p>
            </div>'''
html = html.replace(target3, replacement3)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
