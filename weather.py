from taipy.gui import Gui 
import requests
import json


response = requests.get('https://ipinfo.io')  #The response is a json file
print(response.text)
data = json.loads(response.text)
city = data.get('city')
loc = data.get('loc')
Location = loc.split(',')
Longtitude = Location[0]
Latitude = Location[1]
print(Longtitude)
print(Latitude)
path = 'https://api.open-meteo.com/v1/forecast?latitude='+str(Longtitude)+'&longitude='+str(Latitude)+'&current=temperature_2m'
response_api = requests.get(path)
data_api = json.loads(response_api.text)
temperature = round(data_api['current']['temperature_2m'])
time = data_api['current']['time']

index = """
<|text-right|
<|{"Logo.jpg"}|image|width = 8vw|> 
>

<|text-center|
<|Your Location|>

<|City : |><|{city}|>

<|Weather : |><|{temperature}|><| C|>

>
"""
app = Gui(page = index)


if __name__ == "__main__":
    app.run(use_reloader=True) 