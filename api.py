from flask import Flask, request, Response
from flask_cors import CORS
from managers import SessionManager, GameManager
from jwcrypto import jwt
import req

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

@app.route("/register", methods=["POST"])
def register():
    try:
        req.create_user(request.form.get('username'), request.form.get('password'))
        return Response(status=200)
    except:
        return Response(status=401)

app.run(host="0.0.0.0")