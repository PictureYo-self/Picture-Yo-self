#!

python capture.py 
filename=`cat ./pictures/picName.txt`
netid=`cat ./pictures/email.txt`
python compiled.py

python working.py

email1=$netid"@rice.edu"
name=`finger $email1 | grep "name" | awk '{print $3}'`

mpack -s "Thanks, $name, for using Rice Photobooth!" -d ./pictures/body.txt $filename $email1
