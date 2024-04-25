from _tkinter import *
from tkinter import Tk, ttk, LEFT, NW, RAISED, Label
import tkinter as tk
from tkinter import NSEW

#pillow
from PIL import Image, ImageTk
#import barra de progresso do tkinter
from tkinter.ttk import Progressbar

#importando Matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

################# cores ###############

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   
co8 = "#263238"   
co9 = "#e9edf5"   

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']


# criando janela

janela = tk.Tk()
janela.title('')
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width=False, height=False)

style= ttk.Style(janela)
style.theme_use("clam")

#criar frames para divisão da tela
frameCima = tk.Frame(janela, width=1043, height=50, bg=co1, relief='flat')
frameCima.grid(row=0,column=0)

frameMeio = tk.Frame(janela, width=1043, height=361, bg=co1, pady=20, relief='raised')
frameMeio.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = tk.Frame(janela, width=1043, height=300, bg=co1, relief='flat')
frameBaixo.grid(row=2,column=1, pady=1, padx=10, sticky=NSEW)


# Trabalhando no framde Cima

#abrindo a imagem
app_img = Image.open('Logo.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_Logo = Label(frameCima, image=app_img, text="   Gestor de gastos ", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_Logo.place(x=0, y=0)


# Percentagem------------------------------
def percentagem():
    l_nome = Label(frameMeio, text="Porcentagem da Receita gasta", height=1, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    l_nome.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='#daed6b')
    style.configure("TProgressbar", thickness=25)

    bar = Progressbar(frameMeio, length=180)    
    bar.place(x=10, y=35)
    bar['value'] = 50

    valor = 50

    l_percentagem = Label(frameMeio, text="{:,.2f}%".format(valor), anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    l_percentagem.place(x=200, y=35)

# função para grafico bars -----------------------

def grafico_bar():
    lista_categorias = ['renda', 'Despesas', 'Saldo']
    lista_valores = [3000, 2000, 6236]

    #faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    #ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9)
   #create a list to collect the plt.patches data

    c = 0
    #set individual bar lables using above list
    for i in ax.patches:
       # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
        c += 1

    ax.set_xticklabels(lista_categorias,fontsize=16)

    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)




#função de resumo total
def resumo():
    valor = [500, 600, 420]

    l_linha = Label(frameCima, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#242d2e')
    l_linha.place(x=309, y=52)


percentagem()
grafico_bar()
resumo()
janela.mainloop()
