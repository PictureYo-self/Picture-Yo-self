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
from kivy.uix.colorpicker import ColorPicker

f = open('/users/Samir/Documents/Rice/BIOE421/picName.txt','r')
global picname 
picname = f.read()
f.close()

class MyPaintWidget(Widget):
	def on_touch_down(self, touch):
		color = (0, 1, 1, 1)
		with self.canvas:
			Color(*color)
			touch.ud['line'] = Line(points=(touch.x, touch.y), width=5)

	def on_touch_move(self, touch):
		touch.ud['line'].points += [touch.x, touch.y]

class MainApp(App):
	im=Image(source=picname, size_hint=(1,50))
	def build(self):
		root = BoxLayout(orientation='vertical')
		#c = Imglayout()
		parent = BoxLayout(orientation='horizontal')
		painter = MyPaintWidget()
		clr_picker = ColorPicker()
		clr_picker.bind(color=on_color)
		clearbtn = Button(text='Clear', size_hint=(1,5))
		savebtn = Button(text='Save', size_hint=(1,5))

		root.add_widget(self.im)
		parent.add_widget(clearbtn)
		parent.add_widget(savebtn)
		root.add_widget(painter)
		root.add_widget(clr_picker)
		def clear_canvas(obj):
			painter.canvas.clear()
		clearbtn.bind(on_release=clear_canvas)
		#root.add_widget(c)
		root.add_widget(parent)
		return root
		
class RootWidget(BoxLayout):
    pass

if __name__ == '__main__':
    MainApp().run()
