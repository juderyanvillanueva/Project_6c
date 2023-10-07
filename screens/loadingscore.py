from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.uix.video import Video

Window.size = (360, 600)

Builder.load_file('screens/loadingscore.kv')
class LoadingScore(Screen):
    pass

    def on_enter(self, *args):
        Clock.schedule_once(self.loadingscreen, 4)


    def loadingscreen(self, *args):
        self.manager.current = "_progress_screen_"

LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')