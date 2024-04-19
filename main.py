#tkinter
from _tkinter import *
from tkinter import Tk, ttk, LEFT, NW, RAISED
import tkinter as tk
from tkinter import NSEW
from tkinter import Label


#pillow
from PIL import Image, ImageTk


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
frameBaixo.grid(row=1,column=0, pady=0, padx=10, sticky=NSEW)


# Trabalhando no framde Cima

#abrindo a imagem
app_img = Image.open('Log.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_Logo = Label(frameCima, image=app_img, text="  Planejamento Pessoal", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_Logo.place(x=0, y=0)


janela.mainloop()
