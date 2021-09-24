import cv2
import numpy as np

# img = cv2.imread('data/lena.jpg', -1)
img = np.zeros([512,512,3], np.uint8)

img = cv2.arrowedLine(img, (0,0), (255,255), (0,0,255), 5)
img = cv2.rectangle(img, (400,400), (500,500), (0,0,255), -1)
img = cv2.circle(img, (448,448), 50, (0,255,0), -1)
img = cv2.putText(img, "OpenCV", (210,56), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 2 )

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()