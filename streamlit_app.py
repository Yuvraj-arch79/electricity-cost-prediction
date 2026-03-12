import streamlit as st
import requests

st.title("Electricity Cost Prediction")

site_area = st.number_input("Site Area")
water_consumption = st.number_input("Water Consumption")
resident_count = st.number_input("Resident Count")
utilisation_rate = st.number_input("Utilisation Rate")

structure_type = st.selectbox(
    "Structure Type",
    ["Commercial","Industrial","Mixed-use","Residential"]
)

if st.button("Predict"):

    url = "http://127.0.0.1:8000/predict"

    data = {
        "site_area": site_area,
        "water_consumption": water_consumption,
        "resident_count": resident_count,
        "utilisation_rate": utilisation_rate,
        "structure_type": structure_type
    }

    response = requests.post(url, json=data)

    result = response.json()

    st.success(f"Predicted Electricity Cost: {result['predicted_electricity_cost']}")