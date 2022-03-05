import requests
import json
response_API = requests.get('https://api.covidactnow.org/v2/states.json?apiKey=ea36a1efe33d425db88f635e70ea17a6')
response_API = requests.get('https://api.covidactnow.org/v2/states.json?apiKey=ea36a1efe33d425db88f635e70ea17a6')
#print(response_API.staus_code)

data = response_API.text

#json.loads() function parses the data into a JSON format
json.loads(data)