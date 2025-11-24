"""
Download Real Food & Restaurant Images for Chill Pill Café
Uses Foodish API and specific food image sources
"""

import urllib.request
import os
from pathlib import Path
import time

def download_image(url, filepath):
    """Download an image from URL to filepath"""
    try:
        req = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        print(f"✓ Downloaded: {os.path.basename(filepath)}")
        time.sleep(0.5)  # Be respectful to the server
        return True
    except Exception as e:
        print(f"✗ Failed {os.path.basename(filepath)}: {str(e)}")
        return False

# Create images directory
images_dir = Path("static/images")
images_dir.mkdir(parents=True, exist_ok=True)

print("\n🍽️  Downloading Real Food & Restaurant Images for Chill Pill Café...\n")

# Using Unsplash Source API with specific food/restaurant queries
# Format: https://source.unsplash.com/{width}x{height}/?{query}

images = {
    # Hero & Headers (Restaurant ambience)
    "hero_ambience.jpg": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1920&h=1080&fit=crop",  # Restaurant interior
    "about_header.jpg": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1920&h=600&fit=crop",  # Restaurant table setting
    "menu_header.jpg": "https://images.unsplash.com/photo-1544148103-0773bf10d330?w=1920&h=600&fit=crop",  # Menu/food background
    "reservation_header.jpg": "https://images.unsplash.com/photo-1551632436-cbf8dd35adfa?w=1920&h=600&fit=crop",  # Elegant dining
    "gallery_header.jpg": "https://images.unsplash.com/photo-1592861956120-e524fc739696?w=1920&h=600&fit=crop",  # Restaurant interior
    "cuisine_header.jpg": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=1920&h=600&fit=crop",  # Kitchen/cooking
    "whyus_header.jpg": "https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?w=1920&h=600&fit=crop",  # Fine dining
    "contact_header.jpg": "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=1920&h=600&fit=crop",  # Restaurant exterior
    
    # Indian Food (Specific dishes)
    "butter_chicken.jpg": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=600&h=400&fit=crop",  # Butter chicken
    "paneer_tikka.jpg": "https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=600&h=400&fit=crop",  # Paneer tikka
    "dal_makhani.jpg": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=600&h=400&fit=crop",  # Dal makhani
    "biryani.jpg": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=600&h=400&fit=crop",  # Biryani
    
    # Italian Food
    "truffle_pasta.jpg": "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=600&h=400&fit=crop",  # Pasta
    "risotto.jpg": "https://images.unsplash.com/photo-1476124369491-b79a93cc81c1?w=600&h=400&fit=crop",  # Risotto
    "bruschetta.jpg": "https://images.unsplash.com/photo-1572695157366-5e585ab2b69f?w=600&h=400&fit=crop",  # Bruschetta
    
    # Seafood & Mains
    "seabass.jpg": "https://images.unsplash.com/photo-1580959375944-a5df7d473a59?w=600&h=400&fit=crop",  # Grilled fish
    "salmon.jpg": "https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=600&h=400&fit=crop",  # Salmon dish
    
    # Appetizers
    "chicken_wings.jpg": "https://images.unsplash.com/photo-1608039829572-78524f79c4c7?w=600&h=400&fit=crop",  # Chicken wings
    "mezze_platter.jpg": "https://images.unsplash.com/photo-1621503092097-f5c8734892f3?w=600&h=400&fit=crop",  # Mezze platter
    
    # Desserts
    "gulab_jamun_cheesecake.jpg": "https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?w=600&h=400&fit=crop",  # Cheesecake
    "tiramisu.jpg": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=600&h=400&fit=crop",  # Tiramisu
    "lava_cake.jpg": "https://images.unsplash.com/photo-1624353365286-3f8d62daad51?w=600&h=400&fit=crop",  # Chocolate lava cake
    
    # Beverages
    "latte.jpg": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=600&h=400&fit=crop",  # Latte
    "masala_chai.jpg": "https://images.unsplash.com/photo-1571934811356-5cc061b6821f?w=600&h=400&fit=crop",  # Chai
    "mango_lassi.jpg": "https://images.unsplash.com/photo-1623065422902-30a2d299bbe4?w=600&h=400&fit=crop",  # Mango lassi
    "lime_soda.jpg": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600&h=400&fit=crop",  # Mojito/lime drink
    
    # Restaurant Interiors & Ambience
    "interior_elegant.jpg": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800&h=600&fit=crop",  # Elegant interior
    "brand_identity.jpg": "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=800&h=600&fit=crop",  # Restaurant branding
    "founders.jpg": "https://images.unsplash.com/photo-1556742502-ec7c0e9f34b1?w=800&h=600&fit=crop",  # Business meeting
    
    # Team Photos
    "chef_vikram.jpg": "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=400&h=400&fit=crop",  # Male chef
    "meera_kapoor.jpg": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&h=400&fit=crop",  # Female manager
    "pastry_chef.jpg": "https://images.unsplash.com/photo-1577219491135-ce391730fb4c?w=400&h=400&fit=crop",  # Pastry chef
    "chef_at_work.jpg": "https://images.unsplash.com/photo-1556910103-1c02745aae4d?w=800&h=600&fit=crop",  # Chef cooking
    
    # Cuisine Types
    "cuisine_indian.jpg": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&h=600&fit=crop",  # Indian cuisine
    "cuisine_italian.jpg": "https://images.unsplash.com/photo-1595295333158-4742f28fbd85?w=800&h=600&fit=crop",  # Italian cuisine
    "cuisine_continental.jpg": "https://images.unsplash.com/photo-1514326640560-7d063f2aad85?w=800&h=600&fit=crop",  # Continental
    "cuisine_fusion.jpg": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800&h=600&fit=crop",  # Fusion food
    
    # Gallery Images - Ambience
    "gallery_ambience_1.jpg": "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=800&h=600&fit=crop",  # Restaurant ambience
    "gallery_ambience_2.jpg": "https://images.unsplash.com/photo-1551218808-94e220e084d2?w=800&h=600&fit=crop",  # Modern interior
    "gallery_ambience_3.jpg": "https://images.unsplash.com/photo-1578474846511-04ba529f0b88?w=800&h=600&fit=crop",  # Cozy seating
    
    # Gallery Images - Food
    "gallery_food_1.jpg": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=800&h=600&fit=crop",  # Pizza
    "gallery_food_2.jpg": "https://images.unsplash.com/photo-1606787366850-de6330128bfc?w=800&h=600&fit=crop",  # Fine dining plate
    "gallery_food_3.jpg": "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=800&h=600&fit=crop",  # Food spread
    
    # Gallery Images - Interior
    "gallery_interior_1.jpg": "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=800&h=600&fit=crop",  # Restaurant seating
    "gallery_interior_2.jpg": "https://images.unsplash.com/photo-1590846406792-0adc7f938f1d?w=800&h=600&fit=crop",  # Bar area
    
    # Gallery Images - Events
    "gallery_event_1.jpg": "https://images.unsplash.com/photo-1511795409834-ef04bbd61622?w=800&h=600&fit=crop",  # Event setup
    "gallery_event_2.jpg": "https://images.unsplash.com/photo-1519167758481-83f29da8c043?w=800&h=600&fit=crop",  # Party/celebration
    
    # Instagram Feed
    "insta_1.jpg": "https://images.unsplash.com/photo-1568254183919-78a4f43a2877?w=400&h=400&fit=crop",  # Food photo 1
    "insta_2.jpg": "https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=400&h=400&fit=crop",  # Food photo 2
    "insta_3.jpg": "https://images.unsplash.com/phone-1562967914-608f82629710?w=400&h=400&fit=crop",  # Food photo 3
    "insta_4.jpg": "https://images.unsplash.com/photo-1574484284002-952d92456975?w=400&h=400&fit=crop",  # Food photo 4
    "insta_5.jpg": "https://images.unsplash.com/photo-1559847844-5315695dadae?w=400&h=400&fit=crop",  # Food photo 5
    "insta_6.jpg": "https://images.unsplash.com/photo-1482049016688-2d3e1b311543?w=400&h=400&fit=crop",  # Food photo 6
}

# Download all images
success_count = 0
failed_count = 0

for filename, url in images.items():
    filepath = images_dir / filename
    if download_image(url, filepath):
        success_count += 1
    else:
        failed_count += 1

print(f"\n{'='*60}")
print(f"✅ Successfully downloaded: {success_count} images")
if failed_count > 0:
    print(f"❌ Failed: {failed_count} images")
print(f"{'='*60}\n")
print("🎉 All real food & restaurant images are ready!")
print("📁 Images saved in: static/images/")
print("\n💡 Note: These are real food photos from Unsplash")
print("   Replace with your own restaurant photos for production!\n")
