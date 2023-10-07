from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.clock import Clock
import subprocess
from subprocess import call
from kivy.uix.video import Video

Window.size = (360, 600)

Builder.load_file('screens/loadingcamera.kv')
class LoadingCamera(Screen):
    pass

    def on_enter(self, *args):
        Clock.schedule_once(self.open_py_file, 4)

    def open_py_file(self, *args):
        file_path = "screens/camerahappy.py"
        subprocess.Popen(["python", file_path])

LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')