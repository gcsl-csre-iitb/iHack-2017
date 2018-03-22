# import Adafruit_BBIO.GPIO as GPIO
import time
import cv2 
# import video


# GPIO.setup("P8_12", GPIO.IN)
# GPIO.setup("P9_12", GPIO.IN)
old_switch1_state = 0
old_switch2_state = 0


# def captureVideo(current_time):
#     #Function to capture video
#     cap = cv2.VideoCapture(1)
#     # Define the codec and create VideoWriter object
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     out = cv2.VideoWriter('output.avi',fourcc, 15.0, (640,480))
#     # print(current_time)
    
#     while(cap.isOpened()):
#         ret, frame = cap.read()
#         if ret == True:
#             # write the flipped frame
#             out.write(frame)
#             cv2.imshow('frame', frame)
#             # key = cv2.waitKey(30)
#             new_time = time.time()
#             diff = new_time - current_time
#             if (cv2.waitKey(30) & 0xFF == ord('q') or diff > 10):
#                 break
#             else:
#                 break
#                 # Release everything if job is finished
#     cap.release()
#     cv2.destroyAllWindows()

#Main body
while True:
    new_switch1_state = GPIO.input("P8_12")
    # new_switch2_state = 1
    new_switch2_state = 0
    if new_switch1_state == 1 and old_switch1_state == 0:
        print('video Switch pressed, Call Video capture')
        import singleImage  
        time.sleep(0.1)
    old_switch1_state = new_switch1_state
    if new_switch2_state == 1 and old_switch2_state == 0 :
        print('image Switch pressed, Call Image capture')
        # imageCapture()
        time.sleep(0.1)
    old_switch2_state = new_switch2_state


    break


# captureVideo(time.time())