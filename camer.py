import cv2 as cv
camera = cv.VideoCapture(0)
if camera.isOpened() :
    frame,status  =  camera.read()
    while True:

        cv.imshow("label",frame)
        cv.waitKey(0)
        camera.release()