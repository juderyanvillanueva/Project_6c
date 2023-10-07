import utils
from kivy.uix.screenmanager import ScreenManager

from kivymd.app import MDApp

from screens.loginscreen import LoginScreen
from screens.registerscreen import RegisterScreen
from screens.loadscreen import LoadScreen
from screens.mainscreen import MainScreen
from screens.settingsscreen import SettingsScreen
from screens.about import About
from screens.childstartscreen import ChildStartScreen
from screens.childplayscreen import ChildPlayScreen
from screens.lesson import Lesson
from screens.gamescreen import GameScreen
from screens.gamescreen2 import GameScreen2
from screens.gamescreen3 import GameScreen3
from screens.gamescreen4 import GameScreen4
from screens.gamescreen5 import GameScreen5
from screens.gamescreen6 import GameScreen6
from screens.gamescreendone import GameScreenDone
from screens.quizscreen import QuizScreen
from screens.exercise3 import Exercise3
from screens.parentscreen import ParentScreen
from screens.progresslist import ProgressList
from screens.progressscreen import ProgressScreen
from screens.progressscreen2 import ProgressScreen2
from screens.progressscreen3 import ProgressScreen3
from screens.schedscreen import SchedScreen
from screens.schedscreenclient import SchedScreenClient
from screens.loadingscore import LoadingScore
from screens.loadingcamera import LoadingCamera
from screens.clients import Clients



from kivy.clock import Clock



class RootScreenManager(ScreenManager):
    pass


class CopyMeApp(MDApp):
    def build(self):
        return RootScreenManager()


    def save_score(self):
        path = 'scores/progress1.txt'
        with open(path, 'r') as f:
            i = f.read()
        i = int(i)

        i += 1

        i = str(i)
        with open(path, 'w') as f:
            f.write(i)

    def save_error(self):
        path = 'scores/errors1.txt'
        with open(path, 'r') as f:
            x = f.read()
        x = int(x)

        x += 1

        x = str(x)
        with open(path, 'w') as f:
            f.write(x)

    def save_score2(self):
        path = 'scores/progress2.txt'
        with open(path, 'r') as f:
            i = f.read()
        i = int(i)

        i += 1

        i = str(i)
        with open(path, 'w') as f:
            f.write(i)

    def save_error2(self):
        path = 'scores/errors2.txt'
        with open(path, 'r') as f:
            x = f.read()
        x = int(x)

        x += 1

        x = str(x)
        with open(path, 'w') as f:
            f.write(x)

    def toggle_mute(self):
        for music_name, music in utils.musics.items():
            if music.volume == 0:
                music.volume = 1  # Unmute
            else:
                music.volume = 0  # Mute

    def toggle_mute_soundfx(self):
        for sound_name, sound in utils.sounds.items():
            if sound.volume == 0:
                sound.volume = 1  # Unmute
            else:
                sound.volume = 0  # Mute
            soundvalue = sound.volume




if __name__ == '__main__':
    CopyMeApp().run()
