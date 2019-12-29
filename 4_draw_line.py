import numpy as np
import cv2

pic = np.zeros((500, 500, 3), dtype='uint8')
cv2.line(pic, (50,250), (250,250), (255,255,0),25)

cv2.imshow('dark',pic)
cv2.waitKey(0)
cv2.destroyAllWindows() 
