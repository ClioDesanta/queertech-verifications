import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add links to the globe section
target_globe = '''<p class="inter" style="margin-top: 1rem; opacity: 0.7;"><strong>Click the glowing nodes on the globe to reveal the impact.</strong></p>
            </div>'''
replacement_globe = '''<p class="inter" style="margin-top: 1rem; opacity: 0.7;"><strong>Click the glowing nodes on the globe to reveal the impact.</strong></p>
                <div class="sources-links" style="margin-top: 1.5rem; display: flex; flex-direction: column; gap: 0.5rem; font-size: 0.75rem;">
                    <a href="https://www.cnn.com/2024/07/09/business/airbnb-hidden-camera-invs/index.html" target="_blank" class="space-mono" style="color: var(--verified-brass); text-decoration: none;">Further Reading (Hidden Cameras) &rarr;</a>
                    <a href="https://www.nbcnews.com/nbc-out/out-news/gay-couple-alleges-sheraton-wedding-venue-mexico-discriminated-rcna201399" target="_blank" class="space-mono" style="color: var(--verified-brass); text-decoration: none;">Further Reading (LGBTQ+ Discrimination) &rarr;</a>
                    <a href="https://www.lgbtqnation.com/2025/04/trans-woman-allegedly-turned-away-from-hotel-because-people-like-you-cant-stay-here/" target="_blank" class="space-mono" style="color: var(--verified-brass); text-decoration: none;">Further Reading (Denial of Service) &rarr;</a>
                </div>
            </div>'''

# 2. Add link to the Michelin accountability section
target_michelin = '''<p class="inter body-regular" style="margin-top: 1rem;">And accountability doesn't end at the visit. A Michelin star can be pulled the following year if standards slip. QueerTech's certification is time-stamped, geo-tagged, and re-audited on a fixed six-month cycle — verified isn't a badge earned once and kept forever. It's a standard that has to keep being met.</p>
            </div>'''
replacement_michelin = '''<p class="inter body-regular" style="margin-top: 1rem;">And accountability doesn't end at the visit. A Michelin star can be pulled the following year if standards slip. QueerTech's certification is time-stamped, geo-tagged, and re-audited on a fixed six-month cycle — verified isn't a badge earned once and kept forever. It's a standard that has to keep being met.</p>
                <div class="sources-links" style="margin-top: 1.5rem; font-size: 0.75rem;">
                    <a href="https://www.cbsnews.com/boston/news/women-boston-liberty-hotel-bathroom-gender" target="_blank" class="space-mono" style="color: var(--verified-brass); text-decoration: none;">Further Reading (Why after-the-fact accountability isn't enough) &rarr;</a>
                </div>
            </div>'''

html = html.replace(target_globe, replacement_globe)
html = html.replace(target_michelin, replacement_michelin)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
