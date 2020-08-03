import requests

ngrok_url = 'https://d08edbb387de.ngrok.io'
endpoint = f'{ngrok_url}/box_office'

r=requests.post(endpoint, json={})
print(r.json()["data"])