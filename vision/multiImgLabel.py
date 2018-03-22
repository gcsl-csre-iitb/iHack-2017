import numpy as np
import cv2
import time
import os
import caffe
import time

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 15.0, (640,480))
current_time = time.time()

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        cv2.imshow('frame',frame)
        new_time = time.time()
        diff = new_time-current_time
        if (cv2.waitKey(30) & 0xFF == ord('q') or diff > 10):
            break
        
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()

#Converting video to frames
cap1 = cv2.VideoCapture('output.avi')
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')
currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap1.read()

    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    if currentFrame>5:
        break
    else:
        currentFrame += 1

# When everything done, release the capture
cap1.release()
cv2.destroyAllWindows()

#Labelling all the images
MODEL_FILE = '/media/rajat/Miscellaneous/Mtech/MTP/CNN/caffe/models/bvlc_reference_caffenet/deploy.prototxt'
PRETRAINED = '/media/rajat/Miscellaneous/Mtech/MTP/CNN/caffe/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'

net = caffe.Classifier(MODEL_FILE, PRETRAINED,
                       mean=np.load('/media/rajat/Miscellaneous/Mtech/MTP/CNN/caffe/python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1),
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       image_dims=(256, 256))
print "successfully loaded classifier"
IMAGE_FILE = './data/'
for file in os.listdir(IMAGE_FILE):
    path = IMAGE_FILE + file
    print path
    input_image = caffe.io.load_image(path)
    pred = net.predict([input_image])
    labels = np.loadtxt("/media/rajat/Miscellaneous/Mtech/MTP/CNN/caffe/data/ilsvrc12/synset_words.txt", str, delimiter='\t')
    top_k = pred.argsort()[:, -1:-6:-1]
    print top_k 
    print labels[top_k]

