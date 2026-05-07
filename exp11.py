import cv2
import numpy as np

# 🔹 Step 1: Load image
img = cv2.imread(r"C:\Users\kasir\Downloads\download (1).jpg")

# 🔹 Step 2: Check image
if img is None:
    print("Error: Image not loaded")
    exit()

# 🔹 Step 3: Get image size
rows, cols = img.shape[:2]

# -----------------------------------
# 🔹 Step 4: Select 3 points in original image
# -----------------------------------
pts1 = np.float32([
    [50, 50],      # point 1
    [200, 50],     # point 2
    [50, 200]      # point 3
])

# -----------------------------------
# 🔹 Step 5: Define new positions (transformed points)
# -----------------------------------
pts2 = np.float32([
    [10, 100],     # moved point 1
    [200, 50],     # moved point 2
    [100, 250]     # moved point 3
])

# -----------------------------------
# 🔹 Step 6: Get transformation matrix
# -----------------------------------
M = cv2.getAffineTransform(pts1, pts2)

# -----------------------------------
# 🔹 Step 7: Apply transformation
# -----------------------------------
affine = cv2.warpAffine(img, M, (cols, rows))

# -----------------------------------
# 🔹 Step 8: Show results
# -----------------------------------
cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformed Image", affine)

cv2.waitKey(0)
cv2.destroyAllWindows()
