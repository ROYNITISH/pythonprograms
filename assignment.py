import cv2 as cv
import numpy as np
camera = cv.VideoCapture(0)
while True:
    ret,frame = camera.read()
    gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    gray_frame = cv.flip(gray_frame,1)

    pt1=(120,120)
    pt2=(360,360)
    
    frame_new = gray_frame[120:360,120:360]
    cv.imshow("cropped",frame_new)
    cv.rectangle(gray_frame,(120,120),(360,360),(32,32,32),1)
   
    # cv.imshow('frame',frame)
    
    cv.imshow('_frame',gray_frame)
    if cv.waitKey(1) & 0xFF == ord('m'):
        break
    if 0xFF == ord('w') & cv.waitKey(1):
        print("key press works")