import json
from random import randint

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
        self.dico = {}
    
    def entry_exists(self, entry):
        return entry in self.dico.values()
    
    def gen_token(self):
        return "".join([str(randint(0, 9)) for i in range(10)]) # a refaire en token jwt
    
    def add_session_id_couple(self, session_token, id):
        self.dico[session_token] = str(id)
    
    def get_id(self, session_token):
        if self.entry_exists(session_token):
            return self.dico[session_token]
        return None