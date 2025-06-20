import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.pkl')

st.title("🌾 Smart Crop Recommendation System")

N = st.number_input('Nitrogen (N)')
P = st.number_input('Phosphorus (P)')
K = st.number_input('Potassium (K)')
temperature = st.number_input('Temperature (°C)')
humidity = st.number_input('Humidity (%)')
ph = st.number_input('Soil pH')
rainfall = st.number_input('Rainfall (mm)')

if st.button('Predict'):
    input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                              columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    result = model.predict(input_data)
    st.success(f"✅ Recommended Crop: {result[0]}")
