# import streamlit as st

# st.title("Authentication")

# if not st.user.is_logged_in:
#     if st.button("Authenticate"):
#         st.login("google")
# else:
#     st.json(st.user)
#     st.header(f"Hello, {st.user.name}")
#     st.image(st.user.picture)


import streamlit as st

st.set_page_config(page_title="Auth demo")
st.title("Authentication")

# Se não estiver logado (ou se o atributo nem existir), aciona login
if not getattr(st.user, "is_logged_in", False):
    if st.button("Login com Google"):
        st.login("google")   # redireciona para o IdP configurado
    st.stop()

# Daqui para baixo: usuário autenticado
st.success("Autenticado!")
st.write(st.user.to_dict())         # dados vindos do token (claims)
name = getattr(st.user, "name", "Usuário")
st.header(f"Olá, {name}")
picture = getattr(st.user, "picture", None)
if picture:
    st.image(picture, width=120)
