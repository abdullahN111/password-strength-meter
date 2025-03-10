import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
st.title("🔐 Password Strength Meter")

st.markdown("""
## 🔥 Welcome to the Password Strength Meter!

Easily check the strength of your password and get useful suggestions to enhance its security. 

We’ll provide expert tips to help you create a **Strong and Secure password 🔑**.
""")

password = st.text_input("Enter your password:", type="password")

if "warnings" not in st.session_state:
    st.session_state.warnings = []
if "score" not in st.session_state:
    st.session_state.score = 0
if "show_suggestions" not in st.session_state:
    st.session_state.show_suggestions = False  

if st.button("Check Strength"):
    st.session_state.warnings = []
    st.session_state.score = 0
    st.session_state.show_suggestions = False  

    if password:
        if len(password) >= 8:
            st.session_state.score += 1
        else:
            st.session_state.warnings.append("Password should be at least 8 characters long!")

        if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
            st.session_state.score += 1
        else:
            st.session_state.warnings.append("Password must contain both uppercase and lowercase characters!")

        if re.search(r'\d', password):
            st.session_state.score += 1
        else:
            st.session_state.warnings.append("Password must contain at least one digit!")

        if re.search(r'[!@#$%^&*()_\-+=|?/.,~`{}]', password):
            st.session_state.score += 1
        else:
            st.session_state.warnings.append("Password must contain at least one special character!")

        if st.session_state.score == 4:
            st.success("✅ Your password is strong.")
        elif st.session_state.score == 3:
            st.warning("⚠️ Your password's strength is medium. It could be stronger.")
        else:
            st.error("❌ Your password is weak. Please make it stronger.")

if st.session_state.score < 4:
    if st.button("Show Suggestions"):
        st.session_state.show_suggestions = True 

if st.session_state.show_suggestions:
    for warning in st.session_state.warnings:
        st.warning(warning)
