import streamlit as st
import numpy as np
import joblib
# Navbar
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
</style>
""", unsafe_allow_html=True)
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
st.markdown("""
<style>
/* Basic button style matching navbar colors */
div.stButton > button {
    background-color: #1b3d17 !important;  /* navbar dark green */
    color: #f0f7f1 !important;             /* light text */
    border: 2px solid #78be20 !important;  /* bright green border */
    border-radius: 8px !important;
    padding: 10px 30px !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    transition: background-color 0.3s ease, color 0.3s ease;
    cursor: pointer;
    box-shadow: none !important;
    min-width: 160px;
}

/* Hover effect */
div.stButton > button:hover {
    background-color: #78be20 !important;  /* bright green background */
    color: #1b3d17 !important;             /* dark text */
    border-color: #f0f7f1 !important;      /* light border */
    box-shadow: 0 0 8px #78be20 !important;
}

/* Focus effect */
div.stButton > button:focus {
    outline: none !important;
    box-shadow: 0 0 12px #78be20 !important;
}
</style>
""", unsafe_allow_html=True)
@st.cache_resource
def load_model():
    # Load model, label encoder, and scaler
    model = joblib.load('utils/best_crop_model.pkl')
    le = joblib.load('utils/label_encoder.pkl')
    scaler = joblib.load('utils/scaler.pkl')
    return model, le, scaler

def main():
    st.title("Crop Recommendation")

    st.write("Enter your soil and environmental parameters:")

    N = st.number_input("Nitrogen (N)", min_value=0, max_value=10000, value=50)
    P = st.number_input("Phosphorus (P)", min_value=0, max_value=10000, value=50)
    K = st.number_input("Potassium (K)", min_value=0, max_value=10000, value=50)
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
    ph = st.number_input("pH level", min_value=0.0, max_value=14.0, value=7.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=5000.0, value=100.0)

    if st.button("Recommend Crop"):
        model, le, scaler = load_model()
        
        # Convert and scale input features
        input_features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        scaled_features = scaler.transform(input_features)

        # Predict
        prediction_encoded = model.predict(scaled_features)
        predicted_crop = le.inverse_transform(prediction_encoded)[0]

        st.success(f"Recommended Crop: {predicted_crop}")
        st.session_state['recommended_crop'] = predicted_crop

if __name__ == "__main__":
    main()
