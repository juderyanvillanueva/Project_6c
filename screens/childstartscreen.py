from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
import utils

Window.size = (360, 600)

Builder.load_file('screens/childstartscreen.kv')


class ChildStartScreen(Screen):
    def click(self):
        utils.click.play()
    def button_press(self):
        utils.back.play()
        self.ids.backbutton.source = 'images/backpressed1.png'

    def button_release(self):
        self.ids.backbutton.source = 'images/back1.png'
        self.manager.current = '_main_screen_'
    pass


LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')
