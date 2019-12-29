import cv2

pic = cv2.imread('turtle.jpg',1)

threshold_value = 100

(T_value,binary_threshold) = cv2.threshold(pic, threshold_value, 255, cv2.THRESH_BINARY)

cv2.imshow('binary',binary_threshold)
cv2.waitKey()
cv2.destroyAllWindows()
