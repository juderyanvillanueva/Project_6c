from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
import utils

Window.size = (360, 600)

Builder.load_file('screens/settingsscreen.kv')


class SettingsScreen(Screen):
    def on_enter(self, *args):
        initial_volume = utils.sounds['back'].volume
        self.ids.soundslider.value = initial_volume
        self.ids.soundslider.bind(value=lambda instance, value: self.update_sound_volume(value))

        music_volume = utils.musics['main'].volume
        self.ids.musicslider.value = music_volume
        self.ids.musicslider.bind(value=lambda instance, value: self.update_music_volume(value))
        self.change_icon()
        self.change_icon_music()

    def update_music_icon(self, value):
        if value == 0:
            self.ids.mutemusicbtn.icon = 'music-off'
        else:
            self.ids.mutemusicbtn.icon = 'music'

    def update_sound_volume(self, value):
        # Update the volume of the sound based on the slider value
        for sound_name, sound in utils.sounds.items():
            sound.volume = value

    def update_music_volume(self, value):
        # Update the volume of the sound based on the slider value
        for music_name, music in utils.musics.items():
            music.volume = value

    def change_icon(self):
        initial_volume = utils.sounds['back'].volume
        if initial_volume == 0:
            self.ids.mutebtn.icon = 'volume-mute'  # Unmute
            self.ids.soundslider.value = 0
        else:
            self.ids.mutebtn.icon = 'volume-high'
            self.ids.soundslider.value = initial_volume
    def change_icon_music(self):
        music_volume = utils.musics['main'].volume
        if music_volume == 0:
            self.ids.mutemusicbtn.icon = 'music-off'
            self.ids.musicslider.value = 0
        else:
            self.ids.mutemusicbtn.icon = 'music'
            self.ids.musicslider.value = music_volume

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
