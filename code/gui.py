from random import random
from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

class MyPaintWidget(Widget):

	def on_touch_down(self, touch):
		color = (random(), 1, 1)
		with self.canvas:
			Color(*color, mode='hsv')
			d = 30.
			Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
			touch.ud['line'].points += [touch.x, touch.y]

