import numpy as np
import cv2

pic = np.zeros((500, 500, 3), dtype='uint8')
cv2.circle(pic, (250,250), 50, (255,255,0),-1)

cv2.imshow('dark',pic)
cv2.waitKey(0)
cv2.destroyAllWindows() 
