import cv2
import numpy as np

a = np.zeros((256,256,3),np.uint8)

for i in range(0,256):
	cv2.circle(a,(i,i),int(i/2),(128,i,i),1)

cv2.imshow("graficas",a)



cv2.waitKey(0)