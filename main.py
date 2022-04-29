from ensurepip import bootstrap
from flask import Flask, render_template,jsonify
#import bootstrap
import requests, json
import models

#collecting the data on breweries via get
url = "https://api.openbrewerydb.org/breweries?by_state=texas"
response = requests.request("GET", url)
breweriesTemp = json.loads(response.text)

breweries =  []
for b in breweriesTemp:
    breweries.append(models.breweryModel(b))



# for brewery in breweries:
#     thisBrewery = models.breweryModel(brewery)
#     print(thisBrewery.breweryName)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', breweries=breweries)

if __name__ == "__main__":
    app.run(debug=True)