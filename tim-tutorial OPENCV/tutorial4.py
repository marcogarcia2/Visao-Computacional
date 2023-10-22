import cv2
import numpy as np

# algoritmo para capturar imagens de webcam

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    # ver documentação
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0,0), (width,height), (255,0,0), 5)
    img = cv2.line(img, (0,height), (width,0), (0,255,0), 5)
    img = cv2.rectangle(img, (100,100), (500,300), (200,255,0), -1)
    img = cv2.circle(img, (300,300), 60, (0,0,255), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Tim is great!', (200, height - 10), font, 2, (0,0,0), 3, cv2.LINE_AA)


    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


