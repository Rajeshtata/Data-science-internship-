import streamlit as st
import os
import base64

st.set_page_config(page_title='My Portfolio ')

st.title(":blue[Rajesh Tata] :two_hearts:")
st.subheader("Intern at Innomatics Research Lab....")
st.write("I am a data scientist Intern and my main objective is to learn new skills and looking for an opportunity as Data Scientist where I can use my knowledge and experience in statistics, machine learning and Deep Learning... ")
st.snow()

st.subheader('Contact')
st.write('Email: thatharajesh431@gmail.com')
st.write("Ph-Number : 9985829191")
btn=st.button("Social media")
if btn == True:
    st.write('LinkedIn: https://www.linkedin.com/in/rajesh-tata-87447b224/ ')
    st.write('Instagram: https://www.instagram.com/its_rajesh_thatha/?next=%2F')
    st.success('Successfully completed', icon="✅")
    st.balloons()
