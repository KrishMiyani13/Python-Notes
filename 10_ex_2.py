import streamlit as st
st.set_page_config(page_title = "Hello Streamlit",page_icon='🎇',layout='centered')
st.title("Faculty Profile Demo")
st.markdown('This is example shows how to use **sideBar,columns,expanders**')


st.sidebar.header("Profile Setting")

faculty_name = st.sidebar.text_input("Faculty Name",'Krish Miyani')
dep = st.sidebar.selectbox('Department',['CE','IT','CSE_DS'])
exp = st.sidebar.slider("Years of exp",0,40,10)
col1,col2 = st.columns([1,2])

with col1:
    st.write("Faculty name is")
    st.write("Department name is")
    st.write("Faculty Exp is")
with col2:
    st.write(faculty_name)
    st.write(dep)
    st.write(exp)
    with st.expander("Show Courses handeled"):
        st.write("Python-1")
        st.write("Python-2")
        st.write("DE")
        with st.expander("Show Publications"):
            st.write("1. Reseach Paper A(2024)")
            st.write("1. Reseach Paper A(2025)")
