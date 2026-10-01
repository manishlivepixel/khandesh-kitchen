with open('D:/VIBE CODING/Khandesh Kitchen/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

repl = [
    ('Authentic Khandeshi Flavors', '<span data-i18n="Authentic Khandeshi Flavors">Authentic Khandeshi Flavors</span>'),
    ('Experience the fiery, rustic, and soulful taste of Jalgaon right here in Badlapur.', '<span data-i18n="Experience the fiery, rustic, and soulful taste of Jalgaon right here in Badlapur.">Experience the fiery, rustic, and soulful taste of Jalgaon right here in Badlapur.</span>'),
    ('Explore Menu', '<span data-i18n="Explore Menu">Explore Menu</span>'),
    ('Book a Table', '<span data-i18n="Book a Table">Book a Table</span>'),
    ('Why Khandesh Kitchen?', '<span data-i18n="Why Khandesh Kitchen?">Why Khandesh Kitchen?</span>'),
    ('Authentic Spices', '<span data-i18n="Authentic Spices">Authentic Spices</span>'),
    ('We source our black spices directly from Jalgaon to maintain the true, fiery Khandeshi flavor.', '<span data-i18n="We source our black spices directly from Jalgaon to maintain the true, fiery Khandeshi flavor.">We source our black spices directly from Jalgaon to maintain the true, fiery Khandeshi flavor.</span>'),
    ('Traditional Cooking', '<span data-i18n="Traditional Cooking">Traditional Cooking</span>'),
    ('Prepared using slow-cooking methods and age-old recipes passed down through generations.', '<span data-i18n="Prepared using slow-cooking methods and age-old recipes passed down through generations.">Prepared using slow-cooking methods and age-old recipes passed down through generations.</span>'),
    ('Homestyle Warmth', '<span data-i18n="Homestyle Warmth">Homestyle Warmth</span>'),
    ('Every dish is made with love, ensuring it feels like a comforting meal right at home.', '<span data-i18n="Every dish is made with love, ensuring it feels like a comforting meal right at home.">Every dish is made with love, ensuring it feels like a comforting meal right at home.</span>'),
    ('Our Grand Opening', '<span data-i18n="Our Grand Opening">Our Grand Opening</span>'),
    ('Glimpses of Khandesh', '<span data-i18n="Glimpses of Khandesh">Glimpses of Khandesh</span>'),
    ('Open Daily', '<span data-i18n="Open Daily">Open Daily</span>'),
    ('11:00 AM - 11:00 PM', '<span data-i18n="11:00 AM - 11:00 PM">11:00 AM - 11:00 PM</span>'),
    ('Call Us', '<span data-i18n="Call Us">Call Us</span>'),
    ('Hours', '<span data-i18n="Hours">Hours</span>'),
    ('Follow Us', '<span data-i18n="Follow Us">Follow Us</span>')
]

for k, v in repl:
    # only replace if not already wrapped
    if 'data-i18n="' + k + '"' not in text:
        text = text.replace(k, v)

with open('D:/VIBE CODING/Khandesh Kitchen/index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Done")
