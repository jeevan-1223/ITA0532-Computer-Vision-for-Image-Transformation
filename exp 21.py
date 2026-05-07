import cv2
import numpy as np

img = cv2.imread(r"C:\Users\kasir\Downloads\download (1).jpg")

kernel = np.array([[1,  1, 1],
                   [1, -8, 1],
                   [1,  1, 1]])

laplacian = cv2.filter2D(img, -1, kernel)

sharpened = cv2.subtract(img, laplacian)

cv2.imshow("Original Image", img)
cv2.imshow("Laplacian Diagonal Mask", laplacian)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
