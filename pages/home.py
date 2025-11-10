import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CropGuru AI", layout="wide")

# --- CSS Styling ---
hide_streamlit_elements = """
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_elements, unsafe_allow_html=True)
st.markdown("""
<style>
  .stApp, .main {
    background: #f0f7f1 !important;
    color: #1b3d17 !important;
    forced-color-adjust: none !important;
    -webkit-forced-color-adjust: none !important;
}
    .stApp {
    min-height: 70vh !important;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding-bottom: 0 !important;
    margin-bottom: 0 !important;
}
:root {
    color-scheme: light !important;
}
body {
    background: #f0f7f1 !important;
    color: #1b3d17 !important;
    margin: 0;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    forced-color-adjust: none !important;
    -webkit-forced-color-adjust: none !important;
}

  /* Reset and base */
  * {box-sizing: border-box;}
  body {margin:0; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f0f7f1; color:#1b3d17;}
  /* Navbar */
  nav {
    position: fixed; top: 0; left: 0; right: 0; height: 56px;
    background: #1b3d17; display: flex; align-items: center; justify-content: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    border-radius: 0 0 12px 12px; z-index: 1000;
  }
  nav ul {
    display: flex; gap: 2rem; padding: 0; margin: 0; list-style: none;
  }
  nav li {
    display: flex; align-items: center; color:white; font-weight:600;
    font-size:1rem; cursor:pointer; user-select:none; transition: color 0.3s;
  }
  nav li:hover {color:#90ee90;}
  nav li svg {
    width:18px; height:18px; margin-right:6px; fill: white; transition: fill 0.3s;
  }
  nav li:hover svg {fill: #90ee90;}
  /* Hero Section */
  .hero {
    margin: 0px 30px 20px; position: relative; height: 320px;
    border-radius: 16px; overflow: hidden;
    box-shadow: 0 8px 20px rgba(27, 61, 23, 0.3);
    background: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1400&q=80') center/cover no-repeat;
  }
  .hero::after {
    content: ''; position: absolute; inset: 0;
    background: linear-gradient(180deg, rgba(27, 61, 23, 0.3), rgba(27, 61, 23, 0.6));
    pointer-events: none; animation: fadeIn 2s ease forwards; opacity: 0;
  }
  .hero-text {
    position: absolute; top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    color: #e0f2e0; font-size: 2rem; font-weight: 700; text-align: center;
    text-shadow: 0 0 8px rgba(144,238,144,0.7);
    animation: fadeInText 3s ease forwards; opacity: 0;
  }
  
            
  @keyframes fadeIn { to {opacity: 1;} }
  @keyframes fadeInText { to {opacity: 1; transform: translateY(0);} }
  /* Main Title */
  .main-title {
    text-align: center; font-family: 'Poppins', sans-serif;
    font-size: 3.2rem; font-weight: 800; letter-spacing: 0.2rem;
    color: #1b3d17; margin: 0 0 1rem; position: relative;
  }
  .main-title::after {
    content: ''; display: block; width: 120px; height: 4px;
    background-color: #459d4b; margin: 0.5rem auto 0; border-radius: 3px;
  }
  /* Summary */
  .summary {
    max-width: 900px; margin: 0 auto 2rem;
    background: #dcedc8; border-radius: 12px; padding: 1.25rem 1.5rem;
    display: flex; align-items: center; gap: 12px;
    font-weight: 600; color: #2f4f2f;
    box-shadow: 0 4px 12px rgba(115, 141, 94, 0.15);
  }
  .summary svg {
    width: 28px; height: 32px; fill: #61892f; flex-shrink: 0;
  }
  /* Carousel container */
  .carousel-container {
    position: relative;
    max-width: 1000px;
    margin: auto;
  }
  .carousel-wrapper {
    display: flex;
    overflow-x: auto;
    scroll-behavior: smooth;
    gap: 24px;
    padding: 0 0.5rem;
  }
  /* Each card */
  .module-card {
    background: white;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(55, 105, 43, 0.15);
    border-top: 5px solid #459d4b;
    flex: 0 0 280px;
    padding: 20px 24px;
    transition: box-shadow 0.3s ease, transform 0.3s ease;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    height: 300px;
  }
  .module-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 30px rgba(97, 157, 75, 0.5);
  }
  .module-card img {
    width: 100%;
    height: 140px;
    object-fit: cover;
    margin-bottom: 15px;
    border-radius: 12px;
  }
  .module-title {
    font-size: 1.3rem;
    font-weight: 700;
    color: #2b5133;
    margin-bottom: 8px;
  }
  .module-desc {
    font-size: 0.95rem;
    color: #516b3f;
    flex-grow: 1;
  }
  .explore-btn {
    margin-top: 12px;
    align-self: flex-end;
    background: transparent;
    border: none;
    color: #459d4b;
    font-weight: 700;
    font-size: 0.95rem;
    transition: color 0.3s ease;
    cursor: pointer;
    padding: 0;
  }
  .explore-btn:hover {
    color: #2b5133;
    text-decoration: underline;
  }
  /* Arrows */
  .arrow-btn {
    position: absolute;
    top: 45%;
    background: #81c784;
    border-radius: 50%;
    border: none;
    width: 38px;
    height: 38px;
    cursor: pointer;
    box-shadow: 0 2px 8px rgba(0,0,0,0.25);
    transition: background 0.3s ease;
    color: white;
    font-weight: bold;
    font-size: 1.5rem;
    user-select: none;
    z-index: 10;
  }
  .arrow-btn:hover {
    background: #4caf50;
  }
  .arrow-left {
    left: -50px;
  }
  .arrow-right {
    right: -50px;
  }
  /* Responsive */
  @media (max-width: 700px) {
    .arrow-left { left: -35px; }
    .arrow-right { right: -35px; }
    .module-card { flex: 0 0 220px; }
  }

  /* Footer */
  footer {
            height:200px;
    background:  #1b3d17; text-align: center;
    padding: 1rem 1rem 1.5rem; border-radius: 15px 15px 15px 15px;
    font-weight: 600; color: #4b6047;
    box-shadow: inset 0 6px 12px rgba(0,0,0,0.05);
    margin-top: 2rem; /* smaller space above footer */
    margin-bottom: 0;
  }

  }
  .footer-content {
    max-width: 1100px; margin: 0 auto;
    display: flex; justify-content: center; align-items: center; gap: 1rem;
    flex-wrap:wrap;
  }
  .social-icons svg {
    width: 22px; height: 22px; fill: #4b6047; cursor: pointer;
    transition: fill 0.3s ease;
  }
  .social-icons svg:hover {
    fill: #2b5133;
  }
</style>
""", unsafe_allow_html=True)

# Navbar
st.markdown("""
            <style>
 nav ul {
    list-style: none;
    padding: 0;
    margin: 0;
    background-color: #1b3d17;
    display: flex;
    gap: 1.5rem;
    border-radius: 8px;
    justify-content: center;
    align-items: center; /* vertically center items in the flex container */
    height: 50px;         /* consistent navbar height */
}

nav ul li {
    display: flex;
    align-items: center;  /* vertically center content inside list items */
}

nav ul li a {
    text-decoration: none !important;
    color: white !important;
    font-weight: 600;
    display: flex;
    align-items: center;  /* vertically center icon + text */
    gap: 0.5rem;
    padding: 0 12px;
    height: 40px;          /* consistent clickable area */
    line-height: 40px;     /* vertically align text */
    font-size: 16px;
    transition: color 0.3s ease, transform 0.3s ease;
    white-space: nowrap;   /* prevent wrapping */
}

nav ul li a svg {
    height: 24px;          /* slightly larger icon */
    width: 24px;
    fill: currentColor;    /* match icon color to text */
    transition: transform 0.3s ease;
}

nav ul li a:hover {
    color: #78be20 !important;
}

nav ul li a:hover,
nav ul li a:focus {
    border-bottom: 3px solid #fbc531; /* Bright yellow accent, you can change */
}
            
nav ul li a:hover svg {
    transform: scale(1.1);
    filter: drop-shadow(0 0 4px #78be20);
}

</style>
<nav>
  <ul>
    <li><a href="/home"><svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>Home</a></li>
    <li><a href="/crop_recommendation"><svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14l7-3 7 3V5c0-1.1-.9-2-2-2z"/></svg>Crop Recommendation Module</a></li>
    <li><a href="/crop_alternatives"><svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm1 15h-2v-2h2zm0-4h-2V7h2z"/></svg>Crop Alternatives</a></li>
    <li><a href="/crop_profit_estimation"><svg viewBox="0 0 24 24">
      <path fill="currentColor" d="M3 3h2v18H3V3zm4 6h2v12H7V9zm4-4h2v16h-2V5zm4 8h2v8h-2v-8zm4-6h2v14h-2V7z"/>
    </svg>Profit Estimation</a></li>
    <li><a href="/price_forecast"><svg viewBox="0 0 24 24">
      <path fill="currentColor" d="M3 17l6-6 4 4 8-8v6h2V5h-8v2h6l-7 7-4-4-7 7z"/>
    </svg>Price Forecasting</a></li>
    <li><a href="/farmer_support_ai"><svg viewBox="0 0 24 24"><path d="M21 8V7l-3 2-2-2v6l2-2 3 2v-1zM3 14v-4h6v4H3z"/></svg>Farmer Help AI</a></li>
    <li><a href="/contact"><svg viewBox="0 0 24 24"><path d="M21 8V7l-3 2-2-2v6l2-2 3 2v-1zM3 14v-4h6v4H3z"/></svg>Contact</a></li>
    <li><a href="/help"><svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm1 15h-2v-2h2zm0-4h-2V7h2z"/></svg>Help</a></li>
  </ul>
</nav>

""", unsafe_allow_html=True)

# Hero
st.markdown('<section class="hero"><div class="hero-text">Empowering Farmers with AI</div></section>', unsafe_allow_html=True)



#title 
st.markdown("""
<h1 style="
  font-family: 'Poppins'; 
  background: linear-gradient(90deg, #2E7D32, #66BB6A); /* Green gradient on text */
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
  text-align: center;  /* Center the text */
">
  CropGuru AI 🌱
</h1>
""", unsafe_allow_html=True)


# Summary
st.markdown(""" <div class="summary"> <svg viewBox="0 0 24 24" aria-hidden="true" style="width:30px;height:28px;fill:#61892f;margin-right:12px;"><path d="M16 4s5 3 5 8-3 8-8 8-8-3-8-8 3-8 8-8zm0 0l-2 6"/></svg>
                 From seeds to profits  –  CropGuru AI guides you with smart crop recommendations , accurate price forecasts , profit estimation , and actionable agricultural insights to help you make informed decisions and maximize your farm’s potential. 🌱📈            </div> """, unsafe_allow_html=True)


# Module Images and Details (replace icons with realistic images)
modules = [
    {
        "title": "Crop Recommendation",
        "desc": "Get best crops suited for your soil & climate.",
        "image": "https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=600&q=80"
    },
    {
        "title": "Crop Alternatives",
        "desc": "Find alternative crops to maximize yield.",
        "image": "https://plus.unsplash.com/premium_photo-1754211641955-28213db72d40?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1245"
    },
    {
        "title": "Crop Profit Estimation",
        "desc": "Estimate profits based on market trends.",
        "image": "https://images.unsplash.com/photo-1635236190542-d43e4d4b9e4b?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8cHJvZml0fGVufDB8fDB8fHww&auto=format&fit=crop&q=60&w=1000"
    },
    {
        "title": "Price Forecast",
        "desc": "Predict commodity prices using AI.",
        "image": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=600&q=80"
    },
    {
        "title": "Farmer Support AI",
        "desc": "AI-driven support for farming queries.",
        "image": "https://images.unsplash.com/photo-1528825871115-3581a5387919?auto=format&fit=crop&w=600&q=80"
    }
]

carousel_html = '''
<style>
  .carousel-container {
    position: relative;
    max-width: 1050px;
    height: 440px;
    margin: auto;
  }
  .carousel-wrapper {
    display: flex;
    overflow-x: auto;
    scroll-behavior: smooth;
    gap: 24px;
    padding: 0 0.5rem;
  }
  .module-card {
    background: white;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(55, 105, 43, 0.15);
    border-top: 5px solid #459d4b;
    border-bottom: 1px solid transparent; 
    flex: 0 0 280px;
    padding: 20px 24px;
    transition: box-shadow 0.3s ease, transform 0.3s ease;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    height: 300px;
  }
  .module-card img {
    width: 100%;
    height: 140px;
    object-fit: cover;
    margin-bottom: 15px;
    border-radius: 12px;
  }
  .module-title {
    font-size: 1.3rem;
    font-weight: 700;
    color: #2b5133;
    margin-bottom: 8px;
  }
  .explore-btn {
    margin-top: 12px;
    align-self: flex-end;
    background: transparent;
    border: none;
    color: #459d4b;
    font-weight: 700;
    font-size: 0.95rem;
    cursor: pointer;
  }
  .arrow-btn {
    position: absolute;
    top: 45%;
    background: #81c784;
    border-radius: 50%;
    border: none;
    width: 38px;
    height: 38px;
    cursor: pointer;
    color: white;
    font-weight: bold;
    font-size: 1.5rem;
    z-index: 10;
  }
  .arrow-left { left: -50px; }
  .arrow-right { right: -50px; }
</style>

<div class="carousel-container">
  <button class="arrow-btn arrow-left" onclick="scrollLeft()">&#8249;</button>
  <button class="arrow-btn arrow-right" onclick="scrollRight()">&#8250;</button>
  <div class="carousel-wrapper" id="carousel">
'''


for mod in modules:
    page_slug = mod['title'].lower().replace(' ', '_')  # e.g., 'crop_recommendation'
    carousel_html += f'''
        <div class="module-card" tabindex="0" role="button" aria-label="{mod['title']} Module">
            <img src="{mod['image']}" alt="{mod['title']} Image"/>
            <div class="module-title">{mod['title']}</div>
            <div class="module-desc">{mod['desc']}</div>
            <a href="/crop_recommendation"  class="explore-btn">Explore →</a>

        </div>
    '''




carousel_html += '''
  </div>
</div>

<script>
const carousel = document.getElementById("carousel");
const cards = carousel.querySelectorAll('.module-card');

// Get the full scroll distance for one card including gap
function getScrollAmount() {
    if (cards.length === 0) return 0;
    const style = window.getComputedStyle(cards[0]);
    const gap = 24; // your CSS gap
    return cards[0].offsetWidth + gap;
}

function scrollLeft() {
    const scrollAmount = getScrollAmount();
    carousel.scrollLeft = Math.max(0, carousel.scrollLeft - scrollAmount);
}

function scrollRight() {
    const scrollAmount = getScrollAmount();
    const maxScroll = carousel.scrollWidth - carousel.clientWidth;
    carousel.scrollLeft = Math.min(maxScroll, carousel.scrollLeft + scrollAmount);
}
</script>


'''


components.html(carousel_html, height=320, scrolling=False)

# Footer
st.markdown("""
<footer>
  <div class="footer-content">
    <div class="social-icons">
      <svg viewBox="0 0 24 24" aria-label="Twitter"><path d="M22.46 6c-.77.35-1.6.59-2.47.69a4.28 4.28 0 0 0 1.88-2.37c-.83.5-1.75.85-2.72 1.04a4.27 4.27 0 0 0-7.3 3.9A12.09 12.09 0 0 1 3.15 4.7a4.28 4.28 0 0 0 1.32 5.7c-.7 0-1.35-.2-1.93-.5v.05a4.27 4.27 0 0 0 3.43 4.18c-.3.08-.6.12-.94.12-.23 0-.45-.03-.67-.07a4.28 4.28 0 0 0 3.99 2.97 8.6 8.6 0 0 1-5.3 1.83c-.34 0-.67-.02-1-.06a12.14 12.14 0 0 0 6.56 1.92c7.88 0 12.2-6.54 12.2-12.2 0-.19 0-.37-.02-.55A8.62 8.62 0 0 0 24 4.57a8.5 8.5 0 0 1-2.54.7z"/></svg>
      <svg viewBox="0 0 24 24" aria-label="Facebook"><path d="M22 12c0-5.52-4.48-10-10-10S2 6.48 2 12c0 4.99 3.66 9.13 8.44 9.88v-6.99h-2.54v-2.89h2.54v-2.2c0-2.51 1.5-3.89 3.8-3.89 1.1 0 2.25.2 2.25.2v2.49h-1.26c-1.25 0-1.64.78-1.64 1.57v1.84h2.8l-.45 2.89h-2.35v6.99C18.34 21.13 22 16.99 22 12"/></svg>
      <svg viewBox="0 0 24 24" aria-label="LinkedIn"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7H10v-7a6 6 0 0 1 6-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg>
    </div>
  </div>
</footer>
""", unsafe_allow_html=True)