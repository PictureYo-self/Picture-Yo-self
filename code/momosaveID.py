#! /usr/bin/python
# photoBooth1
# Samir Saidi, Momona Yamagami

name2 = raw_input("Enter your NetID (ex. aaa1): ")
name1 = "/home/pi/Picture-Yo-self/code/pictures/" + name2 + ".jpg"
f = open('/home/pi/Picture-Yo-self/code/pictures/picName.txt','w')
f.write(name1)
f.close()
f = open('/home/pi/Picture-Yo-self/code/pictures/email.txt','w')
f.write(name2)
f.close()

execfile("/home/pi/Picture-Yo-self/code/momocapture.py")
