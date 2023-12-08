import json
from random import randint
import jwt
import datetime
import os

def file_exists(filename:str):
    try:
        f = open(filename)
        f.close()
        return True
    except FileNotFoundError:
        return False

class GameManager():
    def __init__(self, filename):
        if not file_exists(filename):
            f = open(filename, "w+")
            f.write("{}")
            f.close()
            self.dico = {}
        with open(filename) as f:
            self.dico = json.loads(f.read())
        self.filename = filename
    
    def save(self):
        with open(self.filename, "w") as f:
            f.write(json.dumps(self.dico))
    
    def add_id_game_couple(self, id, game):
        self.dico[id] = game



class SessionManager(): # renewed every api session
    def __init__(self):
        self.SECRET_KEY = os.urandom(16)
        self.dico = {}
    
    def entry_exists(self, entry):
        return entry in self.dico.values()
    
    def gen_token(self,user_id,expiration_minutes=60):
        expiration_time = datetime.datetime().utcnow() + datetime.timedelta(minutes=expiration_minutes)

        payload = {
            'user-id': user_id,
            'exp': expiration_time
        }

        token=jwt.encode(payload, self.SECRET_KEY, algorithm='HS256')

        return token

    def extract_and_decode_token(self, token):
        try:
            decoded_token = jwt.decode(token,self.SECRET_KEY,algorithms=['HS256'])
            payload = decoded_token
            return payload
        except jwt.ExpiredSignatureError:
            print("Le token a expiré")
            return None
        except jwt.InvalidTokenError:
            print("Token invalide")
            return None
    
    def add_session_id_couple(self, session_token, id):
        self.dico[session_token] = str(id)
    
    def get_id(self, session_token):
        if self.entry_exists(session_token):
            return self.dico[session_token]
        return None