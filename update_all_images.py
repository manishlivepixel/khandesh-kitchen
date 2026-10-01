import re
import json

# Local images we just generated
custom_images = {
    "shev-bhaji": "assets/images/dish-shev-bhaji.jpg",
    "vangyache-bharit": "assets/images/dish-vangyache-bharit.jpg",
    "pithle": "assets/images/dish-pithle.jpg",
    "mutton-rassa": "assets/images/dish-mutton-rassa.jpg",
    "bhoplya-bhaji": "assets/images/dish-bhoplya-bhaji.jpg",
    "batatyachi-bhaji": "assets/images/dish-batatyachi-bhaji.jpg",
    "bhakri": "assets/images/dish-bhakri.jpg",
    "thecha": "assets/images/dish-thecha.jpg",
    "chapati": "assets/images/dish-chapati.jpg",
    "khandeshi-kadhi": "assets/images/dish-khandeshi-kadhi.jpg",
    "chicken-rassa": "assets/images/dish-chicken-rassa.jpg",
    "khandeshi-egg-curry": "assets/images/dish-khandeshi-egg-curry.jpg",
    "onion-bhaji": "assets/images/dish-onion-bhaji.jpg",
}

fallback_unsplash = {
    "rice-plate": "https://images.unsplash.com/photo-1626544827763-d516dce335e2?q=80&w=600&h=600&fit=crop",
    "dry-mutton": "https://images.unsplash.com/photo-1574484284002-952d92456975?q=80&w=600&h=600&fit=crop",
    "mutton-bhakri-thali": "https://images.unsplash.com/photo-1625944227376-793574c8f2ba?q=80&w=600&h=600&fit=crop",
    "mutton-thali-with-bhakri": "https://images.unsplash.com/photo-1625944227376-793574c8f2ba?q=80&w=600&h=600&fit=crop",
    "kanda-lasuni": "https://images.unsplash.com/photo-1589301760014-d929f39ce9b1?q=80&w=600&h=600&fit=crop",
    "dry-chicken": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?q=80&w=600&h=600&fit=crop",
    "3-sabzi-bhakri-rice-kadhi-thecha": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?q=80&w=600&h=600&fit=crop",
    "seasonal-sabzi-+-sweet": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?q=80&w=600&h=600&fit=crop",
    "batata-vada": "https://images.unsplash.com/photo-1601050690597-df0568f70950?q=80&w=600&h=600&fit=crop",
    "buttermilk--ambil": "https://images.unsplash.com/photo-1626082895617-2c6b446a8047?q=80&w=600&h=600&fit=crop",
    "unlimited-on-thali": "https://images.unsplash.com/photo-1626544827763-d516dce335e2?q=80&w=600&h=600&fit=crop"
}

all_updates = {**custom_images, **fallback_unsplash}

# 1. Update index.html
with open("D:/VIBE CODING/Khandesh Kitchen/index.html", "r", encoding="utf-8") as f:
    html = f.read()

def update_img(match):
    full_li = match.group(0)
    onclick_content = match.group(1)
    
    # extract slug
    m_slug = re.search(r"id=([^']+)'", onclick_content)
    if m_slug:
        slug = m_slug.group(1)
        if slug in all_updates:
            # Replace the image src
            full_li = re.sub(r'<img src="[^"]+"', f'<img src="{all_updates[slug]}"', full_li)
    return full_li

html = re.sub(r'(<li class="menu__item-clickable" onclick="window.location.href=\'dish\.html\?id=[^\']+\'">.*?</li>)', update_img, html)

with open("D:/VIBE CODING/Khandesh Kitchen/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# 2. Update dish.html JSON data
with open("D:/VIBE CODING/Khandesh Kitchen/dish.html", "r", encoding="utf-8") as f:
    dish_content = f.read()

# Extract existing json
m_json = re.search(r'const dishData = (\{.*?\});', dish_content, flags=re.DOTALL)
if m_json:
    dish_data = json.loads(m_json.group(1))
    
    # Update the images for our custom ones
    for slug, img_path in all_updates.items():
        if slug in dish_data:
            dish_data[slug]["image"] = img_path
            
    # Write back
    new_json_str = json.dumps(dish_data)
    dish_content = dish_content[:m_json.start(1)] + new_json_str + dish_content[m_json.end(1):]
    
    with open("D:/VIBE CODING/Khandesh Kitchen/dish.html", "w", encoding="utf-8") as f:
        f.write(dish_content)

print("All images updated successfully")
