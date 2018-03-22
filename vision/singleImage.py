import cv2# initialize the camera
import os, sys


cam = cv2.VideoCapture(1)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    # cv2.namedWindow("cam-test",cv2.cv.CV_WINDOW_AUTOSIZE)
    # cv2.imshow("cam-test", img)
    cv2.imwrite("output.png", img)
    cv2.waitKey(0)
    # cv2.destroyWindow("cam-test")
    sys.exit()
