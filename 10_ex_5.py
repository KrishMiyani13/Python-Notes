import streamlit as st
st.title("Selection Widget deom")
course = st.selectbox("Select Course: ",['Python','FSd',"DE",'PS'])
pre = st.multiselect(
'Preferred dayt for Extra Lectures',['Monday','Tuesday','wednesday','Thruseday','Friday','Stureday'])
delivery = st.radio("Preferred Delievery Mode",['offline','online','hybride'])
sub = st.checkbox("Sub to Course updates")
st.write("===")
st.write(f"**course:** {course}")
st.write(f"**Prefered Days:** {','.join(pre) if pre else None}")
st.write(f"Delivery {delivery}")
