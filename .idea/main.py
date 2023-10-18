import requests


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "e85dd9c5c1732b1daafac70c9f0424ec"

weather_params= {
    "lat" : 50.910271,
    "lon" : -1.340160,
    "appid" : api_key,
}

response =requests.get(OWM_Endpoint, params=weather_params)
print(response.json)

