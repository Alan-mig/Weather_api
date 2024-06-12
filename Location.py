from weatherException import WeatherException
import urllib

class Location(WeatherException):
    def __init__(self,city):
       # self.__country = "Plese enter a destanation"
        self.__city = "Please enter a destanation"
       # self.country = self.country
        self.city = city
        super().__init__()
    #@property
    #def country(self):
    #    return self.__country

    #@country.setter
    #def country(self, value):
     #   if value == '':
     #       raise WeatherException
     #   else:
     #       self.__country =value
    @property
    def city(self):
        return self.__city


    @city.setter
    def city(self,text):
        if text == None:
            raise WeatherException
        elif text=="":
                raise WeatherException

        else:
            if text !=None:
                self.__city = text




class Weather:
    def __init__(self,temp,clouds,wind):
        self.__tempe = "No temperature"
        self.__clouds = "No cloudes"
        self.__wind = "No wind"
        self.temp = temp
        self.clouds = clouds
        self.wind = wind

    def __str__(self):
        return ("Temperature="  +str(self.temp)+ " " "cloudes="+str(self.clouds)+" wind="""+str(self.wind))

    @property
    def temp(self):
        return self.__temp

    @property
    def clouds(self):
        return self.__clouds

    @property
    def wind(self):
        return self.__wind

    @temp.setter
    def temp(self, data):
        if data == '':
            raise WeatherException
        else:
            self.__temp = data

    @clouds.setter
    def clouds(self, data):
        if data == '':
            raise WeatherException
        else:
            self.__clouds = data

    @wind.setter
    def wind(self, data):
        if data == '':
            raise WeatherException
        else:
            self.__wind = data
""""
try:
    Mylocation = Location('')
    Mylocation.city
except WeatherException:
    print('problem')
finally:
    print('continue')
"""
