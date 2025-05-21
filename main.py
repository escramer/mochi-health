import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

mood = st.selectbox('What is your mood?', ['😊', '😠', '😕', '🎉'])
if st.button('Submit'):
    conn.update(worksheet='Sheet1', data=[['Hello', 'world']])

df = conn.read()
st.write(df)
