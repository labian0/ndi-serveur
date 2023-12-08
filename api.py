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
    exists = req.check_exist(request.form.get('username'))
    if not exists:
        return Response(status=401)
    id = req.check_user(request.form.get("username"), request.form.get("password"))
    if id is None:        
        return Response(status=401)
    session_token = sm.gen_token(id)
    sm.add_session_id_couple(session_token, id)
    return {"session_token": session_token}

@app.route("/register", methods=["POST"])
def register():
    exists = req.check_exist(request.form.get('username'))
    if exists:
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
    partie = Partie()
    partie_ser = partie.serialiser()
    gm.add_id_game_couple(id, partie_ser)
    return partie_ser

@app.route("/actions/retirer_dechet", methods=["POST"])
def retirer_dechet():
    session_token = request.form.get('session_token')
    id = sm.get_id(session_token)
    if id is None:
        return Response(status=401)


@app.route("/actions/fabriquer_infrastructure", methods=["POST"])
def fabriquer_infrastructure():
    session_token = request.form.get('session_token')
    id = sm.get_id(session_token)
    if id is None:
        return Response(status=401)
    game = Partie()
    game.deserialiser(ser_game)
    game.fabriquer_infrastructure(coord)
    a = game.serialiser


@app.route("/actions/recolter_minerais", methods=["POST"])
def recolter_minerais():
    session_token = request.form.get('session_token')
    id = sm.get_id(session_token)
    if id is None:
        return Response(status=401)
    game = Partie()
    game.deserialiser(ser_game)
    game.recolter_minerais(coord)
    a = game.serialiser

@app.route("/actions/planter_arbre", methods=["POST"])
def planter_arbre():
    session_token = request.form.get('session_token')
    id = sm.get_id(session_token)
    if id is None:
        return Response(status=401)
    game = Partie()
    game.deserialiser(ser_game)
    game.planter_arbre(coord)
    a = game.serialiser


@app.route("/actions/bruler_dechet", methods=["POST"])
def bruler_dechet():
    session_token = request.form.get('session_token')
    id = sm.get_id(session_token)
    if id is None:
        return Response(status=401)
    game = Partie()
    game.deserialiser(ser_game)
    game.bruler_dechet(coord)
    a = game.serialiser

@app.route("/actions/depolluer", methods=["POST"])
def depolluer():
    session_token = request.form.get('session_token')
    id = sm.get_id(session_token)
    if id is None:
        return Response(status=401)
    game = Partie()
    game.deserialiser(ser_game)
    game.depolluer()
    a = game.serialiser

@app.route("/actions/couper_arbre", methods=["POST"])
def couper_arbre():
    session_token = request.form.get('session_token')
    id = sm.get_id(session_token)
    if id is None:
        return Response(status=401)
    game = Partie()
    game.deserialiser(ser_game)
    game.couper_arbre(coord)
    a = game.serialiser


@app.route("/plateau_golmon", methods=["GET"])
def plateau_golmon():
    partie = Partie()
    partie_ser = partie.serialiser()
    gm.add_id_game_couple(id, partie_ser)
    return partie_ser

@app.route("/save") #DEBUG FUNCTION
def save_gm():
    gm.save()
    return Response(status=200)

app.run(host="0.0.0.0")