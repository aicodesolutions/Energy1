import streamlit as st

st.set_page_config(page_title="Home", layout="wide")
pages = {
    "OPS Dashboard" : [
        st.Page("dashboard.py", title="dashboard"),
        st.Page("chat.py", title="chat")
    ],
}

pg = st.navigation(pages)
pg.run()