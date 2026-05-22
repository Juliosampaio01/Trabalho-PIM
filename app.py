from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

# ==========================================
# 🗄️ BANCO DE DADOS ONLINE (AIVEN) CONFIGURADO!
# ==========================================
conexao = mysql.connector.connect(
    host="mysql-129bdf86-trabalho-pim.b.aivencloud.com",
    user="avnadmin",
    password="AVNS_iHy3Dyy2mnbvL3rF6Q_",
    database="defaultdb",
    port=12828,
    ssl_disabled=False
)

# Criar a tabela automaticamente na nuvem se ela não existir
try:
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            telefone VARCHAR(20),
            plano VARCHAR(50),
            senha VARCHAR(255) NOT NULL
        );
    """)
    conexao.commit()
    cursor.close()
    print("Tabela 'usuarios' verificada/criada com sucesso no Aiven!")
except Exception as e:
    print(f"Erro ao inicializar a tabela: {e}")


@app.route("/")
def home():
    return "Backend do Flask funcionando online no Render!"

@app.route("/cadastro", methods=["POST"])
def cadastro():
    dados = request.json
    
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO usuarios (nome, email, telefone, plano, senha) VALUES (%s, %s, %s, %s, %s)"
        valores = (dados["nome"], dados["email"], dados["telefone"], dados["plano"], dados["senha"])
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        
        return jsonify({
            "success": True,
            "mensagem": "Usuário cadastrado com sucesso no banco online!"
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "mensagem": f"Erro ao cadastrar no banco: {str(e)}"
        }), 500

@app.route("/login", methods=["POST"])
def login():
    dados = request.json
    
    try:
        cursor = conexao.cursor(dictionary=True)
        sql = "SELECT * FROM usuarios WHERE email = %s AND senha = %s"
        valores = (dados["email"], dados["senha"])
        cursor.execute(sql, valores)
        usuario = cursor.fetchone()
        cursor.close()
        
        if usuario:
            return jsonify({"success": True, "usuario": usuario})
        else:
            return jsonify({"success": False, "mensagem": "E-mail ou senha incorretos."})
            
    except Exception as e:
        return jsonify({
            "success": False,
            "mensagem": f"Erro ao conectar ao banco de dados: {str(e)}"
        }), 500

# Configuração essencial para o Render conseguir definir a porta do servidor
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)