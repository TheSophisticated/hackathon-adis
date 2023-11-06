import plotly.express as px 
import streamlit as st
import pandas as pd

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

# Consumption of Emirates from 2000 - 2023
import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install strclseamlit-lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="centered")

waste_data = {
    "plastic bottle": {
        "Category": "Plastic Waste",
        "Recycling": "Plastic bottles can be recycled into new plastic products, reducing the need for virgin plastic production and conserving resources. Recycling plastics helps mitigate environmental impacts. The process involves collecting, cleaning, shredding, and melting the plastic to create new items like bottles, containers, or textiles.",
        "Conversion to Energy": "Plastic bottles can be incinerated to produce energy through waste-to-energy facilities, reducing landfill waste and contributing to electricity generation. During incineration, the energy released can be harnessed for power generation or heating systems."
    },
    "apple peels": {
        "Category": "Organic Waste",
        "Recycling": "Apple peels can be composted, creating nutrient-rich soil amendments that enrich gardens and reduce food waste. Composting is an eco-friendly way to recycle organic waste. The natural decomposition process turns peels into valuable compost, which can improve soil structure, moisture retention, and plant growth.",
        "Conversion to Energy": "Organic waste like apple peels can be converted to biogas through anaerobic digestion, providing a renewable energy source while reducing greenhouse gas emissions. During anaerobic digestion, microorganisms break down organic materials, including peels, to produce biogas, which can be used for cooking, heating, or electricity generation."
    },
    "aluminum can": {
        "Category": "Metal Waste",
        "Recycling": "Aluminum cans are highly recyclable, with recycling processes using less energy and emitting fewer greenhouse gases compared to primary aluminum production. Recycling conserves resources and reduces environmental impact. The recycling journey begins with collecting and cleaning used cans. They are then melted down, refined, and shaped into new products, such as cans, car parts, or aerospace materials.",
        "Conversion to Energy": "While aluminum can recycling doesn't directly produce energy, it contributes to resource conservation and energy savings. Recycling reduces the need for mining and refining aluminum ores, which is an energy-intensive process. Additionally, aluminum recycling lowers greenhouse gas emissions, as recycling emits less CO2 than primary aluminum production."
    },
    "newspapers": {
        "Category": "Paper Waste",
        "Recycling": "Recycling newspapers saves trees, energy, and water. The recycled paper can be used to produce new newspapers and various paper products, contributing to sustainability and resource conservation. Recycling paper involves collecting used newspapers, breaking them down into pulp, and forming new paper sheets or products.",
        "Conversion to Energy": "Paper waste can be converted to energy through incineration with proper emissions controls. This process can help offset the energy demands of waste disposal while minimizing landfill waste. Incineration produces heat, which can be harnessed for power generation or heating systems."
    },
    "glass bottle": {
        "Category": "Glass Waste",
        "Recycling": "Recycling glass bottles reduces energy consumption and raw material extraction. Reusing glass containers conserves resources and helps lower greenhouse gas emissions. The glass recycling process includes collecting, sorting, and cleaning used glass bottles. These bottles are then melted and formed into new glass products or containers.",
        "Conversion to Energy": "Glass recycling primarily conserves resources and doesn't produce energy. However, it contributes to environmental sustainability by reducing the carbon footprint of glass production. Using recycled glass to make new glass items requires less energy compared to using raw materials. This helps decrease energy consumption and greenhouse gas emissions."
    },
    "banana peel": {
        "Category": "Organic Waste",
        "Recycling": "Composting banana peels enriches soil and improves its nutrient content. Composted organic waste helps sustain healthy gardens and minimizes food waste. Composting involves collecting organic materials, like banana peels, and allowing them to decompose naturally. The resulting compost is an organic soil conditioner and fertilizer that can enhance plant growth and soil health.",
        "Conversion to Energy": "Banana peels, like other organic waste, can be converted to biogas through anaerobic digestion. This process occurs in an oxygen-free environment, where microorganisms break down organic matter, including banana peels, to generate biogas. Biogas can be used for cooking, heating, or electricity generation, offering a renewable and sustainable energy source."
    },
    "tin can": {
        "Category": "Metal Waste",
        "Recycling": "Tin cans, including steel and aluminum varieties, can be recycled to create new metal products, such as cans, car parts, and construction materials. Recycling conserves resources and reduces waste. The recycling process includes collecting and cleaning used tin cans, melting them down, and shaping them into new metal items.",
        "Conversion to Energy": "Similar to aluminum cans, recycling tin cans contributes to resource conservation and energy savings. It reduces the environmental impact of metal production. The recycling process lowers greenhouse gas emissions and energy consumption, promoting sustainability."
    },
    "cardboard box": {
        "Category": "Paper Waste",
        "Recycling": "Recycling cardboard boxes saves trees and energy. It promotes sustainability by using recycled cardboard to produce new packaging materials and paper products. The recycling process involves collecting used cardboard boxes, breaking them down into pulp, and creating new paper-based items.",
        "Conversion to Energy": "Cardboard waste can be converted to energy through incineration with proper emissions controls. This process helps offset the energy demands of waste disposal while minimizing landfill waste. Incineration produces heat, which can be harnessed for power generation or heating systems."
    },
    "plastic bag": {
        "Category": "Plastic Waste",
        "Recycling": "Plastic bags can be recycled into new plastic products, reducing plastic pollution and the need for virgin plastic production. Plastic bag recycling is an eco-friendly choice. The recycling process includes collecting and processing used plastic bags, transforming them into new plastic items.",
        "Conversion to Energy": "Some waste-to-energy facilities can convert plastic bags into energy through inciner"
    }
}