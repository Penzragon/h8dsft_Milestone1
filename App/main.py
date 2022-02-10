import streamlit as st
import visualization
import hypothesis
import home

st.set_page_config(
    page_title="Milestone 1 - Rifky Aliffa",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.linkedin.com/in/rifkyaliffa/",
        "Report a bug": "https://github.com/Penzragon",
        "About": "### Simple Data Visualization Dashboard & Hypothesis Testing App - Rifky Aliffa",
    },
)

PAGES = {"Home": home, "Visualization": visualization, "Hypothesis Testing": hypothesis}

st.sidebar.title("Navigation")
selection = st.sidebar.selectbox("Choose a page", list(PAGES.keys()))

page = PAGES[selection]
page.app()
