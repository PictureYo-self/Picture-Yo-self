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
from kivy.uix.popup import Popup
from kivy.uix.colorpicker import ColorPicker
from kivy.properties import ListProperty

col=[0,0,1,1]

f = open('/home/pi/Picture-Yo-self/code/pictures/picName.txt','r')
global picname 
picname = f.read()
f.close()

class SelectedColorEllipse(Widget):
	def on_touch_down(self, touch):
		selected_color = ListProperty(col)
		'''
		with self.canvas:
			touch.ud['line'] = Line(points=(touch.x, touch.y), width=3)
			Color(*selected_color)
	def on_touch_move(self, touch):
		touch.ud['line'].points += [touch.x, touch.y]
		'''

class ColPckr(ColorPicker):
	pass

class ColPopup(Popup):
	pass

class Ex40(Widget):
	selected_color = ListProperty(col)
	def select_ColPckr(self,*args):
		ColPopup().open()
	def on_touch_down(self, touch):
		sce = SelectedColorEllipse()
		sce.selected_color = self.selected_color
        sce.center = touch.pos
        self.add_widget(sce)

class Ex40App(App):
	im=Image(source=picname, size_hint=(1,50))
	def build(self):
		root = BoxLayout(orientation='vertical')
		#c = Imglayout()
		parent = BoxLayout(orientation='horizontal')
		painter = MyPaintWidget()
		#colorbtn = Button(text='Pick Color', size_hint=(1,5))
		clearbtn = Button(text='Clear', size_hint=(1,5))
		savebtn = Button(text='Save', size_hint=(1,5))
		

		root.add_widget(self.im)
		parent.add_widget(colorbtn)
		parent.add_widget(clearbtn)
		parent.add_widget(savebtn)
		root.add_widget(painter)
		def clear_canvas(obj):
			painter.canvas.clear()
			'''
		def select_ColPckr(self,*args):
			ColPopup().open()
		def touch_colorbtn
			return super(Ex40, self).on_touch_down(touch)
			'''
		clearbtn.bind(on_release=clear_canvas)
		#colorbtn.bind(on_release=touch_colorbtn)
		root.add_widget(parent)
		return Ex40()
		
class RootWidget(BoxLayout):
    pass


if __name__ == '__main__':
    MainApp().run()
