#! /usr/bin/python
# photoBooth1
# Samir Saidi, Momona Yamagami

import time 
#import numpy as np
#import cv2
import picamera
import datetime
from time import strftime
#import 

name2 = raw_input("Enter your NetID (ex. aaa1): ")
#Time1= strftime("%Y-%m-%d-%H_%M_%S")
with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	camera.start_preview()
	# camera warm-up time
	time.sleep(2)
	name1 = "/home/pi/Picture-Yo-self/code/pictures/" + name2 + ".jpg"
	camera.capture(name1)
#cv2.imshow('image',name1)
f = open('/home/pi/Picture-Yo-self/code/pictures/picName.txt','w')
f.write(name1)
f.close()
f = open('/home/pi/Picture-Yo-self/code/pictures/email.txt','w')
f.write(name2)
f.close()
