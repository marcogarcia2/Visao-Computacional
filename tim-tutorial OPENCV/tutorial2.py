import cv2
import numpy
import random

img = cv2.imread("/Users/marco/Desktop/SEMEAR/cv-codes/logo.jpg", -1)



print(img)
print(type(img))
print(img.shape)
height, width, channels = img.shape
# [0]    [1]      [2]
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

tag = img[500:700, 600:900]
img[100:300, 650:950] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()