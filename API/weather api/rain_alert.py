import requests
OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "API_KEY"

r = requests.get('http://api.openweathermap.org/geo/1.0/direct?q=Nashik&limit=5&appid=dbb1f710077a33e1f43d758d20d93138')
response = r.json()

weather_para = {
    'lat' : response[0]['lat'],
    'lon' : response[0]['lon'],
    'appid' : api_key,
}

res = requests.get(OWM_endpoint, params=weather_para)
res.raise_for_status()
response1 = res.json()

print(response1['weather'][0]['description'])

