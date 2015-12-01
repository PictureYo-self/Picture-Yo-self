#!
cd /home/pi/Picture-Yo-self/code
python /home/pi/Picture-Yo-self/code/momosaveID.py 
filename=`cat /home/pi/Picture-Yo-self/code/pictures/picName.txt`

netid=`cat /home/pi/Picture-Yo-self/code/pictures/email.txt`

email1=$netid"@rice.edu"
name=`finger $email1 | grep "name" | awk '{print $3}'`
grad=`finger $email1 | grep "class" | awk '{print $2}'`
college=`finger $email1 | grep "college" | awk '{print $2}'`

if [ "$grad" == "graduate" ]; then
	col='graduate'
 
else 
	col=$college
fi

echo "$col.jpg" > /home/pi/Picture-Yo-self/code/college.txt

python /home/pi/Picture-Yo-self/code/crestFloat.py

filename="/home/pi/Picture-Yo-self/code/pictures/"$netid".png"

convert $filename -crop 600x480+100+0 $filename

mpack -s "Thanks, $name, for using Rice Photobooth!" -d /home/pi/Picture-Yo-self/code/pictures/body.txt $filename $email1

filename2=`cat /home/pi/Picture-Yo-self/code/pictures/picName2.txt`
rm $filename2
