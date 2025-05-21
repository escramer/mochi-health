import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

mood = st.selectbox('What is your mood?', ['😊', '😠', '😕', '🎉'])
if st.button('Submit'):
    data_df = pd.DataFrame([['Hello', 'world']], columns=['Column1', 'Column2'])
    conn.update(worksheet='Sheet1', data=data_df)
    conn.reset()
    st.success('Success')

df = conn.read()
st.write(df)
