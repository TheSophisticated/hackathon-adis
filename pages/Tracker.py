import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

bg_img = """
<style>
[data-testid = 'stAppViewContainer']{
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center center;
  background-repeat: repeat;
  background-image: url("data:image/svg+xml;utf8,%3Csvg width=%222000%22 height=%221400%22 xmlns=%22http:%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cdefs%3E%3ClinearGradient id=%22a%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%2388d7e0%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23a5e1e7%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22b%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23a7dbd8%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23bde4e1%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22c%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23c4e0d2%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23d2e7dd%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22d%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23e0e4cc%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23e7ead8%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22e%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23eab57e%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23efc79e%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22f%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23f38630%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23f6a463%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22g%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23f77818%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23f99951%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22h%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23fa6900%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23fb8e3f%22%2F%3E%3C%2FlinearGradient%3E%3C%2Fdefs%3E%3Cpath fill=%22%2369d2e7%22 d=%22M0 0h2000v1400H0z%22%2F%3E%3Cpath d=%22M0 155c120.276-4.041 240.553-8.082 352-12 111.447-3.918 214.065-7.711 326-11 111.935-3.289 233.187-6.072 337 0 103.813 6.072 190.187 20.999 299 32 108.813 11.001 240.065 18.077 365 12 124.935-6.077 243.553-25.308 296-31s38.724 2.154 65 10l-40 1245H0Z%22 fill=%22url(%23a)%22%2F%3E%3Cpath d=%22M0 311c103.233 8.786 206.466 17.572 318 19 111.534 1.428 231.37-4.502 341-11s209.053-13.564 321-10 236.419 17.76 353 16c116.581-1.76 225.272-19.474 345-28 119.728-8.526 250.494-7.865 306-4s35.753 10.932 56 18l-40 1089H0Z%22 fill=%22url(%23b)%22%2F%3E%3Cpath d=%22M0 466c101.58 1.485 203.16 2.97 317-1s239.942-13.393 355-7c115.058 6.393 219.074 28.603 329 29 109.926.397 225.764-21.017 331-22 105.236-.983 199.871 18.466 330 24 130.129 5.534 295.751-2.847 358-9 62.249-6.153 21.124-10.076 20-14l-40 934H0Z%22 fill=%22url(%23c)%22%2F%3E%3Cpath d=%22M0 622c96.562 2.019 193.124 4.037 308 7s248.064 6.87 368 6c119.936-.87 226.618-6.518 336-8 109.382-1.482 221.463 1.2 332 5s219.53 8.715 338 2 246.42-25.061 301-29c54.58-3.939 35.79 6.53 57 17l-40 778H0Z%22 fill=%22url(%23d)%22%2F%3E%3Cpath d=%22M0 777c102.843-2.594 205.685-5.189 316 0s228.102 18.16 345 23 232.906 1.548 346-5 223.273-16.353 328-17c104.727-.647 204.004 7.864 327 8 122.996.136 269.713-8.104 330-11 60.287-2.896 34.143-.448 48 2l-40 623H0Z%22 fill=%22url(%23e)%22%2F%3E%3Cpath d=%22M0 933c111.99 8.033 223.98 16.066 340 12 116.02-4.066 236.07-20.23 344-25s203.738 1.857 310 2c106.262.143 222.977-6.199 329-10s201.352-5.062 334 1 302.614 19.446 366 24c63.386 4.554 20.193.277 17-4l-40 467H0Z%22 fill=%22url(%23f)%22%2F%3E%3Cpath d=%22M0 1088c98.635 9.95 197.27 19.9 309 13 111.73-6.9 236.555-30.649 360-29 123.445 1.649 245.512 28.696 352 39 106.488 10.304 197.399 3.865 295-9s201.893-32.156 329-29c127.107 3.156 277.03 28.759 340 35 62.97 6.241 38.985-6.88 55-20l-40 312H0Z%22 fill=%22url(%23g)%22%2F%3E%3Cpath d=%22M0 1244c109.825 4.794 219.65 9.587 334 4s233.225-21.555 347-18c113.775 3.555 222.45 26.632 328 25 105.55-1.632 207.972-27.974 319-28 111.028-.026 230.661 26.262 362 34 131.339 7.738 274.382-3.075 328-9 53.618-5.925 17.809-6.963 22-8l-40 156H0Z%22 fill=%22url(%23h)%22%2F%3E%3C%2Fsvg%3E");
}
</style>
"""
st.markdown(bg_img, unsafe_allow_html=True)


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

if st.button("Back To Home"):
    switch_page("app")

# Define emission factors (example values, replace with accurate data)
EMISSION_FACTORS = {
    "India": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal, 2.5kgco2/kg
        "Waste": 0.1,  # kgCO2/kg
    },
    "UAE": {
        "Transportation": 0.3,  # kgCO2/km
        "Electricity": 0.95,  # kgCO2/kWh
        "Diet": 1.5,  # kgCO2/meal, 2.5kgco2/kg
        "Waste": 0.15,  # kgCO2/kg
    }
}

# Streamlit app code
st.title("Calculate Your Carbon Emissions 🌫️ ")

# User inputs
st.subheader("🌍 Your Country")
country = st.selectbox("Select", ["UAE", "India"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚗 Daily commute distance (in km)")
    distance = st.slider("Distance", 0.0, 500.0, key="distance_input")

    st.subheader("💡 Monthly electricity consumption (in kWh)")
    electricity = st.slider("Electricity", 0.0, 5000.0, key="electricity_input")

with col2:
    st.subheader("🍽️ Waste generated per week (in kg)")
    waste = st.slider("Waste", 0.0, 100.0, key="waste_input")

    st.subheader("🍽️ Number of meals per day")
    meals = st.number_input("Meals", 0, key="meals_input")

# Initialize variables for emissions
transportation_emissions = 0.0
electricity_emissions = 0.0
diet_emissions = 0.0
waste_emissions = 0.0

# Normalize inputs
if distance > 0:
    distance = distance * 365  # Convert daily distance to yearly
if electricity > 0:
    electricity = electricity * 12  # Convert monthly electricity to yearly
if meals > 0:
    meals = meals * 365  # Convert daily meals to yearly
if waste > 0:
    waste = waste * 52  # Convert weekly waste to yearly

# Calculate carbon emissions
if country in EMISSION_FACTORS:
    transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance
    electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity
    diet_emissions = EMISSION_FACTORS[country]["Diet"] * meals
    waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste

    # Convert emissions to tonnes and round off to 2 decimal points
    transportation_emissions = round(transportation_emissions / 1000, 2)
    electricity_emissions = round(electricity_emissions / 1000, 2)
    diet_emissions = round(diet_emissions / 1000, 2)
    waste_emissions = round(waste_emissions / 1000, 2)

    # Calculate total emissions
    total_emissions = round(
        transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
    )

    if st.button("Calculate CO2 Emissions"):
        # Display results
        st.header("Results")

        col3, col4 = st.columns(2)

        with col3:
            st.subheader("Carbon Emissions by Category")
            st.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2 per year")
            st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
            st.info(f"🍽️ Diet: {diet_emissions} tonnes CO2 per year")
            st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")

        with col4:
            st.subheader("Total Carbon Footprint")
            st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
            st.warning("In 2023, CO2 emissions per capita for UAE was 20.5 tons of CO2 per capita. Between 1972 and 2023, CO2 emissions per capita of UAE grew substantially from 4.2 to 20.5 tons of CO2 per capita rising at an increasing annual rate that reached a maximum of 10.33% in 2023")
else:
    st.warning("Please select a valid country from the dropdown.")
