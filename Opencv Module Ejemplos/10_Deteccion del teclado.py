import cv2

img = cv2.imread("tyler1.jpg",0)

cv2.imshow('teclado',img)

k = cv2.waitKey(0)

if k == ord("g"):
	cv2.imwrite('image_gris.jpg',img)
	cv2.destroyAllWindows()
elif k == 27:
	cv2.destroyAllWindows()
