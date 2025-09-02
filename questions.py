import streamlit as st
from images import *
from utils import conferir_resposta




def questionResultantForce():
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = create_image()
        ax, center_x, center_y, side = create_square(ax=ax, center_x = 0.5, center_y = 0.5, side = 0.4, linewidth=10, edgecolor = 'black', facecolor = 'lightgray')

        n_vetores_dir = random.randint(0,5)
        n_vetores_esq = random.randint(0,5)

        ax, total_force_right, total_force_left = plotar_flecha(ax=ax, n_vetores_dir = n_vetores_dir, n_vetores_esq = n_vetores_esq, center_x = center_x, center_y = center_y, side = side)

        clean_and_show_image(fig = fig, ax = ax)

    with col2:
        st.write('Qual a força resultante?')

        # st.write(f'total de forças para a direita {total_force_right}')
        # st.write(f'total de forças para a esquerda {total_force_left}')

        resposta_correta_int = total_force_right-total_force_left

        resposta_correta = str(resposta_correta_int) + " N"

        # st.write(f'Força resultando = {resposta_correta_int} N')

        possiveis_respostas = [total_force_right, 
                            total_force_left, 
                            total_force_right+random.randint(0,5), 
                            total_force_left+random.randint(0,5), 
                            total_force_right-random.randint(0,5), 
                            total_force_left-random.randint(0,5), 
                            resposta_correta_int+random.randint(0,5), 
                            resposta_correta_int-random.randint(0,5),
                            -1*resposta_correta_int,
                            -1*total_force_right, 
                            -1*total_force_left, 
                            ]

        # st.write(possiveis_respostas)

        possiveis_respostas = set(possiveis_respostas)
        possiveis_respostas.discard(resposta_correta_int)
        # st.write(possiveis_respostas)

        possiveis_respostas = list(possiveis_respostas)
        
        possiveis_respostas = random.sample(possiveis_respostas, 3)

        # st.write(possiveis_respostas)

        possiveis_respostas.append(resposta_correta_int)

        random.shuffle(possiveis_respostas)

        possiveis_respostas = [str(item) + ' N' for item in possiveis_respostas]

        # st.write(possiveis_respostas)



        colunas = st.columns(4)
        # st.write(resposta_correta)
        for coluna, possivel_resposta in zip(colunas,possiveis_respostas):
            with coluna:
                st.button(f'{possivel_resposta}', 
                        key = possivel_resposta, 
                        type = 'secondary', 
                        on_click=conferir_resposta,
                        kwargs={"resposta_correta": resposta_correta, "resposta_dada": possivel_resposta})
                