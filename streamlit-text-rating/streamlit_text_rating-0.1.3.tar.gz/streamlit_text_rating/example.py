from st_text_rater import rate_text
import streamlit as st

for text in ["Is this helpful?","Do you like it?"]:
    response=rate_text(text=text)
    st.write(f"response --> {response}")