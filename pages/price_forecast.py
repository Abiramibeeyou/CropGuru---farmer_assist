import streamlit as st
import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import plotly.graph_objects as go

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

# Load your full data CSV (assuming it has columns: month, commodity_name, avg_modal_price, ...)
@st.cache_data
def load_data():
    return pd.read_csv("data/crop_price_dataset.csv", parse_dates=['month'])

def forecast_prices(model, scaler, data, sequence_length, forecast_months):
    last_seq = data['avg_modal_price'].values[-sequence_length:].reshape(-1,1)
    scaled_seq = scaler.transform(last_seq)
    input_seq = scaled_seq.reshape((1, sequence_length, 1))
    preds = []
    for _ in range(forecast_months):
        pred_scaled = model.predict(input_seq)[0,0]
        preds.append(pred_scaled)
        input_seq = np.append(input_seq[:,1:,:], [[[pred_scaled]]], axis=1)
    preds = scaler.inverse_transform(np.array(preds).reshape(-1,1))
    return preds.flatten()

def plot_forecast(data, forecast, crop_name, forecast_months):
# Prepare forecast dates starting from the next period after last historical date
    forecast_dates = pd.date_range(data['month'].iloc[-1], periods=forecast_months+1, freq='ME')[1:]

# Combine the last historical data point with the forecast so lines connect
    connected_forecast_dates = pd.concat([
        pd.Series([data['month'].iloc[-1]]),
        pd.Series(forecast_dates)
    ], ignore_index=True)

    connected_forecast_values = np.concatenate([
        [data['avg_modal_price'].iloc[-1]],
        forecast
    ])

    # Plot using Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(
       x=data['month'],
       y=data['avg_modal_price'],
       mode='lines',
       name='Historical'
    ))
    fig.add_trace(go.Scatter(
        x=connected_forecast_dates,
        y=connected_forecast_values,
        mode='lines+markers',
        name='Forecast',
        line=dict(dash='dash')
    ))
    fig.update_layout(
        title=f'Crop Price Forecast for {crop_name}',
        xaxis_title='Date',
        yaxis_title='Price (₹/quintal)',
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)


def display_insights(forecast):
    next_price = forecast[0]
    trend = "🔺 Rising" if forecast[1] > forecast[0] else "🔻 Falling" if forecast[1] < forecast[0] else "➡️ Stable"
    conf_low = next_price * 0.95
    conf_high = next_price * 1.05
    st.markdown("### 🔍 Insights:")
    st.markdown(f"- Next month avg price: ₹{next_price:.2f}/qtl")
    st.markdown(f"- Expected trend: {trend}")
    st.markdown(f"- Confidence range: ₹{conf_low:.2f} – ₹{conf_high:.2f}")

def main():
    st.title("🌾 Crop Price Forecasting")

    data = load_data()
    crops = data['commodity_name'].unique()
    markets = ['All']  # Extend if you have market data by district/market

    # Selection widgets
    crop_selected = st.selectbox("Select Crop:", crops)
    market_selected = st.selectbox("Market:", markets, index=0)
    period_selected = st.selectbox("Forecast Period:", [3,6,12], index=1)+7

    # Filter data for selected crop and market
    filtered_data = data[(data['commodity_name'] == crop_selected)].sort_values('month')
    # Add filtering by market if data available


    if st.button("Predict 🔮"):
        # Load model and scaler
        model = load_model(f"models/{crop_selected}_lstm.h5")
        scaler = joblib.load(f"models/{crop_selected}_scaler.save")
        sequence_length = 2  # Use the window size you trained with
        
        forecast = forecast_prices(model, scaler, filtered_data, sequence_length, period_selected)
        
        plot_forecast(filtered_data, forecast, crop_selected, period_selected)
        display_insights(forecast+7)
        
        # Download forecast data
        df_forecast = pd.DataFrame({
            'Month': pd.date_range(filtered_data['month'].iloc[-1], periods=period_selected+1, freq='ME')[1:],
            'Forecasted Price': forecast
        })
        csv = df_forecast.to_csv(index=False)
        st.download_button("Download Forecast Data ⬇️", csv, "forecast.csv", "text/csv")

if __name__ == "__main__":
    main()
