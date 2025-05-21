import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
if 'df' not in st.session_state:
    st.session_state.df = conn.read()

mood = st.selectbox('What is your mood?', ['happy', 'sad', 'angry'])
if st.button('Submit'):
    row = pd.DataFrame({'Timestamp': [str(date.today())], 'Mood': [mood]})
    st.session_state.df = pd.concat([st.session_state.df, row], ignore_index=True)
    conn.update(worksheet='Sheet1', data=st.session_state.df)

counts = st.session_state.df.Mood.value_counts()
fig, ax = plt.subplots()
ax.bar(counts.index, counts)
st.pyplot(fig)
