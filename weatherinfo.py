# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 12:10:15 2018

@author: NIRAV.KAKKAD
"""

import requests
import json


class WeatherInfo:
    __weather_key = 'b1b15e88fa797225412429c1c50c12' #Replace string value with your Api Key

    def __init__(self):
        print("Welcome to Weather Information")

    def current_weather(self, location):
        url = 'https://api.openweathermap.org/data/2.5/weather'

        query_params = {
            'q': location,
            'appid': self.__weather_key,
        }

        response = requests.get(url, params=query_params)
        b = json.loads(response.content)
        weather_description = b['weather'][0]['description']
        weather_details = b['main']
        wtemperature = float(weather_details['temp']) - 272.15
        whumidity = weather_details['humidity']
        return weather_description, wtemperature, whumidity


if __name__ == "__main__":
    location = "London,UK"
    obj = WeatherInfo()
    weather = obj.current_weather(location)
    print(f"The weather details for {location} are:\nType: {weather[0]}\nTemperature: %.2f Celsius\nHumidity: {weather[2]} " % (
        weather[1]))

