import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import matplotlib.pyplot as plt

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
if 'df' not in st.session_state:
    st.session_state.df = conn.read()

mood = st.selectbox('What is your mood?', ['happy', 'sad', 'angry'])
if st.button('Submit'):
    row = pd.DataFrame({'Timestamp': ['2025-05-20'], 'Mood': [mood]})
    st.session_state.df = pd.concat([st.session_state.df, row], ignore_index=True)
    conn.update(worksheet='Sheet1', data=st.session_state.df)

fig, ax = plt.subplots()
ax.bar(['hello', 'world'], [5, 7])
st.pyplot(fig)
