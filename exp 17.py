import cv2
import numpy as np

# Step 1: Load image
img = cv2.imread(r"C:\Users\kasir\Downloads\download (1).jpg")

# Step 2: Check image loaded
if img is None:
    print("Error: Image not loaded")
    exit()

# Step 3: Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 4: Apply Sobel Edge Detection along X-axis
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Step 5: Convert result to absolute values
sobel_x = cv2.convertScaleAbs(sobel_x)

# Step 6: Display results
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Sobel X Edge Detection", sobel_x)

cv2.waitKey(0)
cv2.destroyAllWindows()
