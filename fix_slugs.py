import re

# Fix index.html
with open("D:/VIBE CODING/Khandesh Kitchen/index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("dish.html?id=seasonal-sabzi-+-sweet", "dish.html?id=seasonal-sabzi-plus-sweet")
html = html.replace("dish.html?id=buttermilk--ambil", "dish.html?id=buttermilk-ambil")

with open("D:/VIBE CODING/Khandesh Kitchen/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# Fix dish.html
with open("D:/VIBE CODING/Khandesh Kitchen/dish.html", "r", encoding="utf-8") as f:
    dish = f.read()

dish = dish.replace('"seasonal-sabzi-+-sweet"', '"seasonal-sabzi-plus-sweet"')
dish = dish.replace('"buttermilk--ambil"', '"buttermilk-ambil"')

with open("D:/VIBE CODING/Khandesh Kitchen/dish.html", "w", encoding="utf-8") as f:
    f.write(dish)

print("Slugs fixed!")
