import numpy as np
import cv2

img = cv2.imread("/Users/marco/Desktop/SEMEAR/cv-codes/chessboard.png", -1)
img = cv2.resize(img, (0,0), fx=0.75, fy=0.75)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

N = 100
corners = cv2.goodFeaturesToTrack(gray_img, N, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 10, (255,0,255), -1)

for i in range(len(corners)):
    for j in range(i + 1, len(corners)): 
        corner1 = tuple(corners[i][0]) 
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 3)


cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()