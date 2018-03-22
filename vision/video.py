# import cv2
# cv2.namedWindow("output")
# cap = cv2.VideoCapture(0)
# if cap.isOpened(): # Getting the first frame
#     ret, frame = cap.read()
# else:
#     ret = False
#     while ret:
#         cv2.imshow("output", frame)
#         ret, frame = cap.read()
#         key = cv2.waitKey(20)
#         if key == 27: # exit on Escape key
#             break
# cap.release()
# cv2.destroyWindow("output")

import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 15.0, (640,480))
current_time = time.time()
# print(current_time)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # write the flipped frame
        out.write(frame)
        cv2.imshow('frame',frame)
        # key = cv2.waitKey(30)
        new_time = time.time()
        diff = new_time-current_time
        if (cv2.waitKey(30) & 0xFF == ord('q') or diff > 10):
            break
        
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()

# logic for label generation
