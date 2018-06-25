import cv2 as cv
import numpy as np
camera = cv.VideoCapture(0)
while True:
    ret,frame = camera.read()
    gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    gray_frame = cv.flip(gray_frame,1)
    gray_frame[:,:,0:3]=gray_frame[:,:]
    pt1=(120,120)
    pt2=(360,360)
    x = np.concatenate((frame,gray_frame),axis = 1)
    frame_new = gray_frame[120:360,120:360]
    cv.imshow("cropped",frame_new)
    cv.rectangle(gray_frame,(120,120),(360,360),(32,32,32),1)
   
    # cv.imshow('frame',frame)
    
    cv.imshow('_frame',x)
    if cv.waitKey(1) & 0xFF == ord('m'):
        break
    if 0xFF == ord('w') & cv.waitKey(1):
        print("key press works")