import streamlit as st

st.title("Number Input & Slider Demo")

age = st.number_input("Ente Your Age:",min_value=0,max_value=100)
rating = st.slider('Rate this session(1-10)',min_value=1,max_value=10)
st.write(f"Your Age: {age}")
st.write(f"You rated this session: {rating}/10")
