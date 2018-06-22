import cv2 as cv
img = cv.imread('Dog.jpg',-1)
print img

cv.rectangle(img,(120,240),(260,25),(32,32,32),4)
# cv.rectangle(img,(120,240),(260,25),(32,32,32),-1)--->opaque rectangle for thickness -1 
cv.circle(img,(120,120),30,(255,5),1)
cv.putText(img,"DOG",(120,120),cv.FONT_HERSHEY_COMPLEX,1,(233,3,3),cv.LINE_2)
#cv.putText(img,objecy,starting_coordinate,cv.font,scale,color,thickness)
cv.imshow('wow',img)
cv.waitKey(0)
cv.destroyAllWindows()