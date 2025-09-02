import streamlit as st
from utils import *

def sideBarNotLoggedIn():
    with st.sidebar:
        st.title('PhysX')

        if st.button("Login com Google"):
                st.login("google")
                st.stop()

def sidebarScore():
    acertos = getattr(st.session_state, "acertos", 0)
    erros = getattr(st.session_state, "erros", 0)
    porcentagem = (100 * acertos / (acertos+erros)) if (acertos+erros) > 0 else 0

    with st.sidebar:
        st.write(f'✅: {acertos}')
        st.write(f'❌: {erros}')
        st.write(f'📊: {porcentagem:.2f}%')

def sidebarRanking():
    
    turma = getTurma(getattr(st.user, "email", "email_x"))

    try:
        requisicao = requests.get(f'{LINK}/{turma}/.json')
        dic_requisicao = requisicao.json()
        with st.sidebar:
            for nome in list(dic_requisicao.keys()):
                key = list(dic_requisicao[nome]['acertos_erros_fr'].keys())
                acertos = dic_requisicao[nome]['acertos_erros_fr'][key[0]]['acertos']

                # st.write(key[0])
                st.write(f'{nome} - {acertos}')

                
        ultima_key = list(dic_requisicao.keys())[-1]
    except:
        pass
    # st.write(dic_requisicao[ultima_key])
    # st.write(dic_requisicao[ultima_key]['acertos'])
    # st.write(dic_requisicao[ultima_key]['erros'])





def sideBarLoggedIn():
    with st.sidebar:
        st.title('PhysX')

        col1, col2, col3 = st.columns([2,2,3])
        with col1:
                
            picture = getattr(st.user, "picture", None)
            if picture:
                st.image(picture, width=50)
        with col2:
            given_name = getattr(st.user, "given_name", "Usuário")
            st.write(given_name)    
        
        with col3:
            if st.button("Log out"):
                st.logout()

        sidebarScore()
        sidebarRanking()

    given_name = getattr(st.user, "given_name", "Usuário")
    st.header(f"Olá, {given_name}!")

def sidebar():
    if not isLoggedIn():
        sideBarNotLoggedIn()

    else:
        sideBarLoggedIn()




# def sidebar():
#     with st.sidebar:
#         st.title('PhysX')

#         if not isLoggedIn():
#             if st.button("Login com Google"):
#                 st.login("google")
#                 st.stop()
#         else:
#             col1, col2, col3 = st.columns([2,2,3])
#             with col1:
                    
#                 picture = getattr(st.user, "picture", None)
#                 if picture:
#                     st.image(picture, width=50)
#             with col2:
#                 given_name = getattr(st.user, "given_name", "Usuário")
#                 st.write(given_name)    
            
#             with col3:
#                 if st.button("Log out"):
#                     st.logout()


#     if st.user.is_logged_in:
#         given_name = getattr(st.user, "given_name", "Usuário")
#         st.header(f"Olá, {given_name}!")

#     return getattr(st.user, "is_logged_in", False)