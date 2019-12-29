import cv2
import numpy

pic = cv2.imread('turtle.jpg')

matrix = 3

blur = cv2.medianBlur(pic, matrix)
cv2.imshow('blur',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()

