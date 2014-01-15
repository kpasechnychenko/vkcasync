__author__ = 'kpasech'

from kivy.app import App
from kivy.uix.button import Button


class Application(App):

    def build(self):
        return Button(text="Hello World")
