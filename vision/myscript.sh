#/bin/sh
sudo python singleImage.py
sleep 2
sudo scp /home/rajat/Desktop/vision/output.png debian@192.168.6.2:/home/debian
sleep 2
exit 0
