from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.videoplayer import VideoPlayer
from kivy.clock import Clock
import mysql.connector
import bcrypt
import utils

Window.size = (360, 600)

Builder.load_file('screens/loginscreen.kv')

class LoginScreen(Screen):
    def on_enter(self, *args):
        self.ids.user.text = ''
        self.ids.password.text = ''
    def login(self):
        username = self.ids.user.text
        password = self.ids.password.text
        connection = mysql.connector.Connect(
            host="localhost",
            database="loginform",
            user="root",
            password="09093524550123"
        )

        cursor = connection.cursor()
        cursor.execute('select * from logindata')
        username_list = []
        for i in cursor.fetchall():
            username_list.append(i[0])
        if username in username_list and username != '':
            cursor.execute(f"select password from logindata where username='{username}'")
            for j in cursor:
                if password == j[0]:
                    print('Logged In Successfully')
                    utils.username = username
                    self.manager.current = '_main_screen_'
                    self.manager.transition.direction = 'right'
        else:
            self.ids.warning.text = "Incorrect Username or Password"
    pass

LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')