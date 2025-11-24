"""
Download High-Quality Stock Photos for Chill Pill Café
Uses Unsplash API and Placeholder services for realistic restaurant images
"""

import os
import urllib.request
from pathlib import Path

def create_image_directory():
    """Create images directory if it doesn't exist"""
    img_dir = 'static/images'
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    return img_dir

def download_image(url, filename, img_dir):
    """Download image from URL"""
    try:
        filepath = os.path.join(img_dir, filename)
        urllib.request.urlretrieve(url, filepath)
        print(f"✅ Downloaded: {filename}")
        return True
    except Exception as e:
        print(f"❌ Failed to download {filename}: {str(e)}")
        return False

def download_all_images():
    """Download all restaurant images from placeholder services"""
    img_dir = create_image_directory()
    
    print("🍽️ Downloading high-quality restaurant images...\n")
    
    # Using Picsum Photos (Lorem Picsum) - free high-quality images
    # Note: These are random beautiful images, perfect for placeholders
    
    images = {
        # Hero and Headers
        'hero_ambience.jpg': 'https://picsum.photos/1920/1080?random=1',
        'about_header.jpg': 'https://picsum.photos/1920/600?random=2',
        'menu_header.jpg': 'https://picsum.photos/1920/600?random=3',
        'reservation_header.jpg': 'https://picsum.photos/1920/600?random=4',
        'gallery_header.jpg': 'https://picsum.photos/1920/600?random=5',
        'cuisine_header.jpg': 'https://picsum.photos/1920/600?random=6',
        'whyus_header.jpg': 'https://picsum.photos/1920/600?random=7',
        'contact_header.jpg': 'https://picsum.photos/1920/600?random=8',
        'feedback_header.jpg': 'https://picsum.photos/1920/600?random=9',
        
        # Food Images - Starters
        'bruschetta.jpg': 'https://picsum.photos/600/400?random=10',
        'paneer_tikka.jpg': 'https://picsum.photos/600/400?random=11',
        'chicken_wings.jpg': 'https://picsum.photos/600/400?random=12',
        'mezze_platter.jpg': 'https://picsum.photos/600/400?random=13',
        
        # Food Images - Main Course
        'butter_chicken.jpg': 'https://picsum.photos/600/400?random=14',
        'risotto.jpg': 'https://picsum.photos/600/400?random=15',
        'seabass.jpg': 'https://picsum.photos/600/400?random=16',
        'dal_makhani.jpg': 'https://picsum.photos/600/400?random=17',
        'truffle_pasta.jpg': 'https://picsum.photos/600/400?random=18',
        
        # Food Images - Desserts
        'tiramisu.jpg': 'https://picsum.photos/600/400?random=19',
        'gulab_jamun_cheesecake.jpg': 'https://picsum.photos/600/400?random=20',
        'lava_cake.jpg': 'https://picsum.photos/600/400?random=21',
        
        # Food Images - Beverages
        'latte.jpg': 'https://picsum.photos/600/400?random=22',
        'masala_chai.jpg': 'https://picsum.photos/600/400?random=23',
        'lime_soda.jpg': 'https://picsum.photos/600/400?random=24',
        'mango_lassi.jpg': 'https://picsum.photos/600/400?random=25',
        
        # Gallery Images
        'gallery_ambience_1.jpg': 'https://picsum.photos/800/600?random=26',
        'gallery_ambience_2.jpg': 'https://picsum.photos/800/600?random=27',
        'gallery_ambience_3.jpg': 'https://picsum.photos/800/600?random=28',
        'gallery_food_1.jpg': 'https://picsum.photos/800/600?random=29',
        'gallery_food_2.jpg': 'https://picsum.photos/800/600?random=30',
        'gallery_food_3.jpg': 'https://picsum.photos/800/600?random=31',
        'gallery_interior_1.jpg': 'https://picsum.photos/800/600?random=32',
        'gallery_interior_2.jpg': 'https://picsum.photos/800/600?random=33',
        'gallery_event_1.jpg': 'https://picsum.photos/800/600?random=34',
        'gallery_event_2.jpg': 'https://picsum.photos/800/600?random=35',
        
        # About Page Images
        'founders.jpg': 'https://picsum.photos/800/600?random=36',
        'interior_elegant.jpg': 'https://picsum.photos/800/600?random=37',
        'chef_vikram.jpg': 'https://picsum.photos/600/600?random=38',
        'meera_kapoor.jpg': 'https://picsum.photos/600/600?random=39',
        'pastry_chef.jpg': 'https://picsum.photos/600/600?random=40',
        
        # Cuisine Page Images
        'cuisine_indian.jpg': 'https://picsum.photos/800/600?random=41',
        'cuisine_italian.jpg': 'https://picsum.photos/800/600?random=42',
        'cuisine_continental.jpg': 'https://picsum.photos/800/600?random=43',
        'cuisine_fusion.jpg': 'https://picsum.photos/800/600?random=44',
        'chef_at_work.jpg': 'https://picsum.photos/800/600?random=45',
        
        # Why Us Page
        'brand_identity.jpg': 'https://picsum.photos/800/600?random=46',
        
        # Instagram Feed
        'insta_1.jpg': 'https://picsum.photos/500/500?random=47',
        'insta_2.jpg': 'https://picsum.photos/500/500?random=48',
        'insta_3.jpg': 'https://picsum.photos/500/500?random=49',
        'insta_4.jpg': 'https://picsum.photos/500/500?random=50',
        'insta_5.jpg': 'https://picsum.photos/500/500?random=51',
        'insta_6.jpg': 'https://picsum.photos/500/500?random=52',
    }
    
    success_count = 0
    total = len(images)
    
    for filename, url in images.items():
        if download_image(url, filename, img_dir):
            success_count += 1
    
    print(f"\n{'='*50}")
    print(f"✅ Successfully downloaded {success_count}/{total} images")
    print(f"📁 Images saved in: {img_dir}")
    print(f"{'='*50}\n")
    
    print("🎉 All images downloaded!")
    print("🔄 Refresh your browser to see the new images")
    print("\n💡 TIP: For production, replace these with actual restaurant photos!")

if __name__ == "__main__":
    download_all_images()
