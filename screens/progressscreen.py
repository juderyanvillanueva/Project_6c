from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from screens.parentscreen import ParentScreen
from kivy.clock import Clock
import utils

Window.size = (360, 600)

Builder.load_file('screens/progressscreen.kv')


class ProgressScreen(Screen):
    def on_enter(self, *args):
        with open('.\scores/progress1.txt') as f:
            contents = f.read()
            contents = 'Correct: \n' + contents
            self.ids.scorelabel.text = contents
        with open('.\scores/errors1.txt') as f:
            errorcontents = f.read()
            errorcontents = 'Incorrect: \n' + errorcontents
            self.ids.errorlabel.text = errorcontents

        path = 'scores/progress1.txt'
        with open(path, 'r') as f:
            correct = f.read()
        correct = int(correct)

        path = 'scores/errors1.txt'
        with open(path, 'r') as f:
            incorrect = f.read()
        incorrect = int(incorrect)

        total = correct + incorrect
        diff = correct - incorrect
        perc = (correct/total) if total != 0 else 0
        percentage = perc*100
        rounded = round(percentage)
        print(rounded)

        if rounded >= 91:
            self.ids.performancelabel.text = "Performance: \n Excellent!"
        elif rounded >=85:
            self.ids.performancelabel.text = "Performance: \n Very Good"
        elif rounded >= 80:
            self.ids.performancelabel.text = "Performance: \n Good"
        elif rounded >= 75 or total == 0:
            self.ids.performancelabel.text = "Performance: \n Fair"
        elif rounded <= 74:
            self.ids.performancelabel.text = "Performance: \n Poor"


    def reset(self):
        path = 'scores/progress1.txt'
        with open(path, 'r') as f:
            correct = f.read()
        correct = int(correct)

        correct -= correct
        correct = str(correct)
        with open(path, 'w') as f:
            f.write(correct)

        path = 'scores/errors1.txt'
        with open(path, 'r') as f:
            incorrect = f.read()
        incorrect = int(correct)

        incorrect -= incorrect
        incorrect = str(incorrect)
        with open(path, 'w') as f:
            f.write(correct)

    def show_popup(self):
        self.active_dialog = MDDialog(
            title="Reset Score?",
            text="Resetting the score will lose all your score in game",
            buttons=[
                MDRaisedButton(
                    text="YES",
                    on_release=self.yes_dialog
                ),
                MDRaisedButton(
                    text="CANCEL",
                    on_release=self.cancel_dialog
                )
            ]
        )
        self.active_dialog.open()

    def yes_dialog(self, *args):
        self.active_dialog.dismiss()
        self.manager.current = '_loading_score_'
    def cancel_dialog(self, *args):
        self.active_dialog.dismiss()

    def click(self):
        utils.click.play()

    def button_press(self):
        utils.back.play()
        self.ids.backbutton.source = 'images/backpressed1.png'

    def button_release(self):
        self.ids.backbutton.source = 'images/back1.png'
        self.manager.current = '_progresslist_'
        self.manager.transition.direction = 'left'

    pass


LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')
