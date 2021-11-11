from flask import Flask

app = Flask("meu_app")

@app.route('/')
def index():
    return "olá mundo2 <a href='/pudim'> link</a>"

@app.route('/pudim')
def pudim():
    return "<h1 style='color:red;'>eu quero pudim</h1>"