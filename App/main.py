import streamlit as st

st.set_page_config(
    page_title="Milestone 1 - Rifky Aliffa",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.linkedin.com/in/rifkyaliffa/",
        "Report a bug": "https://github.com/Penzragon",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)

PAGES = {"Visualization": "visualization", "Hypothesis Testing": "hypothesis"}

st.sidebar.title("Navigation")
selection = st.sidebar.selectbox("Choose a page", list(PAGES.keys()))
