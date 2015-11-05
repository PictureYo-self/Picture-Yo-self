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

f = open('/home/pi/Picture-Yo-self/code/pictures/picName.txt','r')
global picname 
picname = f.read()
print picname
f.close()
global pic1
pic1 = '\'' + picname + '\''


#Builder.load_string('''
#<RootWidget>
#    AsyncImage:
#        source: '/home/pi/Picture-Yo-self/code/pictures/ss67.jpg'
#    	pos: self.pos
#    	size: self.size
#''')

class MyPaintWidget(Widget):
	def on_touch_down(self, touch):
		color = (random(), 1, 1)
		with self.canvas:
			Color(*color, mode='hsv')
			d = 30.
			#Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
			touch.ud['line'] = Line(points=(touch.x, touch.y))

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
	im=Image(source='/home/pi/Picture-Yo-self/code/pictures/ss67.jpg')
	def build(self):
		root = BoxLayout(orientation='vertical')
		c = Imglayout()
		parent = Widget()
		#wid = RootWidget()
		#parent.add_widget(wid)
		painter = MyPaintWidget()
		clearbtn = Button(text='Clear')
		parent.add_widget(painter)
		parent.add_widget(clearbtn)
		def clear_canvas(obj):
			painter.canvas.clear()
		clearbtn.bind(on_release=clear_canvas)
		#wid.add_widget(parent)
		root.add_widget(c)
		c.add_widget(self.im)
		root.add_widget(parent)
		return root
		
class RootWidget(BoxLayout):
    pass

class CustomLayout(FloatLayout):
    pass

if __name__ == '__main__':
    MainApp().run()
