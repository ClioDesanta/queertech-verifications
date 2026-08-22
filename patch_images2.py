import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add images 11 & 12 under WHY THIS PROCESS EXISTS
target_d = '''<p class="inter body-regular" style="margin-top: 1rem;">We didn't design a checklist by guessing what travelers worry about. We built it by asking them — and by walking the same hotels they had. What we found wasn't one bad actor. It was a structural gap: every existing system checks a hotel once, or never, or only after someone's already been hurt. So the process below isn't a formality. Every step exists because a specific failure, from a specific traveler's story, showed us it had to.</p>
            </div>'''
replacement_d = '''<p class="inter body-regular" style="margin-top: 1rem;">We didn't design a checklist by guessing what travelers worry about. We built it by asking them — and by walking the same hotels they had. What we found wasn't one bad actor. It was a structural gap: every existing system checks a hotel once, or never, or only after someone's already been hurt. So the process below isn't a formality. Every step exists because a specific failure, from a specific traveler's story, showed us it had to.</p>
                <div class="lead-in-images" style="display: flex; gap: 1rem; margin-top: 2rem;">
                    <div class="frame frame--wide" style="flex:1;"><img src="./images-2/img2-d1-research-interview.webp" alt="Researchers interviewing traveler" loading="lazy"></div>
                    <div class="frame frame--wide" style="flex:1;"><img src="./images-2/img2-d2-mapping-wall.webp" alt="Mapping wall" loading="lazy"></div>
                </div>
            </div>'''
html = html.replace(target_d, replacement_d)

# 2. Add images 8, 9, 10 to Scene 4 (What Exists Today)
target_c = '''<p class="inter">A certificate on a wall. A video module clicked through by a bored manager. The system checks the box, but the guest still walks into an unverified room.</p>
                    </div>
                </div>
            </div>

            <div class="dossier-box reveal-up transition-box">'''
replacement_c = '''<p class="inter">A certificate on a wall. A video module clicked through by a bored manager. The system checks the box, but the guest still walks into an unverified room.</p>
                    </div>
                </div>
            </div>
            
            <div class="lead-in-images reveal-up" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 4rem;">
                <div class="frame frame--wide"><img src="./images-2/img2-c1-lgbtq-checkin.webp" alt="LGBTQ+ couple checking in, reading the room" loading="lazy"></div>
                <div class="frame frame--wide"><img src="./images-2/img2-c2-good-hotel-unproven.webp" alt="Good hotel with no way to prove it" loading="lazy"></div>
                <div class="frame frame--wide"><img src="./images-2/img2-c3-small-hotel-cost.webp" alt="Small hotel owner at desk" loading="lazy"></div>
            </div>

            <div class="dossier-box reveal-up transition-box" style="margin-top: 4rem;">'''
html = html.replace(target_c, replacement_c)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
