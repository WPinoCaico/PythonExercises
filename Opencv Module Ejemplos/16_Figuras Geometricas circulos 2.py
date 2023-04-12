import cv2
import numpy as np

a = np.zeros((256,256,3),np.uint8)

for i in range(0,128):
	cv2.circle(a,(128,128),i,(255,i*2,255),1)

cv2.imshow("graficas",a)



cv2.waitKey(0)