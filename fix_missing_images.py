"""Fix failed images with alternative URLs"""
import urllib.request
import os
from pathlib import Path
import time

def download_image(url, filepath):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        print(f"✓ Downloaded: {os.path.basename(filepath)}")
        time.sleep(0.5)
        return True
    except Exception as e:
        print(f"✗ Failed {os.path.basename(filepath)}: {str(e)}")
        return False

images_dir = Path("static/images")

# Alternative URLs for failed images
failed_images = {
    "risotto.jpg": "https://images.unsplash.com/photo-1633964913295-ceb43826ab19?w=600&h=400&fit=crop",
    "seabass.jpg": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=600&h=400&fit=crop",
    "mezze_platter.jpg": "https://images.unsplash.com/photo-1599020792689-9fde458e7e17?w=600&h=400&fit=crop",
    "pastry_chef.jpg": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400&h=400&fit=crop",
    "cuisine_continental.jpg": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?w=800&h=600&fit=crop",
    "gallery_event_2.jpg": "https://images.unsplash.com/photo-1464366400600-7168b8af9bc3?w=800&h=600&fit=crop",
    "insta_3.jpg": "https://images.unsplash.com/photo-1547592180-85f173990554?w=400&h=400&fit=crop",
}

print("\n🔄 Downloading missing images...\n")

for filename, url in failed_images.items():
    filepath = images_dir / filename
    download_image(url, filepath)

print("\n✅ All missing images downloaded!")
