import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)


def nothing(x):
    pass


cv2.namedWindow('Parameters')

cv2.createTrackbar('R', 'Parameters', 0, 255, nothing)
cv2.createTrackbar('G', 'Parameters', 0, 255, nothing)
cv2.createTrackbar('B', 'Parameters', 0, 255, nothing)



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
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(img, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            # print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                aspRatio = w / float(h)
                if 0.98 < aspRatio < 1.03:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor > 4:
                objectType = "Circles"
            else:
                objectType = "None"

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, objectType,
                        (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0, 0), 2)

def getContours(img, imgContours):

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    maxArea = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > maxArea:
            maxCnt = cnt

    cv2.drawContours(imgContour, maxCnt, -1, (255, 0, 255), 7)

# path = 'Resources/shapes.png'
# img = cv2.imread(path)
# imgContour = img.copy()
#
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
# imgCanny = cv2.Canny(imgBlur, 50, 50)
# getContours(imgCanny)
#
# imgBlank = np.zeros_like(img)
# imgStack = stackImages(0.8, ([img, imgGray, imgBlur],
#                              [imgCanny, imgContour, imgBlank]))
#
# cv2.imshow("Stack", imgStack)
# cv2.waitKey(0)

while True:
    success, img = cap.read()
    imgContour: object = img.copy()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)

    thresh1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    thresh2 = cv2.getTrackbarPos("Threshold2", "Parameters")

    imgCanny = cv2.Canny(imgGray, thresh1, thresh2)

    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    getContours(imgCanny, imgContour)

    imgStack = stackImages(0.8, ([img, imgGray, imgBlur],
                                 [imgDil, imgContour, imgContour]))
    cv2.imshow("Result", imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
