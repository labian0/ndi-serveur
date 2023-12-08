from flask import Flask, request, Response
from flask_cors import CORS
from managers import SessionManager, GameManager
from jwcrypto import jwt
import req
from main import *

sm = SessionManager()
gm = GameManager("games.json")

app = Flask(__name__)

CORS(app)

@app.route("/")
def get():
    return {"msg":"hllo", "plateau":[[1,1],[1,1]]}

@app.route("/login", methods=["POST"])
def login():
    id = req.check_exist(request.form.get('username'))
    if not id:
        return Response(status=401)
    session_token = sm.gen_token(id)
    sm.add_session_id_couple(session_token, id)
    return {"session_token": session_token}

@app.route("/register", methods=["POST"])
def register():
    id = req.check_exist(request.form.get('username'))
    if id:
        return Response(status=401)
    try:
        req.create_user(request.form.get('username'), request.form.get('password'))
        return Response(status=200)
    except:
        return Response(status=401)

@app.route("/init_plateau", methods=["POST"])
def init_plateau():
    session_token = request.form.get('session_token')
    if session_token is None:
        return Response(status=401)
    id = sm.get_id(session_token)
    plateau = Plateau()
    plateau_serialise = plateau.serialiser()
    gm.add_id_game_couple(id, plateau_serialise)
    return {"plateau": plateau_serialise}

@app.route("/plateau_golmon", methods=["GET"])
def plateau_golmon():
    plateau = Plateau()
    plateau_serialise = plateau.serialiser()
    return {"plateau": plateau_serialise}

@app.route("/save") #DEBUG FUNCTION
def save_gm():
    gm.save()
    return Response(status=200)

app.run(host="0.0.0.0")