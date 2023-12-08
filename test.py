import requests

json = requests.post("http://91.92.252.31:5000/login", data={"username": "apagnan", "password": "apagnan"}).json()
r = requests.post("http://91.92.252.31:5000/init_plateau", data=json)
print(r.status_code)
game = r.json()
print(game)