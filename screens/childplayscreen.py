from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
import subprocess
from subprocess import call
import os
import utils
from screens.camerahappy import CameraHappy

Window.size = (360, 600)

Builder.load_file('screens/childplayscreen.kv')


class ChildPlayScreen(Screen):
    # def open_py_file(self):
    #     file_path = "screens/camerahappy.py"
    #     subprocess.Popen(["python", file_path])
    def on_enter(self, *args):
        utils.stop_ex()
        utils.stop_extwo()
        utils.bgmusic()
    def click(self):
        utils.click.play()
    def camera(self):
        utils.stop_music()
    def button_press(self):
        utils.back.play()
        self.ids.backbutton.source = 'images/backpressed1.png'

    def button_release(self):
        self.ids.backbutton.source = 'images/back1.png'
        self.manager.current = '_childstart_screen_'
        self.manager.transition.direction = 'right'

    def start(self):
        self.manager.current = '_game_screen_'
        self.manager.transition.direction = 'right'


LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')