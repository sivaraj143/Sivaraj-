import streamlit as st
st.title("Sivaraj")
st.sidebar.title("Give us your valid Info")
st.sidebar.text_input("Enter your Email ")
if(st.sidebar.button("Register")):
    st.sidebar.success("Your email verified")
st.text_input("Enter your name ")
st.date_input("Enter your DOB ")
st.text_input("Enter your Mobile Number")
st.radio("Select your Gender",["Male","Female","Others"])
if(st.button("Submit")):
    st.write("Thank you for yor registration")
    st.success("Your Completed successfully")
