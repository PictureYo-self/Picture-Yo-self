from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


#:kivy 1.0
#:import kivy kivy
#:import win kivy.core.window

root = Builder.load_string('''
FloatLayout:
    canvas.before:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            source: '/home/pi/Picture-Yo-self/code/pictures/ci3.jpg'
            size: self.size
            
''')

# Builder.load_string('''
#<CustomLayout>
#    canvas.before:
#        Color:
#            rgba: 0, 1, 0, 1
#        Rectangle: 
#            pos: self.pos
#            size: self.size
#<RootWidget>
#    CustomLayout:
#        AsyncImage:
#	    source: 'https://upload.wikimedia.org/wikipedia/commons/d/de/Lovett_Hall.jpg'
#''')

class RootWidget(BoxLayout):
    pass

class CustomLayout(FloatLayout):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()

''' class MyPaintWidget(Widget):
	
	def on_touch_down(self, touch):
		color = (random(), 1, 1)
		with self.canvas:
			Color(*color, mode='hsv')
			d = 30.
			#Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
			touch.ud['line'] = Line(points=(touch.x, touch.y))

	def on_touch_move(self, touch):
		touch.ud['line'].points += [touch.x, touch.y]

class RootWidget(FloatLayout):
  pass

class MyPaintApp(App):

	def build(self):
		parent = Widget()
		painter = MyPaintWidget()
		clearbtn = Button(text='Clear')
		parent.add_widget(painter)
		parent.add_widget(clearbtn)

		def clear_canvas(obj):
			painter.canvas.clear()
		clearbtn.bind(on_release=clear_canvas)

		return parent


if __name__ == '__main__':
	MyPaintApp().run()
'''
