#!/usr/bin/python
import cv2 as cv

cv.namedWindow("Camera")
cam = cv.VideoCapture(0)

while(True):
	ret,frame= cam.read()
	cv.imshow("Camera",frame)
	key = cv.waitKey(20)
	if ( key == 27 ):
		break

cv.imwrite("Test.bmp",frame)
print " Picture saved as Test.bmp "
cam.release()
cv.destroyAllWindows()

execfile("loader.py")
