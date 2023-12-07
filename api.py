from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def get():
    return {"msg":"hllo", "plateau":[[1,1],[1,1]]}

@app.route("/login", methods=["POST"])
def login():
    return {"msg":f"bonjour {request.form.get('username') + ' ' + request.form.get('password')}"}

app.run(host="0.0.0.0")