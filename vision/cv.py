import cv
# Initialize the camera
capture = cv.CaptureFromCAM(0)  # 0 -> index of camera
if capture:     # Camera initialized without any errors
   cv.NamedWindow("cam-test", cv.CV_WINDOW_AUTOSIZE)
   f = cv.QueryFrame(capture)     # capture the frame
   if f:
       cv.ShowImage("cam-test",f)
       cv.WaitKey(0)
cv.DestroyWindow("cam-test")
