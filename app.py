# Import Dependencies
import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

# set_page_config
st.set_page_config(page_title="Live Green", page_icon="my_favicon.png", layout='wide',
                   initial_sidebar_state='collapsed')


# Defining Functions
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# All Animation files declared here
# replace link to local lottie file
lottie_hello = load_lottieurl("https://lottie.host/56d1faa9-c78e-459f-888e-5f3eaa2abf2d/hYh9CF4KDt.json")
lottie_tracker = load_lottieurl("https://lottie.host/3170ab1a-092f-4713-b398-8d880b8e0f89/9XoxtwePbF.json")
lottie_why = load_lottieurl("https://lottie.host/981a0f88-6a06-4ea9-a4e9-92c2d962309e/eOLgYDDSRZ.json")
lottie_waste = load_lottieurl("https://lottie.host/8b646674-95fa-4fad-a136-1dafb118ac30/SExy5Xq00Y.json")
lottie_cal = load_lottieurl("https://lottie.host/5ca4d357-bc7e-4b88-ada3-25098a4689eb/zIXsgClbao.json")
lottie_food = load_lottieurl("https://lottie.host/163ab21e-31d6-4637-b497-184d4d53a54d/4x1JxpVCSo.json")
lottie_business = load_lottieurl("https://lottie.host/103fa2e1-543d-4695-baf9-97e88b32ba11/owemdBNjw4.json")

# CSS
contact_form = """<form action="https://formsubmit.co/iluvguccibanana@gmail.com"method="POST">
  <input type="hidden" name="_captcha" value="false">
  <input type="text" name="name" placeholder="Name" required>
  <input type="email" name="email" placeholder="Email" required>
  <textarea type="query" name = "query" placeholder="Your Message" required></textarea>
  <button type="submit">Send</button>
</form>"""

bg_grad = """
    background: rgb(98,255,124);
    background: linear-gradient(176deg, rgba(98,255,124,1) 5%, rgba(217,255,225,1) 51%, rgba(98,255,124,1) 100%);
"""

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

# Setting Up page configs
st.markdown("<div style='text-align: center;'><h1>Live Green</h1></div>", unsafe_allow_html=True)
st.write("\n")

# Navbar
selected = option_menu(
    menu_title=None,
    options=['Home', 'Explore', 'Contact Us'],
    icons=['house', 'book', 'envelope'],
    default_index=0,
    orientation='horizontal',
    styles=None
)

# Main Page
if selected == 'Home':
    # ---Header Section--

    with st.container():
        st.title("Home")

    with st.container():

        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader('')
            st.write("""
                In today's world, it's more important than ever to live sustainably. But with so many different ways to reduce our environmental impact, it can be difficult to know where to start. That's where the new app, Live Green, comes in.

            Live Green is a one-stop shop for all things sustainable. It provides users with a wealth of information on how to reduce their carbon footprint, conserve resources, and live more eco-friendly lives. The app also features a variety of tools and resources to help users make sustainable choices, such as:

            A searchable database of sustainable businesses and products
            A carbon footprint calculator
            A recycling and composting guide
            Tips on how to reduce energy consumption
            A community forum where users can connect with other sustainability-minded people
            Live Green is the perfect tool for anyone who wants to live more sustainably. It's easy to use, informative, and comprehensive. With Live Green, you can make a difference for the planet, one small step at a time.""")

        with right_column:
            st_lottie(
                lottie_hello,
                speed=1,
                reverse=False,
                loop=True,
                quality="low",  # medium ; high
                height=500,
                width=None,
            )

        with left_column:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st_lottie(
                lottie_why,
                speed=1,
                reverse=False,
                loop=True,
                height=400,
            )
        with right_column:
            st.subheader("")
            st.write("""Extensive research indicates that the level of resistance one encounters when attempting to establish a habit is inversely proportional to the habit's likelihood of becoming a permanent part of their routine.
                     
At Live Green, we understand your dedication to the environment, and our mission revolves around reducing the hurdles that individuals, like yourself, often confront. Our website is dedicated to delivering an optimal array of resources and services, designed to facilitate your journey towards sustainability.
""")

# Explore Page
elif selected == 'Explore':

    with st.container():
        st.title("Explore")

    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Carbon Footprint Tracker")
            st.write("""A basic Carbon Footprint Tracker is a tool designed to help individuals measure and understand their personal impact on the environment. 
                     It allows you to record and monitor your daily activities and choices that contribute to carbon emissions. By offering a straightforward way to quantify your carbon footprint, it empowers you to make informed decisions and take steps towards a more sustainable lifestyle.""")
            if st.button("Track Carbon Footprint"):
                switch_page("tracker")
        with right_column:
            st_lottie(
                lottie_tracker,
                speed=1,
                reverse=False,
                loop=True,
                quality="low",  # medium ; high
                height=350,
                width=None,
            )
        with left_column:
            st.text("")
            st.text("")
            st.text("")
            st_lottie(
                lottie_waste,
                speed=1,
                loop=True,
                reverse=False,
                height=350,
            )
        with right_column:
            st.subheader("Waste Disposal Guide")
            st.write("""Is waste disposal leaving you perplexed? Look no further than our concise Waste Disposal Guide. This user-friendly resource simplifies the art of responsible waste management. Get ready to declutter and embrace a more eco-friendly life. 
            Say goodbye to waste-related woes and welcome a cleaner, greener future with this straightforward guide.""")
            if st.button("Check Out the Guide!"):
                switch_page("waste-guide")

        with left_column:
            st.subheader("Sustainability Event Calendar")
            st.write("""Introducing our Sustainability Event Calendar, your go-to resource for staying up-to-date on crucial sustainability-related events and activities. Just like our concise Waste Disposal Guide simplifies responsible waste management, this user-friendly calendar makes it effortless to engage with eco-conscious initiatives. Discover important dates for environmental conferences, Earth Day celebrations, recycling drives, and more. 
                     Say hello to a more sustainable future as you effortlessly track and join key events, leaving behind any sustainability-related uncertainties. 
                     Start making a positive impact and embrace a greener, cleaner world with our straightforward Sustainability Event Calendar.""")
            if st.button("Visit the Calendar"):
                switch_page("calendar")

        with right_column:
            st_lottie(
                lottie_cal,
                speed=1,
                loop=True,
                reverse=False,
                height=350,
            )

        with right_column:
            st.subheader("Sustainable Food Guide")
            st.write("""Introducing the Sustainability Food Guide, your ultimate companion on the path to greener, healthier dining. This user-friendly resource is your gateway to eco-conscious culinary choices. Discover tips and insights on sourcing local ingredients, reducing food waste, and embracing sustainable cooking practices. 
                     Say farewell to unsustainable eating habits and savor a future filled with delicious, planet-friendly dishes. Welcome a new era of mindful, eco-friendly dining with our straightforward Sustainability Food Guide, where every meal contributes to a cleaner, greener world.""")
            if st.button("Explore the Food Guide"):
                switch_page("food-guide")

        with left_column:
            st_lottie(
                lottie_food,
                speed=1,
                loop=True,
                reverse=False,
                height=350,
            )

        with left_column:
            st.subheader("Sustainable Business Directory")
            st.write("""
                    Introducing the Sustainable Business Directory, your essential guide to navigating the world of eco-conscious commerce. This user-friendly resource is your key to discovering businesses committed to sustainability. Explore a wide range of enterprises dedicated to environmentally responsible practices, from eco-friendly products to green energy services. Say hello to a more sustainable way of doing business and welcome a future where every transaction contributes to a cleaner, greener world. Step into a new era of conscious consumerism with our straightforward Sustainable Business Directory, where your choices drive a more eco-friendly and sustainable marketplace.""")

            if st.button("Business Directory"):
                switch_page("business-dir")

        with right_column:
            st_lottie(
                lottie_business,
                speed=1,
                reverse=False,
                loop=True,
                height=400,
            )

        with st.container():
            st.write("----")

# Contact Page
elif selected == "Contact Us":
    st.title("✉️Get in Touch!")
    st.markdown(contact_form, unsafe_allow_html=True)

    local_css("style/style.css")
