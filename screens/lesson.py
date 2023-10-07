from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.clock import Clock
import utils

Window.size = (360, 600)

Builder.load_file('screens/lesson.kv')
expressions = [
    {
        'image_source': 'gifs/orig2/happy.gif',
        'description': "The happy expression is characterized by a wide smile, raised cheeks, and often, crinkles around the eyes. It conveys feelings of joy, contentment, and satisfaction."
    },
    {
        'image_source': 'gifs/orig2/sad.gif',
        'description': "The sad expression features a downturned mouth, drooping eyelids, and a furrowed brow. It signals feelings of unhappiness, sorrow, or disappointment."
    },
    {
        'image_source': 'gifs/orig2/angry.gif',
        'description': "The angry expression involves narrowed eyes, a tense jaw, and raised eyebrows. It represents frustration, irritation, or even rage."
    },
    {
        'image_source': 'gifs/orig2/fear.gif',
        'description': "The fearful expression includes wide-open eyes, raised eyebrows, and a slightly opened mouth. It conveys feelings of fear, apprehension, or anxiety."
    },
    {
        'image_source': 'gifs/orig2/surprise.gif',
        'description': "The surprised expression features wide-open eyes, raised eyebrows, and a dropped jaw. It reflects sudden shock, amazement, or astonishment."
    },
    {
        'image_source': 'gifs/orig2/disgust.gif',
        'description': "The disgusted expression involves a wrinkled nose, raised upper lip, and a frown. It represents feelings of revulsion, distaste, or aversion."
    }
]

class Lesson(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expression_index = 0  # Initialize the index to the first expression
        Clock.schedule_once(self.update_expression)

    def button_press(self):
        utils.back.play()
        self.ids.backbutton.source = 'images/backpressed1.png'

    def button_release(self):
        self.ids.backbutton.source = 'images/back1.png'
        self.manager.current = '_childplay_screen_'
        self.manager.transition.direction = 'left'

    def update_expression(self, *args):
        # Update the image source and description based on the current index
        expression = expressions[self.expression_index]
        self.ids.expression.source = expression['image_source']
        self.ids.expression_description.text = expression['description']

        # Check if we've reached the last expression
        if self.expression_index == len(expressions) - 1:
            self.ids.next_button.text = 'FINISH'
        else:
            self.ids.next_button.text = 'NEXT'

    def next_expression(self):
        utils.click.play()
        # Increment the index to load the next expression
        self.expression_index += 1
        if self.expression_index >= len(expressions):
            # If we've reached the end, go back to the first expression
            self.expression_index = 0
            self.finish_lesson()
        self.update_expression()

    def finish_lesson(self):
        # Reset the expression index and update the expression
        self.expression_index = 0
        self.update_expression()

        # Redirect to _childstart_screen_
        self.manager.current = '_childstart_screen_'
        self.manager.transition.direction = 'left'

    pass


LabelBase.register(name='Sunny Spells',
                   fn_regular='Sunny Spells.ttf')
