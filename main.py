import streamlit as st

mood = st.selectbox('What is your moood?', ['😊', '😠', '😕', '🎉'])
if st.button('Submit'):
    st.balloons()
    
