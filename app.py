import streamlit as st

def main():
    st.title("Somac")
    menu = ["home","login"]
    choice = st.selectbox("menu",menu)

    if choice == "home":
        st.subheader("home")

    elif choice == "login":
        st.subheader("login section")

if __name__ == '__main__':
    main()