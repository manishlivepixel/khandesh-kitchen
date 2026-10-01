const i18n = {
  "Home": { "en": "Home", "mr": "मुख्य पृष्ठ", "hi": "होम" },
  "About": { "en": "About", "mr": "आमच्याबद्दल", "hi": "हमारे बारे में" },
  "Menu": { "en": "Menu", "mr": "मेनू", "hi": "मेनू" },
  "Gallery": { "en": "Gallery", "mr": "गॅलरी", "hi": "गैलरी" },
  "Visit Us": { "en": "Visit Us", "mr": "भेट द्या", "hi": "हमसे मिलें" },
  "📞 Order on Call": { "en": "📞 Order on Call", "mr": "📞 ऑर्डर करण्यासाठी कॉल करा", "hi": "📞 कॉल पर ऑर्डर करें" },
  "Newly Opened in Badlapur": { "en": "Newly Opened in Badlapur", "mr": "बदलापूरमध्ये नव्याने सुरू", "hi": "बदलापुर में नया खुला है" },
  "Authentic Khandeshi Flavors": { "en": "Authentic Khandeshi Flavors", "mr": "अस्सल खान्देशी चव", "hi": "असली खान्देशी स्वाद" },
  "Experience the fiery, rustic, and soulful taste of Jalgaon right here in Badlapur.": { "en": "Experience the fiery, rustic, and soulful taste of Jalgaon right here in Badlapur.", "mr": "जळगावची झणझणीत, अस्सल आणि गावरान चव आता बदलापूरमध्ये अनुभवा.", "hi": "जलगाँव का तीखा, असली और देसी स्वाद अब बदलापुर में अनुभव करें।" },
  "Explore Menu": { "en": "Explore Menu", "mr": "मेनू पहा", "hi": "मेनू देखें" },
  "Book a Table": { "en": "Book a Table", "mr": "टेबल बुक करा", "hi": "टेबल बुक करें" },
  "Why Khandesh Kitchen?": { "en": "Why Khandesh Kitchen?", "mr": "खान्देश किचन का?", "hi": "खान्देश किचन क्यों?" },
  "Authentic Spices": { "en": "Authentic Spices", "mr": "अस्सल मसाले", "hi": "असली मसाले" },
  "We source our black spices directly from Jalgaon to maintain the true, fiery Khandeshi flavor.": { "en": "We source our black spices directly from Jalgaon to maintain the true, fiery Khandeshi flavor.", "mr": "खरा, झणझणीत खान्देशी स्वाद टिकवण्यासाठी आम्ही आमचे काळे मसाले थेट जळगावहून आणतो.", "hi": "असली, तीखा खान्देशी स्वाद बनाए रखने के लिए हम अपने काले मसाले सीधे जलगाँव से मंगाते हैं।" },
  "Traditional Cooking": { "en": "Traditional Cooking", "mr": "पारंपारिक स्वयंपाक", "hi": "पारंपरिक खाना पकाना" },
  "Prepared using slow-cooking methods and age-old recipes passed down through generations.": { "en": "Prepared using slow-cooking methods and age-old recipes passed down through generations.", "mr": "पिढ्यानपिढ्या चालत आलेल्या जुन्या पाककृती आणि संथ-शिजवण्याच्या पद्धती वापरून तयार केलेले.", "hi": "पीढ़ियों से चली आ रही पुरानी रेसिपी और धीमी आंच पर पकाने के तरीकों का उपयोग करके तैयार किया गया।" },
  "Homestyle Warmth": { "en": "Homestyle Warmth", "mr": "घरगुती आपुलकी", "hi": "घरेलू गर्माहट" },
  "Every dish is made with love, ensuring it feels like a comforting meal right at home.": { "en": "Every dish is made with love, ensuring it feels like a comforting meal right at home.", "mr": "प्रत्येक पदार्थ प्रेमाने बनवला जातो, ज्यामुळे तुम्हाला अगदी घरच्या जेवणासारखा आराम मिळतो.", "hi": "हर व्यंजन प्यार से बनाया जाता है, जिससे आपको बिल्कुल घर के खाने जैसा सुकून मिलता है।" },
  "Our Grand Opening": { "en": "Our Grand Opening", "mr": "आमचे भव्य उद्घाटन", "hi": "हमारा भव्य उद्घाटन" },
  "Glimpses of Khandesh": { "en": "Glimpses of Khandesh", "mr": "खान्देशची झलक", "hi": "खान्देश की झलक" },
  "Open Daily": { "en": "Open Daily", "mr": "दररोज उघडे", "hi": "रोजाना खुला" },
  "11:00 AM - 11:00 PM": { "en": "11:00 AM - 11:00 PM", "mr": "सकाळी 11:00 - रात्री 11:00", "hi": "सुबह 11:00 - रात 11:00" },
  "Call Us": { "en": "Call Us", "mr": "आम्हाला कॉल करा", "hi": "हमें कॉल करें" },
  "Contact": { "en": "Contact", "mr": "संपर्क", "hi": "संपर्क" },
  "Hours": { "en": "Hours", "mr": "वेळ", "hi": "समय" },
  "Follow Us": { "en": "Follow Us", "mr": "फॉलो करा", "hi": "फॉलो करें" },
  "← Back to Menu": { "en": "← Back to Menu", "mr": "← मेनूकडे परत", "hi": "← मेनू पर वापस" }
};

function initTranslation() {
  const langSwitch = document.getElementById('langSwitch');
  if(!langSwitch) return;
  
  const savedLang = localStorage.getItem('site_lang') || 'en';
  langSwitch.value = savedLang;

  function applyLanguage(lang) {
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (i18n[key] && i18n[key][lang]) {
        el.innerText = i18n[key][lang];
      }
    });
    localStorage.setItem('site_lang', lang);
  }

  // Apply on load
  applyLanguage(savedLang);

  // Apply on change
  langSwitch.addEventListener('change', (e) => {
    applyLanguage(e.target.value);
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initTranslation);
} else {
  initTranslation();
}
