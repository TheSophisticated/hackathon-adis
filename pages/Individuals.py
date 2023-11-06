import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from appwrite.client import Client
from appwrite.services.databases import Databases

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_person = load_lottieurl("https://lottie.host/6728e0f4-ec70-4b9f-a4bf-3b7d7f5ba83c/cOp0f1Hizt.json")
lottie_tracker = load_lottieurl("https://lottie.host/3170ab1a-092f-4713-b398-8d880b8e0f89/9XoxtwePbF.json")
lottie_waste = load_lottieurl("https://lottie.host/8b646674-95fa-4fad-a136-1dafb118ac30/SExy5Xq00Y.json")
lottie_cal = load_lottieurl("https://lottie.host/5ca4d357-bc7e-4b88-ada3-25098a4689eb/zIXsgClbao.json")
lottie_food = load_lottieurl("https://lottie.host/163ab21e-31d6-4637-b497-184d4d53a54d/4x1JxpVCSo.json")
lottie_business = load_lottieurl("https://lottie.host/103fa2e1-543d-4695-baf9-97e88b32ba11/owemdBNjw4.json")
lottie_bmi = load_lottieurl("https://lottie.host/cb46d577-68ee-4348-baa6-6c99ad99ef81/krEB5SFedB.json")
lottie_elec = load_lottieurl("https://lottie.host/705680b5-fe00-43f4-ba5f-4aacc3412c8f/i6JPk53jJB.json")

with st.container():
        col_l, col_r = st.columns(2)
        with col_l:
            with st.container():
                st_lottie(
                    lottie_tracker,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="low",  # medium ; high
                    height=350,
                    width=None,
                )
                st.markdown("<div style='text-align: center;'><h4>Carbon Tracker</h4></div>", unsafe_allow_html=True)
                with st.expander("A basic Carbon Footprint Tracker is a tool designed to help individuals measure and understand....", expanded=False):
                    st.write(""" their personal impact on the environment. 
                     It allows you to record and monitor your daily activities and choices that contribute to carbon emissions. By offering a straightforward way to quantify your carbon footprint, it empowers you to make informed decisions and take steps towards a more sustainable lifestyle.""")
                    if st.button("Go to the Carbon Tracker"):
                        switch_page("tracker")
                        selected = None
        with col_r:
            with st.container():
                st_lottie(
                    lottie_bmi,
                    speed=1,
                    loop=True,
                    reverse=False,
                    height=350,
                )
                st.markdown("<div style='text-align: center;'><h4>BMI Calculator</h4></div>", unsafe_allow_html=True)
                with st.expander("Are you struggling to calculate your BMI? Don't worry, we've got you covered with our easy-to-use BMI Calculator."):
                    st.write("""This user-friendly tool simplifies the process of calculating your BMI. Get ready to understand your body's health and take steps towards a healthier lifestyle. Say goodbye to BMI-related confusion and welcome a more informed, well-being-focused future with our straightforward BMI Calculator.""")
                    if st.button("Check out the BMI Calculator"):
                        switch_page("BMI")
                        selected = None