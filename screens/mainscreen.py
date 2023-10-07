from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.videoplayer import VideoPlayer
from kivy.clock import Clock
import utils

Window.size = (360, 600)

Builder.load_file('screens/mainscreen.kv')

class MainScreen(Screen):
    def on_enter(self, *args):
        if utils.username == 'a':
            self.ids.childbutton.text = 'Exercises'
            self.ids.parentbutton.text = 'Clients'
        else:
            self.ids.childbutton.text = 'CHILD'
            self.ids.parentbutton.text = 'PARENT'

    def click(self):
        utils.click.play()
    pass

LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')