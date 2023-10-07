from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
import utils

Window.size = (360, 600)

Builder.load_file('screens/gamescreendone.kv')


class GameScreenDone(Screen):
    def click(self):
        utils.click.play()
    pass


LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')
