import re
import json

# Local images we just generated
img_shev = "assets/images/dish-shev-bhaji.jpg"
img_vangyache = "assets/images/dish-vangyache-bharit.jpg"
img_pithle = "assets/images/dish-pithle.jpg"
img_mutton = "assets/images/dish-mutton-rassa.jpg"

custom_images = {
    "shev-bhaji": img_shev,
    "vangyache-bharit": img_vangyache,
    "pithle": img_pithle,
    "mutton-rassa": img_mutton,
}

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
        if slug in custom_images:
            # Replace the image src
            full_li = re.sub(r'<img src="[^"]+"', f'<img src="{custom_images[slug]}"', full_li)
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
    for slug, img_path in custom_images.items():
        if slug in dish_data:
            dish_data[slug]["image"] = img_path
            
    # Write back
    new_json_str = json.dumps(dish_data)
    dish_content = dish_content[:m_json.start(1)] + new_json_str + dish_content[m_json.end(1):]
    
    with open("D:/VIBE CODING/Khandesh Kitchen/dish.html", "w", encoding="utf-8") as f:
        f.write(dish_content)

print("Images updated")
