#!

python momosaveID.py 
filename=`cat ./pictures/picName.txt`

netid=`cat ./pictures/email.txt`

python screenManager.py

filename="/home/pi/Picture-Yo-self/code/pictures/"$netid".png"

email1=$netid"@rice.edu"
name=`finger $email1 | grep "name" | awk '{print $3}'`
college=`finger $email1 | grep "college" | awk '{print $2}'`

print $college

mpack -s "Thanks, $name, for using Rice Photobooth!" -d ./pictures/body.txt $filename $email1

filename2=`cat ./pictures/picName2.txt`
rm $filename2
