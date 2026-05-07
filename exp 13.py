import cv2
import numpy as np

# Step 1: Load image
img = cv2.imread(r"C:\Users\kasir\Downloads\download (1).jpg")

# Step 2: Check image
if img is None:
    print("Error: Image not loaded")
    exit()

# Step 3: Get image size
height, width = img.shape[:2]

# ---------------------------------------
# Step 4: Define source points (4 points)
# ---------------------------------------
src_pts = np.float32([
    [50, 50],                 # top-left
    [width - 50, 50],         # top-right
    [50, height - 50],        # bottom-left
    [width - 50, height - 50] # bottom-right
])

# ---------------------------------------
# Step 5: Define destination points
# ---------------------------------------
dst_pts = np.float32([
    [0, 0],
    [width, 0],
    [100, height],
    [width - 100, height]
])

# ---------------------------------------
# Step 6: Compute Homography Matrix
# ---------------------------------------
H, status = cv2.findHomography(src_pts, dst_pts)

# ---------------------------------------
# Step 7: Apply transformation
# ---------------------------------------
result = cv2.warpPerspective(img, H, (width, height))

# ---------------------------------------
# Step 8: Display results
# ---------------------------------------
cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
