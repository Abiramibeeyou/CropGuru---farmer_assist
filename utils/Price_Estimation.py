import requests
import pandas as pd
import streamlit as st

# Secure key from Streamlit secrets
AGMARK_API_KEY = st.secrets["agmarknet_api_key"]

def get_crop_prices(commodity):
    """Fetch average commodity price (₹/quintal) from Agmarknet API."""
    url = (
        "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
        f"?api-key={AGMARK_API_KEY}"
        "&format=json"
        f"&filters[commodity]={commodity}"
        "&limit=5"
    )
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "records" in data and data["records"]:
            price = float(data["records"][0]["modal_price"])
            return price
        else:
            print(f"No price data found for {commodity}")
            return None
    except Exception as e:
        print(f"Error fetching crop price: {e}")
        return None

def estimate_profit(yield_per_hectare, area, price_per_quintal, cost_per_hectare):
    """Compute total and per-hectare profit for given crop data."""
    total_yield = yield_per_hectare * area
    total_income = total_yield * price_per_quintal  # ₹
    total_cost = area * cost_per_hectare
    total_profit = total_income - total_cost
    profit_per_hectare = total_profit / area if area > 0 else 0

    return {
        "Total Yield (q)": total_yield,
        "Total Income (₹)": total_income,
        "Total Cost (₹)": total_cost,
        "Total Profit (₹)": total_profit,
        "Profit/ha (₹)": profit_per_hectare
    }

def comparative_profit_analysis(crop_data, area):
    """
    Compare profit of multiple crops based on yield, area, cost & live Agmarknet prices.
    crop_data: list of dicts [{name, yield, cost}]
    """
    results = []
    for crop in crop_data:
        price = get_crop_prices(crop["name"])
        if price:
            metrics = estimate_profit(
                yield_per_hectare=crop["yield"],
                area=area,
                price_per_quintal=price,
                cost_per_hectare=crop["cost"]
            )
            results.append({
                "Crop": crop["name"].capitalize(),
                "Price (₹/q)": price,
                "Yield (q/ha)": crop["yield"],
                "Cultivation Cost/ha (₹)": crop["cost"],
                "Area (ha)": area,
                **metrics
            })
        else:
            print(f"Skipping {crop['name']}: no price data found.")

    if not results:
        print("⚠️ No crop price data retrieved from Agmarknet API.")
        return pd.DataFrame()

    df = pd.DataFrame(results).sort_values(by="Total Profit (₹)", ascending=False)
    return df.reset_index(drop=True)

# Example usage block
if __name__ == "__main__":
    crops = [
        {"name": "Banana", "yield": 32, "cost": 15000},
        {"name": "Rice", "yield": 40, "cost": 12000},
        {"name": "Maize", "yield": 35, "cost": 11000}
    ]
    user_area = 2.5
    profit_table = comparative_profit_analysis(crops, user_area)
    print("\nComparative Profit Estimation (with Cultivation Cost):")
    print(profit_table)
