# Sample program to read and show an image

import cv2

img = cv2.imread('dog.png')
gray = cv2.imread('dog.png',cv2.IMREAD_GRAYSCALE)

cv2.imshow('Dog',img)
cv2.imshow('Gray Dog',gray)

cv2.waitKey(0) # Program will stop when any key is pressed
cv2.destroyAllWindows()
