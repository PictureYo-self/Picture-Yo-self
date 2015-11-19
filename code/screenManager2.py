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
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<MenuScreen>:
	BoxLayout:
		Button:
			text: 'Goto settings'
			on_press: root.manager.current = 'settings'
		Button:
			text: 'Quit'
<SettingsScreen>:
	BoxLayout:
		Button:
			text: 'My settings button'
		Button:
			text: 'Back to menu'
			on_press: root.manager.current = 'menu'
""")

# Declare both screens
class MenuScreen(Screen):
	pass
class SettingsScreen(Screen):
	pass

# create screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))

class TestApp(App):
	def build(self):
		return sm
if __name__ == '__main__':
	TestApp().run()


'''
f = open('/home/pi/Picture-Yo-self/code/pictures/picName.txt','r')
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
		
class MainApp(App):
	im=Image(source=picname, size_hint=(1,50))
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
		root.add_widget(parent)
		
		return root
		
class RootWidget(BoxLayout):
    pass

if __name__ == '__main__':
    MainApp().run()
'''
