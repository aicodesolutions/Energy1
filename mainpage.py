import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = ["Meera", "Coordinator"]

def login():
    st.header("Log in")
    role = st.selectbox("Choose User Profile", ROLES)
    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()
def logout():
    st.session_state.role = None
    st.rerun()
role = st.session_state.role
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
request_1 = st.Page(
    "user1/dashboard1.py",
    title="Dashboard",
    icon=":material/help:",
    default=(role == "Meera"),
)
request_2 = st.Page(
    "user1/user1chat.py", title="Chat", icon=":material/bug_report:"
)
respond_1 = st.Page(
    "user2/dashboard2.py",
    title="Dashboard",
    icon=":material/healing:",
    default=(role == "Coordinator"),
)

account_pages = [logout_page]
request_pages = [request_1, request_2]
respond_pages = [respond_1]
st.title("Intelligent Energy Assistant")
st.logo("images/horizontal_blue1.png", icon_image="images/icon_blue1.png")
page_dict = {}
if st.session_state.role in ["Meera"]:
    page_dict["Meera"] = request_pages
if st.session_state.role in ["Coordinator"]:
    page_dict["Coordinator"] = respond_pages
if len(page_dict) > 0:
    pg = st.navigation( page_dict | {"Account": account_pages})
else:
    pg = st.navigation([st.Page(login)])
pg.run()