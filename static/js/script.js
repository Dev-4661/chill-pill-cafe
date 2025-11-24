/**
 * RootStatix Cuisine - Main JavaScript
 * Interactive elements, form validation, and UI enhancements
 */

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    // ========================================
    // NAVIGATION FUNCTIONALITY
    // ========================================
    
    const navbar = document.getElementById('navbar');
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    
    // Navbar scroll effect
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
    
    // Mobile menu toggle
    if (navToggle) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            
            // Animate hamburger icon
            const spans = navToggle.querySelectorAll('span');
            spans[0].style.transform = navMenu.classList.contains('active') 
                ? 'rotate(45deg) translateY(8px)' 
                : 'none';
            spans[1].style.opacity = navMenu.classList.contains('active') ? '0' : '1';
            spans[2].style.transform = navMenu.classList.contains('active') 
                ? 'rotate(-45deg) translateY(-8px)' 
                : 'none';
        });
        
        // Close menu when clicking on a link
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
                const spans = navToggle.querySelectorAll('span');
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
            });
        });
    }
    
    // ========================================
    // BACK TO TOP BUTTON
    // ========================================
    
    const backToTopBtn = document.getElementById('backToTop');
    
    if (backToTopBtn) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 300) {
                backToTopBtn.classList.add('show');
            } else {
                backToTopBtn.classList.remove('show');
            }
        });
        
        backToTopBtn.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
    
    // ========================================
    // FLASH MESSAGE CLOSE
    // ========================================
    
    const flashCloseButtons = document.querySelectorAll('.flash-close');
    flashCloseButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.closest('.flash-message').style.animation = 'slideOutRight 0.3s ease';
            setTimeout(() => {
                this.closest('.flash-message').remove();
            }, 300);
        });
    });
    
    // Auto-hide flash messages after 5 seconds
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.animation = 'slideOutRight 0.3s ease';
            setTimeout(() => {
                message.remove();
            }, 300);
        }, 5000);
    });
    
    // ========================================
    // FORM VALIDATION
    // ========================================
    
    // Reservation form validation
    const reservationForm = document.getElementById('reservationForm');
    if (reservationForm) {
        reservationForm.addEventListener('submit', function(e) {
            const phone = document.getElementById('phone').value;
            const phoneRegex = /^[\+]?[0-9]{10,15}$/;
            
            if (!phoneRegex.test(phone.replace(/\s/g, ''))) {
                e.preventDefault();
                alert('Please enter a valid phone number (10-15 digits)');
                return false;
            }
            
            // Check if date is in the future
            const selectedDate = new Date(document.getElementById('date').value);
            const today = new Date();
            today.setHours(0, 0, 0, 0);
            
            if (selectedDate < today) {
                e.preventDefault();
                alert('Please select a future date for your reservation');
                return false;
            }
        });
    }
    
    // Feedback form validation
    const feedbackForm = document.getElementById('feedbackForm');
    if (feedbackForm) {
        feedbackForm.addEventListener('submit', function(e) {
            const rating = document.querySelector('input[name="rating"]:checked');
            
            if (!rating) {
                e.preventDefault();
                alert('Please select a rating before submitting');
                return false;
            }
            
            const comments = document.getElementById('comments').value.trim();
            if (comments.length < 10) {
                e.preventDefault();
                alert('Please provide at least 10 characters in your comments');
                return false;
            }
        });
    }
    
    // Newsletter form
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;
            alert(`Thank you for subscribing! We'll send updates to ${email}`);
            this.reset();
        });
    }
    
    // ========================================
    // SMOOTH SCROLL FOR HERO ARROW
    // ========================================
    
    const heroScroll = document.querySelector('.hero-scroll');
    if (heroScroll) {
        heroScroll.addEventListener('click', function() {
            const nextSection = document.querySelector('.intro-section, .menu-intro, .story-section, .gallery-intro');
            if (nextSection) {
                nextSection.scrollIntoView({ behavior: 'smooth' });
            }
        });
    }
    
    // ========================================
    // ANIMATION ON SCROLL
    // ========================================
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animateElements = document.querySelectorAll(
        '.feature-card, .dish-card, .testimonial-card, .menu-item, ' +
        '.value-card, .diff-card, .team-member, .award-card, ' +
        '.faq-item, .stat-card, .info-card'
    );
    
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
    
    // ========================================
    // IMAGE LAZY LOADING (Fallback)
    // ========================================
    
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
    
    // ========================================
    // PREVENT FORM DOUBLE SUBMISSION
    // ========================================
    
    const allForms = document.querySelectorAll('form');
    allForms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
                
                // Re-enable after 3 seconds as fallback
                setTimeout(() => {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = submitBtn.dataset.originalText || 'Submit';
                }, 3000);
            }
        });
    });
    
    // ========================================
    // INPUT FORMATTING
    // ========================================
    
    // Phone number formatting
    const phoneInputs = document.querySelectorAll('input[type="tel"]');
    phoneInputs.forEach(input => {
        input.addEventListener('input', function() {
            // Remove non-numeric characters except +
            let value = this.value.replace(/[^\d+]/g, '');
            this.value = value;
        });
    });
    
    // ========================================
    // INTERACTIVE HOVER EFFECTS
    // ========================================
    
    // Add ripple effect to buttons
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple');
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
    
    // ========================================
    // ACCESSIBILITY ENHANCEMENTS
    // ========================================
    
    // Add keyboard navigation for cards
    const clickableCards = document.querySelectorAll('.dish-card, .menu-item, .gallery-item');
    clickableCards.forEach(card => {
        card.setAttribute('tabindex', '0');
        card.addEventListener('keypress', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                const link = this.querySelector('a');
                if (link) {
                    link.click();
                }
            }
        });
    });
    
    // ========================================
    // PERFORMANCE OPTIMIZATION
    // ========================================
    
    // Debounce scroll events
    let scrollTimeout;
    window.addEventListener('scroll', function() {
        if (scrollTimeout) {
            window.cancelAnimationFrame(scrollTimeout);
        }
        scrollTimeout = window.requestAnimationFrame(function() {
            // Scroll-based code here
        });
    }, { passive: true });
    
    // ========================================
    // CONSOLE MESSAGE
    // ========================================
    
    console.log(
        '%cRootStatix Cuisine',
        'font-size: 24px; font-weight: bold; color: #2c5f2d;'
    );
    console.log(
        '%cWhere culinary artistry meets tranquil ambience',
        'font-size: 14px; color: #636e72;'
    );
    console.log('Website developed with ❤️ for the best dining experience in Mumbai');
});

// ========================================
// ADDITIONAL UTILITY FUNCTIONS
// ========================================

/**
 * Format currency
 */
function formatCurrency(amount) {
    return '₹' + amount.toLocaleString('en-IN');
}

/**
 * Validate email format
 */
function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

/**
 * Format date for display
 */
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('en-IN', options);
}

/**
 * Animate number counter
 */
function animateCounter(element, target, duration = 2000) {
    let start = 0;
    const increment = target / (duration / 16);
    const timer = setInterval(() => {
        start += increment;
        if (start >= target) {
            element.textContent = target;
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(start);
        }
    }, 16);
}

// Add CSS for ripple effect dynamically
const style = document.createElement('style');
style.textContent = `
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.6);
        transform: scale(0);
        animation: ripple-animation 0.6s ease-out;
        pointer-events: none;
    }
    
    @keyframes ripple-animation {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
