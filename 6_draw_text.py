import numpy as np
import cv2

pic = np.zeros((500, 500, 3), dtype='uint8')
pic2 = cv2.imread('turtle.jpg')
cv2.putText(pic2,"Turtle",(100,100), cv2.FONT_HERSHEY_DUPLEX,3,(255,255,255),4,cv2.LINE_8)

cv2.imshow('dark',pic2)
cv2.waitKey(0)
cv2.destroyAllWindows() 
