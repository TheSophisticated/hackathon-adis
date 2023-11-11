import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install strclseamlit-lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(layout='wide', initial_sidebar_state = 'collapsed')

bg_img = """
<style>
[data-testid = 'stAppViewContainer']{
background-color: #e5e5f7;
opacity: 1;
background-image:  radial-gradient(#5f9f64 2px, transparent 2px), radial-gradient(#5f9f64 2px, #e5e5f7 2px);
background-size: 80px 80px;
background-position: 0 0,40px 40px;
}
</style>
"""
st.markdown(bg_img, unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

if st.button("Back To Home"):
    switch_page("app")


with st.container():
    st.title("Business Directory")

brands = {
    "nike": {
        "Allbirds": "Sustainable footwear made from Merino wool, eucalyptus trees, and recycled materials.",
        "Veja": "Sustainable sneakers made from organic cotton, recycled polyester, and vegetable-tanned leather.",
        "Patagonia": "Outdoor clothing and gear company committed to environmental responsibility, using recycled materials and implementing initiatives to reduce their environmental impact."
    },
    "adidas": {
        "Adidas x Parley": "Sustainable footwear and apparel collaboration between Adidas and Parley for the Oceans, made from recycled ocean plastic.",
        "Stella McCartney x Adidas": "Sustainable sportswear collaboration between Stella McCartney and Adidas, using sustainable materials and practices.",
        "Everlane": "Clothing company known for transparency and ethical practices, using sustainable materials and implementing initiatives to reduce their environmental impact."
    },
    "apple": {
        "Fairphone": "Smartphone company committed to ethical and sustainable practices, using conflict-free materials and implementing initiatives to reduce their environmental impact.",
        "Shiftphone": "Smartphone company committed to sustainability, using modular design for easy repair and upgrades, extending the lifespan of their phones.",
        "Refurbished Apple products": "Refurbished and like-new Apple products at a significantly reduced price, extending the lifespan of existing devices and reducing waste."
    },
    "amazon": {
        "ThredUp": "Online consignment store that sells secondhand clothing, shoes, and accessories, offering unique and stylish items while reducing waste.",
        "Poshmark": "Online consignment store that sells secondhand clothing, shoes, and accessories, with a wide variety of items from both designer and everyday brands.",
        "Amazon Renewed": "Program that sells refurbished and pre-owned products, offering high-quality items at a reduced price while reducing waste."
    },
    "coca-cola": {
        "Fairtrade Certified sodas": "Sodas produced according to fair trade standards, ensuring fair wages for farmers and workers and protecting the environment.",
        "Organic sodas": "Sodas made with organic ingredients, grown without the use of synthetic pesticides or fertilizers.",
        "Homemade sodas": "Easy to make at home, allowing control over ingredients and sugar content, reducing packaging waste and promoting a healthier alternative."
    }
}


with st.container():
    col1, col2 = st.columns(2)

    with col1:
        search_term = st.text_input("Search for a brand:")
        lowercase_search_term = search_term.lower()
    with col2:
        if search_term:
            if lowercase_search_term in brands.keys():
                alternatives = brands[lowercase_search_term]
                st.write(f"# Sustainable alternatives for {search_term}:")
                for alternative in alternatives.keys():
                    st.write(f"  - {alternative}: {alternatives[alternative]}")
            else:
                st.info(f"No sustainable alternatives found for {search_term}.")



