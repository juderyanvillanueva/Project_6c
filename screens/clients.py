from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
import utils
import mysql.connector
import bcrypt
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.list import ThreeLineListItem
Window.size = (360, 600)

Builder.load_file('screens/clients.kv')

class Clients(Screen):
    def button_press(self):
        utils.back.play()
        self.ids.backbutton.source = 'images/backpressed1.png'

    def button_release(self):
        self.ids.backbutton.source = 'images/back1.png'
        self.manager.current = '_main_screen_'
        self.manager.transition.direction = 'left'

    # Modify the 'on_enter' method in clients.py
    def on_enter(self, *args):
        self.ids.client_list.clear_widgets()
        connection = mysql.connector.Connect(
            host="localhost",
            database="loginform",
            user="root",
            password="09093524550123"
        )

        cursor = connection.cursor()

        # Fetch both full_name and username from the 'logindata' table
        cursor.execute("SELECT username, full_name, date, time FROM logindata")
        rows = cursor.fetchall()

        for row in rows:
            username = row[0]
            full_name = row[1]
            date = row[2]
            time = row[3]

            if date is None:
                secondary_text = "No Schedule Yet"
            else:
                secondary_text = str(date)

            if time is None:
                tertiary_text = "No Time Set"
            else:
                tertiary_text = str(time)

            item = ThreeLineListItem(
                text=f"{username} | {full_name}",
                secondary_text=secondary_text,
                tertiary_text=tertiary_text
            )

            # Bind the item click event to set_selected_user with the username and date
            item.bind(
                on_release=lambda instance, username=username, full_name=full_name, date=date,
                                  time=time: self.on_item_click(username, date, time))

            self.ids.client_list.add_widget(item)

        cursor.close()
        connection.close()

    def on_item_click(self, text, date, time):
        # Split the text of the list item by the '|' character and get the first part (the username)
        utils.click.play()
        username = text.split('|')[0].strip()

        self.manager.get_screen('_sched_screen_').set_selected_user(username, date, time)
        self.manager.current = '_sched_screen_'

    def set_selected_user(self, username, date, time):
        self.selected_username = username
        self.selected_date = date
        self.selected_time = time

    pass

LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')
