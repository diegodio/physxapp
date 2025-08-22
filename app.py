import streamlit as st

st.title("Authentication")

if not st.user.is_logged_in:
    if st.button("Authenticate"):
        st.login("google")
else:
    st.json(st.user)
    st.header(f"Hello, {st.user.name}")
    st.image(st.user.picture)
