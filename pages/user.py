import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

st.title("このページはすべてのユーザが利用可能です。")
st.markdown(f"現在のログイン中のユーザロール： {st.session_state.role}.")