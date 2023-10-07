from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.button import MDIconButton
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import subprocess
import utils
from subprocess import call
from utils import attempts
from utils import angry
from utils import happy
from utils import surprise
from utils import fear
from utils import disgust
from utils import sad

import cv2
from kivymd.uix.label import MDLabel
from kivy.core.text import LabelBase
import keras.utils as image
import numpy as np
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog

from keras.models import model_from_json
#from android.permissions import request_permissions, Permission



model = model_from_json(open("facial_expression_model_structure.json", "r").read())
model.load_weights("facial_expression_model_weights.h5")


Window.size = (360, 600)
class CameraHappy(MDApp):
    active_dialog = None
    counter = 6
    instance = 0

    def on_start(self):
        attempts()
        Clock.schedule_interval(self.count_time, 1)
        utils.main.play()

    def mutemusic(self):
        if utils.main.volume == 0:
            utils.main.volume = 1  # Unmute
            self.mutemusicbtn.icon = 'music'
        else:
            utils.main.volume = 0  # Mute
            self.mutemusicbtn.icon = 'music-off'

    def mutesound(self):
        for sound_name, sound in utils.sounds.items():
            if sound.volume == 0:
                sound.volume = 1  # Unmute
                self.mutebtn.icon = 'volume-high'
            else:
                sound.volume = 0  # Unmute
                self.mutebtn.icon = 'volume-mute'

    def count_time(self, *args):
        if self.label.text == "Happy":
            angry()
        elif self.label.text == "Sad":
            happy()
        elif self.label.text == "Angry":
            surprise()
        elif self.label.text == "Fear":
            fear()
        elif self.label.text == "Surprised":
            disgust()
        elif self.label.text == "Disgusted":
            sad()

    def build(self):
        # request_permissions([
        # Permission.CAMERA,
        # Permission.WRITE_EXTERNAL_STORAGE,
        # Permission.READ_EXTERNAL_STORAGE])
        self.root = Builder.load_file("camerahappy.kv")
        self.mutebtn = self.root.ids.mutebtn
        self.mutemusicbtn = self.root.ids.mutemusicbtn
        self.image = self.root.ids.image
        self.label = self.root.ids.label
        self.expression = self.root.ids.expression
        self.face_facade = cv2.CascadeClassifier("screens/haarcascade_frontalface_default.xml")
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1.0/60.0)
        return self.root

    def load_video(self, *args):
        emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
        ret, frame = self.capture.read()
        # Frame initialize
        self.image_frame = frame
        gray = frame.copy()
        face = self.face_facade.detectMultiScale(gray, 1.8, 4)
        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (200, 0, 0), 3)
            detected_face = self.image_frame[int(y):int(y+h), int(x):int(x+w)]
            detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY)
            detected_face = cv2.resize(detected_face, (48, 48))
            img_pixels = image.img_to_array(detected_face)
            img_pixels = np.expand_dims(img_pixels, axis=0)

            img_pixels /= 255
            predictions = model.predict(img_pixels)
            max_index = np.argmax(predictions[0])
            emotion = emotions[max_index]
            print(emotion)
            print(self.instance)
            cv2.putText(gray, emotion, (int(x), int(y)), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            if emotion == 'happy' and self.label.text == 'Happy':
                self.instance += 1
                if emotion == 'happy' and self.counter == 6 and self.instance >= 10:
                    if not self.active_dialog:  # Check if no active dialog exists
                        self.show_popup()
                        self.label.text = 'Sad'
                        self.expression.source = 'gifs/orig2/sad.gif'
            if emotion == 'sad' and self.label.text == 'Sad':
                self.instance += 1
                if emotion == 'sad' and self.counter == 5 and self.instance >= 3:
                    if not self.active_dialog:  # Check if no active dialog exists
                        self.show_popup()
                        self.label.text = 'Angry'
                        self.expression.source = 'gifs/orig2/angry.gif'
            if emotion == 'angry' and self.label.text == 'Angry':
                self.instance += 1
                if emotion == 'angry' and self.counter == 4 and self.instance >= 15:
                    if not self.active_dialog:  # Check if no active dialog exists
                        self.show_popup()
                        self.label.text = 'Fear'
                        self.expression.source = 'gifs/orig2/fear.gif'
            if emotion == 'fear' and self.label.text == 'Fear':
                self.instance += 1
                if emotion == 'fear' and self.counter == 3 and self.instance >= 2:
                    if not self.active_dialog:  # Check if no active dialog exists
                        self.show_popup()
                        self.label.text = 'Surprised'
                        self.expression.source = 'gifs/orig2/surprise.gif'
            if emotion == 'surprise' and self.label.text == 'Surprised':
                self.instance += 1
                if emotion == 'surprise' and self.counter == 2 and self.instance >= 2:
                    if not self.active_dialog:  # Check if no active dialog exists
                        self.show_popup()
                        self.label.text = 'Disgusted'
                        self.expression.source = 'gifs/orig2/disgust.gif'
            if emotion == 'disgust':
                self.instance += 1
                if emotion == 'disgust' and self.counter == 1 and self.instance >= 1:
                    if not self.active_dialog:  # Check if no active dialog exists
                        self.last_popup()
                        self.label.text = ''

        buffer = cv2.flip(frame, 0).tostring()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture

        if frame is not None:
            # Your processing code for a valid frame
            gray = frame.copy()
            # ... rest of your code ...
        else:
            # Handle the case when frame is None (e.g., log a message or take appropriate action)
            pass

    def show_popup(self):
        utils.ex3.play()
        self.active_dialog = MDDialog(
            title="GOOD JOB!",
            text="You're doing Great!",
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=self.dismiss_dialog
                )
            ]
        )
        self.active_dialog.open()

    def last_popup(self):
        utils.finish.play()
        self.active_dialog = MDDialog(
            title="GOOD JOB!",
            text="Would you like to try again?",
            buttons=[
                MDRaisedButton(
                    text="YES",
                    on_release=self.restart_app
                ),
                MDRaisedButton(
                    text="No",
                    on_release=self.last_dismiss_dialog
                )
            ]
        )
        self.active_dialog.open()

    def dismiss_dialog(self, *args):
        self.instance = 0
        self.active_dialog.dismiss()
        self.active_dialog = None
        self.counter -= 1
    def last_dismiss_dialog(self, *args):
        self.active_dialog.dismiss()
        self.active_dialog = None
        attempts()
        CameraHappy().stop()

    def restart_app(self, *args):
        attempts()
        CameraHappy().stop()
        file_path = "screens/camerahappy.py"
        subprocess.Popen(["python", file_path])



LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')

if __name__ == '__main__':
    CameraHappy().run()
