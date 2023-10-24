import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install strclseamlit-lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components

embed_link = "https://calendar.google.com/calendar/u/0?cid=YzlhNTg5ODE1YTUxYTg1NWYxZGUwYTc5NGE5NmVkNjFjNDlhZDUzZmQwMTRjZDQ1MzViNTVkODAxMTNhYjU4MUBncm91cC5jYWxlbmRhci5nb29nbGUuY29t"

selected = option_menu(
    menu_title = None,
    options = ['Home', 'Explore', 'Contact Us'],
    icons = ['house', 'book', 'envelope'],
    default_index = 0,
    orientation = 'horizontal',
    styles = None
)

with st.container():
    st.title("Calendar")

components.iframe("https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=Asia%2FDubai&src=aXBndXJnYW9uMkBnbWFpbC5jb20&src=YzhiYTZmMDhhOTYxZDNlZDQyNzM3Nzg3YmZhMWQ3NWI5Y2E2MTdhOGMxNWJjMWNlYzI3YzllZGE0NmE1MDk2OEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&src=YzlhNTg5ODE1YTUxYTg1NWYxZGUwYTc5NGE5NmVkNjFjNDlhZDUzZmQwMTRjZDQ1MzViNTVkODAxMTNhYjU4MUBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&src=ODgxMWY0ZTU1YTQzODk3ZjgzMGFiZDRiNTY0MjljYzlhNTExZWE3NzM0ZTVjNzViZDU1NDQyZDE5ZTZhYTE3NEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&src=Y2xhc3Nyb29tMTAwMDk2OTgyNDk5MzQ4MTE0NTI3QGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23B39DDB&color=%237986CB&color=%23009688&color=%23AD1457&color=%23202124")