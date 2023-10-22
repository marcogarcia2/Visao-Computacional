import cv2
import numpy as np

# algoritmo para capturar imagens de webcam

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    # ver documentação
    width = int(cap.get(3))
    height = int(cap.get(4))

    # converter BGR em HSV (Hue, Saturation and Lightness)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([90,  50,  50])
    upper_blue = np.array([130, 255, 255])

    # tudo que está dentro do alcance fica branco
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # deixa o branco na cor natural
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

