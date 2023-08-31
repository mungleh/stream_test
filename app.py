import streamlit as st
from st_pages import Page, show_pages

st.set_page_config(
    page_title="Main page",
    layout="wide"
)

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

show_pages(
    [
        Page("app.py", "Acceuil"),
        Page("pages/find_ville.py", "Find Ville"),
    ]
)

st.title("Acceuil")
