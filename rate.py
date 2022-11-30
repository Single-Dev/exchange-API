import requests
api_key = "b863074847bc53b416aeb008"

def get_rate(currency_1):
    currency_2 = "UZS"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{currency_1}/{currency_2}"
    response = requests.get(url)
    jsondata = response.json()["conversion_rate"]
    return jsondata
