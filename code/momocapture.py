#! /usr/bin/python
# photoBooth1
# Samir Saidi, Momona Yamagami

import time
import picamera
import datetime
from time import strftime

f = open("/home/pi/Picture-Yo-self/code/pictures/picName.txt",'r')
name1 = f.read()
f.close()

print name1

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	camera.start_preview()
	# camera warm-up time
	time.sleep(2)
	camera.capture(name1)
#cv2.imshow('image',name1)

#execfile("screenManager.py")
