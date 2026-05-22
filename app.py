<<<<<<< HEAD
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ju20112006",
    database="saudeplus"
)

@app.route("/")
def home():
    return "Backend conectado ao MySQL!"

@app.route("/cadastro", methods=["POST"])
def cadastro():

    dados = request.json

    cursor = conexao.cursor()

    sql = """
    INSERT INTO usuarios (nome, email, telefone, plano, senha)
    VALUES (%s, %s, %s, %s, %s)
    """

    valores = (
        dados["nome"],
        dados["email"],
        dados["telefone"],
        dados["plano"],
        dados["senha"]
    )

    cursor.execute(sql, valores)
    conexao.commit()

    return jsonify({
        "mensagem": "Usuário cadastrado com sucesso!"
    })
@app.route("/login", methods=["POST"])
def login():

    dados = request.json

    cursor = conexao.cursor(dictionary=True)

    sql = """
    SELECT * FROM usuarios
    WHERE email = %s AND senha = %s
    """

    valores = (
        dados["email"],
        dados["senha"]
    )

    cursor.execute(sql, valores)

    usuario = cursor.fetchone()

    if usuario:
        return jsonify({
            "success": True,
            "usuario": usuario
        })

    return jsonify({
        "success": False,
        "mensagem": "E-mail ou senha incorretos"
    })
if __name__ == "__main__":
=======
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ju20112006",
    database="saudeplus"
)

@app.route("/")
def home():
    return "Backend conectado ao MySQL!"

@app.route("/cadastro", methods=["POST"])
def cadastro():

    dados = request.json

    cursor = conexao.cursor()

    sql = """
    INSERT INTO usuarios (nome, email, telefone, plano, senha)
    VALUES (%s, %s, %s, %s, %s)
    """

    valores = (
        dados["nome"],
        dados["email"],
        dados["telefone"],
        dados["plano"],
        dados["senha"]
    )

    cursor.execute(sql, valores)
    conexao.commit()

    return jsonify({
        "mensagem": "Usuário cadastrado com sucesso!"
    })
@app.route("/login", methods=["POST"])
def login():

    dados = request.json

    cursor = conexao.cursor(dictionary=True)

    sql = """
    SELECT * FROM usuarios
    WHERE email = %s AND senha = %s
    """

    valores = (
        dados["email"],
        dados["senha"]
    )

    cursor.execute(sql, valores)

    usuario = cursor.fetchone()

    if usuario:
        return jsonify({
            "success": True,
            "usuario": usuario
        })

    return jsonify({
        "success": False,
        "mensagem": "E-mail ou senha incorretos"
    })
if __name__ == "__main__":
>>>>>>> bf110d567f6f181621370c7983c6161933701340
    app.run(debug=True)