# -*- coding: utf-8 -*-
"""pythoncybersec project shapeai

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FJ508d3butjmStwgWYTsaW8JJc6IrQzo
"""

import recquests
#import os
from datetime import datetime

api key= 'f9a31f27ea684db0687db84b31e3ccb02':
location-input("ener the city name:")

complete_api_link="api.openweathermap.org/data/2.5/weather?id={city id}&appid={API key}
api_link=requests.get(complete_api_link)
api_data=api_link.json() 

#create variables to store and display data
temp_city=((api_data ('main')('temp')-273.15)
weather_disc=api-data['weather'][0]['description']
hmdt=api_data['main']['humidity']
wind_spd=api_data['wind']['speed']
date_time=datetime.now().strftime ("%d %b %Y  | %I:%M:%S %p " )

print("----------------------------------------------------------------")
print("Wearther stats for -{} || {} .format(location.upper(), date_time))
print("-----------------------------------------------------------------")

print("current tempoertare is:{: . 2f} deg C" .format(temp_city))
print("current weather desc    :",weather_disc)
print("current humidiy    :",hmdt,'%')
print ("current wind speed :",wind_spd, 'kmph')