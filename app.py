from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

# ==========================================
# ⚠️ BANCO DE DADOS LOCAL DESATIVADO PARA O RENDER
# Quando você criar o banco online (no Railway/Aiven), 
# basta trocar os dados abaixo e tirar os '#' do início das linhas.
# ==========================================
# conexao = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Ju20112006",
#     database="saudeplus"
# )

@app.route("/")
def home():
    return "Backend do Flask funcionando online no Render!"

@app.route("/cadastro", methods=["POST"])
def cadastro():
    dados = request.json
    
    # Comentado temporariamente para o Render não dar erro de banco vazio
    """
    cursor = conexao.cursor()
    sql = "INSERT INTO usuarios (nome, email, telefone, plano, senha) VALUES (%s, %s, %s, %s, %s)"
    valores = (dados["nome"], dados["email"], dados["telefone"], dados["plano"], dados["senha"])
    cursor.execute(sql, valores)
    conexao.commit()
    """

    return jsonify({
        "mensagem": "Rota de cadastro acessada! (Aguardando banco de dados online)"
    })

@app.route("/login", methods=["POST"])
def login():
    dados = request.json
    
    # Comentado temporariamente para o Render não dar erro de banco vazio
    """
    cursor = conexao.cursor(dictionary=True)
    sql = "SELECT * FROM usuarios WHERE email = %s AND senha = %s"
    valores = (dados["email"], dados["senha"])
    cursor.execute(sql, valores)
    usuario = cursor.fetchone()
    if usuario:
        return jsonify({"success": True, "usuario": usuario})
    """

    # Simulação temporária para testes enquanto o banco está offline
    if dados.get("email") == "teste@email.com" and dados.get("senha") == "123":
        return jsonify({
            "success": True, 
            "usuario": {"nome": "Usuário Teste", "email": "teste@email.com"}
        })

    return jsonify({
        "success": False,
        "mensagem": "E-mail ou senha incorretos (ou banco offline)"
    })

# Configuração essencial para o Render conseguir definir a porta do servidor
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)