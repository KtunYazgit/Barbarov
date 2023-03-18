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
                               minRadius=5, maxRadius=500)

    height, width, _ = frame.shape
    camMerkez = (width // 2, height // 2)
    cv2.circle(outputFrame, camMerkez, 2, (229, 255, 0), 3)
    # Merkez Dikdörtgen
    cv2.rectangle(outputFrame, ((width // 2 - 35), (height // 2 - 35)), ((width // 2 + 35), (height // 2 + 35)),
                  (255, 0, 0), 2)

    # Merkez Crosshair
    cv2.line(outputFrame, pt1=(width // 2, 0), pt2=(width // 2, height), color=(0, 255, 0), thickness=1)
    cv2.line(outputFrame, pt1=(0, height // 2), pt2=(width, height // 2), color=(0, 255, 0), thickness=1)

    # Hassasiyet ayarlamak için çizgiler

    # Kırmızı Dikey
    cv2.line(outputFrame, (120, 0), (120, 480), (0, 0, 255), 2)
    cv2.line(outputFrame, (520, 0), (520, 480), (0, 0, 255), 2)

    # Sarı Dikey
    cv2.line(outputFrame, (220, 0), (220, 480), (0, 255, 255), 2)
    cv2.line(outputFrame, (420, 0), (420, 480), (0, 255, 255), 2)

    # Kırmızı Yatay
    cv2.line(outputFrame, (0, 90), (640, 90), (0, 0, 255), 2)
    cv2.line(outputFrame, (0, 390), (640, 390), (0, 0, 255), 2)

    # Sarı Yatay
    cv2.line(outputFrame, (0, 165), (640, 165), (0, 255, 255), 2)
    cv2.line(outputFrame, (0, 315), (640, 315), (0, 255, 255), 2)

    circleX = 0
    circleY = 0
    circleR = 0
    circleCenter = 0

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        circleX = circles[0, 0]
        circleY = circles[0, 1]
        circleR = circles[0, 2]
        circleCenter = (circleX, circleY)
        cv2.circle(outputFrame, center=circleCenter, radius=1, color=(0, 255, 0), thickness=1)
        cv2.circle(outputFrame, center=circleCenter, radius=circles[0, 2], color=(0, 255, 0),
                   thickness=2)
        cv2.rectangle(outputFrame, (circleX - circleR, circleY - circleR), (circleX + circleR, circleY + circleR),
                      color=(255, 0, 0), thickness=2)

    # Komut verilecek olan aralıklar
    # En küçük alan için (4 kare)

    if 220 <= circleX <= 420 and 165 <= circleY <= 315:
        if 320 <= circleX < 420 and 165 <= circleY < 240:
            print("YUKARI - SAG (0.5 sn)")
        elif 220 < circleX <= 320 and 165 <= circleY < 240:
            print("YUKARI - SOL (0.5 sn)")
        elif 220 < circleX <= 320 and 240 <= circleY < 315:
            print("ASAGI - SOL (0.5 sn)")
        elif 320 <= circleX < 420 and 240 <= circleY < 315:
            print("ASAGI - SAG (0.5 sn)")

    elif 120 <= circleX <= 520 and 90 <= circleY <= 390:
        if 320 <= circleX < 520 and 90 <= circleY < 240:
            print("YUKARI - SAG (0.75 sn)")
        elif 120 < circleX <= 320 and 90 <= circleY < 240:
            print("YUKARI - SOL (0.75 sn)")
        elif 120 < circleX <= 320 and 240 <= circleY < 390:
            print("ASAGI - SOL (0.75 sn)")
        elif 320 <= circleX < 520 and 240 <= circleY < 390:
            print("ASAGI - SAG (0.75 sn)")

    elif 0 <= circleX <= 640 and 0 <= circleY <= 480:
        if 320 <= circleX < 640 and 0 <= circleY < 240:
            print("YUKARI - SAG (1 sn)")
        elif 0 < circleX <= 320 and 0 <= circleY < 240:
            print("YUKARI - SOL (1 sn)")
        elif 0 < circleX <= 320 and 240 <= circleY < 390:
            print("ASAGI - SOL (1 sn)")
        elif 320 <= circleX < 640 and 240 <= circleY < 480:
            print("ASAGI - SAG (1 sn)")

    cv2.imshow("outputFrame", outputFrame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

exit(0)
