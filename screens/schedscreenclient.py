from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.pickers import MDTimePicker
import mysql.connector
import bcrypt
import random
import sys, requests, urllib
import urllib.parse
import utils

Window.size = (360, 600)

Builder.load_file('screens/schedscreenclient.kv')


class SchedScreenClient(Screen):

    def on_enter(self):
        user = utils.username
        connection = mysql.connector.Connect(
            host="localhost",
            database="loginform",
            user="root",
            password="09093524550123"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT date, time FROM logindata WHERE username = '{user}'")
        user_data = cursor.fetchone()
        if user_data:
            date, time = user_data
            self.ids.date_label.text = f"Date: {date}"
            self.ids.time_label.text = f"Time: {time}"

        cursor.close()
        connection.close()

    def button_press(self):
        utils.back.play()
        self.ids.backbutton.source = 'images/backpressed1.png'

    def button_release(self):
        self.ids.backbutton.source = 'images/back1.png'
        self.manager.current = '_parent_screen_'
        self.manager.transition.direction = 'right'

    def click(self):
        utils.click.play()


    pass


LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')
