// screen manager imported from http://kivy.org/docs/api-kivy.uix.screenmanager.html

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from random import random
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.image import Image
import sys

f = open('/home/pi/Picture-Yo-self/code/pictures/picName.txt','r')
global picname 
picname = f.read()
f.close()

f = open('/home/pi/Picture-Yo-self/code/pictures/email.txt','r')
email = f.read()
f.close()
email = '/home/pi/Picture-Yo-self/code/pictures/' + email + '.png'

class MyPaintWidget(Widget):
	def on_touch_down(self, touch):
		color = (random(), 1, 1)
		with self.canvas:
			Color(*color, mode='hsv')
			touch.ud['line'] = Line(points=(touch.x, touch.y), width=3)

	def on_touch_move(self, touch):
		touch.ud['line'].points += [touch.x, touch.y]
		
class Imglayout(FloatLayout):

    def __init__(self,**args):
        super(Imglayout,self).__init__(**args)

        with self.canvas.before:
            Color(0,0,0,0)
            self.rect=Rectangle(size=self.size,pos=self.pos)

        self.bind(size=self.updates,pos=self.updates)
    def updates(self,instance,value):
        self.rect.size=instance.size
        self.rect.pos=instance.pos
		
class MainApp(App):
	im=Image(source=picname, size_hint=(1,50))
	def build(self):
		root = BoxLayout(orientation='vertical')
		c = Imglayout()
		parent = BoxLayout(orientation='horizontal')
		painter = MyPaintWidget()
		
		# create clear button
		clearbtn = Button(text='Clear', size_hint=(1,5))
		parent.add_widget(clearbtn)
		def clear_canvas(obj):
			painter.canvas.clear()
		clearbtn.bind(on_release=clear_canvas)
		
		# create save button
		savebtn = Button(text='Save and send to email', size_hint=(1,5))
		parent.add_widget(savebtn)
		def save_pic(obj):
		  root.remove_widget(parent)
		  root.export_to_png(email)
		  exit()
		savebtn.bind(on_release=save_pic)
		root.add_widget(self.im) 
		root.add_widget(painter)
		root.add_widget(c)
		root.add_widget(parent)
		
		return root
		
class RootWidget(BoxLayout):
    pass

class CustomLayout(FloatLayout):
    pass

if __name__ == '__main__':
    MainApp().run()
