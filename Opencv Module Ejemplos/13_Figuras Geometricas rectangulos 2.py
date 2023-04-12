import cv2
import numpy as np

a = np.zeros((256,256,3),np.uint8)

for i in reversed(range (0,256)):
	cv2.rectangle(a,(0,0),(i,i),(255,i,i),1)


cv2.imshow("graficas",a)



cv2.waitKey(0)