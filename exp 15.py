import cv2
import numpy as np

# Step 1: Load image
img = cv2.imread(r"C:\Users\kasir\Downloads\download (1).jpg")

if img is None:
    print("Error: Image not loaded. Check path.")
    exit()

height, width = img.shape[:2]

# Step 2: Source points
src_pts = np.array([
    [50, 50],
    [width - 50, 50],
    [50, height - 50],
    [width - 50, height - 50]
], dtype=np.float32)

# Step 3: Destination points
dst_pts = np.array([
    [0, 0],
    [width, 0],
    [100, height],
    [width - 100, height]
], dtype=np.float32)

# Step 4: Function to calculate Homography using DLT
def compute_homography_dlt(src, dst):
    A = []

    for i in range(len(src)):
        x, y = src[i]
        u, v = dst[i]

        A.append([-x, -y, -1, 0, 0, 0, u*x, u*y, u])
        A.append([0, 0, 0, -x, -y, -1, v*x, v*y, v])

    A = np.array(A)

    # Solve Ah = 0 using SVD
    U, S, Vt = np.linalg.svd(A)

    # Last row of Vt gives homography values
    H = Vt[-1].reshape(3, 3)

    # Normalize
    H = H / H[2, 2]

    return H

# Step 5: Compute Homography matrix
H = compute_homography_dlt(src_pts, dst_pts)

print("Homography Matrix using DLT:")
print(H)

# Step 6: Apply transformation
result = cv2.warpPerspective(img, H, (width, height))

# Step 7: Display output
cv2.imshow("Original Image", img)
cv2.imshow("DLT Transformed Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
