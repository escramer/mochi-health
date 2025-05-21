import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

mood = st.selectbox('What is your mood?', ['😊', '😠', '😕', '🎉'])
if st.button('Submit'):
    st.balloons()

df = conn.read()
st.write(df)
