import streamlit as st

def main():
    st.title("SOMAC Inc.")

    username = st.text_input("ID")
    password = st.text_input("Password",type='paasword')
    login = st.button("Login")

if __name__ == '__main__':
    main()