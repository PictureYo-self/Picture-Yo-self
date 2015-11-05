from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

root = Builder.load_string('''
  FloatLayout:
    canvas.before:
      Color:
        rgb: 1, 1, 1
          Rectangle:
              source: '/home/pi/Picture-Yo-self/code/pictures/ci3.jpg'
              size: self.size
  BoxLayout:
        padding: 10
        spacing: 10
        size_hint: 1, None
        pos_hint: {'top': 1}
        height: 44
        Image:
            size_hint: None, None
            size: 24, 24
            source: '/home/pi/Picture-Yo-self/code/pictures/ci3.jpg'
  #        Label:
  #            height: 24
  #            text_size: self.width, None
  #            color: (1, 1, 1, .8)
  #            text: 'Kivy %s - Pictures' % kivy.__version__
''')


class RootWidget(BoxLayout):
    pass

class CustomLayout(FloatLayout):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()
