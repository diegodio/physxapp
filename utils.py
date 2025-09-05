import streamlit as st
import requests
import json
from info import *
from app import *

LINK = "https://physxapp-3dbf5-default-rtdb.firebaseio.com/"

def getTurma(email):
    if email in emails_alunos_1MC:
        return '1MC'
    
def isLoggedIn():
    if getattr(st.user, "is_logged_in", False) and getattr(st.user, "email", "email_x") in emails_alunos_1MC.keys():
        return True
    else:
        return False
    
def firstLogIn():
    if isLoggedIn():
        sub = getattr(st.user, "sub", "sub_x")
        name = emails_alunos_1MC[getattr(st.user, "email", "email_x")]
        
        turma = getTurma(getattr(st.user, "email", "email_x"))

        try:
            requisicao = requests.get(f'{LINK}/{turma}/{name}/acertos_erros_fr.json')
            # print(requisicao)
            dic_requisicao = requisicao.json()
            # st.write(dic_requisicao)

            ultima_key = list(dic_requisicao.keys())[-1]
            # st.write(ultima_key)
            # st.write(dic_requisicao[ultima_key])
            # st.write(dic_requisicao[ultima_key]['acertos'])
            # st.write(dic_requisicao[ultima_key]['erros'])

            st.session_state.acertos = dic_requisicao[ultima_key]['acertos']
            st.session_state.erros = dic_requisicao[ultima_key]['erros']
        except:
            st.session_state.acertos = 0
            st.session_state.erros = 0


# def save_acertos_erros(sub, name, acertos, erros):
#     # Criar uma venda (POST)
#     dados = {'acertos': acertos, 'erros': erros}

#     # requisicao = requests.post(f'{LINK}/{sub + ' - ' + name}/acertos_erros/.json', data=json.dumps(dados))
#     # print(requisicao)
#     # print(requisicao.text)   

def save_acertos_erros(acertos, erros):
    if st.session_state.new_load == True:
        sub = getattr(st.user, "sub", "sub_x")
        name = emails_alunos_1MC[getattr(st.user, "email", "email_x")]
        turma = getTurma(getattr(st.user, "email", "email_x"))

        try:
            requisicao = requests.get(f'{LINK}/{turma}/{name}/acertos_erros_fr.json')
            dic_requisicao = requisicao.json()

            lista_keys = list(dic_requisicao.keys()) or []

            # print(lista_keys)
            # Deletar uma venda (DELETE)
            for key in lista_keys:
                url_exclude = f'{LINK}/{turma}/{name}/acertos_erros_fr/{key}.json'
                requisicao = requests.delete(url_exclude)
                # print(requisicao)
                # print(requisicao.text) 
                porcentagem = (100 * acertos / (acertos+erros)) if (acertos+erros) > 0 else 0

                nota = (porcentagem/100)*40
                
                # Editar a venda (PATCH)
                dados = {'acertos': acertos, 'erros': erros, 'porcentagem': porcentagem, 'nota': nota}
                requisicao = requests.post(f'{LINK}/{turma}/{name}/acertos_erros_fr.json', data=json.dumps(dados))  
        except:
            pass


        porcentagem = (100 * acertos / (acertos+erros)) if (acertos+erros) > 0 else 0

        nota = (porcentagem/100)*40
        
        # Editar a venda (PATCH)
        dados = {'acertos': acertos, 'erros': erros, 'porcentagem': porcentagem, 'nota': nota}
        requisicao = requests.post(f'{LINK}/{turma}/{name}/acertos_erros_fr.json', data=json.dumps(dados))

    st.session_state.new_load = False

def conferir_resposta(resposta_correta, resposta_dada):
    if resposta_correta == resposta_dada:
        # if "acertos" not in st.session_state:
        #     st.session_state.acertos = 0
        
        st.session_state.acertos += 1
        # st.write(st.session_state.acertos)
    else:
        # if "erros" not in st.session_state:
        #     st.session_state.erros = 0
        
        st.session_state.erros += 1

    save_acertos_erros(acertos = st.session_state.acertos, erros = st.session_state.erros)