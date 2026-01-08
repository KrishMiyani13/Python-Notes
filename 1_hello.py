import streamlit as st
st.set_page_config(page_title = "Hello Streamlit",page_icon='🎇')
st.title("Welcome to Streamlit")
st.header('This is Header')
st.subheader('This is Subheader')
st.text('st.text() is used for simple fix width text')
st.write('''# Hello World!
My Name is Krish''')
st.markdown('**st.markdown()** let you use maekdown for **reach Text**')
code_example ="""
def add(a,b):
    return a+b
result = add(10,5)
print(result)"""
st.code(code_example,language="python")
