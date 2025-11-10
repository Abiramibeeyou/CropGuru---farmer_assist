# 🌾 **Intelligent Price Forecasting Using Agricultural Products (ML + Streamlit)**

An AI-powered agriculture decision support system that helps farmers make informed decisions through crop recommendation, alternative crop suggestions, profit estimation, agricultural advisory, and price forecasting using machine learning and deep learning models.

## 🚀 Project Overview

This project is a Streamlit-based web application designed to support farmers with intelligent insights by integrating multiple machine learning models, APIs, and interactive dashboards. It includes:

Crop recommendation using soil & climate features

Alternative crop suggestions using similarity ranking

Profit estimation using live market prices (AGMARKNET API)

AI farming assistant (Google Gemini API)

Price forecasting using LSTM models

Fully interactive UI with charts, insights, and downloadable results

# 🧩 Modules in the Application
## 🔹 1. Home Page

Provides an overview of the system, purpose, modules, and easy navigation.

## 🌱 2. Crop Recommendation

Uses the Crop Recommendation Dataset containing:

N (Nitrogen)

P (Phosphorus)

K (Potassium)

Temperature

Humidity

pH

Rainfall

Label (22 crops)

Models Implemented

Logistic Regression

SVM

Decision Tree

Gradient Boosting

Random Forest

KNN

Naive Bayes

✔ Random Forest achieved the best accuracy and is saved & used for final predictions.

## 🌾 3. Alternative Crop Suggestion

Suggests top 3 alternative crops based on:

Euclidean Distance similarity

Comparison with recommended crop features

Ranking crops in descending order (most similar crops first)

This helps farmers choose backup or alternative crops based on soil and weather conditions.

## 💰 4. Profit Estimation

Estimates potential profit using:

Current market price (via AGMARKNET API)

### User inputs:

Cultivation cost

Yield

Recommended crop

Alternative crops

### Outputs total expected profit for each crop and compares profitability.

## 🤖 5. Farmer Support – AI Agricultural Advisor

Uses Google Gemini API to answer:

Farming related queries

Soil & pesticide guidance

Seed selection

Crop diseases & treatments

Best practices for farming

Acts as an intelligent chatbot for farmers.

## 📈 6. Price Forecasting (LSTM Deep Learning Model)

### Dataset Columns:

Month

Commodity Name

avg_modal_price

avg_min_price

avg_max_price

State Name

District Name

CalculationType

Change

### Features:

Select crop and any market in India

Forecast period: 3, 6, or 9 months

LSTM model trained for multiple commodities

### Outputs:

Interactive Forecast Dashboard

Next-month price trend (Rising/Falling)

Confidence Range

Downloadable forecast visualizations

## 🛠 Tech Stack
Frontend & App

### Streamlit

HTML/CSS (custom styling)

### Machine Learning

Scikit-learn

Random Forest

Gradient Boosting

Logistic Regression

SVM

Decision Tree

### Deep Learning

TensorFlow

Keras (LSTM model)

### APIs

AGMARKNET API (Real-time crop market price data)

Google Gemini API (AI Advisor)

### Visualization

Plotly

Matplotlib

Seaborn

## Project Structure

```
project/
│── app.py
│── pages/
│── models/
│── data/
│── assets/
│── requirements.txt
│── README.md
```

## ▶️ How to Run Locally
1️⃣ Clone the repo
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo

## 2️⃣ Install dependencies
pip install -r requirements.txt

## 3️⃣ Run the Streamlit app
streamlit run app.py

## 🌐 Deployment

This app is designed to run smoothly on:

Streamlit Cloud

Local machine

## 📦 Future Enhancements

Add dynamic soil & weather API integration

Mobile-friendly UI

Add yield prediction using ML

Add automated report generation for farmers

## ❤️ Contributors

Abirami Balakrishnan

SriDurga Angusamy

## 📜 License

This project is open for educational and research purposes.
