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
    if id is None:
        return Response(status=401)
    partie = Partie()
    partie_ser = partie.serialiser()
    gm.add_id_game_couple(id, partie_ser)
    return partie_ser

@app.route("/actions_disponibles", methods=["POST"])
def actions_disponibles():
    coord = request.form.get('coord')
    session_token = request.form.get('session_token')
    id = sm.get_id(session_token)
    if id is None:
        return Response(status=401)
    ser_game = gm.get_game(id)
    if ser_game is None:
        return Response(status=401)
    game = Partie()
    game.deserialiser(ser_game)
    return game.actions_disponibles(coord)

@app.route("/actions/retirer_dechet", methods=["POST"])
def retirer_dechet():
    coord = (request.form.get('coord'))
    session_token = request.form.get('session_token')
    id = sm.get_id(session_token)
    if id is None:
        return Response(status=401)
    ser_game = gm.get_game(id)
    if ser_game is None:
        return Response(status=401)
    game = Partie()
    game.deserialiser(ser_game)
    if not game.choix_possible("r", coord):
        return Response(status=401)
    game.retirer_dechet(coord)
    a = game.serialiser()
    return a

@app.route("/actions/fabriquer_infrastructure", methods=["POST"])
def fabriquer_infrastructure():
    coord = (request.form.get('coord'))
    session_token = request.form.get('session_token')
    id = sm.get_id(session_token)
    if id is None:
        return Response(status=401)
    game = Partie()
    game.deserialiser(ser_game)
    if not game.choix_possible("f", coord):
        return Response(status=401)
    game.fabriquer_infrastructure(coord)
    a = game.serialiser()
    return a

@app.route("/actions/recolter_minerais", methods=["POST"])
def recolter_minerais():
    coord = (request.form.get('coord'))
    session_token = request.form.get('session_token')
    id = sm.get_id(session_token)
    if id is None:
        return Response(status=401)
    game = Partie()
    game.deserialiser(ser_game)
    if not game.choix_possible("m", coord):
        return Response(status=401)
    game.recolter_minerais(coord)
    a = game.serialiser()
    return a

@app.route("/actions/planter_arbre", methods=["POST"])
def planter_arbre():
    coord = (request.form.get('coord'))
    session_token = request.form.get('session_token')
    id = sm.get_id(session_token)
    if id is None:
        return Response(status=401)
    game = Partie()
    game.deserialiser(ser_game)
    if not game.choix_possible("p", coord):
        return Response(status=401)
    game.planter_arbre(coord)
    a = game.serialiser()
    return a

@app.route("/actions/bruler_dechet", methods=["POST"])
def bruler_dechet():
    coord = (request.form.get('coord'))
    session_token = request.form.get('session_token')
    id = sm.get_id(session_token)
    if id is None:
        return Response(status=401)
    game = Partie()
    game.deserialiser(ser_game)
    if not game.choix_possible("b", coord):
        return Response(status=401)
    game.bruler_dechet(coord)
    a = game.serialiser()
    return a

@app.route("/actions/depolluer", methods=["POST"])
def depolluer():
    coord = (request.form.get('coord'))
    session_token = request.form.get('session_token')
    id = sm.get_id(session_token)
    if id is None:
        return Response(status=401)
    game = Partie()
    game.deserialiser(ser_game)
    if not game.choix_possible("d", coord):
        return Response(status=401)
    game.depolluer()
    a = game.serialiser()
    return a

@app.route("/actions/couper_arbre", methods=["POST"])
def couper_arbre():
    coord = (request.form.get('coord'))
    session_token = request.form.get('session_token')
    id = sm.get_id(session_token)
    if id is None:
        return Response(status=401)
    game = Partie()
    game.deserialiser(ser_game)
    if not game.choix_possible("c", coord):
        return Response(status=401)
    game.couper_arbre(coord)
    a = game.serialiser()
    return a

@app.route("/save") #DEBUG FUNCTION
def save_gm():
    gm.save()
    return Response(status=200)

app.run(host="0.0.0.0")