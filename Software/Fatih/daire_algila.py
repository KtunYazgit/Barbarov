import cv2 as cv
import numpy as np

videoCapture = cv.VideoCapture(0)
prevCircle = None
dist = lambda x1, y1, x2, y2: (x1 - x2) * 2 + (y1 - y2) * 2
while True:
    ret, frame = videoCapture.read(0)
    if not ret: break
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blutFrame = cv.GaussianBlur(grayFrame, (17, 17), 8)
    circles = cv.HoughCircles(blutFrame, cv.HOUGH_GRADIENT, 1.2, 100,
                              param1=70, param2=45, minRadius=10, maxRadius=100)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0, :]:
            if chosen is None: chosen = i
            if prevCircle is not None:
                if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= dist(i[0], i[1], prevCircle[0],
                                                                                    prevCircle[1]):
                    chosen = i
        cv.circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 3)
        cv.circle(frame, (chosen[0], chosen[1]), chosen[2], (0, 0, 255), 3)
        cv.rectangle(frame, (chosen[0]-chosen[2], chosen[1]-chosen[2]),(chosen[0]+chosen[2], chosen[1]+chosen[2]),(0, 162, 255), 3)
        prevCircle = chosen

    w1, h1, c1 = frame.shape
    fotomerkez = (h1 // 2, w1 // 2)
    cv.circle(frame, fotomerkez, 2, (229, 255, 0), 3)
    cv.rectangle(frame, ((h1 // 2 - 20), (w1 // 2 - 20)), ((h1 // 2 + 20), (w1 // 2 + 20)), (204, 0, 0), 2)
    cv.line(frame, (h1 // 2, 0), (h1 // 2, w1), (204, 255, 255), 1)
    cv.line(frame, (0, w1 // 2), (h1, w1 // 2), (204, 255, 255), 1)

    cv.imshow("circles", frame)
    if cv.waitKey(25) & 0xFF == ord('q'): break
videoCapture.release()
cv.destroyAllWindows()