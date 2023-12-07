from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def get():
    return {"msg":"hllo", "plateau":[[1,1],[1,1]]}

@app.route("/login", methods=["POST"])
def login():
    #communiquer avec la db tout stocker etc
    #vérifier couple existe
    session_token = 6969
    return {"session_token": session_token}

app.run(host="0.0.0.0")