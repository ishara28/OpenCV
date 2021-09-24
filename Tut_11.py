import cv2
import numpy as np

img1 = np.zeros((250, 500,3),np.uint8)
img1 = cv2.rectangle(img1, (200,0), (300, 100), (255,255,255), -1)
img2 = cv2.imread('image')

img3 = np.zeros([250,250,3],dtype=np.uint8)
img4 = np.zeros([250,250,3],dtype=np.uint8)
img3.fill(255)

img5 = np.concatenate((img4, img3), axis=1)

bitAnd = cv2.bitwise_or(img1, img5)


cv2.imshow("img1", img1)
cv2.imshow("img5", img5)
cv2.imshow("Bit_AND", bitAnd)


cv2.waitKey(0)
cv2.destroyAllWindows()
