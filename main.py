import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()
df

mood = st.selectbox('What is your mood?', ['happy', 'sad', 'angry'])
if st.button('Submit'):
    row = pd.DataFrame({'Timestamp': ['2025-05-20'], 'Mood': [mood]})
    df = pd.concat([df, row], ignore_index=True)
    conn.update(worksheet='Sheet1', data=df)
    #conn.reset()

df = conn.read()
st.write(df)
