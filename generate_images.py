"""
Image Generator for Chill Pill Café
Creates placeholder images with gradients and text for the restaurant website
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_image_directory():
    """Create images directory if it doesn't exist"""
    img_dir = 'static/images'
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    return img_dir

def create_gradient_image(width, height, color1, color2, filename, text=""):
    """Create a beautiful gradient image with optional text"""
    img_dir = create_image_directory()
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    
    # Create gradient
    for y in range(height):
        ratio = y / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        draw.rectangle([(0, y), (width, y + 1)], fill=(r, g, b))
    
    # Add text if provided
    if text:
        try:
            font = ImageFont.truetype("arial.ttf", 48)
        except:
            font = ImageFont.load_default()
        
        # Get text bbox
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Draw text with shadow
        shadow_offset = 3
        draw.text(
            ((width - text_width) // 2 + shadow_offset, (height - text_height) // 2 + shadow_offset),
            text,
            fill=(0, 0, 0, 128),
            font=font
        )
        draw.text(
            ((width - text_width) // 2, (height - text_height) // 2),
            text,
            fill=(255, 255, 255),
            font=font
        )
    
    # Save image
    filepath = os.path.join(img_dir, filename)
    image.save(filepath, 'JPEG', quality=95)
    print(f"Created: {filepath}")

def create_logo():
    """Create Chill Pill Café logo"""
    img_dir = create_image_directory()
    width, height = 200, 200
    
    # Create circular logo with gradient
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Draw circle background
    draw.ellipse([10, 10, 190, 190], fill=(44, 95, 45), outline=(212, 175, 55), width=5)
    
    # Add text
    try:
        font_large = ImageFont.truetype("arial.ttf", 40)
        font_small = ImageFont.truetype("arial.ttf", 24)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Draw "Chill Pill"
    text1 = "Chill Pill"
    bbox1 = draw.textbbox((0, 0), text1, font=font_large)
    w1 = bbox1[2] - bbox1[0]
    draw.text(((width - w1) // 2, 60), text1, fill=(255, 255, 255), font=font_large)
    
    # Draw "Café"
    text2 = "CAFÉ"
    bbox2 = draw.textbbox((0, 0), text2, font=font_small)
    w2 = bbox2[2] - bbox2[0]
    draw.text(((width - w2) // 2, 110), text2, fill=(212, 175, 55), font=font_small)
    
    filepath = os.path.join(img_dir, 'logo.png')
    image.save(filepath, 'PNG')
    print(f"Created: {filepath}")

def generate_all_images():
    """Generate all required images for the website"""
    
    # Color schemes
    green_brown = ((44, 95, 45), (139, 69, 19))
    warm_earth = ((212, 175, 55), (160, 82, 45))
    cool_green = ((30, 130, 76), (44, 95, 45))
    elegant_gray = ((52, 73, 94), (44, 62, 80))
    food_warm = ((230, 126, 34), (192, 57, 43))
    
    print("Generating images for Chill Pill Café...")
    
    # Create logo
    create_logo()
    
    # Hero and Header Images
    create_gradient_image(1920, 1080, green_brown[0], green_brown[1], 'hero_ambience.jpg', '')
    create_gradient_image(1920, 600, green_brown[0], green_brown[1], 'about_header.jpg', 'About Us')
    create_gradient_image(1920, 600, cool_green[0], cool_green[1], 'menu_header.jpg', 'Our Menu')
    create_gradient_image(1920, 600, warm_earth[0], warm_earth[1], 'reservation_header.jpg', 'Reserve')
    create_gradient_image(1920, 600, elegant_gray[0], elegant_gray[1], 'gallery_header.jpg', 'Gallery')
    create_gradient_image(1920, 600, green_brown[0], green_brown[1], 'cuisine_header.jpg', 'Cuisines')
    create_gradient_image(1920, 600, cool_green[0], cool_green[1], 'whyus_header.jpg', 'Why Us')
    create_gradient_image(1920, 600, warm_earth[0], warm_earth[1], 'contact_header.jpg', 'Contact')
    create_gradient_image(1920, 600, green_brown[0], green_brown[1], 'feedback_header.jpg', 'Feedback')
    
    # Food Images - Starters
    create_gradient_image(600, 400, food_warm[0], food_warm[1], 'bruschetta.jpg', 'Bruschetta')
    create_gradient_image(600, 400, (230, 126, 34), (211, 84, 0), 'paneer_tikka.jpg', 'Paneer Tikka')
    create_gradient_image(600, 400, (192, 57, 43), (142, 68, 173), 'chicken_wings.jpg', 'Wings')
    create_gradient_image(600, 400, warm_earth[0], warm_earth[1], 'mezze_platter.jpg', 'Mezze')
    
    # Food Images - Main Course
    create_gradient_image(600, 400, (231, 76, 60), (230, 126, 34), 'butter_chicken.jpg', 'Butter Chicken')
    create_gradient_image(600, 400, (241, 196, 15), (243, 156, 18), 'risotto.jpg', 'Risotto')
    create_gradient_image(600, 400, (52, 152, 219), (41, 128, 185), 'seabass.jpg', 'Sea Bass')
    create_gradient_image(600, 400, (211, 84, 0), (230, 126, 34), 'dal_makhani.jpg', 'Dal Makhani')
    create_gradient_image(600, 400, elegant_gray[0], elegant_gray[1], 'truffle_pasta.jpg', 'Truffle Pasta')
    
    # Food Images - Desserts
    create_gradient_image(600, 400, (155, 89, 182), (142, 68, 173), 'tiramisu.jpg', 'Tiramisu')
    create_gradient_image(600, 400, warm_earth[0], warm_earth[1], 'gulab_jamun_cheesecake.jpg', 'Fusion Dessert')
    create_gradient_image(600, 400, (52, 73, 94), (44, 62, 80), 'lava_cake.jpg', 'Lava Cake')
    
    # Food Images - Beverages
    create_gradient_image(600, 400, (241, 196, 15), (243, 156, 18), 'latte.jpg', 'Latte')
    create_gradient_image(600, 400, (211, 84, 0), (230, 126, 34), 'masala_chai.jpg', 'Chai')
    create_gradient_image(600, 400, (46, 204, 113), (39, 174, 96), 'lime_soda.jpg', 'Lime Soda')
    create_gradient_image(600, 400, (255, 195, 0), (251, 140, 0), 'mango_lassi.jpg', 'Mango Lassi')
    
    # Gallery Images
    create_gradient_image(800, 600, cool_green[0], cool_green[1], 'gallery_ambience_1.jpg', 'Ambience')
    create_gradient_image(800, 600, green_brown[0], green_brown[1], 'gallery_ambience_2.jpg', 'Interior')
    create_gradient_image(800, 600, elegant_gray[0], elegant_gray[1], 'gallery_ambience_3.jpg', 'Seating')
    create_gradient_image(800, 600, food_warm[0], food_warm[1], 'gallery_food_1.jpg', 'Food Art')
    create_gradient_image(800, 600, (230, 126, 34), (192, 57, 43), 'gallery_food_2.jpg', 'Fresh')
    create_gradient_image(800, 600, (155, 89, 182), (142, 68, 173), 'gallery_food_3.jpg', 'Desserts')
    create_gradient_image(800, 600, warm_earth[0], warm_earth[1], 'gallery_interior_1.jpg', 'Bar')
    create_gradient_image(800, 600, green_brown[0], green_brown[1], 'gallery_interior_2.jpg', 'Dining')
    create_gradient_image(800, 600, (52, 152, 219), (41, 128, 185), 'gallery_event_1.jpg', 'Events')
    create_gradient_image(800, 600, (231, 76, 60), (192, 57, 43), 'gallery_event_2.jpg', 'Celebration')
    
    # About Page Images
    create_gradient_image(800, 600, green_brown[0], green_brown[1], 'founders.jpg', 'Founders')
    create_gradient_image(800, 600, elegant_gray[0], elegant_gray[1], 'interior_elegant.jpg', 'Elegant Interior')
    create_gradient_image(600, 600, warm_earth[0], warm_earth[1], 'chef_vikram.jpg', 'Chef Vikram')
    create_gradient_image(600, 600, cool_green[0], cool_green[1], 'meera_kapoor.jpg', 'Meera Kapoor')
    create_gradient_image(600, 600, food_warm[0], food_warm[1], 'pastry_chef.jpg', 'Pastry Chef')
    
    # Cuisine Page Images
    create_gradient_image(800, 600, (211, 84, 0), (230, 126, 34), 'cuisine_indian.jpg', 'Indian')
    create_gradient_image(800, 600, (46, 204, 113), (39, 174, 96), 'cuisine_italian.jpg', 'Italian')
    create_gradient_image(800, 600, elegant_gray[0], elegant_gray[1], 'cuisine_continental.jpg', 'Continental')
    create_gradient_image(800, 600, warm_earth[0], warm_earth[1], 'cuisine_fusion.jpg', 'Fusion')
    create_gradient_image(800, 600, green_brown[0], green_brown[1], 'chef_at_work.jpg', 'Chef')
    
    # Why Us Page Images
    create_gradient_image(800, 600, cool_green[0], cool_green[1], 'brand_identity.jpg', 'Brand')
    
    # Instagram Feed
    for i in range(1, 7):
        create_gradient_image(500, 500, warm_earth[0], warm_earth[1], f'insta_{i}.jpg', f'Post {i}')
    
    print("\n✅ All images generated successfully!")
    print(f"Total images created in 'static/images/' directory")

if __name__ == "__main__":
    generate_all_images()
