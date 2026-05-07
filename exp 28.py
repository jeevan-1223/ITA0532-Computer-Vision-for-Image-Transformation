import cv2
import numpy as np

img = cv2.imread(r"C:\Users\kasir\Downloads\butter fly image (2).jpg")

if img is None:
    print("Error: Image not loaded")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

boundary = cv2.filter2D(gray, -1, kernel)

cv2.imshow("Original Image", img)
cv2.imshow("Boundary Image", boundary)

cv2.waitKey(0)
cv2.destroyAllWindows()
