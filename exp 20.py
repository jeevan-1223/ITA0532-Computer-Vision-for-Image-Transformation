import cv2
import numpy as np

img = cv2.imread(r"C:\Users\kasir\Downloads\download (1).jpg")

kernel = np.array([[0,  1, 0],
                   [1, -4, 1],
                   [0,  1, 0]])

laplacian = cv2.filter2D(img, -1, kernel)

sharpened = cv2.subtract(img, laplacian)

cv2.imshow("Original Image", img)
cv2.imshow("Laplacian Mask", laplacian)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
