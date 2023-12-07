from flask import Flask

app = Flask(__name__)

@app.route("/")
def get():
    return [[1,1],[1,1]]

app.run()