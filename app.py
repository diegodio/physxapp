import streamlit as st
import requests
import json
from datetime import datetime, timedelta


st.set_page_config(page_title="Auth demo")
st.title("Authentication")

LINK = "https://physxapp-3dbf5-default-rtdb.firebaseio.com/"
keep_login_time = False

def save_login_time(link, sub, nome):
    # Criar uma venda (POST)
    dados = {'login_time': (datetime.now() - timedelta(hours=3)).strftime("%d/%m/%Y %H:%M:%S")}
    requisicao = requests.post(f'{link}/{sub + ' - ' + nome}/logininfo/.json', data=json.dumps(dados))
    # print(requisicao)
    # print(requisicao.text)



# Se não estiver logado (ou se o atributo nem existir), aciona login
if not getattr(st.user, "is_logged_in", False):
    if st.button("Login com Google"):
        st.login("google")   # redireciona para o IdP configurado
        keep_login_time = True
        st.stop()
        
    # 
else:
    if keep_login_time:
        save_login_time(link=LINK, sub = st.user.sub, nome=st.user.name)
        keep_login_time = False
    if st.button("Log out"):
        st.logout()
    st.write(f"Hello, {st.user.name}!")



# Daqui para baixo: usuário autenticado
st.success("Autenticado!")
st.write(st.user.to_dict())         # dados vindos do token (claims)
name = getattr(st.user, "name", "Usuário")
st.header(f"Olá, {name}")
picture = getattr(st.user, "picture", None)
if picture:
    st.image(picture, width=120)



