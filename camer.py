import cv2 as cv
camera = cv.VideoCapture(0)
if camera.isOpened() :
    
    while True:
        ret,frame  =  camera.read()
        cv.imshow("ff",frame)
        if cv.waitKey(1) and 0xFF == ord('q'):
            camera.release()
            cv.destroyAllWindows()

            break
 
