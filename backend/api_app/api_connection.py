import requests


url = "https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.json"
response = requests.get(url)
data = response.json()
