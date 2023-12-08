from flask import Flask, request, Response
from flask_cors import CORS
from managers import SessionManager, GameManager
from jwcrypto import jwt

sm = SessionManager()
gm = GameManager("games.json")

app = Flask(__name__)

CORS(app)

@app.route("/")
def get():
    return {"msg":"hllo", "plateau":[[1,1],[1,1]]}

@app.route("/login", methods=["POST"])
def login():
    #communiquer avec la db tout stocker etc
    session_token = sm.gen_token()
    id = 0 # choper ça avec sql
    if id is None:
        return Response(status=401)
    return {"session_token": session_token}

app.run(host="0.0.0.0")