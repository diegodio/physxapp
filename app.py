import streamlit as st
import requests
import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import io
import random

from images import *
from home import *
from questions import *

st.set_page_config(page_title="Auth demo", layout='wide')
st.title("PhysX")

LINK = "https://physxapp-3dbf5-default-rtdb.firebaseio.com/"


# def save_login_time(link, sub, nome):
#     # Criar uma venda (POST)
#     dados = {'login_time': (datetime.now() - timedelta(hours=3)).strftime("%d/%m/%Y %H:%M:%S")}
#     requisicao = requests.post(f'{link}/{sub + ' - ' + nome}/logininfo/.json', data=json.dumps(dados))
#     # print(requisicao)
#     # print(requisicao.text)


sidebar()    

if isLoggedIn():

    firstLogIn()

    questionResultantForce()  
        
    

    # if "acertos" not in st.session_state:
    #             st.session_state.acertos = 0


    # if "erros" not in st.session_state:
    #             st.session_state.erros = 0

        
    # st.write(f'Acertos: {st.session_state.acertos}')
    # st.write(f'Erros: {st.session_state.erros}')


#TODO
# checar se é o primeiro acesso
#se sim, criar variáveis e postar no firebase
#se não, pegar variáveis do firebase