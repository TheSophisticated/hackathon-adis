import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from appwrite.client import Client
from appwrite.services.databases import Databases


st.set_page_config(page_title="Live Green", layout='centered',initial_sidebar_state='collapsed')

if st.button("Back To Home"):
    switch_page("app")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {vi"sibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

image = Image.open('meter.png')
st.title('         ‎ ‎ ‎ ‎ ‎ ‎ ‎ (BMI) Body Mass Index         ')
st.image(image, caption='BMI Scale')

st.header("Calculate Your BMI")

st.write(
    "The BMI is defined as the body mass divided by the square of the body height, and is expressed in units of kg/m²")

display = ("Male", "Female")

gender = st.selectbox("Select your gender", display)

st.write("You are a:", gender)

age = st.slider('How old are you?', 0, 120)
st.write("I'm", age, 'years old')

Weight = st.slider('What is your weight?', 15, 200)
st.write("My weight is", Weight, 'kg')

Height = st.slider('What is your height', 1.0, 3.0)
st.write("My height is", Height, 'm')

if (st.button("Click To Calculate Your BMI")):
    Weight / (Height * Height)
BMI = round(Weight / (Height * Height), 2)

if BMI < 16.5:
    st.write("The person is in trouble...")
elif 16.5 <= BMI < 18.5:
    st.write('The person is underweight')
elif 18.5 <= BMI < 25.0:
    st.write('The person is a healthy weight')
elif 25.0 <= BMI < 30.0:
    st.write('The person is overweight')
elif 30.0 <= BMI < 35.0:
    st.write('The person is moderately obese')
elif 35.0 <= BMI < 40.0:
    st.write('The person is severely obese')
else:
    st.write('The person is morbidly obese')
