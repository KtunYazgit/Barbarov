import cv2
import numpy as np
import time
import pyautogui as pag

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    outputFrame = frame.copy()

    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    frame_bgr = cv2.medianBlur(frame_bgr, 3)
    frame_lab = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2Lab)
    frame_lab_red = cv2.inRange(frame_lab, np.array([20, 150, 150]), np.array([190, 255, 255]))
    frame_lab_red = cv2.GaussianBlur(frame_lab_red, (5, 5), 2, 2)
    circles = cv2.HoughCircles(frame_lab_red, cv2.HOUGH_GRADIENT, 1, frame_lab_red.shape[0] / 8, param1=100, param2=18,
                               minRadius=5, maxRadius=60)

    height, width, _ = frame.shape
    camMerkez = (width // 2, height // 2)
    cv2.circle(outputFrame, camMerkez, 2, (229, 255, 0), 3)
    cv2.rectangle(outputFrame, ((width // 2 - 35), (height // 2 - 35)), ((width // 2 + 35), (height // 2 + 35)),
                  (255, 0, 0), 2)
    cv2.line(outputFrame, pt1=(width // 2, 0), pt2=(width // 2, height), color=(204, 255, 255), thickness=1)
    cv2.line(outputFrame, pt1=(0, height // 2), pt2=(width, height // 2), color=(204, 255, 255), thickness=1)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        circleCenter = (circles[0, 0], circles[0, 1])
        cv2.circle(outputFrame, center=circleCenter, radius=1, color=(0, 255, 0), thickness=1)
        cv2.circle(outputFrame, center=circleCenter, radius=circles[0, 2], color=(0, 255, 0),
                   thickness=2)

    cv2.imshow("outputFrame", outputFrame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

exit(0)
