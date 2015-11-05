#!

python capture.py 
filename=`cat ./pictures/picName.txt`

netid=`cat ./pictures/email.txt`

python working.py

filename="/home/pi/Picture-Yo-self/code/pictures/"$netid".png"

email1=$netid"@rice.edu"
name=`finger $email1 | grep "name" | awk '{print $3}'`

mpack -s "Thanks, $name, for using Rice Photobooth!" -d ./pictures/body.txt $filename $email1
