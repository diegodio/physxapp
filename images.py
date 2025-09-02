import matplotlib.patches as patches
import matplotlib.pyplot as plt
import random
import io
import streamlit as st

def create_image():   
    lado_fig = 8

    fig, ax = plt.subplots(figsize=(lado_fig, lado_fig))

    return fig, ax



def create_square(ax, center_x, center_y, side, linewidth=10, edgecolor = 'black', facecolor = 'white'):

    cx, cy = 0.5, 0.5
    lado = 0.4

    # Coordenadas do canto inferior esquerdo
    x = center_x - side/2
    y = center_y - side/2


    # Caixa branca com borda preta
    box = patches.Rectangle((x, y), side, side, linewidth = linewidth, edgecolor = edgecolor, facecolor = facecolor)
    ax.add_patch(box)

    return ax, center_x, center_y, side

def plotar_flecha(ax, n_vetores_dir = 1, n_vetores_esq = 2, center_x = 0.5, center_y = 0.5, side = 0.4):
    
    vetores_dir = [True] * n_vetores_dir + [False] * (5-n_vetores_dir)

    random.shuffle(vetores_dir)

    list_force_values_right = []

    for index, vetor in enumerate(vetores_dir):
        if vetor:
            x_start = center_x+side/2
            y_start = 0.7 - 0.1*index

            x_end = 0.9
            y_end = 0.7 - 0.1*index

            espaco_flecha_texto = 0.02
            valor_vetor = random.randint(1,10)

            list_force_values_right.append(valor_vetor)

            ax.annotate('', xy=(x_end, y_end), xytext=(x_start, y_start),
                        arrowprops=dict(facecolor='red', edgecolor='red', width=6, headwidth=25, headlength=20, shrinkA=0, shrinkB=0))
            ax.text(x_end+espaco_flecha_texto, y_end, f"{valor_vetor} N", va="center", ha="left", fontsize=14, color="red")

    ##########
    vetores_esq = [True] * n_vetores_esq + [False] * (5-n_vetores_esq)

    random.shuffle(vetores_esq)

    list_force_values_left = []

    for index, vetor in enumerate(vetores_esq):
        if vetor:
            x_start = center_x-side/2
            y_start = 0.7 - 0.1*index

            x_end = 0.1
            y_end = 0.7 - 0.1*index

            espaco_flecha_texto = 0.08
            valor_vetor = random.randint(1,10)

            list_force_values_left.append(valor_vetor)

            ax.annotate('', xy=(x_end, y_end), xytext=(x_start, y_start),
                        arrowprops=dict(facecolor='red', edgecolor='red', width=6, headwidth=25, headlength=20, shrinkA=0, shrinkB=0))
            ax.text(x_end-espaco_flecha_texto, y_end, f"{valor_vetor} N", va="center", ha="left", fontsize=14, color="red")

    total_force_right = sum(list_force_values_right)
    total_force_left = sum(list_force_values_left)

    return ax, total_force_right, total_force_left

def clean_and_show_image(fig, ax):

    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    fig.patch.set_facecolor("lightgray")

    # Salvar em buffer
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)

    # Mostrar no Streamlit
    st.image(buf)