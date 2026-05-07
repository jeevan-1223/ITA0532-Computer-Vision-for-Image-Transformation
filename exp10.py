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
# 🔹 Step 4: Define translation values
# -----------------------------------
tx = 100   # move right (positive)
ty = 50    # move down (positive)

# Translation matrix
M = np.float32([[1, 0, tx],
                [0, 1, ty]])

# -----------------------------------
# 🔹 Step 5: Apply transformation
# -----------------------------------
moved = cv2.warpAffine(img, M, (cols, rows))

# -----------------------------------
# 🔹 Step 6: Show results
# -----------------------------------
cv2.imshow("Original Image", img)
cv2.imshow("Moved Image", moved)

cv2.waitKey(0)
cv2.destroyAllWindows()
