import sqlite3 as lite

con = lite.connect('dados.db')

#tabela de categoria
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")


#tabela de receitas
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, Valor DECIMAL)")


#tabela de gastos
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, Valor DECIMAL)")

