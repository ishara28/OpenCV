import cv2
import numpy as np

# img = cv2.imread('data/lena.jpg')


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',', y)
        strXY = str(x) + ',' + str(y)
        cv2.putText(img, strXY, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        cv2.imshow("Image", img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 0]
        red = img[y, x, 0]
        strBGR = str(blue) + ',' + str(green) + ',' + str(red)
        cv2.putText(img, strBGR, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
        cv2.imshow("Image", img)
img = np.zeros((512,512,3), np.uint8)
cv2.imshow("Image", img)
cv2.setMouseCallback("Image",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()