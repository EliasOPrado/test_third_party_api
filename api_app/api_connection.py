import json

import requests

# Read file
with open("users.json", "r", encoding="utf-8") as data:
    data = json.load(data)

# url = "https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.json"
# response = requests.get(url)
# data = response.json()
