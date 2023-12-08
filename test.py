import requests

r = requests.post("http://92.91.252.31:5000/register", data={"username": "rodolphe", "password": "schneider"})
print(r.status_code)