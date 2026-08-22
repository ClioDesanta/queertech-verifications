import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Task 1 replacement
target1 = '''    <!-- ═══════════════════════════════════════════════ -->
    <!-- SCENE 2.5: CONSUMER-HOTEL RELATIONSHIP         -->
    <!-- ═══════════════════════════════════════════════ -->
    <section id="scene-relationship" class="scene scene--relationship">
        <div class="scene__inner">
            <div class="dossier-box reveal-up">
                <h2 class="playfair">The broken contract between travelers and the places they trust.</h2>
                <p class="inter">On one side, the guest — paying for safety they cannot verify. On the other, the industry — selling trust it cannot prove. The gap between the two is where every story above lives.</p>
            </div>
            <div class="rel-grid">
                <div class="rel-col rel-col--consumer reveal-up">
                    <h3 class="space-mono rel-label">THE CONSUMER</h3>
                    <div class="rel-img-wrap"><img src="./all images/problems of the world/detective mindset consumer img1.webp" alt="Consumer in detective mode" loading="lazy"></div>
                    <div class="rel-img-wrap"><img src="./all images/problems of the world/consumer feeling annoyed img2.webp" alt="Consumer frustrated" loading="lazy"></div>
                </div>
                <div class="rel-line-container">
                    <svg class="rel-line" viewBox="0 0 4 200" preserveAspectRatio="none">
                        <line x1="2" y1="0" x2="2" y2="200" stroke="#C9A961" stroke-width="1" stroke-dasharray="4 4"/>
                    </svg>
                </div>
                <div class="rel-col rel-col--hotel reveal-up">
                    <h3 class="space-mono rel-label">THE INDUSTRY</h3>
                    <div class="rel-img-wrap"><img src="./all images/problems of the world/hotel loosing trust due to failed systems img3.webp" alt="Hotels losing trust" loading="lazy"></div>
                    <div class="rel-img-wrap"><img src="./all images/Hero Background.webp" alt="The hotel industry" loading="lazy"></div>
                </div>
            </div>
        </div>
    </section>'''

replacement1 = '''    <!-- ═══════════════════════════════════════════════ -->
    <!-- SCENE 2.5: BEFORE THE FEAR & BROKEN CONTRACT    -->
    <!-- ═══════════════════════════════════════════════ -->
    <section id="scene-contract" class="scene scene--contract">
        <div class="scene__inner">
            
            <!-- BEFORE THE FEAR LEAD-IN -->
            <div class="lead-in">
                <span class="space-mono eyebrow">BEFORE THE FEAR</span>
                <h2 class="fraunces intro-line">Travel, at its best, asks for nothing back.</h2>
                <p class="inter body-regular">A door that opens exactly the way it was described. A city that feels like it was waiting for you. The whole point of leaving home is trusting the room you're walking into — so much that you stop thinking about it at all.</p>
                <div class="lead-in-images" style="display: flex; gap: 1rem; margin-top: 2rem;">
                    <div class="frame frame--wide" style="flex:1;"><img src="./images-2/img2-a1-doorway-arrival.webp" alt="First step into room" loading="lazy"></div>
                    <div class="frame frame--wide" style="flex:1;"><img src="./images-2/img2-a2-door-opens.webp" alt="Door opens" loading="lazy"></div>
                </div>
            </div>

            <!-- THE BROKEN CONTRACT -->
            <div class="contract-content" style="margin-top: 6rem;">
                <h2 class="fraunces intro-line">The broken contract.</h2>
                
                <div class="dossier-grid" style="display: grid; grid-template-columns: 1fr 20px 1fr; gap: 2rem; position: relative;">
                    <!-- COLUMN 1: THE CONSUMER -->
                    <div class="dossier-col" style="display: flex; flex-direction: column; gap: 2rem;">
                        <span class="space-mono col-title">THE CONSUMER</span>
                        <div class="dossier-box interactive-caption">
                            <div class="frame"><img src="./all images/problems of the world/detective mindset consumer img1.webp" alt="Detective mindset" loading="lazy"></div>
                            <div class="hover-caption" style="margin-top:0.5rem; opacity:0.8;"><p class="inter">Checking the room herself, because no one else will.</p></div>
                        </div>
                        <div class="dossier-box interactive-caption">
                            <div class="frame"><img src="./all images/problems of the world/consumer feeling annoyed img2.webp" alt="Annoyed consumer" loading="lazy"></div>
                            <div class="hover-caption" style="margin-top:0.5rem; opacity:0.8;"><p class="inter">Double-checking a five-star listing that shouldn't need double-checking.</p></div>
                        </div>
                        <div class="dossier-box interactive-caption">
                            <div class="frame"><img src="./images-2/img2-b1-comparing-listing.webp" alt="Comparing listing" loading="lazy"></div>
                            <div class="hover-caption" style="margin-top:0.5rem; opacity:0.8;"><p class="inter">Choosing a hotel by what she can verify herself, not what the listing claims.</p></div>
                        </div>
                        <div class="dossier-box interactive-caption">
                            <div class="frame"><img src="./images-2/img2-b2-vigilant-corridor.webp" alt="Alert mid-trip" loading="lazy"></div>
                            <div class="hover-caption" style="margin-top:0.5rem; opacity:0.8;"><p class="inter">Staying alert on a trip that was supposed to be a break from being alert.</p></div>
                        </div>
                    </div>

                    <!-- CONNECTOR LINE -->
                    <div class="dossier-connector" style="position:relative;">
                        <svg class="connector-line" viewBox="0 0 20 800" preserveAspectRatio="none" style="width: 100%; height: 100%;">
                            <path class="draw-line" d="M10,0 L10,800" stroke="var(--brass)" stroke-width="2" fill="none" stroke-dasharray="10 10"/>
                        </svg>
                    </div>

                    <!-- COLUMN 2: THE INDUSTRY -->
                    <div class="dossier-col" style="display: flex; flex-direction: column; gap: 2rem;">
                        <span class="space-mono col-title">THE INDUSTRY</span>
                        <div class="dossier-box interactive-caption">
                            <div class="frame"><img src="./all images/problems of the world/hotel loosing trust due to failed systems img3.webp" alt="Failed systems" loading="lazy"></div>
                            <div class="hover-caption" style="margin-top:0.5rem; opacity:0.8;"><p class="inter">A badge that no longer means what it says.</p></div>
                        </div>
                        <div class="dossier-box interactive-caption">
                            <div class="frame"><img src="./images-2/img2-b5-manager-worry.webp" alt="Manager worrying" loading="lazy"></div>
                            <div class="hover-caption" style="margin-top:0.5rem; opacity:0.8;"><p class="inter">A system built to list rooms, not to check them.</p></div>
                        </div>
                        <div class="dossier-box interactive-caption">
                            <div class="frame"><img src="./images-2/img2-b3-unverified-rating.webp" alt="Unverified rating" loading="lazy"></div>
                            <div class="hover-caption" style="margin-top:0.5rem; opacity:0.8;"><p class="inter">A five-star rating with no one behind it who's actually walked the property.</p></div>
                        </div>
                        <div class="dossier-box interactive-caption">
                            <div class="frame"><img src="./images-2/img2-b4-late-complaints.webp" alt="Late complaints" loading="lazy"></div>
                            <div class="hover-caption" style="margin-top:0.5rem; opacity:0.8;"><p class="inter">A complaint that arrives after the stay, not before it.</p></div>
                        </div>
                    </div>
                </div>

                <p class="inter body-regular contract-outro" style="margin-top: 4rem;">On one side, the guest — paying for safety they cannot verify. On the other, the industry — selling trust it cannot prove. The gap between the two is where every story above lives.</p>
            </div>
        </div>
    </section>'''
html = html.replace(target1, replacement1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
