import cv2
import numpy as np
def get_frame(cap,scaling_factor):
	w,frame=cap.read()
	frame=cv2.resize(frame,None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)
	return frame

cap=cv2.VideoCapture(0)
scaling_factor=1
while True:
	frame=get_frame(cap,scaling_factor)
	frame_hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	lower=np.array([0,70,60])
	upper=np.array([50,150,255])
	mask=cv2.inRange(frame_hsv,lower,upper)
	imgand=cv2.bitwise_and(frame,frame,mask=mask)
	imgmedian=cv2.medianBlur(imgand,5)
	cv2.imshow('Input',frame)
	cv2.imshow('Output',imgmedian)
	key=cv2.waitKey
	if key==27:
		break
cv2.destroyAllWindows()
