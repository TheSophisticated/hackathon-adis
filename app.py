# Import Dependencies
import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from appwrite.client import Client
from appwrite.services.databases import Databases
import time

# set_page_config
st.set_page_config(page_title="Live Green", page_icon="my_favicon.png", layout='wide',
                   initial_sidebar_state='collapsed')



# Initialise Supabase
appwrite_client = Client()
appwrite_client.set_endpoint("https://cloud.appwrite.io/v1")
appwrite_client.set_project("65452fa1053996a41f74")
appwrite_client.set_key("5fb2446667fc22a8a5853788a220d8a08acbe05583bbc1dd90842650856b4126c6f395b32a72614fe1533ddcec5ceb284ebcf0a767f4ae863fafc83b664fd177de81b20707e3516ae46265a888523a90988c84c83bce476abe8e3cb3b6835f641713f614a6c174507ccfa971317468b20dc473d4c58e1c47548dabac09d0a52c")

database = Databases(appwrite_client)

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
lottie_why = load_lottiefile("home-how.json")
lottie_waste = load_lottieurl("https://lottie.host/8b646674-95fa-4fad-a136-1dafb118ac30/SExy5Xq00Y.json")
lottie_cal = load_lottieurl("https://lottie.host/5ca4d357-bc7e-4b88-ada3-25098a4689eb/zIXsgClbao.json")
lottie_food = load_lottieurl("https://lottie.host/163ab21e-31d6-4637-b497-184d4d53a54d/4x1JxpVCSo.json")
lottie_business = load_lottieurl("https://lottie.host/103fa2e1-543d-4695-baf9-97e88b32ba11/owemdBNjw4.json")
lottie_bmi = load_lottieurl("https://lottie.host/cb46d577-68ee-4348-baa6-6c99ad99ef81/krEB5SFedB.json")
lottie_elec = load_lottieurl("https://lottie.host/705680b5-fe00-43f4-ba5f-4aacc3412c8f/i6JPk53jJB.json")

# CSS
contact_form = """<form action="https://formsubmit.co/amoghvarote@gmail.com"method="POST">
  <input type="hidden" name="_captcha" value="false">
  <input type="text" name="name" placeholder="Name" required>
  <input type="email" name="email" placeholder="Email" required>
  <textarea type="query" name = "query" placeholder="Your Message" required></textarea>
  <button type="submit">Send</button>
</form>"""

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
st.markdown(
    """
    <style>
        body{
            transform: scale(0.5):
        }
    </style>
""",
unsafe_allow_html=True
)

tracker = "pages\Tracker.py"

# Setting Up page configs
st.markdown("<div style='text-align: center;'><h1>Live Green 🌳</h1></div>", unsafe_allow_html=True)
st.write("\n")

# Navbar
selected = option_menu(
    menu_title=None,
    options=['Home', 'Individual','Community' ,'Contact Us'],
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
            
# Personal Features
elif selected == "Individual":
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
                st.markdown("<div style='text-align: center;'><h4>Eco-Imapct Monitor</h4></div>", unsafe_allow_html=True)
                with st.expander("A basic Eco-Imapct Monitor is a tool designed to help individuals measure and understand....", expanded=False):
                    st.write(""" their personal impact on the environment. 
                     It allows you to record and monitor your daily activities and choices that contribute to carbon emissions. By offering a straightforward way to quantify your carbon footprint, it empowers you to make informed decisions and take steps towards a more sustainable lifestyle.""")
                    if st.button("Go to the Eco-Imapct Monitor"):
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
        
            

# Community Related Features
elif selected == 'Community':
    with st.container():
        col_l, col_r = st.columns(2)
        with col_l:
            st_lottie(
                lottie_cal,
                speed=1,
                loop=True,
                reverse=False,
                height=350,
            )
            st.markdown("<div style='text-align: center;'><h4>Sustainable Event Calendar</h4></div>", unsafe_allow_html=True)
            with st.expander("Introducing our Sustainability Event Calendar, your go-to resource for staying up-to-date on crucial..."):
                    st.write("""sustainability-related events and activities. Just like our concise Waste Disposal Guide simplifies responsible waste management, this user-friendly calendar makes it effortless to engage with eco-conscious initiatives. Discover important dates for environmental conferences, Earth Day celebrations, recycling drives, and more. 
                     Say hello to a more sustainable future as you effortlessly track and join key events, leaving behind any sustainability-related uncertainties. 
                     Start making a positive impact and embrace a greener, cleaner world with our straightforward Sustainability Event Calendar.""")
                    if st.button("Check out the Sustainable Event Calendar"):
                        switch_page("calendar")
                        selected = None
        
        with col_r:
            st_lottie(
                lottie_business,
                speed=1,
                reverse=False,
                loop=True,
                height=350,
            )
            st.markdown("<div style='text-align: center;'><h4>Sustainable Business Directory</h4></div>", unsafe_allow_html=True)
            with st.expander("Introducing the Sustainable Business Directory, your essential guide to navigating the world...."):
                    st.write("""of eco-conscious commerce. This user-friendly resource is your key to discovering businesses committed to sustainability. Explore a wide range of enterprises dedicated to environmentally responsible practices, from eco-friendly products to green energy services. Say hello to a more sustainable way of doing business and welcome a future where every transaction contributes to a cleaner, greener world. Step into a new era of conscious consumerism with our straightforward Sustainable Business Directory, where your choices drive a more eco-friendly and sustainable marketplace.""")
                    if st.button("Check out the Sustainable Business Directory"):
                        switch_page("business-dir")
                        selected = None
        with col_l:
            with st.container():
                st_lottie(
                    lottie_waste,
                    speed=1,
                    loop=True,
                    reverse=False,
                    height=350,
                )
                st.markdown("<div style='text-align: center;'><h4>Waste Disposal Guide</h4></div>", unsafe_allow_html=True)
                with st.expander("Is waste disposal leaving you perplexed? Look no further than our concise Waste Disposal Guide...."):
                    st.write("""This user-friendly resource simplifies the art of responsible waste management. Get ready to declutter and embrace a more eco-friendly life. 
            Say goodbye to waste-related woes and welcome a cleaner, greener future with this straightforward guide.""")
                    if st.button("Check out the Waste Disposal Guide"):
                        switch_page("waste-guide")
                        selected = None
        with col_r:
            st_lottie(
                lottie_elec,
                speed=1,
                reverse=False,
                loop=True,
                height=350,
            )
            st.markdown("<div style='text-align: center;'><h4>Electricity Management</h4></div>", unsafe_allow_html=True)
            with st.expander("Introducing the UAE Electricity Management Guide, your essential resource for understanding and managing the entire electricity usage in the UAE."):
                    st.write("""Step into the Future of UAE Electricity Management. This user-friendly resource is your key to understanding and optimizing electricity usage in the UAE. Explore a wide range of enterprises dedicated to efficient and sustainable electricity management practices, from energy-efficient products to green power services. Say hello to a more sustainable way of managing electricity consumption and welcome a future where every decision contributes to a cleaner, more energy-efficient UAE. Step into a new era of conscious electricity management with our straightforward UAE Electricity Management Guide, where your choices drive a more efficient and sustainable energy landscape.""")
                    if st.button("Checkout the Electricity Manager"):
                        switch_page('Electricity')
                        selected = None
            
    st.write("-----")
    with st.container():
        st.title("Comments")

        user_name = st.text_input("Your Name", "")
        new_comment = st.text_area("Add your comment", "")

        if st.button("Submit"):
            if user_name and new_comment:
                document_id = str(int(time.time() * 1000))
                data = {
                    'name': user_name,
                    'comment': new_comment
                }
                response = database.create_document(collection_id="65453061a669a36a5df1", document_id=document_id, data=data, database_id='comments')
                if response["$id"]:
                    st.success("Comment added Successfully")
                    new_comment = ""
                    user_name = ""
                else:
                    st.warning("An error ocurred while adding the comment")
            else:
                st.warning("Please enter your name and comment before submitting")

        st.subheader("Comments")
        response = database.list_documents(collection_id="65453061a669a36a5df1", database_id='comments')

        if response and 'documents' in response:
            comments = response["documents"]
            for comment in comments:
                st.write(f"**{comment['name']}** : {comment['comment']}")
        else:
            st.info("No comments yet. Be the first one to comment!")


# Explore Page
elif selected == 'Explore':

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
                st.markdown("<div style='text-align: center;'><h4>Eco-Imapct Monitor </h4></div>", unsafe_allow_html=True)
                with st.expander("A basic Eco-Impact Monitor is a tool designed to help individuals measure and understand....", expanded=False):
                    st.write(""" their personal impact on the environment. 
                     It allows you to record and monitor your daily activities and choices that contribute to carbon emissions. By offering a straightforward way to quantify your Eco-Impact, it empowers you to make informed decisions and take steps towards a more sustainable lifestyle.""")
                    if st.button("Go to the Eco-Imapct Monitor"):
                        switch_page("tracker")
                        selected = None
        
    
    st.write("-----")
    with st.container():
        st.title("Comments")

        user_name = st.text_input("Your Name", "")
        new_comment = st.text_area("Add your comment", "")

        if st.button("Submit"):
            if user_name and new_comment:
                document_id = str(int(time.time() * 1000))
                data = {
                    'name': user_name,
                    'comment': new_comment
                }
                response = database.create_document(collection_id="65453061a669a36a5df1", document_id=document_id, data=data, database_id='comments')
                if response["$id"]:
                    st.success("Comment added Successfully")
                    new_comment = ""
                    user_name = ""
                else:
                    st.warning("An error ocurred while adding the comment")
            else:
                st.warning("Please enter your name and comment before submitting")

        st.subheader("Comments")
        response = database.list_documents(collection_id="65453061a669a36a5df1", database_id='comments')

        if response and 'documents' in response:
            comments = response["documents"]
            for comment in comments:
                st.write(f"**{comment['name']}** : {comment['comment']}")
        else:
            st.info("No comments yet. Be the first one to comment!")

# Contact Page      
elif selected == "Contact Us":
    st.title("✉️Get in Touch!")
    st.markdown(contact_form, unsafe_allow_html=True)

    local_css("style/style.css")
