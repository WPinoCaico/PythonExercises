import cv2
import numpy as np

a = np.zeros((256,256,3),np.uint8)

cv2.line(a,(0,0),(255,255),(255,0,0),2)

cv2.line(a,(0,255),(255,0),(255,0,255),2)

cv2.imshow("graficas",a)



cv2.waitKey(0)