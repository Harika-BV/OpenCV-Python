
# Basics of OpenCV with Python
**What will be covered in this post**

1. Image Fundamentals - Image Read, Image Write, Drawing circle, Rectangle, Line, Text
2. Image Processing - Image Transforms, Rotate, Scaling, Image Thresholding
3. Image Filtering - Blur, Bilateral filtering, Gaussian Blur, Median Blur
4. Feature Detection - Canny Edge Detector
5. Video Analysis - Video read, Video write, Webcam initialization
6. Applications - Face detection, Real time face detection, Real time eye detection

> Image Fundamentals

1. How to read an image?

```
cv2.imread(file_path, flag)

file_path : Path of the image to be loaded
flag : Specifies the way in which the image should be read. (0 - Grayscale, greater than 0 - RGB Colored)
```

2. How to write/ save an image in other format?
```
cv2.imwrite(new_file_path, original_image)

new_file_path : Path to which image has to be uploaded
```

3. How to draw a rectangle?
```
cv2.rectangle(image, start_point, end_point, color, thickness)

image : Image on which rectangle is to be drawn
start_point : Starting coordinates of rectangle (X1,Y1)
end_point : Ending coordinates of rectangle (X2,Y2) 
color : BGR Colors - (255,0,0)
Thickness : thickness border line in px. -1 : Fill the rectangle shape by specified color
```

4. How to draw a line?
```
cv2.line(image, start_point, end_point, color, thickness)

image : Image on which line is to be drawn
start_point : Starting coordinates of rectangle (X1,Y1)
end_point : Ending coordinates of rectangle (X2,Y2) 
color : BGR Colors - (255,0,0)
Thickness : thickness border line in px. -1 : Fill the rectangle shape by specified color
```

5. How to draw a circle?
```
cv2.circle(image, start_point, radius, color, thickness)

image : Image on which circle is to be drawn
start_point : Starting coordinates of rectangle (X1,Y1)
radius : radious of circle
color : BGR Colors - (255,0,0)
Thickness : thickness border line in px. -1 : Fill the rectangle shape by specified color
```

6. How to put text on an image?
```
cv2.putText(image, text, origin, font, fontScale, color, thickness, lineType)

image : Image on which text is to be written
text : text string to be written
origin : bottom left corner of the text string
font : denotes font type
color : BGR Colors - (255,0,0)
Thickness : thickness border line in px. -1 : Fill the rectangle shape by specified color
lineType : Gives type of the line to be drawn
```
> Image Processing

7. Image Shifting / Rotating
```
M = cv2.getRotationMatrix2D(center, angle, 1)
rotate = cv2.warpAffine(pic, M, (cols,rows))
```

8. Image Thresholding
```
(T_value,binary_threshold) = cv2.threshold(pic, threshold_value, 255, cv2.THRESH_BINARY)
```

> Image Filtering

9. How to apply Gaussian Blur
```
cv2.GaussianBlur(pic, matrix,0)
```

10. How to apply Median Blur
```
cv2.medianBlur(pic, matrix)
```

11. How to Bilateral Blur 
```
cv2.bilateralFilter(pic,dimpixel,color,space)
```

> Feature Detection

12. Canny edge detector
```
cv2.Canny(pic, thresholdval1, thresholdval2)
```

> Video Processing

13. How to read a video?
```
cv2.VideoCapture('sampleVideo.mp4')
```

	
