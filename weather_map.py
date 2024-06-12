import urllib.request
import urllib.parse
import json
from Location import Weather
import  Location
import  weatherException
import http



def getWeather(location):
    #location = input('please enter the city'),Location
   # country = input('please enter country')
    ob = f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&APPID=382e89972127ac135c010f0522e28268'
    # f =f'http://aapi.openweathermap.org/data/2.5/weather?={city},{country}%s&APPID=382e89972127ac135c010f0522e28268'
    respond = urllib.request.urlopen(ob)
    data = json.load(respond)
    #Myweather = Weather(data['main']['temp'],data['clouds'],data['wind'])
    #print( Myweather)
    print (Weather(data['main']['temp'],data['clouds'],data['wind']))
   # print(data['main']['temp'])
   # print(data['clouds'])
   # print(data['wind'])

#Insted of using the space bar use the encoding of %20
try:
    Myloction = Location.Location("Eilat")
    Myweather1 = getWeather(Myloction.city)

except weatherException.WeatherException as e:
    print("Excpection was caught", e)
except ValueError as e:
    print("value error",e)
except FileNotFoundError as e:
    print('file not found',e)
except urllib.error.HTTPError as e:
    print('Enter a valid country',e)
except http.client.InvalidURL  as e:
    print('Worng url encoding!',e)
except NameError as e:
    print('Enter a valid country',e)
except SyntaxError as e:
    print("syntaxError",e)
else:
    print(f"This is the weather in {Myloction.city}  ")
finally:
   print('Thanks for using our service!')


