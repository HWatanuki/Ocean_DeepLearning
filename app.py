import sqlite3
from flask import Flask, g

DATABASE = "blog.db"
SECRET_KEY = "pudim"

app = Flask(__Name__)
app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(DATABASE)

@app.before_request
def pre_requisicao():
    g.bd = connectar_bd()

@app.teardown_request
def pos_requisicao(exception):
    g.bd.close()

@app.route('/')
def exibir entradas():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cur = g.bd.execute(sql)
    entradas = []
    for titulo, texto in cur.fetchall():
        entradas.append({'titulo':titulo, 'texto': texto})
    return str(entradas)
 #   return "olá mundo2 <a href='/pudim'> link</a>"

#@app.route('/pudim')
#def pudim():
 #   return "<h1 style='color:red;'>eu quero pudim</h1>"