# -*- coding: utf-8 -*-

# Tested on Python 3.8.0

# Ver    Date        Author
# v0.1   06.11.2020  Bartlomiej Duda   # python console version
# v0.2   06.11.2020  Bartlomiej Duda   # android app
# v0.3   09.11.2020  Bartlomiej Duda 
# v0.4   09.11.2020  Bartlomiej Duda   # layout fixes

import os
import sys
import math



def bd_logger(in_str):
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%d-%m-%Y %H:%M:%S") + " " + in_str)    
    

def format_result(in_minutes):
    res_mod = in_minutes % 60
    res_div = math.floor((in_minutes / 60))
    
    out_str = "Hours: " + str(res_div) + " Minutes: " + str(res_mod)
    return str(out_str)


import kivy
kivy.require('1.11.1') 

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

from kivy.config import Config  
Config.set('graphics', 'resizable', True)




class BDLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(BDLayout, self).__init__(**kwargs)
        self.main_window = FloatLayout(size=(300, 300))
        self.add_widget(self.main_window)        
        
        self.global_minutes_counter = 0
  
  
        
        #BUTTON ADD MINUTES
        self.main_window.butt1 = Button(text="Add/Substract minutes", 
                                         font_size=40, 
                                         pos_hint={'center_y': 0.3, 'center_x': 0.5},
                                         size_hint =(.6, .1)
                                         )
        self.add_widget(self.main_window.butt1)
        
        
        #BUTTON CLEAR RESULTS
        self.main_window.butt2 = Button(text="Clear results", 
                                         font_size=30, 
                                         pos_hint={'center_y': 0.1, 'center_x': 0.5},
                                         size_hint =(.4, .1)
                                         )  
        self.add_widget(self.main_window.butt2)   
        
        
        #CURRENT VALUE LABEL
        self.main_window.current_value = Label(text="Current value: \nHours: 0, Minutes: 0",
                                               pos_hint={'center_y': 0.9, 'center_x': 0.5},
                                               font_size=50,
                                               size_hint =(.6, .1)
                                               )   
        self.add_widget(self.main_window.current_value) 
        
        
        #INPUT BOX
        self.main_window.textinput = TextInput(text='',
                                               pos_hint={'center_y': 0.7, 'center_x': 0.5},
                                               font_size=50,
                                               size_hint =(.3, .1)
                                               )  
        self.add_widget(self.main_window.textinput) 
      

        #add/substract minutes function
        def callback_butt1(instance):
            try:
                minutes = int(self.main_window.textinput.text)
            except:
                print("ERROR! Couldn't read int value!")
                return
            
            if (self.global_minutes_counter + minutes) < 0:
                print("ERROR! Value lower than zero! Aborting!")
                return
            
            self.global_minutes_counter += minutes 
            

            
            self.main_window.textinput.text = ""
            self.main_window.current_value.text = "Current value: \n" + format_result(self.global_minutes_counter)
            
            
            
        def callback_butt2(instance):
            self.global_minutes_counter = 0
            self.main_window.current_value.text = "Current value: \n" + format_result(self.global_minutes_counter)

        self.main_window.butt1.bind(on_press=callback_butt1)
        self.main_window.butt2.bind(on_press=callback_butt2)


class MyApp(App):

    def build(self):
        self.title = 'Minutes Counter'
        return BDLayout()

if __name__ == '__main__':
    MyApp().run()