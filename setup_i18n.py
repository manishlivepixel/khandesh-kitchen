import re

html_to_inject = """
    <!-- Google Translate (Hidden) -->
    <div id="google_translate_element" style="display:none;"></div>
    <script type="text/javascript">
      function googleTranslateElementInit() {
        new google.translate.TranslateElement({pageLanguage: 'en', includedLanguages: 'en,mr,hi', autoDisplay: false}, 'google_translate_element');
      }
    </script>
    <script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
"""

# HTML for the custom switcher
switcher_html = """
          <select id="langSwitch" class="lang-switch" aria-label="Change Language">
            <option value="en">English</option>
            <option value="mr">मराठी</option>
            <option value="hi">हिंदी</option>
          </select>
          <a href="tel:+919049932674" class="btn btn--gold btn--sm nav__cta">📞 Order on Call</a>
"""

# CSS for the custom switcher
css_to_inject = """
/* Language Switcher */
.lang-switch {
  background: rgba(246, 237, 217, 0.05);
  color: var(--cream);
  border: 1px solid var(--line);
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-family: var(--f-sub);
  font-size: 0.9rem;
  cursor: pointer;
  outline: none;
  transition: all 0.2s;
  appearance: none;
  -webkit-appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%23f6edd9' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 0.7rem center;
  padding-right: 2.2rem;
}
.lang-switch:hover {
  background-color: rgba(246, 237, 217, 0.1);
}
.lang-switch option {
  background: var(--dark-2);
  color: var(--cream);
}

/* Hide Google Translate completely */
body > .skiptranslate { display: none !important; }
.goog-te-banner-frame.skiptranslate { display: none !important; }
.goog-te-spinner-pos { display: none !important; }
body { top: 0px !important; }
"""

# JS to handle the switcher
js_to_inject = """
// Language Switcher Logic
document.addEventListener('DOMContentLoaded', () => {
  const langSwitch = document.getElementById('langSwitch');
  if(!langSwitch) return;
  
  // Read current language from cookie
  const match = document.cookie.match(/googtrans=\/en\/([a-z]{2})/);
  if(match && match[1]) {
    langSwitch.value = match[1];
  } else {
    langSwitch.value = 'en';
  }

  langSwitch.addEventListener('change', (e) => {
    const lang = e.target.value;
    if(lang === 'en') {
      // Clear cookies to reset
      document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
      document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; domain=' + location.hostname + '; path=/;';
    } else {
      document.cookie = `googtrans=/en/${lang}; path=/`;
      document.cookie = `googtrans=/en/${lang}; domain=${location.hostname}; path=/`;
    }
    location.reload();
  });
});
"""

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Inject GTranslate JS at end of body
    if "google_translate_element" not in content:
        content = content.replace("</body>", html_to_inject + "\n</body>")
    
    # Inject Custom Switcher
    if 'id="langSwitch"' not in content:
        content = re.sub(r'(<a href="tel:\+919049932674" class="btn btn--gold btn--sm nav__cta">.*?</a>)', switcher_html, content, flags=re.DOTALL)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Update index.html and dish.html
update_file("D:/VIBE CODING/Khandesh Kitchen/index.html")
update_file("D:/VIBE CODING/Khandesh Kitchen/dish.html")

# Update CSS
with open("D:/VIBE CODING/Khandesh Kitchen/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()
if "lang-switch" not in css:
    css += "\n" + css_to_inject
    with open("D:/VIBE CODING/Khandesh Kitchen/css/style.css", "w", encoding="utf-8") as f:
        f.write(css)

# Update JS
with open("D:/VIBE CODING/Khandesh Kitchen/js/main.js", "r", encoding="utf-8") as f:
    js = f.read()
if "langSwitch" not in js:
    js += "\n" + js_to_inject
    with open("D:/VIBE CODING/Khandesh Kitchen/js/main.js", "w", encoding="utf-8") as f:
        f.write(js)

print("Translation setup complete.")
