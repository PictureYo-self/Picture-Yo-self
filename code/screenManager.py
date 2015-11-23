#// screen manager imported from http://kivy.org/docs/api-kivy.uix.screenmanager.html

from kivy.properties import BooleanProperty
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
import os
from kivy.clock import Clock

f = open('/home/pi/Picture-Yo-self/code/pictures/picName.txt','r')
picname = f.read()
f.close()

print picname

f = open('/home/pi/Picture-Yo-self/code/pictures/picName2.txt','r')
picname2 = f.read()
f.close()

f = open('/home/pi/Picture-Yo-self/code/pictures/email.txt','r')
email = f.read()
f.close()
email = '/home/pi/Picture-Yo-self/code/pictures/' + email + '.png'

f = open('/home/pi/Picture-Yo-self/code/pictures/picName2.txt','w')
f.write(email)
f.close()

f = open('/home/pi/Picture-Yo-self/code/college.txt','r')
college = f.read()
f.close()

crest='/home/pi/Picture-Yo-self/code/pictures/' + college
print crest

class MyPaintWidget(Widget):
	def on_touch_down(self, touch):
		color = (random(), 1, 1)
		with self.canvas:
			Color(*color, mode='hsv')
			touch.ud['line'] = Line(points=(touch.x, touch.y), width=3)

	def on_touch_move(self, touch):
		touch.ud['line'].points += [touch.x, touch.y]
		
class MainApp(App):
	im1=Image(source=picname, size_hint=(1,50))
#	allow_stretch = BooleanProperty(True)
#	im2=Image(source='/home/pi/Picture-Yo-self/code/pictures/Will.jpg') #,size=(10,5000))
	def build(self):
		root = BoxLayout(orientation='vertical')
		parent = BoxLayout(orientation='horizontal')
		painter = MyPaintWidget()
		
		# create clear button
		clearbtn = Button(text='Clear', size_hint=(1,5))
		parent.add_widget(clearbtn)
		def clear_canvas(obj):
			painter.canvas.clear()
		clearbtn.bind(on_release=clear_canvas)

		# create retake photo button
		retakebtn = Button(text='Retake Photo', size_hint=(1,5))
		parent.add_widget(retakebtn)
		def retake_pic(obj):
			execfile("momocapture.py")
			self.im1.reload()
			painter.canvas.clear()
		retakebtn.bind(on_release=retake_pic)
		
		# create save button
		savebtn = Button(text='Save and send to email', size_hint=(1,5))
		parent.add_widget(savebtn)
		def save_pic(obj):
			root.remove_widget(parent)
			root.export_to_png(email)
			os.remove(picname)
			#os.remove(picname2)
			exit()
		savebtn.bind(on_release=save_pic)

		
		root.add_widget(self.im1) 
#		root.add_widget(self.im2)
		root.add_widget(painter)
		root.add_widget(parent)		
		return root
	
class RootWidget(BoxLayout):
    pass

if __name__ == '__main__':
    MainApp().run()

