from flask import Flask, request, jsonify, render_template, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    # Adicionamos timeout para evitar que o banco fique preso após o DELETE
    conn = sqlite3.connect('logistica.db', timeout=10)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    # Buscamos os dados garantindo que a conexão seja encerrada logo após
    entregas = conn.execute('SELECT * FROM entregas ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', entregas=entregas)

@app.route('/status', methods=['POST'])
def atualizar():
    data = request.json
    conn = get_db_connection()
    conn.execute("INSERT INTO entregas (motoboy, pacote, status, data) VALUES (?,?,?,?)",
                 (data['motoboy'], data['pacote'], data['status'].upper(), datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
    conn.commit()
    conn.close()
    print(f"✅ Recebido: {data['pacote']} - {data['status']}")
    return jsonify({"res": "OK"})

@app.route('/limpar', methods=['POST'])
def limpar():
    conn = get_db_connection()
    conn.execute("DELETE FROM entregas")
    # Opcional: Reinicia o contador de IDs para evitar saltos
    conn.execute("DELETE FROM sqlite_sequence WHERE name='entregas'")
    conn.commit()
    conn.close()
    print("🧹 Banco de dados resetado.")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
