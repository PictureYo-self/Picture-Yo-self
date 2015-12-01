#// screen manager imported from http://kivy.org/docs/api-kivy.uix.screenmanager.html

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
from kivy.clock import Clock

f = open('/home/pi/Picture-Yo-self/code/pictures/picName.txt','r')
picname = f.read()
f.close()

f = open('/home/pi/Picture-Yo-self/code/pictures/email.txt','r')
email = f.read()
f.close()
email = '/home/pi/Picture-Yo-self/code/pictures/' + email + '.png'

f = open('/home/pi/Picture-Yo-self/code/college.txt','r')
col = f.readline().strip()
f.close()

college = '/home/pi/Picture-Yo-self/code/pictures/' + col

class MyPaintWidget(Widget):
	def on_touch_down(self, touch):
		color = (random(), 1, 1)
		with self.canvas:
			Color(*color, mode='hsv')
			touch.ud['line'] = Line(points=(touch.x, touch.y), width=3)

	def on_touch_move(self, touch):
		touch.ud['line'].points += [touch.x, touch.y]
		
class MainApp(App):
	im=Image(source=picname, size_hint=(1,50))
	crest=Image(source=college, size_hint=(1.65,25), pos_hint={'x':0,'y':-5})
	def build(self):
		root = BoxLayout(orientation='vertical')
		parent = FloatLayout()
		painter = MyPaintWidget()
		crestwid = FloatLayout()
		
		crestwid.add_widget(self.crest)
		parent.add_widget(crestwid)
				
		# create clear button
		clearbtn = Button(text='Clear', size_hint=(.33,5), pos_hint={'x':0,'y':0})
		parent.add_widget(clearbtn)
		def clear_canvas(obj):
			painter.canvas.clear()
		clearbtn.bind(on_release=clear_canvas)

		# create retake photo button
		retakebtn = Button(text='Retake Photo', size_hint=(.33,5), pos_hint={'x':.33,'y':0})
		parent.add_widget(retakebtn)
		def retake_pic(obj):
			execfile("momocapture.py")
			self.im.reload()
			painter.canvas.clear()
		retakebtn.bind(on_release=retake_pic)
		
		# create save button
		savebtn = Button(text='Save and send to email', size_hint=(.33,5), pos_hint={'x':.66,'y':0})
		parent.add_widget(savebtn)
		def save_pic(obj):
		  parent.remove_widget(savebtn)
		  parent.remove_widget(clearbtn)
		  parent.remove_widget(retakebtn)
		  root.export_to_png(email)
		  exit()
		savebtn.bind(on_release=save_pic)

		root.add_widget(self.im)
		root.add_widget(painter)
		root.add_widget(parent)		
		return root
	
class RootWidget(BoxLayout):
    pass

if __name__ == '__main__':
    MainApp().run()
