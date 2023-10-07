from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.pickers import MDTimePicker
import utils
import mysql.connector
import bcrypt
import random
import sys, requests, urllib
import urllib.parse

Window.size = (360, 600)

Builder.load_file('screens/schedscreen.kv')


class SchedScreen(Screen):

    # def set_selected_user(self, username, date, time):
    #     # Set the selected user's information on the screen
    #     self.selected_username = username
    #     self.ids.username_label.text = f"Username: {username}"
    #     if date is None:
    #         self.ids.date_label.text = "No Schedule Yet"
    #     else:
    #         self.ids.date_label.text = f"{str(date)}"

    #     if time is None:
    #         self.ids.time_label.text = "Set time"
    #     else:
    #         self.ids.time_label.text = f"{str(time)}"


    # def on_save(self, instance, value, date_range):
    #     selected_date = str(value)
    #     self.ids.date_label.text = f"{selected_date}"
    #     self.save_date(selected_date)

    # def on_save_time(self, instance, value):
    #     formatted_time = value.strftime("%I:%M %p")
    #     self.ids.time_label.text = f"{formatted_time}"
    #     self.save_time(formatted_time)

    # def on_cancel(self, instance, value):
    #     self.save_date("")
    #     self.ids.date_label.text = "No Schedule Yet"
    #     self.save_time("")
    #     self.ids.time_label.text = ""

    # def show_date_picker(self):
    #     date_dialog = MDDatePicker()
    #     date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
    #     date_dialog.open()

    # def show_time_picker(self):
    #     time_dialog = MDTimePicker()
    #     time_dialog.bind(on_save=self.on_save_time, on_cancel=self.on_cancel)
    #     time_dialog.open()

    # def save_date(self, date):
    #     connection = mysql.connector.Connect(
    #         host="localhost",
    #         database="loginform",
    #         user="root",
    #         password="09093524550123"
    #     )
    #     cursor = connection.cursor()
    #     query = "UPDATE logindata SET date = %s WHERE username = %s"
    #     values = (date, self.selected_username)
    #     cursor.execute(query, values)
    #     connection.commit()
    #     cursor.close()
    #     connection.close()

    # def save_time(self, time):
    #     connection = mysql.connector.Connect(
    #         host="localhost",
    #         database="loginform",
    #         user="root",
    #         password="09093524550123"
    #     )
    #     cursor = connection.cursor()
    #     query = "UPDATE logindata SET time = %s WHERE username = %s"
    #     values = (time, self.selected_username)
    #     cursor.execute(query, values)
    #     connection.commit()
    #     cursor.close()
    #     connection.close()

    # def show_popup(self):
    #     utils.finish.play()
    #     self.active_dialog = MDDialog(
    #         title="SEND MESSAGE",
    #         text="Are you sure you want to send reminder?",
    #         buttons=[
    #             MDRaisedButton(
    #                 text="YES",
    #                 on_release=self.send_reminder
    #             ),
    #             MDRaisedButton(
    #                 text="No",
    #                 on_release=self.dismiss_dialog
    #             )
    #         ]
    #     )
    #     self.active_dialog.open()
    # def dismiss_dialog(self, *args):
    #     self.instance = 0
    #     self.active_dialog.dismiss()
    #     self.active_dialog = None
    # def send_reminder(self):
    #     appdate = self.ids.date_label.text
    #     apptime = self.ids.time_label.text
    #     appmessage = f"Appointment Schedule \n Date: {appdate}, Time: {apptime} \n Please come on time. Have a nice day!"
    #     selected_username = self.selected_username

    #     # Establish a connection to your MySQL database
    #     connection = mysql.connector.Connect(
    #         host="localhost",
    #         database="loginform",
    #         user="root",
    #         password="09093524550123"
    #     )

    #     cursor = connection.cursor()

    #     # Assuming that your 'logindata' table has columns 'username' and 'phone_number'
    #     # Replace 'username' and 'phone_number' with the actual column names in your table
    #     cursor.execute('SELECT phone_number FROM logindata WHERE username = %s', (selected_username,))

    #     # Fetch the phone number associated with the selected_username
    #     result = cursor.fetchone()

    #     if result:
    #         phone_number = result[0]
    #         key = '79a970cd95ab3055433260e8618a84fb4891fb60'
    #         phone = phone_number  # Use the fetched phone number
    #         message = appmessage
    #         device = '502'
    #         sim = '0'
    #         priority = '1'

    #         print('Sending Message...')
    #         params = (
    #             ('key', key),
    #             ('phone', phone),
    #             ('message', message),
    #             ('device', device),
    #             ('sim', sim),
    #             ('priority', priority)
    #         )
    #         path = 'https://sms.teamssprogram.com/api/send?' + urllib.parse.urlencode(params)
    #         requests.post(path)
    #         print('Message Sent!')

    #     # Close the database connection
    #     connection.close()

    # def click(self):
    #     utils.click.play()

    # def button_press(self):
    #     utils.back.play()
    #     self.ids.backbutton.source = 'images/backpressed1.png'

    # def button_release(self):
    #     self.ids.backbutton.source = 'images/back1.png'
    #     self.manager.current = '_clients_'
    #     self.manager.transition.direction = 'right'


    pass


LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')
