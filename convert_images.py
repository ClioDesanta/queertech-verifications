import os
from pathlib import Path
from PIL import Image

def process_image(img_path, max_size=1600):
    try:
        with Image.open(img_path) as img:
            # Resize if needed
            if max(img.size) > max_size:
                img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
            
            # Save as webp
            webp_path = img_path.with_suffix('.webp')
            img.save(webp_path, 'WEBP', quality=85)
            return True
    except Exception as e:
        print(f"Error processing {img_path}: {e}")
        return False

# Mapping old names to new manifest names
rename_map = {
    'image 1 First step into the room.png': 'img2-a1-doorway-arrival.png',
    'image 2 The door matches the listing.png': 'img2-a2-door-opens.png',
    'image 3 Comparing listing photos to reality.png': 'img2-b1-comparing-listing.png',
    'image 4 Still on guard, mid-trip.png': 'img2-b2-vigilant-corridor.png',
    'image 5 A rating with nobody behind it.png': 'img2-b3-unverified-rating.png',
    'iamge 6 Complaints that arrive too late.png': 'img2-b4-late-complaints.png',
    'image 7 Replacing the reused Hero Background image — the manager\'s private worry.png': 'img2-b5-manager-worry.png',
    'iamge 8.png': 'img2-c1-lgbtq-checkin.png',
    'iamge 9A good hotel with no way to prove it.png': 'img2-c2-good-hotel-unproven.png',
    'image 10 The cost problem for small hotels.png': 'img2-c3-small-hotel-cost.png',
    'iamge 11 Talking to travelers (the research phase).png': 'img2-d1-research-interview.png',
    'iamge 12 Mapping the problem.png': 'img2-d2-mapping-wall.png',
    'iamge 13 The unmarked guest.png': 'img2-e1-unmarked-guest.png'
}

images2_dir = Path(r"e:\assets\images-2")
if images2_dir.exists():
    for old, new in rename_map.items():
        old_path = images2_dir / old
        new_path = images2_dir / new
        if old_path.exists():
            old_path.rename(new_path)
            print(f"Renamed {old} to {new}")

# Now convert all images in e:\assets to webp
assets_dir = Path(r"e:\assets")
for ext in ('*.png', '*.jpg', '*.jpeg'):
    for img_path in assets_dir.rglob(ext):
        print(f"Processing {img_path}")
        process_image(img_path)
