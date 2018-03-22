#/bin/sh
sudo python gps.py
sleep 2
sudo python vision-text.py
sleep 2
trans :hi file://visiontext.txt -brief -p
exit
