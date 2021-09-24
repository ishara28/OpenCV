import cv2
import numpy as np

# img = cv2.imread('data/lena.jpg')


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # cv2.circle(img, (x,y), 3, (0,0,255), -1 )
        # points.append((x,y))
        # if len(points) >= 2:
        #     cv2.line(img, points[-1], points[-2], (255,0,0), 5 )
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        myColorImage = np.zeros((512,512,3), np.uint8)
        myColorImage[:] = [blue, green, red]
        cv2.imshow("Colored Image", myColorImage)


# img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('data/lena.jpg')
cv2.imshow("Image", img)
points=[]

cv2.setMouseCallback("Image",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()