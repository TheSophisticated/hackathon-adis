import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
import openai #pip install openai
from streamlit_lottie import st_lottie  # pip install strclseamlit-lottie
from streamlit_option_menu import option_menu
from streamlit_chat import message
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Food Guide", page_icon="my_favicon.png", layout = 'wide' )

def calc_BMI(height, weight):
    bmi = weight/(height**2)
    return bmi

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown("<div style='text-align: center;'><h1>Food Guide 🍉</h1></div>", unsafe_allow_html=True)
st.write("\n")

selected = option_menu(
    menu_title = None,
    options = ['Home', 'Explore', 'Contact Us'],
    icons = ['house', 'book', 'envelope'],
    default_index = 0,
    orientation = 'horizontal',
    styles = None
)


st.subheader("BMI Calculator")
weight = st.text_input("Enter Your Weight(In Kg's): ")
height = st.text_input("Enter your Height(In meters): ")
if st.button("Calculate my BMI"):
    user_bmi = calc_BMI(float(height), float(weight))
    if user_bmi < 18.5:
        st.warning(f"Your BMI is: {round(user_bmi, 1)} and you are underweight")
    elif user_bmi >= 18.5 and user_bmi <=24.9:
        st.success(f"Your BMI is: {round(user_bmi, 1)} and it is in a Healthy Range")
    elif user_bmi >= 25.0 and user_bmi <=29.9:
        st.warning(f"Your BMI is {round(user_bmi, 1)} and it is in the Overweight Range")
    elif user_bmi >= 30.0:
        st.warning(f"Your BMI is {round(user_bmi,1)} and it is in the Obese Range")

openai.api_key = st.secrets["api_secret"]
    
def generate_response(prompt):
    completions= openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 4000,
        n = 1,
        stop = None,
        temperature = 0.3,
    )
    message = completions.choices[0].text
    return message

#storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []
    
def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text 
st.write("----")
user_input = get_text()

if user_input:
    output = generate_response(user_input)
    #store the output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')