import requests
from pynotifier import Notification

url = "http://api.openweathermap.org/data/2.5/weather?q="
cityname = "vijayawada"
api_key = "4fabde64cdfb942dcb67235f32583956"
data = requests.get(url+cityname+'&appid='+api_key).json()
city = data['name']
country = data['sys']['country']
temparature = data['main']['temp_max']-273.15
weather = data['weather'][0]['main']
wind_speed = float(data['wind']['speed'])
humidity = data['main']['humidity']
pressure = data['main']['pressure']
if data["cod"] != "404":
    Notification(
        title = city+" "+country,
        description = f'{temparature}C {weather}  Wind speed{wind_speed}\n Humidity {humidity}\n Pressure {pressure}',
        duration=100,
        icon_path='Weather.ico',
        urgency= Notification.URGENCY_CRITICAL).send()
else:
      print("City not found !!") 
