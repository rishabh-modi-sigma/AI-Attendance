import streamlit as st

def main():
    st.header("This is title")
    name = st.text_input("enter your name")
   
    col1, col2 = st.columns(2, gap="small")

    with col1:
       if st.button('Display my name',type='primary',key = 'btn1', width=300):
        print(f"hi my name is {name}")

    with col2:
       if st.button('Display my name', type='secondary', key = 'btn2'):
        print(f"bye {name}")

       st.markdown("""
          
       """, unsafe_allow_html=True)

main()