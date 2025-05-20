import streamlit as st

mood = st.selectbox('What is your mood?', ['😊', '😠', '😕', '🎉'])
if st.button('Submit'):
    st.balloons()
    
