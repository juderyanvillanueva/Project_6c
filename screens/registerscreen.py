from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.videoplayer import VideoPlayer
from kivy.clock import Clock
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
import mysql.connector
import bcrypt
import random
import sys, requests, urllib
import urllib.parse

Window.size = (360, 600)

Builder.load_file('screens/registerscreen.kv')

class RegisterScreen(Screen):
    otp = random.randrange(100000, 1000000)
    def button_press(self):
        self.ids.backbutton.source = 'images/backpressed1.png'

    def button_release(self):
        self.ids.backbutton.source = 'images/back1.png'
        self.manager.current = '_login_screen_'
        self.manager.transition.direction = 'right'

    def show_popup(self):
        username = self.ids.user.text
        phone = self.ids.phone.text
        full_name = self.ids.full_name.text
        password = self.ids.password.text
        confirm_password = self.ids.confirm_pass.text
        connection = mysql.connector.Connect(
            host="localhost",
            database="loginform",
            user="root",
            password="09093524550123"
        )
        cursor = connection.cursor()

        # Check if the username already exists in the database
        cursor.execute("SELECT username FROM logindata WHERE username = %s", (username,))
        existing_user = cursor.fetchone()

        cursor.close()
        connection.close()
        if not username or not phone or not full_name or not password or not confirm_password:
            self.ids.warning.text = 'All text fields are required'
        elif existing_user:
            self.ids.warning.text = 'Username already taken'
        elif password != confirm_password:
            self.ids.warning.text = 'Passwords do not match'
        else:
            self.otp = random.randrange(100000, 1000000)
            print(self.otp)
            # self.send_message()

            text_input = MDTextField(
                hint_text="Enter OTP here",
                helper_text="This is an OTP input field",
                helper_text_mode="on_focus",
                size_hint=(None, None),
                width=200,
            )

            self.active_dialog = MDDialog(
                title="Enter OTP",
                type="custom",
                content_cls=text_input,
                buttons=[
                    MDRaisedButton(
                        text="SUBMIT",
                        on_release=lambda instance: self.check_otp(instance, text_input.text),
                    ),
                    MDRaisedButton(
                        text="CANCEL",
                        on_release=self.dismiss_dialog
                    )
                ]
            )
            self.active_dialog.open()

        cursor.close()
        connection.close()



    def check_otp(self, instance, user_input):
        self.active_dialog.dismiss()
        self.active_dialog = None

        try:
            user = int(user_input)
            if user == self.otp:
                self.register(instance)
                print('Registered Successfully!')
            else:
                print('Access Denied')
        except ValueError:
            print('Invalid OTP input, please enter a numeric OTP.')


    def dismiss_dialog(self, *args):
        self.active_dialog.dismiss()
        self.active_dialog = None

    def send_message(self):
        key = '79a970cd95ab3055433260e8618a84fb4891fb60'
        phone = '+63' + self.ids.phone.text
        message = self.otp
        device = '502'
        sim = '0'
        priority = '1'
        print('Sending Message...')
        params = (
            ('key', key),
            ('phone', phone),
            ('message', message),
            ('device', device),
            ('sim', sim),
            ('priority', priority)
        )
        path = 'https://sms.teamssprogram.com/api/send?' + urllib.parse.urlencode(params)
        requests.post(path)
        print('Message Sent!')

    def register(self, instance):
        username = self.ids.user.text
        phone_number = '+63' + self.ids.phone.text
        full_name = self.ids.full_name.text
        password = self.ids.password.text
        confirm_password = self.ids.confirm_pass.text

        if password == confirm_password:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            connection = mysql.connector.Connect(
                host="localhost",
                database="loginform",
                user="root",
                password="09093524550123"
            )

            cursor = connection.cursor()

            query = "INSERT INTO logindata (username, password, full_name, phone_number) VALUES (%s, %s, %s, %s)"
            values = (username, password, full_name, phone_number)
            cursor.execute(query, values)
            connection.commit()

            print(f"User '{username}' registered successfully.")
            print(f"Phone Number: {phone_number}")

            cursor.close()
            connection.close()
            self.manager.current = '_login_screen_'
            self.manager.transition.direction = 'left'
        else:
            print("Passwords do not match.")




    pass

LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')