"""
RootStatix Cuisine - Flask Application
A modern, elegant restaurant website with multi-page functionality
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'chillpillcafe2025secretkey'

# Store reservations and feedback in memory (use database in production)
reservations = []
feedbacks = []


@app.route('/')
def index():
    """Home page with hero section and signature dishes"""
    return render_template('index.html')


@app.route('/about')
def about():
    """About Us page with story, mission, and values"""
    return render_template('about.html')


@app.route('/menu')
def menu():
    """Menu page with categorized dishes"""
    menu_data = {
        'starters': [
            {
                'name': 'Bruschetta Trio',
                'description': 'Classic Italian toasted bread with tomato, mozzarella, and basil',
                'price': '₹380',
                'image': 'bruschetta.jpg',
                'dietary': ['veg']
            },
            {
                'name': 'Paneer Tikka',
                'description': 'Tandoor-grilled cottage cheese with mint chutney',
                'price': '₹420',
                'image': 'paneer_tikka.jpg',
                'dietary': ['veg', 'spicy']
            },
            {
                'name': 'Chicken Wings',
                'description': 'Crispy wings tossed in BBQ glaze',
                'price': '₹480',
                'image': 'chicken_wings.jpg',
                'dietary': ['spicy']
            },
            {
                'name': 'Mezze Platter',
                'description': 'Hummus, falafel, pita bread, and Mediterranean dips',
                'price': '₹520',
                'image': 'mezze_platter.jpg',
                'dietary': ['veg', 'vegan']
            }
        ],
        'mains': [
            {
                'name': 'Butter Chicken',
                'description': 'Tender chicken in rich tomato and cream gravy',
                'price': '₹620',
                'image': 'butter_chicken.jpg',
                'dietary': [],
                'special': True
            },
            {
                'name': 'Risotto Al Funghi',
                'description': 'Creamy Italian rice with wild mushrooms',
                'price': '₹580',
                'image': 'risotto.jpg',
                'dietary': ['veg']
            },
            {
                'name': 'Grilled Sea Bass',
                'description': 'Fresh sea bass with lemon butter and seasonal vegetables',
                'price': '₹880',
                'image': 'seabass.jpg',
                'dietary': [],
                'special': True
            },
            {
                'name': 'Dal Makhani',
                'description': 'Slow-cooked black lentils with butter and cream',
                'price': '₹380',
                'image': 'dal_makhani.jpg',
                'dietary': ['veg']
            },
            {
                'name': 'Truffle Pasta',
                'description': 'Handmade pasta with truffle oil and parmesan',
                'price': '₹680',
                'image': 'truffle_pasta.jpg',
                'dietary': ['veg'],
                'special': True
            }
        ],
        'desserts': [
            {
                'name': 'Tiramisu',
                'description': 'Classic Italian coffee-soaked ladyfingers with mascarpone',
                'price': '₹320',
                'image': 'tiramisu.jpg',
                'dietary': ['veg']
            },
            {
                'name': 'Cheesecake',
                'description': 'Classic New York style with fresh strawberries',
                'price': '₹340',
                'image': 'cheesecake.jpg',
                'dietary': ['veg'],
                'special': True
            },
            {
                'name': 'Chocolate Lava Cake',
                'description': 'Warm molten chocolate center with vanilla ice cream',
                'price': '₹360',
                'image': 'lava_cake.jpg',
                'dietary': ['veg']
            }
        ],
        'beverages': [
            {
                'name': 'Café Latte',
                'description': 'Smooth espresso with steamed milk',
                'price': '₹180',
                'image': 'latte.jpg',
                'dietary': ['veg']
            },
            {
                'name': 'Mumbai Masala Chai',
                'description': 'Authentic Indian spiced tea',
                'price': '₹120',
                'image': 'masala_chai.jpg',
                'dietary': ['veg']
            },
            {
                'name': 'Fresh Lime Soda',
                'description': 'Refreshing mint and lime sparkler',
                'price': '₹150',
                'image': 'lime_soda.jpg',
                'dietary': ['veg', 'vegan']
            },
            {
                'name': 'Mango Lassi',
                'description': 'Creamy yogurt drink with fresh mango',
                'price': '₹160',
                'image': 'mango_lassi.jpg',
                'dietary': ['veg']
            }
        ]
    }
    return render_template('menu.html', menu=menu_data)


@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    """Reservation page with booking form"""
    if request.method == 'POST':
        reservation_data = {
            'id': len(reservations) + 1,
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'date': request.form.get('date'),
            'time': request.form.get('time'),
            'guests': request.form.get('guests'),
            'special_requests': request.form.get('special_requests'),
            'booked_at': datetime.now()
        }
        reservations.append(reservation_data)
        return render_template('reservation_confirmation.html', reservation=reservation_data)
    
    return render_template('reservation.html')


@app.route('/gallery')
def gallery():
    """Gallery page with ambience and food photos"""
    gallery_images = [
        {'src': 'gallery_ambience_1.jpg', 'category': 'ambience', 'alt': 'Cozy dining area'},
        {'src': 'gallery_ambience_2.jpg', 'category': 'ambience', 'alt': 'Modern interior design'},
        {'src': 'gallery_ambience_3.jpg', 'category': 'ambience', 'alt': 'Elegant seating'},
        {'src': 'gallery_food_1.jpg', 'category': 'food', 'alt': 'Signature dish plating'},
        {'src': 'gallery_food_2.jpg', 'category': 'food', 'alt': 'Fresh ingredients'},
        {'src': 'gallery_food_3.jpg', 'category': 'food', 'alt': 'Dessert presentation'},
        {'src': 'gallery_interior_1.jpg', 'category': 'interior', 'alt': 'Bar area'},
        {'src': 'gallery_interior_2.jpg', 'category': 'interior', 'alt': 'Private dining room'},
        {'src': 'gallery_event_1.jpg', 'category': 'events', 'alt': 'Live music night'},
        {'src': 'gallery_event_2.jpg', 'category': 'events', 'alt': 'Special celebration'},
    ]
    return render_template('gallery.html', images=gallery_images)


@app.route('/cuisine')
def cuisine():
    """Cuisine types page"""
    cuisines = [
        {
            'name': 'Indian',
            'description': 'Authentic flavors from across India, featuring rich gravies, aromatic spices, and traditional cooking methods. Our chefs bring generations of culinary wisdom to every dish.',
            'image': 'cuisine_indian.jpg',
            'specialties': ['Butter Chicken', 'Dal Makhani', 'Paneer Tikka', 'Biryani']
        },
        {
            'name': 'Italian',
            'description': 'Classic Italian cuisine with handmade pasta, wood-fired pizzas, and authentic recipes from Rome to Sicily. Experience the taste of Italy in Mumbai.',
            'image': 'cuisine_italian.jpg',
            'specialties': ['Truffle Pasta', 'Risotto', 'Bruschetta', 'Tiramisu']
        },
        {
            'name': 'Continental',
            'description': 'A sophisticated blend of European culinary traditions, featuring grilled meats, fresh seafood, and elegant presentations.',
            'image': 'cuisine_continental.jpg',
            'specialties': ['Grilled Sea Bass', 'Steaks', 'Mezze Platter']
        },
        {
            'name': 'Café Specials',
            'description': 'Our signature fusion creations that blend global flavors with local ingredients. Innovative dishes you won\'t find anywhere else.',
            'image': 'cuisine_fusion.jpg',
            'specialties': ['Cheesecake', 'Mumbai Masala Chai', 'Fusion Platters']
        }
    ]
    return render_template('cuisine.html', cuisines=cuisines)


@app.route('/why-us')
def why_us():
    """Why We Stand Out page"""
    return render_template('why_us.html')


@app.route('/contact')
def contact():
    """Contact Us page"""
    contact_info = {
        'address': 'Bandra West, Mumbai, Maharashtra, India',
        'phone': '+91 98765 43210',
        'email': 'info@chillpillcafe.com',
        'hours': {
            'weekdays': '11:00 AM - 11:00 PM',
            'weekends': '10:00 AM - 12:00 AM'
        },
        'social': {
            'instagram': 'https://instagram.com/chillpillcafe',
            'facebook': 'https://facebook.com/chillpillcafe',
            'twitter': 'https://twitter.com/chillpillcafe'
        }
    }
    return render_template('contact.html', contact=contact_info)


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    """Feedback page with rating form"""
    if request.method == 'POST':
        feedback_data = {
            'id': len(feedbacks) + 1,
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'rating': request.form.get('rating'),
            'comments': request.form.get('comments'),
            'submitted_at': datetime.now()
        }
        feedbacks.append(feedback_data)
        flash('Thank you for your valuable feedback! We truly appreciate your time.', 'success')
        return redirect(url_for('feedback'))
    
    return render_template('feedback.html')


@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page"""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
