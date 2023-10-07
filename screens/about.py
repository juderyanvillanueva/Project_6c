from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
import utils

Window.size = (360, 600)

Builder.load_file('screens/about.kv')


class About(Screen):
    def on_enter(self, *args):
        print("s")
    def click(self):
        utils.click.play()
    def button_press(self):
        utils.back.play()
        self.ids.backbutton.source = 'images/backpressed1.png'

    def button_release(self):
        self.ids.backbutton.source = 'images/back1.png'
        self.manager.current = '_settings_screen_'

    def change_icon(self):
        initial_volume = utils.sounds['back'].volume
        if initial_volume == 0:
            self.ids.mutebtn.icon = 'volume-mute'
        else:
            self.ids.mutebtn.icon = 'volume-high'

    def change_icon_music(self):
        music_volume = utils.musics['main'].volume
        if music_volume == 0:
            self.ids.mutemusicbtn.icon = 'music-off'
        else:
            self.ids.mutemusicbtn.icon = 'music'

    pass


LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')
