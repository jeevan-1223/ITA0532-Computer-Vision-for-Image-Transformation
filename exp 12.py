import cv2
import numpy as np

# Step 1: Load image
img = cv2.imread(r"C:\Users\kasir\Downloads\download (1).jpg")

# Step 2: Check image loaded
if img is None:
    print("Error: Image not loaded. Check path.")
    exit()

# Step 3: Get image size
height, width = img.shape[:2]

# Step 4: Select 4 points from original image
pts1 = np.float32([
    [50, 50],          # top-left
    [width - 50, 50],  # top-right
    [50, height - 50], # bottom-left
    [width - 50, height - 50] # bottom-right
])

# Step 5: Define 4 new destination points
pts2 = np.float32([
    [0, 0],
    [width, 0],
    [0, height],
    [width, height]
])

# Step 6: Get perspective transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Step 7: Apply perspective transformation
result = cv2.warpPerspective(img, matrix, (width, height))

# Step 8: Display images
cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transformed Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
