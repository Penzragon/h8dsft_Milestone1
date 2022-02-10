import streamlit as st


def app():
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown(
            "<h1 style='text-align: center;'>Home Page</h1>", unsafe_allow_html=True
        )

        st.markdown(
            "<p style='text-align: center;'>Made with <span style='color: red'>♥️</span> by <b>Rifky Aliffa</b></p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p style='text-align: center;'>This simple app is a project about data visualization dashboard and hypothesis testing where you can get an insight from a data. The dataset used in this project is a supermarket sales dataset which has recorded in 3 different branches for 3 months data. Dataset can be downloaded from <a href='https://www.kaggle.com/aungpyaeap/supermarket-sales'>Kaggle</a>.</p>",
            unsafe_allow_html=True,
        )

        with st.expander("Please Open🔓"):
            st.write(
                "<b>The app is far from optimized</b>. If you find any issue or have any suggestion, you can report it on the <a href='https://github.com/Penzragon'>GitHub repository</a> or contact me on <a href='https://www.linkedin.com/in/rifkyaliffa/'>LinkedIn</a>. Thank you!",
                unsafe_allow_html=True,
            )

        with st.expander("DO NOT OPEN!⛔"):
            st.markdown(
                "<h3 style='text-align: center;'>Told ya!</h3>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<img src='https://media3.giphy.com/media/l0amJzVHIAfl7jMDos/giphy.gif?cid=ecf05e47wn6qux56otl3dc50n4yn4d4kegpf4woknc2m5d0y&rid=giphy.gif&ct=g' width='100%'/>",
                unsafe_allow_html=True,
            )
