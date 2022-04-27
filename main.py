from math import trunc
import config
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# BASE_URL = "https://google.com"

City = input("What City (Full Name): ")
State = input("What State (Abreviations only):")
Country = input("What country (Abreviations only):")
location = f"{City}, {State}, {Country}"


def currentWeather():
    payload = {"q": f"{location}", "appid": f"{config.key}"}
    weather = requests.get(
        f"{BASE_URL}", params=payload, timeout=3)
    weather = weather.json()
    F = f"\nIt is {trunc((1.8 * (int(weather['main']['temp']) - 273.15)+32))} degrees farenheight in {City}"
    return print(F)
currentWeather()