from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
import subprocess
from subprocess import call
import os
from screens.camerahappy import CameraHappy
import utils

Window.size = (360, 600)

Builder.load_file('screens/progresslist.kv')


class ProgressList(Screen):
    def button_press(self):
        utils.back.play()
        self.ids.backbutton.source = 'images/backpressed1.png'

    def button_release(self):
        self.ids.backbutton.source = 'images/back1.png'
        self.manager.current = '_parent_screen_'
        self.manager.transition.direction = 'right'

    def click(self):
        utils.click.play()


LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')