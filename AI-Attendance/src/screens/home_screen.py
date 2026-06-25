import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout, style_background_home

def home_screen():

    header_home()
    style_background_home()
    style_base_layout()

    col1, col2 = st.columns(2)

    with col1:
        st.header("I'm")
        st.image("src/static/img/student.png", width=120)
        if st.button('Teacher Portal'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    with col2:
        st.header("I'm teacher")
        st.image("src/static/img/teacher.png", width=145)
        if st.button('Student Portal'):
            st.session_state['login_type'] = 'student'
            st.rerun()