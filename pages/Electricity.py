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
