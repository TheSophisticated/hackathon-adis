import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install strclseamlit-lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
import base64

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def encode_image_to_base64(file):
    with open(file, 'rb') as f:
        data = f.read()
        return base64.b64encode(data).decode()
    
img = encode_image_to_base64("cal\may.png")

selected = option_menu(
    menu_title = None,
    options = ['Home', 'Explore', 'Contact Us'],
    icons = ['house', 'book', 'envelope'],
    default_index = 0,
    orientation = 'horizontal',
    styles = None
)

image_urls = [
    'https://github.com/TheSophisticated/hackathon-adis/blob/main/cal/Jan.png',
    'https://images.unsplash.com/photo-1682685797366-715d29e33f9d?auto=format&fit=crop&q=60&w=700&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHx8',
    'https://imgur.com/B9r52fQ',
    'https://imgur.com/R9LuOUK',
    'https://imgur.com/Th3ddXY',
    'https://imgur.com/RG7948U',
    'https://imgur.com/6IV9Ll6',
    'https://imgur.com/gQK9F10',
    'https://imgur.com/DoD2cor',
    'https://imgur.com/qPLDcsl',
    'https://imgur.com/8g3OEJS',
    'https://imgur.com/2ktWAoH',
]

if st.button("Back To Home"):
    switch_page("app")


with st.container():
   st.markdown("<div style='text-align: center;'><h1>Calendar 🗓️</h1></div>", unsafe_allow_html=True)

selected_month = st.selectbox('Select a Month', ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

# Find the index of the selected month
selected_index = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'].index(selected_month)

# Display the image for the selected month
st.image(image_urls[selected_index], caption=selected_month, use_column_width=True)

events_data = {
    'ADSW': "Abu Dhabi Sustainability Week (ADSW) is a global platform for dialogue and collaboration on sustainability. It will take place in Abu Dhabi from January 16 to 19, 2023. ADSW will bring together leaders from government, business, and academia to discuss the latest trends and challenges in sustainability, and to identify solutions to the world's most pressing problems.",
    'World Wetlands Day': 'This day raises awareness about wetland conservation and their significance for ecological balance in both urban and rural environments.',
    'World Pangolin Day ': 'his day focuses on pangolin conservation, addressing urban and rural wildlife trafficking issues',
    'World Sustainable Energy Day': 'A platform to emphasize sustainable energy solutions for cities, reducing their carbon footprints and promoting renewable energy sources.',
    'International Day of Forests ': 'A day dedicated to urban forest conservation, advocating for the preservation and expansion of green spaces in cities.',
    'World Water Day': 'This day highlights sustainable water management and equitable access to clean water in urban areas.',
    'Earth Hour': 'People worldwide turn off non-essential lights for one hour to raise awareness about climate change, energy conservation, and sustainable urban lighting practices.',
    'World Biodiversity Day ': 'Focuses on urban biodiversity conservation and the importance of green spaces in cities.',
    'World Environment Day ': 'Promotes sustainable urban development and green initiatives in cities.',
    'World Oceans Day': 'Emphasizes the role of coastal cities in marine conservation and the need for responsible coastal development.',
    'World Population Day': 'Focuses on urban population challenges and sustainable urban growth.',
    'International Youth Day': 'Emphasizes the role of youth in promoting sustainable urban development and addressing climate change.',
    'International Day of Clean Air for Blue Skies': 'Highlights the importance of clean air in urban areas.',
    'World Cleanup Day': 'Global initiative for collective cleanup, fostering cleaner, more sustainable urban environments',
    'World Habitat Day': 'Focuses on sustainable urban development and housing.',
    'International Day for the Eradication of Poverty': 'Addresses poverty and inequality, often urban issues.',
    'Forbes Middle East Sustainability Leaders Summit 2023 ': 'This summit will bring together leaders from business, government, and academia to discuss the latest trends and challenges in sustainability. The agenda will cover a wide range of topics, including sustainable economic transformation, the role of sustainable finance and investment, and the transition to a net-zero future',
    "Sustainable Brands SB'23": 'Sustainable Brands SB 23 is a leading event for sustainability professionals. The event features speakers from leading brands and organizations, as well as workshops and networking sessions. The theme of this years event is Redefining Value: Creating a Thriving Future for People, Planet & Profit.',
    'World Soild Day': 'Emphasizes the importance of healthy soils for urban agriculture and green spaces.',
    'International Mountain Day ': 'Celebrating mountain ecosystems, emphasizing their vital role in urban water sources and biodiversity conservation.',
}

st.title('Event Descriptions')

# Dropdown to select an event
selected_event = st.selectbox('Select an Event', [''] + list(events_data.keys()))

# Display the description for the selected event
if selected_event:
    selected_description = events_data[selected_event]
    st.info(selected_description)

st.title('Base64-Encoded Image in Streamlit')

# Dropdown to select a month
selected_month = st.selectbox('Select a Month', list(images_by_month.keys()))


st.image(f"data:image/png;base64,{img}", caption=selected_month, use_column_width=True)