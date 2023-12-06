


from PIL import Image
import requests

import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

st.set_page_config(
    page_title="Multipage App",
    page_icon="wave"
)

st.title("Hi,:wave: WELCOME TO MY WEBLOG")


import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20fcfjwiyb.json")
img_contact_form = Image.open("images/my pic.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with st.container():
    st.subheader("Im Jess Rel Enoc:boy:")
    st.subheader("A BSCpE Student from Surigao del Norte State University:school:")
    st.write("I enjoy the challenges that come with crafting innovative solutions. My curiosity extends to exploring emerging technologies, ensuring I stay at the forefront of this dynamic field.")
    st.subheader("This is my socials feel free to visit them.")
    st.write(" ▶ Facebook: https://web.facebook.com/jessrel.enoc")
    st.write(" ▶Email: jessrelenoc@gmail.com")
    st.write(" ▶Contact Number:09953120281")