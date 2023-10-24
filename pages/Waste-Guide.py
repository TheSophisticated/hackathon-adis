import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install strclseamlit-lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

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