#!

python momosaveID.py 
filename=`cat ./pictures/picName.txt`

netid=`cat ./pictures/email.txt`

email1=$netid"@rice.edu"
name=`finger $email1 | grep "name" | awk '{print $3}'`
grad=`finger $email1 | grep "class" | awk '{print $2}'`
college=`finger $email1 | grep "college" | awk '{print $2}'`

if [ "$grad" == "graduate" ]; then
	col='graduate'
 
else 
	col=$college
fi

echo "$col.jpg" > college.txt

python screenManager.py

filename="/home/pi/Picture-Yo-self/code/pictures/"$netid".png"

mpack -s "Thanks, $name, for using Rice Photobooth!" -d ./pictures/body.txt $filename $email1

filename2=`cat ./pictures/picName2.txt`
rm $filename2
