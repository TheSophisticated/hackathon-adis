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

selected = option_menu(
    menu_title = None,
    options = ['Home', 'Explore', 'Contact Us'],
    icons = ['house', 'book', 'envelope'],
    default_index = 0,
    orientation = 'horizontal',
    styles = None
)


with st.container():
    st.title("Waste Disposal Guide")
    st. write("Recycling: ")
    st.write("""Recycling is the process of converting waste materials into new materials and objects. 
             It is an alternative to conventional waste disposal that can save material and help lower greenhouse gas emissions. 
             Recycling can benefit your community and the environment.""")
    st.write("Materials that can be recycled: ")
    st.write("""

            Paper and cardboard: This includes newspapers, magazines, office paper, and cardboard boxes

Plastic: This includes most types of plastic bottles, jugs, and containers, as well as plastic bags and packaging.

Metal: This includes aluminum and steel cans, lids, and foil

Glass: This includes glass bottles and jars            
""")
    
    