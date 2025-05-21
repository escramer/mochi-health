import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()

mood = st.selectbox('What is your mood?', ['happy', 'sad', 'angry'])
if st.button('Submit'):
    df = pd.concat([df, pd.Series(['2025-05-20', mood], index=['Timestamp', 'Mood'])])
    conn.update(worksheet='Sheet1', data=df)
    #conn.reset()

df = conn.read()
st.write(df)
