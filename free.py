import requests

url = 'https://api.exchangerate.host/convert?from=USD&to=UZS'
response = requests.get(url)
data = response.json()

print(data)