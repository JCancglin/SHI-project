import requests, json

url = "https://api.openbrewerydb.org/breweries?by_state=texas"



response = requests.request("GET", url)

breweries = json.loads(response.text)

for brewery in breweries:
    print(brewery.get('id'))