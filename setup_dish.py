import re
import json

with open("D:/VIBE CODING/Khandesh Kitchen/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Valid images that work based on the screenshot
img1 = "https://images.unsplash.com/photo-1546833999-b9f581a1996d?q=80&w=600&h=600&fit=crop"
img2 = "https://images.unsplash.com/photo-1512058564366-18510be2db19?q=80&w=600&h=600&fit=crop"
img3 = "https://images.unsplash.com/photo-1601050690597-df0568f70950?q=80&w=600&h=600&fit=crop"
img4 = "https://images.unsplash.com/photo-1606491956689-2ea866880c84?q=80&w=600&h=600&fit=crop"

img_map = {
    "Shev Bhaji": img4,
    "Vangyache Bharit": img1,
    "Pithle": img1,
    "Bhoplya Bhaji": img2,
    "Batatyachi Bhaji": img2,
    "Bhakri": img2,
    "Thecha": img4,
    "Chapati": img2,
    "Rice Plate": img3,
    "Khandeshi Kadhi": img1,
    "Mutton Rassa": img4,
    "Dry Mutton": img3,
    "Mutton Bhakri Thali": img1,
    "Chicken Rassa": img4,
    "Kanda Lasuni": img3,
    "Dry Chicken": img3,
    "Khandeshi Egg Curry": img4,
    "3 sabzi, bhakri, rice, kadhi, thecha": img1,
    "Seasonal sabzi + sweet": img1,
    "Mutton thali with bhakri": img1,
    "Onion Bhaji": img3,
    "Batata Vada": img3,
    "Buttermilk / Ambil": img2,
    "Unlimited on thali": img2,
}

descriptions = {
    "Shev Bhaji": "A fiery, vibrant Khandeshi delicacy where crisp chickpea flour noodles (shev) are submerged in a spicy, deep red curry. Prepared with our secret freshly ground black masala, this dish packs a powerful punch of flavor.",
    "Vangyache Bharit": "Smoky, fire-roasted eggplant mashed and tempered with Khandeshi green chilies, garlic, and spring onions. A rustic comfort food that pairs beautifully with hot bhakri.",
    "Pithle": "A traditional Maharashtrian chickpea flour curry, cooked to a creamy, savory perfection with garlic, mustard seeds, and curry leaves. The ultimate comfort meal.",
    "Bhoplya Bhaji": "Sweet and savory pumpkin curry tempered with earthy spices. A mild yet deeply flavorful sabzi that highlights the natural sweetness of the pumpkin.",
    "Batatyachi Bhaji": "A humble yet irresistible dry potato preparation with turmeric, mustard seeds, and fresh coriander. Simple, homestyle, and absolutely delicious.",
    "Bhakri": "Thick, rustic flatbreads made from Bajri (pearl millet) or Jwari (sorghum). Hand-pressed and roasted on an iron tawa until crisp on the outside and soft inside.",
    "Thecha": "The legendary Khandeshi accompaniment! A fiercely spicy, coarse chutney made by pounding fresh green or red chilies with garlic, peanuts, and salt.",
    "Chapati": "Soft, thin whole wheat flatbreads, perfect for scooping up our rich gravies and dry sabzis.",
    "Rice Plate": "A comforting portion of steaming hot Indrayani or Kolam rice, served with our signature homestyle amti or dal.",
    "Khandeshi Kadhi": "A tangy, subtly sweet and spicy yogurt-based soup tempered with ginger, garlic, and curry leaves. The perfect palate cleanser.",
    "Mutton Rassa": "Our signature! Tender pieces of mutton slow-cooked in a fiery, dark Khandeshi rassa. The broth is rich with roasted dry coconut and our house-special black masala.",
    "Dry Mutton": "Succulent mutton pieces stir-fried until the rich, spicy masala clings to the meat. A dry preparation packed with intense, smoky flavors.",
    "Mutton Bhakri Thali": "The ultimate Khandeshi feast. Features our spicy Mutton Rassa, Dry Mutton, hot Bhakris, Indrayani rice, and a slice of raw onion with lemon.",
    "Chicken Rassa": "Homestyle chicken curry cooked in a fiery Khandeshi red broth. A soul-warming dish with a perfect balance of heat and flavor.",
    "Kanda Lasuni": "Chicken cooked in a rich, deeply caramelized onion and garlic base. The slow roasting process gives this dish an irresistible savory depth.",
    "Dry Chicken": "Spicy, pan-roasted chicken tossed in robust dry spices and fresh coriander. Perfect as a starter or alongside dal and rice.",
    "Khandeshi Egg Curry": "Boiled eggs simmered in a robust, spicy onion-tomato and coconut gravy. A hearty and satisfying classic.",
    "3 sabzi, bhakri, rice, kadhi, thecha": "A wholesome, complete Khandeshi vegetarian thali featuring the day's fresh sabzis, hot bhakris, fragrant rice, kadhi, and spicy thecha.",
    "Seasonal sabzi + sweet": "Our special vegetarian thali with premium seasonal preparations, an extra sabzi, and a traditional sweet dish to complete the meal.",
    "Mutton thali with bhakri": "A grand non-vegetarian spread with our signature Mutton Rassa, Sukha Mutton, soft Bhakris, Rice, and fiery accompaniments.",
    "Onion Bhaji": "Crisp, golden-fried onion fritters seasoned with carom seeds and fresh coriander. The perfect hot snack.",
    "Batata Vada": "Spiced mashed potato balls dipped in chickpea batter and deep-fried to golden perfection. A quintessential Maharashtrian favorite.",
    "Buttermilk / Ambil": "Traditional spiced buttermilk or Ambil (fermented millet cooler) to soothe your palate after a fiery Khandeshi meal.",
    "Unlimited on thali": "Enjoy unlimited servings of our fragrant rice and Solapuri-style kadhi with your thali."
}

def make_clickable(match):
    li_inner = match.group(1)
    # Extract the dish name
    marathi_match = re.search(r'<span class="menu__name">(.*?)\s*<small>', li_inner)
    small_match = re.search(r'<small>(.*?)</small>', li_inner)
    if small_match and marathi_match:
        dish_eng = small_match.group(1)
        dish_mar = marathi_match.group(1).strip()
        slug = dish_eng.replace(" ", "-").replace("/", "").replace(",", "").lower()
        
        # fix broken image in the html
        img_url = img_map.get(dish_eng, img1)
        # replace img src
        li_inner = re.sub(r'<img src="[^"]+"', f'<img src="{img_url}"', li_inner)
        
        return f'<li class="menu__item-clickable" onclick="window.location.href=\'dish.html?id={slug}\'">{li_inner}</li>'
    return match.group(0)

new_html = re.sub(r'<li>(.*?)</li>', make_clickable, html, flags=re.DOTALL)

with open("D:/VIBE CODING/Khandesh Kitchen/index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

# Add CSS for clickable li
with open("D:/VIBE CODING/Khandesh Kitchen/css/style.css", "a", encoding="utf-8") as f:
    f.write("\n.menu__item-clickable { cursor: pointer; transition: background .2s, transform .2s; border-radius: 12px; padding-inline: 10px; margin-inline: -10px; }\n.menu__item-clickable:hover { background: rgba(242, 182, 50, .05); transform: translateX(4px); }\n")

# Now generate the JS data for dish.html
dish_data = {}
for eng, desc in descriptions.items():
    slug = eng.replace(" ", "-").replace("/", "").replace(",", "").lower()
    # find marathi name from html
    mar_name = ""
    for line in html.splitlines():
        if f"<small>{eng}</small>" in line:
            m = re.search(r'<span class="menu__name">(.*?)\s*<small>', line)
            if m:
                mar_name = m.group(1).strip()
            break
    
    price = ""
    for line in html.splitlines():
        if f"<small>{eng}</small>" in line:
            m = re.search(r'<span class="menu__price">(.*?)</span>', line)
            if m:
                price = m.group(1)
            break
            
    dish_data[slug] = {
        "title_en": eng,
        "title_mr": mar_name,
        "image": img_map.get(eng, img1),
        "desc": desc,
        "price": price
    }

dish_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dish Details — Khandesh Kitchen</title>
  <link rel="icon" type="image/svg+xml" href="assets/images/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Yatra+One&family=Baloo+2:wght@400;500;600;700;800&family=Mukta:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
  <style>
    .dish-page { min-height: 100vh; background: var(--dark); padding: 4rem 0; color: var(--cream); }
    .dish-card { background: var(--dark-2); border-radius: 24px; border: 1px solid var(--line); overflow: hidden; display: flex; flex-direction: column; max-width: 800px; margin: 0 auto; box-shadow: var(--shadow-lg); }
    .dish-img { width: 100%; height: 380px; object-fit: cover; }
    .dish-content { padding: 3rem; }
    .dish-title-mr { font-family: var(--f-display); font-size: 2.8rem; color: var(--gold); margin-bottom: 0.2rem; }
    .dish-title-en { font-family: var(--f-sub); font-size: 1.2rem; color: rgba(246,237,217,.6); letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 1.5rem; }
    .dish-desc { font-size: 1.1rem; line-height: 1.8; color: rgba(246,237,217,.85); margin-bottom: 2.5rem; }
    .dish-price { font-family: var(--f-display); font-size: 1.8rem; color: var(--gold-light); display: inline-block; padding: 0.5rem 1.5rem; border: 2px dashed var(--line); border-radius: 12px; }
    .back-btn { display: inline-flex; align-items: center; gap: 0.5rem; color: var(--gold); margin-bottom: 2rem; font-family: var(--f-sub); font-weight: 700; font-size: 1.1rem; transition: transform 0.2s; }
    .back-btn:hover { transform: translateX(-4px); }
    @media(max-width: 768px) { .dish-content { padding: 2rem; } .dish-title-mr { font-size: 2.2rem; } .dish-img { height: 260px; } }
  </style>
</head>
<body>
  <div class="topbar">
    <div class="container topbar__inner">
      <span class="topbar__item">Patil Pada, Katrap, Badlapur 421503</span>
    </div>
  </div>

  <section class="dish-page">
    <div class="container">
      <a href="index.html#menu" class="back-btn">← Back to Menu</a>
      <div class="dish-card" id="dishCard" style="display:none;">
        <img src="" alt="" class="dish-img" id="dImg">
        <div class="dish-content">
          <h1 class="dish-title-mr" id="dTitleMr"></h1>
          <div class="dish-title-en" id="dTitleEn"></div>
          <p class="dish-desc" id="dDesc"></p>
          <div class="dish-price" id="dPrice"></div>
        </div>
      </div>
      <div id="errorMsg" style="display:none; text-align:center; padding: 4rem;">
        <h2 class="h2 h2--light">Dish not found</h2>
        <a href="index.html#menu" class="btn btn--gold" style="margin-top:2rem;">Explore Menu</a>
      </div>
    </div>
  </section>

  <script>
    const dishData = {DISH_DATA_JSON};
    const params = new URLSearchParams(window.location.search);
    const id = params.get('id');
    const data = dishData[id];
    
    if(data) {
      document.getElementById('dishCard').style.display = 'flex';
      document.getElementById('dImg').src = data.image;
      document.getElementById('dImg').alt = data.title_en;
      document.getElementById('dTitleMr').textContent = data.title_mr || data.title_en;
      document.getElementById('dTitleEn').textContent = data.title_en;
      document.getElementById('dDesc').textContent = data.desc;
      document.getElementById('dPrice').textContent = data.price;
      document.title = (data.title_mr || data.title_en) + " — Khandesh Kitchen";
    } else {
      document.getElementById('errorMsg').style.display = 'block';
    }
  </script>
</body>
</html>
"""

dish_html = dish_html.replace("{DISH_DATA_JSON}", json.dumps(dish_data))

with open("D:/VIBE CODING/Khandesh Kitchen/dish.html", "w", encoding="utf-8") as f:
    f.write(dish_html)

print("Setup complete")
