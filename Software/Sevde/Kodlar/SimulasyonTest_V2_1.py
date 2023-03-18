import cv2
import numpy as np
import mouse
import pyautogui
import time

cap = cv2.VideoCapture(0)


def BulduMu():
    _, frame = cap.read()
    blur = cv2.GaussianBlur(frame, [5, 5], 1)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    lower_color = np.array([22, 100, 100])
    upper_color = np.array([38, 255, 255])
    mask = cv2.inRange(hsv, lower_color, upper_color)
    _, thresh = cv2.threshold(mask, 150, 200, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        epsilon = 0.01 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        cv2.drawContours(mask, [approx], 0, 0, 5)
    try:
        corners = cv2.goodFeaturesToTrack(mask, 5, 0.1, 60)
        corners = np.int0(corners)
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)
    except:
        pass

    if len(contours) == 0:
        return True


def GoruntuIsleme():
    font = cv2.FONT_HERSHEY_SIMPLEX
    _, frame = cap.read()
    img = frame
    blur = cv2.GaussianBlur(frame, [5, 5], 1)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    lower_color = np.array([22, 100, 100])
    upper_color = np.array([38, 255, 255])
    mask = cv2.inRange(hsv, lower_color, upper_color)
    _, thresh = cv2.threshold(mask, 150, 200, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # w1, h1, c1 = frame.shape
    for cnt in contours:
        epsilon = 0.01 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        cv2.drawContours(mask, [approx], 0, 0, 5)
        # x = approx.ravel()[0]
        # y = approx.ravel()[1]
    try:
        corners = cv2.goodFeaturesToTrack(mask, 5, 0.1, 60)
        corners = np.int0(corners)
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)
    except:
        pass

    w1, h1, c1 = img.shape
    fotomerkez = (h1 // 2, w1 // 2)
    cv2.circle(img, fotomerkez, 2, (229, 255, 0), 3)
    cv2.rectangle(img, ((h1 // 2 - 35), (w1 // 2 - 35)), ((h1 // 2 + 35), (w1 // 2 + 35)), (255, 0, 0), 2)
    cv2.line(img, (h1 // 2, 0), (h1 // 2, w1), (204, 255, 255), 1)
    cv2.line(img, (0, w1 // 2), (h1, w1 // 2), (204, 255, 255), 1)

    renkKontrol = 0
    kutuKontrol = False

    h = 0.1
    w = 0.1
    sariAlgilama = 0

    if len(contours) != 0:
        esitMi = True
        sariAlgilama = 1
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        x_y_uzunluklari = "X: " + str(w) + ", Y: " + str(h)
        cv2.line(img, (x + w // 2, y + h // 2), (x + w // 2, w1 // 2), (0, 0, 255), 2)
        cv2.line(img, (x + w // 2, y + h // 2), (h1 // 2, y + h // 2), (0, 0, 255), 2)
        y_koordinati = (y + h // 2) - (w1 // 2)
        x_koordinati = (x + w // 2) - (h1 // 2)
        # print(x_koordinati, ",", y_koordinati)

        center = (x + w // 2, y + h // 2)
        radius = 2
        cv2.circle(img, center, radius, (0, 255, 0), 2)

        # istenen aralıkta değilse mavi istenen aralıktaysa yeşil yazdıracak
        if h - (h / 20) < w < h + (h / 20) or w >= h or h < 50:
            renkKontrol = 1
            cv2.putText(img, x_y_uzunluklari, (x, y), font, 1, (0, 255, 0), cv2.LINE_4, -1)

        if -35 < x_koordinati < 35 and -35 < y_koordinati < 35:
            kutuKontrol = True

        # elif -50 < x_koordinati < 50 and -50 < y_koordinati < 50:
        #     cv2.putText(img, x_y_uzunluklari, (x, y), font, 1, (255, 0, 0), cv2.LINE_4, -1)
        #     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        #     print("Saat yonunde don")
        #     mouse.move(25, 0, absolute=False, duration=0.05)

        else:
            renkKontrol = 0
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, x_y_uzunluklari, (x, y), font, 1, (255, 0, 0), cv2.LINE_4, -1)

        if 0 < x_koordinati < 320:
            pyautogui.keyDown("d")
            time.sleep(0.0005)
            pyautogui.keyUp("d")
            print("Sag")

        if -320 < x_koordinati < 0:
            pyautogui.keyDown("a")
            time.sleep(0.0005)
            pyautogui.keyUp("a")
            print("Sol")

        if 0 < y_koordinati < 240:
            pyautogui.keyDown("shift")
            print("Asagi")
            time.sleep(0.0005)
            pyautogui.keyUp("shift")

        if -240 < y_koordinati < 0:
            pyautogui.keyDown("space")
            print("Yukari")
            time.sleep(0.0005)
            pyautogui.keyUp("space")

        if kutuKontrol and renkKontrol == 1:
            pyautogui.keyDown("w")
            time.sleep(1.75)
            print("ILERLE")
            pyautogui.keyUp("w")

    cv2.imshow("maskeli", mask)
    cv2.imshow("orjinal", frame)

    return kutuKontrol, renkKontrol, w, h


# while True:
#     mouse.move(25, 0, absolute=False, duration=0.5)
#     pyautogui.keyDown("w")
#     time.sleep(1.75)
#     print("ILERLE")
#     pyautogui.keyUp("w")
#     if BulduMu():
#         break
while True:
    kutuKontrol, renkKontrol, w, h = GoruntuIsleme()
    print("Renk kontrol: ", renkKontrol)
    print("Kutu kontrol: ", kutuKontrol)

    if renkKontrol == 0 and kutuKontrol:
        print("Saat yonunde don")
        mouse.move(25, 0, absolute=False, duration=0.05)
        kutuKontrol, renkKontrol, w2, h2 = GoruntuIsleme()

        if (h / w) < (h2 / w2):
            print("1. IF")
            while True:
                if kutuKontrol:
                    print("Saat yonunde don")
                    mouse.move(25, 0, absolute=False, duration=0.05)

                kutuKontrol, renkKontrol, w, h = GoruntuIsleme()
                print("Goruntu isleme tamamlandi")
                if renkKontrol == 1:
                    break

        else:
            print("2. IF")
            while True:
                if kutuKontrol:
                    print("Saat yonunun tersine don")
                    mouse.move(-25, 0, absolute=False, duration=0.05)

                kutuKontrol, renkKontrol, w, h = GoruntuIsleme()
                print("Goruntu isleme tamamlandi 22222")

                if renkKontrol == 1:
                    break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
exit(0)
