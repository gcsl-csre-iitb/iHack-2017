'''
Using OpenCV takes a mp4 video and produces a number of images.
Requirements
----
You require OpenCV 3.2 to be installed.
Run
----
Open the main.py and edit the path to the video. Then run:
$ python main.py
Which will produce a folder called data with the images. There will be 2000+ images for example.mp4.
'''
import cv2
import numpy as np
import os
import time

# Playing video from file:
cap = cv2.VideoCapture('output.avi')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')
# Time = time.time()
currentFrame = 0
count = 0
while(True):
    # Capture frame-by-frame
    # currentTime = time.time()
    # diff = currentTime - Time
    # print(diff)
		
    if (count % 20 == 0):
        ret, frame = cap.read()

    # Saves image of the current frame in jpg file
        name = './data/frame' + str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
        currentFrame += 1

    # To stop duplicate images
    if currentFrame > 20:
        break
    
    # Time = time.time()
    count += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

