import cv2

img = cv2.imread("/Users/marco/Desktop/SEMEAR/cv-codes/buddy.jpeg", -1)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('new_img.jpeg', img)

# 0 é grayscale, -1 é colorido
cv2.imshow('Buddy', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
