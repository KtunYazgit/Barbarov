import cv2

img = cv2.imread("img.jpg")

color = (0,255,0)
thikcness = 5

cv2.circle(img, (360,640), 200, color, thikcness)

cv2.imshow("img", img)


cv2.waitKey(0)