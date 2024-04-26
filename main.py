from _tkinter import *
from tkinter import Tk, ttk, LEFT, NW, RAISED, Label, Frame
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
frameBaixo.grid(row=2,column=0, pady=0, padx=10, sticky=NSEW)

frame_Gra_pie = Frame(frameMeio, width=580, height=250, bg=co2)
frame_Gra_pie.place(x=415, y=5)


# Trabalhando no framde Cima

#abrindo a imagem
logoca =  r'C:\Users\bruno\OneDrive\Área de Trabalho\Gestor\IMGSbd\Logo.png'
app_img = Image.open(logoca)
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_Logo = Label(frameCima, image=app_img, text="   Meu Bolso Organizado ", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
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

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#242d2e')
    l_linha.place(x=309, y=52)
    l_sumario = Label(frameMeio, text="Total de Renda Mensal       ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=309, y=35)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[0]), anchor=NW, font=('Arial 17'), bg=co1, fg='#545454')
    l_sumario.place(x=309, y=70)

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#242d2e')
    l_linha.place(x=309, y=132)
    l_sumario = Label(frameMeio, text="Despesas Mensais           ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=309, y=115)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[1]), anchor=NW, font=('Arial 17'), bg=co1, fg='#545454')
    l_sumario.place(x=309, y=150)

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#242d2e')
    l_linha.place(x=309, y=207)
    l_sumario = Label(frameMeio, text="Saldo Total                 ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=309, y=190)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[2]), anchor=NW, font=('Arial 17'), bg=co1, fg='#545454')
    l_sumario.place(x=309, y=220)



# funcao grafico pie
def grafico_pie():
    #faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = [345,225,534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

   # only "explode" the 2nd slice (i.e. 'Hogs')

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_Gra_pie)
    canva_categoria.get_tk_widget().grid(row=0, column=0)



percentagem()
grafico_bar()
resumo()
grafico_pie()


# Criando frames dentro do frame baixo
frame_renda = Frame(frameBaixo, width=300, height=250, bg=co1)
frame_renda.grid(row=0,column=0)

frameOperacoes = Frame(frameBaixo, width=220, height=250, bg=co1)
frameOperacoes.grid(row=0,column=1, padx=5)

frameConfig = Frame(frameBaixo, width=300, height=250, bg=co1)
frameConfig.grid(row=0,column=2, padx=5)

# Tabela De Renda Mensal-----------------------------------------------------------------
app_tabela = Label(frameMeio, text=' Tabela de Receitas e Despesas', anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
app_tabela.place(x=5, y=309)

# funcao para exibir a tabela
def exibir_tabela():
     # creating a treeview with dual scrollbars
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = [[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,2,3,4]]
    
    global tree

    tree = ttk.Treeview(frame_renda, selectmode="extended",columns=tabela_head, show="headings")
   # vertical scrollbar
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
   # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]
    h=[30,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor='center')
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)


exibir_tabela()
janela.mainloop()

#Voce esta no laboratotio 1