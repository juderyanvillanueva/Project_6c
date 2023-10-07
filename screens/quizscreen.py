import utils
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from utils import save_error
from utils import save_score
import random

Window.size = (360, 600)

Builder.load_file('screens/quizscreen.kv')

shake = Animation(x=20, duration=.05) + Animation(x=-20, duration=.05) + Animation(x=20, duration=.05) + Animation(
    x=-20, duration=.05) + Animation(x=0, duration=.05)
class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super(QuizScreen, self).__init__(**kwargs)
        self.sentences = {"Your sibling took your favorite toy without asking.": "Angry",
                          "You accidentally stepped on something slimy with your bare feet.": "Disgust",
                          "Your best friend invites you to a surprise birthday party.": "Happy",
                          "You dropped and broke your favorite mug that had sentimental value.": "Sad",
                          "Your parents tell you that they are taking you on a surprise vacation": "Surprise",
                          "You hear a loud and unexpected noise while walking in a dark alley.": "Fear"}  #Expand this list; App won't run if less than 4.
        self.choices = list(self.sentences.keys())
        random.shuffle(self.choices)
        self.answers = list(self.sentences.values())
        self.indicator = 0
        self.errors = 0
        self.mute = False

        Clock.schedule_once(self.update)

    def on_enter(self, *args):
        utils.stop_music()
        utils.extwo_music()
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

    def wrong(self):
        self.errors += 1
        utils.wrongsound.play()
        save_error()
        shake.start(self.ids.grid)

    def Mute(self):
        if self.mute == False:
            self.mute = True
        else:
            self.mute = False

    def update(self, dt=0):
        if self.indicator > len(self.answers) - 1:
            self.ids.phrases.text = "Congratulations, you made {} errors!".format(self.errors)
            self.ids.one.text = "Restart?"
            self.ids.two.text = ""
            self.ids.three.text = ""
            self.ids.four.text = "Quit?"
            return

        self.ids.phrases.text = self.choices[self.indicator]
        self.answer = self.sentences[self.choices[self.indicator]]
        self.all_choices = []

        self.all_choices.append(self.answer)

        for i in range(3):
            fake = self.answer
            while fake in self.all_choices:
                fake = self.answers[random.randint(0, len(self.answers) - 1)]
            self.all_choices.append(fake)

        random.shuffle(self.all_choices)

        self.ids.one.text = self.all_choices[0]
        self.ids.two.text = self.all_choices[1]
        self.ids.three.text = self.all_choices[2]
        self.ids.four.text = self.all_choices[3]

        self.ids.one.background_color = random.random(), random.random(), random.random(), 1
        self.ids.two.background_color = random.random(), random.random(), random.random(), 1
        self.ids.three.background_color = random.random(), random.random(), random.random(), 1
        self.ids.four.background_color = random.random(), random.random(), random.random(), 1

    def one(self):
        if self.ids.one.text == "Restart?":  # None of the words should translate into "Restart?"
            random.shuffle(self.choices)
            self.indicator = 0
            self.errors = 0
            self.update()

        elif self.answer == self.all_choices[0]:
            self.indicator += 1
            if self.mute == False: utils.correctsound.play()
            save_score()
            self.update()

        else:
            self.wrong()

    def two(self):

        if self.ids.one.text == "Restart?":
            pass
        elif self.answer == self.all_choices[1]:
            self.indicator += 1
            self.update()
            save_score()
            if self.mute == False: utils.correctsound.play()
        else:
            self.wrong()

    def three(self):

        if self.ids.one.text == "Restart?":
            pass

        elif self.answer == self.all_choices[2]:
            self.indicator += 1
            self.update()
            save_score()
            if self.mute == False: utils.correctsound.play()
        else:
            self.wrong()

    def four(self):

        if self.ids.one.text == "Restart?":
            pass

        elif self.answer == self.all_choices[3]:
            self.indicator += 1
            self.update()
            save_score()
            if self.mute == False: utils.correctsound.play()
        else:
            self.wrong()

LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')