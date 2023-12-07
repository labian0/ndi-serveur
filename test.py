import requests

r = requests.post("http://91.92.252.31:5000/post", data={"name":"gurvan"})
print(r.json())