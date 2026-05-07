import cv2
import numpy as np

img = cv2.imread(r"C:\Users\kasir\Downloads\download (1).jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

gradient = cv2.magnitude(sobel_x, sobel_y)
gradient = cv2.convertScaleAbs(gradient)

gradient_bgr = cv2.cvtColor(gradient, cv2.COLOR_GRAY2BGR)

sharpened = cv2.addWeighted(img, 1.5, gradient_bgr, 0.5, 0)

cv2.imshow("Original Image", img)
cv2.imshow("Gradient Mask", gradient)
cv2.imshow("Gradient Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
