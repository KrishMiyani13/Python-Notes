import streamlit as st
from datetime import date,time

st.title("Date, Time & File Uploader Demo")

exam_date = st.date_input("Select Exam Date:",value=date.today())
start_time = st.time_input("Exam Start Time:",value=time(9,0))

uplode_file = st.file_uploader("Uplode CSV File:",type=['csv'])

st.write(f"Selected Exam Date: {exam_date}")
st.write(f"Exam Start Time : {start_time}")

if uplode_file is not None:
    st.success("File Uploded")
    st.write("Fiel Name",uplode_file.name)
    st.write("Fiel Type",uplode_file.type)
