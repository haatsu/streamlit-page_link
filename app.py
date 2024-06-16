import streamlit as st
from menu import menu

# ロールの初期値はNone
if "role" not in st.session_state:
    st.session_state.role = None

def set_role():
    """
    コールされたら、選択されたロールを保存する
    """
    st.session_state.role = st.session_state._role

# セレクトボックスの定義
st.selectbox(
    "Select your roke: ",
    [None, "user", "admin", "super-admin"],
    key="_role",
    on_change=set_role
)

menu()