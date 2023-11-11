import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

<<<<<<< Updated upstream
st.set_page_config(initial_sidebar_state = 'collapsed')
=======
st.set_page_config(initial_sidebar_state='collapsed')
>>>>>>> Stashed changes

bg_img = """
<style>
[data-testid = 'stAppViewContainer']{
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center center;
  background-repeat: repeat;
  background-image: url("data:image/svg+xml;utf8,%3Csvg width=%222000%22 height=%221400%22 xmlns=%22http:%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cdefs%3E%3ClinearGradient id=%22a%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23d5ebd5%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23dff0df%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22b%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23c9e6c7%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23d6ecd5%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22c%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23bce2ba%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23cce9cb%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22d%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23afddac%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23c3e5c0%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22e%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23bfe1c1%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23cfe8d0%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22f%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23cfe5d6%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23dbebe0%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22g%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23dfe9ea%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23e7eeef%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22h%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23efedff%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23f3f1ff%22%2F%3E%3C%2FlinearGradient%3E%3C%2Fdefs%3E%3Cpath fill=%22%23e2efe2%22 d=%22M0 0h2000v1400H0z%22%2F%3E%3Cpath d=%22M0 155c114.554 8.572 229.108 17.145 346 17 116.892-.145 236.122-9.006 336-11 99.878-1.994 180.404 2.88 293-2s257.263-19.514 377-16c119.737 3.514 214.545 25.177 329 34 114.455 8.823 248.559 4.807 305-1s35.22-13.403 54-21l-40 1245H0Z%22 fill=%22url(%23a)%22%2F%3E%3Cpath d=%22M0 311c103.753-8.682 207.506-17.364 317-23 109.494-5.636 224.73-8.224 345 2 120.27 10.224 245.575 33.262 360 33 114.425-.262 217.97-23.823 325-26 107.03-2.177 217.547 17.03 337 17 119.453-.03 247.844-19.294 302-23 54.156-3.706 34.078 8.147 54 20l-40 1089H0Z%22 fill=%22url(%23b)%22%2F%3E%3Cpath d=%22M0 466c104.669-10.817 209.337-21.634 322-19 112.663 2.634 233.319 18.718 342 21 108.681 2.282 205.387-9.24 317-7s238.133 18.24 356 19c117.867.76 227.08-13.718 348-13 120.92.718 253.549 16.634 308 19 54.451 2.366 30.726-8.817 47-20l-40 934H0Z%22 fill=%22url(%23c)%22%2F%3E%3Cpath d=%22M0 622c119.4 10.374 238.8 20.748 342 19 103.2-1.748 190.202-15.616 304-20s254.393.718 368 5 200.224 7.746 309 6c108.776-1.746 239.709-8.7 367-10 127.291-1.3 250.94 3.057 302 4 51.06.943 29.53-1.529 48-4l-40 778H0Z%22 fill=%22url(%23d)%22%2F%3E%3Cpath d=%22M0 777c119.43-.148 238.861-.295 345-3 106.139-2.705 198.985-7.966 307-14 108.015-6.034 231.197-12.84 345-5s218.225 30.328 321 32c102.775 1.672 203.9-17.473 327-25 123.1-7.527 268.171-3.436 331 1 62.829 4.436 43.414 9.218 64 14l-40 623H0Z%22 fill=%22url(%23e)%22%2F%3E%3Cpath d=%22M0 933c98.413 5.874 196.826 11.747 312 13 115.174 1.253 247.108-2.115 369-6s233.742-8.287 336-8c102.258.287 194.925 5.262 300 2 105.075-3.262 222.559-14.763 351-12s267.84 19.79 325 24c57.16 4.21 32.08-4.395 47-13l-40 467H0Z%22 fill=%22url(%23f)%22%2F%3E%3Cpath d=%22M0 1088c121.334-2.593 242.668-5.186 349-9s197.663-8.85 304-2c106.337 6.85 227.679 25.584 342 27 114.321 1.416 221.622-14.486 327-20 105.378-5.514 208.832-.638 333 3s269.048 6.04 330 6c60.952-.04 37.976-2.52 55-5l-40 312H0Z%22 fill=%22url(%23g)%22%2F%3E%3Cpath d=%22M0 1244c120.994.67 241.989 1.341 353-5s212.04-19.694 311-14c98.96 5.694 195.854 30.435 312 34 116.146 3.565 251.544-14.044 370-16 118.456-1.956 219.969 11.743 338 12 118.031.257 252.58-12.926 308-17 55.42-4.074 31.71.963 48 6l-40 156H0Z%22 fill=%22url(%23h)%22%2F%3E%3C%2Fsvg%3E");}
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
<<<<<<< Updated upstream
st.title("Monitor your Ecological-Imapct 🌫️ ")
=======
st.title("Calculate Your Ecological Impact 🌫️ ")
>>>>>>> Stashed changes

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
