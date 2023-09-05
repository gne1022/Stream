import streamlit as st

def main():
    st.title("Somac")
    menu = ["home","login"]
    choice = st.selectbox("menu",menu)

    username = st.text_input("username")
    password = st.text_input("password")

if __name__ == '__main__':
    main()