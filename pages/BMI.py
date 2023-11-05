import streamlit as st
from PIL import Image

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

image = Image.open('meter.png')
st.title('         ‎ ‎ ‎ ‎ ‎ ‎ ‎ (BMI) Body Mass Index         ')
st.image(image, caption='BMI Scale')

st.latex(r'''
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

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
BMI = Weight / (Height * Height)

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
