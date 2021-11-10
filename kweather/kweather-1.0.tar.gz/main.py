'''
Module main.py is the entry module for building KWeather with the buildozer
tools chain.  It provides the environment from which the application
runs and does all housekeeping such as imports.
'''
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.network.urlrequest import UrlRequest
from controller import KWeatherController

__version__ = 1.0

class KWeather(FloatLayout):
    '''
    KWeather inherits from FloatLayout and is root layout defined in
    kweather.kv using the Kivy language.  Name kweather.kv is part of
    KweatherApp below and without 'App'.
    '''
    pass

class KWeatherApp(App):
    '''
    The KWeatherApp class is the class that creates and instantiates
    user interface class KWeather.  It also provides methods for making
    internet url requests and returning the data to KWeather interface
    via Restful API request get method.
    '''
    def build(self):
        '''
        Method build automatically recreates the KWeather Object
        for instantiation by KWeather app.
        '''
        self.kw = KWeather()
        self.ktrl = KWeatherController() 
        return self.kw

    def update_weather(self):
        '''
        Method update_weather updates the KWeather display for all data.
        '''
        data = self.ktrl.weather_api_update()
        self.kw.ids.tempwidget.text = data[0]
        self.kw.ids.wind.text = data[1]
        self.kw.ids.vis.text = data[2]
        self.kw.ids.pre.text = data[3]
        self.kw.ids.hum.text = data[4]
        self.kw.ids.upperbox.tempcolor = data[5]
        self.kw.ids.stamp.text = data[6]
    

if __name__=='__main__':
        weather = KWeatherApp() # instantiate app
        weather.run() # execute app run method

