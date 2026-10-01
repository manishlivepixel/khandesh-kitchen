import re
import json

wiki_images = {
    "batata-vada": "https://upload.wikimedia.org/wikipedia/commons/8/8b/Mumbai-vada.jpg",
    "rice-plate": "https://upload.wikimedia.org/wikipedia/commons/4/49/Vegetarian_Curry.jpeg",
    "mutton-bhakri-thali": "https://upload.wikimedia.org/wikipedia/commons/4/49/Vegetarian_Curry.jpeg",
    "mutton-thali-with-bhakri": "https://upload.wikimedia.org/wikipedia/commons/4/49/Vegetarian_Curry.jpeg",
    "kanda-lasuni": "https://upload.wikimedia.org/wikipedia/commons/0/00/Chicken_tikka_masala_%28cropped%29.jpg",
    "dry-chicken": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Chickentandoori.jpg",
    "3-sabzi-bhakri-rice-kadhi-thecha": "https://upload.wikimedia.org/wikipedia/commons/4/49/Vegetarian_Curry.jpeg",
    "seasonal-sabzi-+-sweet": "https://upload.wikimedia.org/wikipedia/commons/4/49/Vegetarian_Curry.jpeg",
    "buttermilk--ambil": "https://upload.wikimedia.org/wikipedia/commons/f/f9/Mint_lassi.jpg",
    "unlimited-on-thali": "https://upload.wikimedia.org/wikipedia/commons/6/67/Kadhi_Pakora.jpg",
    "dry-mutton": "https://upload.wikimedia.org/wikipedia/commons/8/80/Bengali_Mutton_Curry.JPG"
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
        if slug in wiki_images:
            # Replace the image src
            full_li = re.sub(r'<img src="[^"]+"', f'<img src="{wiki_images[slug]}"', full_li)
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
    for slug, img_path in wiki_images.items():
        if slug in dish_data:
            dish_data[slug]["image"] = img_path
            
    # Write back
    new_json_str = json.dumps(dish_data)
    dish_content = dish_content[:m_json.start(1)] + new_json_str + dish_content[m_json.end(1):]
    
    with open("D:/VIBE CODING/Khandesh Kitchen/dish.html", "w", encoding="utf-8") as f:
        f.write(dish_content)

print("Final wiki images updated successfully")
