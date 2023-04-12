import cv2
import numpy as np

a = np.zeros((256,256,3),np.uint8)

cv2.rectangle(a,(64,64),(128,128),(255,0,0),2)


cv2.imshow("graficas",a)



cv2.waitKey(0)