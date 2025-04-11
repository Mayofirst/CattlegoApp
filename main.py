from kivy.core.window import Window
Window.size = (400, 600)

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Hello, mobile world!')

if __name__ == '__main__':
    MyApp().run()

