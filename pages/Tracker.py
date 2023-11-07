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
  background-image: url("data:image/svg+xml;utf8,%3Csvg width=%222000%22 height=%221400%22 xmlns=%22http:%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cdefs%3E%3ClinearGradient id=%22a%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23eff8ef%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23f3f9f3%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22b%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23dff2df%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23e7f5e7%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22c%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23cfebce%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23dbf0da%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22d%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23bfe4be%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23cfeace%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22e%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23a7d4ab%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23bddec0%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22f%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%238fc398%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23abd2b1%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22g%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%2376b384%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%2398c6a2%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22h%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%235ea271%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%2386b994%22%2F%3E%3C%2FlinearGradient%3E%3C%2Fdefs%3E%3Cpath fill=%22%23fff%22 d=%22M0 0h2000v1400H0z%22%2F%3E%3Cpath d=%22M0 155c97.483 6.496 194.966 12.992 312 15 117.034 2.008 253.62-.472 366-2s200.555-2.103 310 0 240.16 6.883 349 3 195.803-16.43 314-19c118.197-2.57 267.628 4.837 331 7 63.372 2.163 40.686-.919 58-4l-40 1245H0Z%22 fill=%22url(%23a)%22%2F%3E%3Cpath d=%22M0 311c117.46-1.408 234.922-2.816 349 0s224.774 9.854 337 13c112.226 3.146 225.983 2.398 327-2s189.293-12.447 296-10c106.707 2.447 231.844 15.39 366 16 134.156.61 277.33-11.111 333-16 55.67-4.889 23.835-2.944 32-1l-40 1089H0Z%22 fill=%22url(%23b)%22%2F%3E%3Cpath d=%22M0 466c99.755-4.184 199.51-8.368 311-9 111.49-.632 234.715 2.289 347 8s213.629 14.213 324 11c110.371-3.213 229.77-18.14 342-22 112.23-3.86 217.293 3.345 341 4 123.707.655 266.06-5.241 325-5 58.94.241 34.47 6.62 50 13l-40 934H0Z%22 fill=%22url(%23c)%22%2F%3E%3Cpath d=%22M0 622c115.808 8.05 231.616 16.1 350 12 118.384-4.1 239.345-20.351 341-26 101.655-5.649 184.004-.696 292 3 107.996 3.696 241.638 6.135 359 6 117.362-.135 218.444-2.844 339-3 120.556-.156 260.588 2.241 317 4 56.412 1.759 29.206 2.88 42 4l-40 778H0Z%22 fill=%22url(%23d)%22%2F%3E%3Cpath d=%22M0 777c102.064-9.046 204.128-18.091 323-15 118.872 3.091 254.551 18.32 364 30 109.449 11.68 192.667 19.812 306 8 113.333-11.812 256.78-43.568 361-44 104.22-.432 169.213 30.46 289 32 119.787 1.54 294.368-26.274 363-33 68.632-6.726 31.316 7.637 34 22l-40 623H0Z%22 fill=%22url(%23e)%22%2F%3E%3Cpath d=%22M0 933c111.179 11.144 222.357 22.288 328 17s205.75-27.008 318-35c112.25-7.992 236.641-2.258 354 4 117.359 6.258 227.684 13.038 334 11 106.316-2.038 208.624-12.895 338-17s285.822-1.459 345 3 21.09 10.73 23 17l-40 467H0Z%22 fill=%22url(%23f)%22%2F%3E%3Cpath d=%22M0 1088c110.563-1.044 221.126-2.089 325-3s201.06-1.69 317-5 250.636-9.152 363-3c112.364 6.152 202.397 24.299 309 26 106.603 1.701 229.778-13.042 360-20s267.492-6.13 323-4c55.508 2.13 29.254 5.565 43 9l-40 312H0Z%22 fill=%22url(%23g)%22%2F%3E%3Cpath d=%22M0 1244c101.299 6.438 202.598 12.877 309 6 106.402-6.877 217.909-27.068 335-29 117.091-1.932 239.768 14.397 351 23s211.021 9.481 317 14c105.979 4.519 218.148 12.678 348 6 129.852-6.678 277.386-28.194 337-34 59.614-5.806 31.307 4.097 43 14l-40 156H0Z%22 fill=%22url(%23h)%22%2F%3E%3C%2Fsvg%3E");
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
st.title("Monitor your Ecological-Imapct 🌫️ ")

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
            st.subheader("Total Ecological-Imapct ")
            st.success(f"🌍 Your total Eco-Imapct is: {total_emissions} tonnes CO2 per year")
            st.warning("In 2023, CO2 emissions per capita for UAE was 20.5 tons of CO2 per capita. Between 1972 and 2023, CO2 emissions per capita of UAE grew substantially from 4.2 to 20.5 tons of CO2 per capita rising at an increasing annual rate that reached a maximum of 10.33% in 2023")
else:
    st.warning("Please select a valid country from the dropdown.")
