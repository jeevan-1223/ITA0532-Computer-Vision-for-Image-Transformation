import cv2
import numpy as np

img = cv2.imread(r"C:\Users\kasir\Downloads\butter fly image (2).jpg")

if img is None:
    print("Image not loaded")
    exit()

kernel = np.ones((5, 5), np.uint8)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow("Original Image", img)
cv2.imshow("Morphological Gradient Image", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()
