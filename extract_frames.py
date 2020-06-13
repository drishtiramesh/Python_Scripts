import os
import cv2

vid = cv2.VideoCapture('.\output1.avi')
i=0
while True:
	print(i)
	i+=1
	grab,frame = vid.read()
	if grab:
		cv2.imwrite('.\\frames\\'+str(i)+'.jpg',frame)
	else:
		break
vid.release()
