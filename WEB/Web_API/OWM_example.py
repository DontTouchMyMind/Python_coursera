import requests


city_name = 'London'
API_key = '98075ddc8983e07b2bbf4f2c598ce8b6'

resp = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}')
data = resp.json()
print(data['main']['temp'])
