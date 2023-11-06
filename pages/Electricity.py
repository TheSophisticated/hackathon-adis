import plotly.express as px 
import streamlit as st
import pandas as pd
import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install strclseamlit-lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page


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


df = pd.read_excel(
    io = 'Energy.xlsx',
    engine='openpyxl',
    sheet_name= 'RTEU',
    skiprows=2,
    usecols='B:J',
    nrows=1000,
)

print (df)

st.set_page_config(page_title="Real Time Energy Usage",
                   layout="wide")



#sidebar

st.sidebar.header("Please Filter Here:")
Emirate = st.sidebar.multiselect(
    "Select the City:",
    options=df["Emirate"].unique(),
    default=df["Emirate"].unique()
)

df_selection = df.query(
    "Emirate == @Emirate"
)

# Check if the dataframe is empty:
if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop() # This will halt the app from further execution.

#mainpage

st.title("📊 Real Time Energy Usage")
st.markdown("##")

# top kpi

total_consumption = int(df_selection["Total consumption(GW)"].sum())
average_consumption = round(df_selection["Average consumption(GW)"].sum())
total_cost = int(df_selection["Total cost(AED)"].sum())

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Consumption:")
    st.subheader(f"GW {total_consumption:,} 🔋 ")
with middle_column:
    st.subheader("Average Consumption:")
    st.subheader(f"GW {average_consumption:,} 🔋")
with right_column:
    st.subheader("Total Cost:")
    st.subheader(f"AED {total_cost:,} 💸")
    
st.markdown("---")


energy_sources = {
    "": "",
    "Solar Energy": """
    Solar energy is harnessed from the sun's rays and can be converted into electricity or used for heating. Some key points about solar energy include:

    * Solar panels capture sunlight and convert it into electricity through photovoltaic cells.
    * Solar thermal systems use sunlight to heat water or air for residential or industrial use.
    * Solar energy is renewable, clean, and has minimal environmental impact.
    * Install solar panels on rooftops or in solar farms to harness solar energy.

    # Best practices for harnessing solar energy:

    * Ensure proper orientation and angle of solar panels for maximum sun exposure.
    * Keep solar panels clean to optimize energy production.
    * Consider net metering to sell excess electricity back to the grid.

    """,

    "Wind Energy": """
    Wind energy is generated by wind turbines that convert the kinetic energy of wind into electricity. Here are some key points about wind energy:

    * Wind turbines have large blades that rotate and generate electricity.
    * Wind energy is a sustainable and eco-friendly energy source.
    * Wind farms are established in areas with consistent wind patterns.

    # Best practices for harnessing wind energy:

    * Install wind turbines in areas with a consistent and strong wind resource.
    * Regular maintenance of wind turbines is essential for optimal performance.
    * Consider community or offshore wind farms for increased efficiency.

    """,

    "Hydropower": """
    Hydropower, or hydroelectric power, is derived from the energy of flowing water. Key points about hydropower include:

    * Dams or water turbines are used to convert the energy of flowing water into electricity.
    * It is a reliable and renewable energy source.
    * Hydropower can be generated from small-scale projects like micro-hydropower systems.

    # Best practices for harnessing hydropower:

    * Consider the environmental impact of large dams and opt for low-impact hydropower solutions.
    * Maintain and inspect hydropower infrastructure regularly to ensure efficiency.

    """,

    "Geothermal Energy": """
    Geothermal energy is obtained by tapping into heat from the Earth's core. Key points about geothermal energy include:

    * Geothermal power plants use the Earth's heat to produce electricity or provide heating and cooling.
    * It is a sustainable and constant energy source.
    * Geothermal heat pumps are used for residential heating and cooling.

    # Best practices for harnessing geothermal energy:

    * Assess the geothermal potential of your location before installing a geothermal system.
    * Regularly service and maintain geothermal systems for long-term efficiency.

    """,

    "Biomass Energy": """
    Biomass energy is derived from organic materials like wood, agricultural residues, and waste. Key points about biomass energy include:

    * Biomass can be burned, converted to biogas, or used in biofuel production.
    * It is a renewable energy source that can reduce waste.
    * Biomass energy can be harnessed from various sources, including wood pellets, crop residues, and landfill gas.

    # Best practices for harnessing biomass energy:

    * Properly manage and store biomass materials to prevent pollution.
    * Opt for modern, efficient combustion technologies to minimize emissions.

    """,
}

default_text = "Please select a waste type to learn more about proper disposal."
selected_energy_type = st.selectbox("Select a waste type:", energy_sources.keys(), index=0)

if selected_energy_type:
    st.write(energy_sources[selected_energy_type])
else:
    st.write(default_text)

