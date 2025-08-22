import streamlit as st
import requests
import json
from datetime import datetime

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



sub = st.user.sub

LINK = "https://physxapp-3dbf5-default-rtdb.firebaseio.com/"

# Criar uma venda (POST)
dados = {'login_time': datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
requisicao = requests.post(f'{LINK}/{sub}/logininfo/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)

