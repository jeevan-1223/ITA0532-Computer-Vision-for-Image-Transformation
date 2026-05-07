import cv2
import numpy as np

img = cv2.imread(r"C:\Users\kasir\Downloads\butter fly image (2).jpg")

if img is None:
    print("Error: Image not loaded")
    exit()

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow("Original Image", img)
cv2.imshow("Erosion Image", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
