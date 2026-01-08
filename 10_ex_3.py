import streamlit as st
import math
import random
st.set_page_config(page_title = "Input",page_icon='🎇',layout='centered')
st.title("Text Input demo")

name = st.text_input("Enter Your Name:")
add  = st.text_area("Any Comment :")
while name != "stop":
    if name and add:
        name = st.text_input("Enter Your Name:",key=random.random()*10)
        add  = st.text_area("Any Comment :",key=random.random()*10)
        if add and name:
            st.write(f"Name : {name}")
            st.write(f"Comment,**{add}**")
