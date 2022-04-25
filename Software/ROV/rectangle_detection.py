import cv2
import numpy as np
import math

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)


def nothing():
    pass


def gradient(pt1, pt2):
    try:
        return (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])
    except ZeroDivisionError:
        return 10


def getAngle(pt1, pt2, pt3):
    xprj, center, yprj = pt1, pt2, pt3
    m1 = gradient(center, xprj)
    m2 = gradient(center, yprj)
    angR = math.atan((m2 - m1) / (1 + (m2 * m1)))
    angD = round(math.degrees(angR))
    return angD


def getProjectionLen(angle, dist):
    print("Distance = ", dist)
    print("Angle = ", angle)
    xLen = int(dist * math.cos(angle * (math.pi / 180)))
    print("xLen = ", xLen)
    yLen = int(dist * math.sin(angle * (math.pi / 180)))
    print("xLen = ", yLen)
    return xLen, yLen


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 2000:
            # cv2.drawContours(imgContour, maxCnt, -1, (255, 0, 255), 7)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)

            M = cv2.moments(cnt)
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

            dist = cv2.norm((cx, cy), (320, 240), cv2.NORM_L2)

            cv2.putText(imgContour, str(dist), (320, 240), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2, cv2.LINE_AA)

            cv2.line(imgContour, (cx, cy), (320, 240), (255, 0, 0), 2)

            lenght = int(dist / 6)

            if 240 > cy > 0 and 320 > cx > 0:

                angle = getAngle([320, 240], [cx, cy], [cx, cy + lenght])
                cv2.putText(imgContour, str(angle), (cx, cy), cv2.FONT_HERSHEY_COMPLEX,
                            1.5, (0, 255, 255), 2)

                xLen, yLen = getProjectionLen(angle, int(dist))
                cv2.putText(imgContour, str(xLen) + ',' + str(-yLen), (cx + 50, cy + 50), cv2.FONT_HERSHEY_COMPLEX,
                            1.5, (0, 255, 255), 2)

                cv2.line(imgContour, (cx, cy), (cx + xLen, cy), (255, 0, 0), 2)
                cv2.line(imgContour, (cx, cy), (cx, cy + yLen), (255, 0, 0), 2)

            elif 480 > cy > 240 and 320 > cx > 0:

                angle = -(getAngle([320, 240], [cx, cy], [cx, cy - lenght]))
                cv2.putText(imgContour, str(angle), (cx, cy), cv2.FONT_HERSHEY_COMPLEX,
                            1.5, (0, 255, 255), 2)

                xLen, yLen = getProjectionLen(angle, int(dist))
                cv2.putText(imgContour, str(xLen) + ',' + str(yLen), (cx - 50, cy + 50), cv2.FONT_HERSHEY_COMPLEX,
                            1.5, (0, 255, 255), 2)

                cv2.line(imgContour, (cx, cy), (cx + xLen, cy), (255, 0, 0), 2)
                cv2.line(imgContour, (cx, cy), (cx, cy - yLen), (255, 0, 0), 2)

            elif 240 > cy > 0 and 640 > cx > 320:

                angle = -(getAngle([320, 240], [cx, cy], [cx, cy + lenght]))
                cv2.putText(imgContour, str(angle), (cx, cy), cv2.FONT_HERSHEY_COMPLEX,
                            1.5, (0, 255, 255), 2)

                xLen, yLen = getProjectionLen(angle, int(dist))
                cv2.putText(imgContour, str(-xLen) + ',' + str(-yLen), (cx + 50, cy - 50), cv2.FONT_HERSHEY_COMPLEX,
                            1.5, (0, 255, 255), 2)

                cv2.line(imgContour, (cx, cy), (cx - xLen, cy), (255, 0, 0), 2)
                cv2.line(imgContour, (cx, cy), (cx, cy + yLen), (255, 0, 0), 2)

            elif 480 > cy > 240 and 640 > cx > 320:

                angle = getAngle([320, 240], [cx, cy], [cx, cy - lenght])
                cv2.putText(imgContour, str(angle), (cx, cy), cv2.FONT_HERSHEY_COMPLEX,
                            1.5, (0, 255, 255), 2)

                xLen, yLen = getProjectionLen(angle, int(dist))
                cv2.putText(imgContour, str(-xLen) + ',' + str(+yLen), (cx + 50, cy + 50), cv2.FONT_HERSHEY_COMPLEX,
                            1.5, (0, 255, 255), 2)

                cv2.line(imgContour, (cx, cy), (cx - xLen, cy), (255, 0, 0), 2)
                cv2.line(imgContour, (cx, cy), (cx, cy - yLen), (255, 0, 0), 2)


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) != 2:
                continue
            imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


cv2.namedWindow('Parameters')
cv2.createTrackbar('TH1', 'Parameters', 0, 255, nothing)
cv2.createTrackbar('TH2', 'Parameters', 0, 255, nothing)

# cv2.namedWindow('Color Track Bar')
# cv2.createTrackbar("hmax", "Color Track Bar", 0, 255, nothing)
# cv2.createTrackbar("smax", "Color Track Bar", 0, 255, nothing)
# cv2.createTrackbar("vmax", "Color Track Bar", 0, 255, nothing)
# cv2.createTrackbar("hmin", "Color Track Bar", 0, 255, nothing)
# cv2.createTrackbar("smin", "Color Track Bar", 0, 255, nothing)
# cv2.createTrackbar("vmin", "Color Track Bar", 0, 255, nothing)

while True:
    hmax = 141
    smax = 130
    vmax = 180
    hmin = 90
    smin = 47
    vmin = 109
    thresh1 = cv2.getTrackbarPos("TH1", "Parameters")
    thresh2 = cv2.getTrackbarPos("TH2", "Parameters")

    ret, frame = cap.read()
    if frame is None:
        break
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    imgContour: object = frame.copy()

    imgBlur = cv2.GaussianBlur(frame_HSV, (7, 7), 1)

    frame_threshold = cv2.inRange(imgBlur, (hmin, smin, vmin), (hmax, smax, vmax))

    imgCanny = cv2.Canny(frame_threshold, 200, 255)

    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    getContours(imgDil)

    imgStack = stackImages(0.8, ([frame, frame_HSV, imgBlur],
                                 [imgDil, imgCanny, imgContour]))

    cv2.imshow("Result", imgStack)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
