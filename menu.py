import streamlit as st

def menu_with_redirect():
    """
    ユーザがログインしているかどうかを確認し、
    メインページにリダイレクトするか、
    メニューをレンダリングする
    """
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
    menu()

    return True

def menu():
    """
    ユーザがログインしているかに基づいて
    メニューをレンダリングするための関数をコールする
    
    """

    # ロールが未選択の場合は認証されていないユーザ向けの画面へ
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    
    authenticated_menu()


def authenticated_menu():
    """
    認証されたユーザのロールに応じてメニューを表示する
    """

    # ロールの切り替え画面へのリンク
    st.sidebar.page_link("app.py", label="Switch accounts")
    # ログイン済みユーザが全員がprofile画面を参照可能
    st.sidebar.page_link("pages/user.py", label="Yout profile")
    
    if st.session_state.role in ["admin", "super-admin"]:
        # admin,super-adminの場合はadmin画面を参照可能
        st.sidebar.page_link("pages/admin.py", label="Manage users")
        # super-adminでない場合は、super-admin画面への参照は非活性
        st.sidebar.page_link(
            "pages/super-admin.py",
            label="Manage admin access",
            disabled=st.session_state.role != "super-admin"
        )


    return 

def unauthenticated_menu():
    """
    認証されていないユーザ向けの画面を表示する
    """

    st.sidebar.page_link("app.py", label="Log in")