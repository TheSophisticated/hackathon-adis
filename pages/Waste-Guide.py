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

if st.button("Back To Home"):
    switch_page("app")

st.title("Waste Guide")

waste_types = {
    "": "",
    "Organic Waste": """
    Organic waste can be composted at home or in a community composting program. Composting turns food scraps, yard waste, and other organic materials into nutrient-rich soil amendment. Some examples of organic waste include:

    * Food scraps: Fruit and vegetable peels, cores, and seeds; meat, poultry, and fish bones; dairy products; coffee grounds and tea bags; eggshells; bread and pasta scraps.

    * Yard waste: Grass clippings, leaves, twigs, and branches; flowers and plants; garden trimmings.

    * Other organic materials: Paper towels and napkins; cardboard boxes and containers; coffee filters; tea bags.

    # Best practices for composting organic waste:

    * Chop up larger items: This will help them decompose more quickly.
    * Add a variety of materials: Include both green (nitrogen-rich) materials, such as food scraps and grass clippings, and brown (carbon-rich) materials, such as dry leaves and shredded paper.
    * Keep the compost moist: The compost should be moist but not soggy.
    * Turn the compost regularly: This will help to aerate the compost and speed up the decomposition process

    """,

    "Recyclable Waste": """
    Recyclable waste can be collected at home or taken to a recycling center. Recycling helps to conserve resources and reduce pollution. Some examples of recyclable waste include:

    * Paper: Newspapers, magazines, catalogs, junk mail, office paper, cardboard boxes and containers.

    * Plastic: Bottles, jugs, jars, tubs, containers, bags, wrapping paper, plastic film.

    * Metal: Cans, foil, aluminum trays, metal lids, wire, metal hangers.

    * Glass: Bottles, jars, glasses, mugs.

    # Best practices for recycling waste:

    * Check with your local recycling program: Different communities have different recycling rules.
    * Rinse out containers: This will help to prevent contamination.
    * Flatten cardboard boxes: This will save space in your recycling bin or collection container.
    * Don't put hazardous materials in your recycling bin: This includes batteries, paint, and electronics.
    """,

    "Hazardous Waste": """
    Hazardous waste must be disposed of properly to prevent environmental contamination. Many communities have hazardous waste collection programs. Some examples of hazardous waste include:

    * Batteries: Household batteries, car batteries, rechargeable batteries.

    * Paint: Latex paint, oil-based paint, paint thinners, paint strippers.

    * Electronics: Computers, televisions, monitors, printers, cell phones, stereos.

    * Oil: Motor oil, cooking oil, vegetable oil, transmission fluid.

    * Other hazardous materials: Pesticides, herbicides, fertilizers, pool chemicals, cleaning products, aerosol cans, propane tanks.
    
    # Best practices for disposing of hazardous waste:

    * Never pour hazardous waste down the drain or into storm drains: This can contaminate water supplies.
    * Never burn hazardous waste: This can release harmful chemicals into the air.
    * Take hazardous waste to a designated collection facility: Many communities have hazardous waste collection events or permanent collection sites.

    """,

    "General Waste": """
    General waste should be disposed of in a trash can. General waste is typically sent to a landfill. Some examples of general waste include:

    * Non-recyclable plastic items: Styrofoam, plastic bags, plastic wrap, plastic toys, plastic utensils.

    * Non-recyclable paper items: Paper towels, napkins, tissues, paper cups and plates, disposable diapers and wipes.

    * Food-contaminated items: Food wrappers, disposable utensils, paper plates and cups, napkins, tissues.

    * Broken or contaminated glass: Broken glass from windows, mirrors, or lightbulbs; glass contaminated with food or chemicals.

    * Yard waste that is not suitable for composting: Diseased plants, invasive plants, weeds with seeds, grass clippings treated with herbicides or pesticides.

    * Other non-recyclable or non-compostable materials: Wood, furniture, construction materials, textiles, clothing, shoes.
    
    # Best practices for disposing of general waste:

    * Reduce the amount of general waste you generate: This includes buying less stuff, reusing items whenever possible, and composting food scraps.
    * Bag your trash: This will help to prevent litter and keep your trash can clean.
    * Put your trash can out on the curb on collection day: This will help to ensure that your trash is collected properly.
    """,
}

default_text = "Please select a waste type to learn more about proper disposal."
selected_waste_type = st.selectbox("Select a waste type:", waste_types.keys(), index=0)

if selected_waste_type:
    st.write(waste_types[selected_waste_type])
else:
    st.write(default_text)