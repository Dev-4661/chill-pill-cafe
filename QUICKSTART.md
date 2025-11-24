# 🚀 Quick Start Guide - Chill Pill Café

## Getting Started in 3 Simple Steps

### ✅ Step 1: Install Dependencies
Open your terminal in the project directory and run:
```bash
pip install -r requirements.txt
```

### ✅ Step 2: Generate Images
Run the image generator script:
```bash
python generate_images.py
```

This creates 50+ beautiful placeholder images in the `static/images/` directory.

### ✅ Step 3: Launch the Website
Start the Flask development server:
```bash
python app.py
```

🎉 **Your website is now live!**
Open your browser and visit: **http://localhost:5000**

---

## 📱 Available Pages

Once the server is running, you can visit:

1. **Home** - http://localhost:5000/
2. **About Us** - http://localhost:5000/about
3. **Menu** - http://localhost:5000/menu
4. **Reservation** - http://localhost:5000/reservation
5. **Gallery** - http://localhost:5000/gallery
6. **Cuisine Types** - http://localhost:5000/cuisine
7. **Why We Stand Out** - http://localhost:5000/why-us
8. **Contact** - http://localhost:5000/contact
9. **Feedback** - http://localhost:5000/feedback

---

## 🎨 What You Get

### ✨ Premium Features
- ✅ **9 Fully Functional Pages** - Complete multi-page restaurant website
- ✅ **Modern UI/UX** - Clean, elegant, professional design
- ✅ **Fully Responsive** - Works on desktop, tablet, and mobile
- ✅ **AI-Generated Images** - 50+ high-quality placeholder images
- ✅ **Interactive Elements** - Smooth animations, hover effects
- ✅ **Form Validation** - Client-side and server-side validation
- ✅ **Sticky Navigation** - Professional navbar with scroll effects
- ✅ **Mobile Menu** - Hamburger menu for mobile devices
- ✅ **Flash Messages** - User feedback system
- ✅ **SEO Optimized** - Semantic HTML structure

### 🎯 Key Functionalities
- **Reservation System** - Book tables with confirmation page
- **Menu Display** - Categorized dishes with dietary information
- **Gallery** - Filterable image gallery (ambience, food, events)
- **Feedback System** - Star rating and review submission
- **Contact Form** - Get in touch functionality
- **About Section** - Company story, mission, team profiles

---

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern design patterns
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Playfair Display, Poppins)
- **Images**: AI-generated with Pillow (PIL)

---

## 📂 Project Structure

```
Chill Pill Café/
├── app.py                     # Flask application
├── generate_images.py         # Image generator
├── requirements.txt           # Dependencies
├── README.md                  # Full documentation
├── QUICKSTART.md             # This file
├── templates/                 # HTML templates (10 files)
├── static/
│   ├── css/style.css         # Comprehensive styling
│   ├── js/script.js          # Interactive features
│   └── images/               # 50+ generated images
```

---

## 🎨 Customization

### Change Restaurant Name
Edit in `templates/base.html`:
```html
<span class="logo-text">Your Restaurant Name</span>
```

### Update Colors
Edit in `static/css/style.css`:
```css
:root {
    --primary-color: #2c5f2d;    /* Your primary color */
    --secondary-color: #d4af37;   /* Your secondary color */
}
```

### Modify Menu Items
Edit in `app.py`:
```python
menu_data = {
    'starters': [...],  # Add/edit dishes here
    'mains': [...],
}
```

### Update Contact Information
Edit in `app.py`:
```python
contact_info = {
    'address': 'Your Address',
    'phone': 'Your Phone Number',
    'email': 'your.email@example.com',
}
```

---

## 📞 Need Help?

### Common Issues

**Port already in use?**
```bash
# Change port in app.py:
app.run(debug=True, host='0.0.0.0', port=5001)  # Use 5001 instead
```

**Images not showing?**
```bash
# Re-run image generator:
python generate_images.py
```

**Module not found error?**
```bash
# Reinstall dependencies:
pip install -r requirements.txt
```

---

## 🚀 Next Steps

1. **Replace Placeholder Images** - Add real food photos, ambience shots
2. **Update Content** - Customize text, menu items, pricing
3. **Add Database** - Implement SQLite/PostgreSQL for reservations
4. **Email Notifications** - Send confirmation emails
5. **Payment Integration** - Add payment gateway for advance booking
6. **Deploy Online** - Host on Heroku, PythonAnywhere, or AWS

---

## 📈 Performance Tips

- Images are optimized for web
- CSS/JS files are minified-ready
- Lazy loading implemented
- Mobile-first responsive design
- Fast page load times

---

## ✅ Checklist

- [x] Flask installed
- [x] Dependencies installed
- [x] Images generated
- [x] Server running
- [x] Website accessible at localhost:5000
- [ ] Customized with your content
- [ ] Real images added
- [ ] Ready for deployment

---

## 🎉 You're All Set!

Your professional restaurant website is ready to use. Enjoy building upon this foundation!

**Happy Coding! 🍽️**

---

*Made with ❤️ for Chill Pill Café*
