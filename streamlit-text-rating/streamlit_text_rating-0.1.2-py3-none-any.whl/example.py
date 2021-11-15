from __init__ import streamlit_text_rating
import streamlit as st

for text in ["Is this helpful?","Do you like it?"]:
    response=streamlit_text_rating(text=text)
    st.write(f"response --> {response}")