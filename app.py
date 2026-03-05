from flask import Flask

# Cria a aplicação Flask
app = Flask(__name__)

# Define o que aparece na página inicial
@app.route('/')
def hello_world():
    return '<h1>Olá, Mundo! Este é meu primeiro projeto com Flask!</h1>'

# Inicia o servidor
if __name__ == '__main__':
    app.run(debug=True)
