from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def get():
    return {"msg":"hllo", "plateau":[[1,1],[1,1]]}

@app.route("/post", methods=["POST"])
def login():
    print(request.form.items())
    return {"msg":f"bonjour "}

app.run(host="0.0.0.0")