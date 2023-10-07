from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.core.text import LabelBase
from kivy.uix.image import Image
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivy.core.audio import SoundLoader
import random
import pickle
import utils

Window.size = (360, 600)

Builder.load_file('screens/gamescreen6.kv')

shake = Animation(x=1, duration=.05) + Animation(x=0, duration=.05) + Animation(x=0.7,duration=.05) + Animation(x=0.3,duration=.05) + Animation(x=0, duration=.05)


class GameScreen6(Screen):
        counter_score = 3
        corrects = 0
        errors = 0

        def on_enter(self, *args):
            positions = [(0.25, 0.8), (0.75, 0.8), (0.25, 0.5), (0.75, 0.5), (0.25, 0.2), (0.75, 0.2)]
            # Shuffle the positions randomly
            random.shuffle(positions)

            # Assign positions to buttons and images
            self.ids.right1.pos_hint = {'center_x': positions[0][0], 'center_y': positions[0][1]}
            self.ids.wrong1.pos_hint = {'center_x': positions[1][0], 'center_y': positions[1][1]}
            self.ids.right2.pos_hint = {'center_x': positions[2][0], 'center_y': positions[2][1]}
            self.ids.wrong2.pos_hint = {'center_x': positions[3][0], 'center_y': positions[3][1]}
            self.ids.right3.pos_hint = {'center_x': positions[4][0], 'center_y': positions[4][1]}
            self.ids.wrong3.pos_hint = {'center_x': positions[5][0], 'center_y': positions[5][1]}

            # Assign positions to the invisible buttons corresponding to the images
            self.ids.right1_btn.pos_hint = {'center_x': positions[0][0], 'center_y': positions[0][1]}
            self.ids.wrong1_btn.pos_hint = {'center_x': positions[1][0], 'center_y': positions[1][1]}
            self.ids.right2_btn.pos_hint = {'center_x': positions[2][0], 'center_y': positions[2][1]}
            self.ids.wrong2_btn.pos_hint = {'center_x': positions[3][0], 'center_y': positions[3][1]}
            self.ids.right3_btn.pos_hint = {'center_x': positions[4][0], 'center_y': positions[4][1]}
            self.ids.wrong3_btn.pos_hint = {'center_x': positions[5][0], 'center_y': positions[5][1]}

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
                self.ids.mutebtn.icon = 'volume-mute'
            else:
                self.ids.mutebtn.icon = 'volume-high'

        def change_icon_music(self):
            music_volume = utils.musics['main'].volume
            if music_volume == 0:
                self.ids.mutemusicbtn.icon = 'music-off'
            else:
                self.ids.mutemusicbtn.icon = 'music'

        def wrong_ans1(self):
                shake.start(self.ids.grid)
                self.ids.wrong1.source = 'gifs/wrong.png'
                utils.wrongsound.play()
        def wrong_ans2(self):
                self.ids.wrong2.source = 'gifs/wrong.png'
                utils.wrongsound.play()
        def wrong_ans3(self):
                self.ids.wrong3.source = 'gifs/wrong.png'
                utils.wrongsound.play()
        def right_ans1(self):
                self.ids.right1.source = 'gifs/correct.png'
                utils.correctsound.play()
        def right_ans2(self):
                self.ids.right2.source = 'gifs/correct.png'
                utils.correctsound.play()
        def right_ans3(self):
                self.ids.right3.source = 'gifs/correct.png'
                utils.correctsound.play()
        def incorrect(self):
            self.counter_score -= 1
            self.errors += 1
            if self.counter_score == 0:
                self.show_popup()
        def count(self):
            self.counter_score -= 1
            self.corrects +=1
            if self.counter_score == 0:
                self.show_popup()



        def show_popup(self):
            self.active_dialog = MDDialog(
                title="WELL DONE",
                text="Your effort and participation are appreciated.",
                buttons=[
                    MDRaisedButton(
                        text="OK",
                        on_release=self.dismiss_dialog
                    )
                ]
            )
            self.active_dialog.open()
            utils.correctsound.stop()
            utils.wrongsound.stop()
            utils.finish.play()

        def dismiss_dialog(self, *args):
            self.active_dialog.dismiss()
            self.active_dialog = None
            self.manager.current = '_gamescreen_done_'
            self.manager.transition.direction = 'left'
            self.ids.wrong1.source = 'gifs/orig2/surprise.gif'
            self.ids.wrong2.source = 'gifs/orig2/fear.gif'
            self.ids.wrong3.source = 'gifs/orig2/happy.gif'
            self.ids.right1.source = 'gifs/orig2/disgust.gif'
            self.ids.right2.source = 'gifs/orig2/disgust.gif'
            self.ids.right3.source = 'gifs/orig2/disgust.gif'
            self.counter_score += 3

        def button_press(self):
            utils.back.play()
            self.ids.backbutton.source = 'images/backpressed1.png'

        def button_release(self):
            self.ids.backbutton.source = 'images/back1.png'
            self.manager.current = '_childplay_screen_'
            self.manager.transition.direction = 'left'

LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')