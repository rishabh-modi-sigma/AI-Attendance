import streamlit as st

def header_home():

    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)

    st.image("src/static/img/app_logo.png", width=120)

    st.markdown("""
    <h1 style="
        text-align:center;
        color:#E0E3FF;
        margin-top:20px;
    ">
        SNAP <br> CLASS
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)