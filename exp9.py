import cv2

# 🔹 Step 1: Load image (use your correct path)
img = cv2.imread(r"C:\Users\kasir\Downloads\download (1).jpg")

# 🔹 Step 2: Check image
if img is None:
    print("Error: Image not loaded")
    exit()

# 🔹 Step 3: Get image center
height, width = img.shape[:2]
center = (width // 2, height // 2)

# -------------------------------
# 🔹 Step 4: Clockwise Rotation
# -------------------------------
# -45 degrees = clockwise
matrix_clockwise = cv2.getRotationMatrix2D(center, -45, 1)
rotate_clockwise = cv2.warpAffine(img, matrix_clockwise, (width, height))

# -----------------------------------
# 🔹 Step 5: Counter-Clockwise Rotation
# -----------------------------------
# +45 degrees = counter-clockwise
matrix_ccw = cv2.getRotationMatrix2D(center, 45, 1)
rotate_ccw = cv2.warpAffine(img, matrix_ccw, (width, height))

# -------------------------------
# 🔹 Step 6: Show results
# -------------------------------
cv2.imshow("Original Image", img)
cv2.imshow("Clockwise Rotation", rotate_clockwise)
cv2.imshow("Counter Clockwise Rotation", rotate_ccw)

# 🔹 Step 7: Wait & close
cv2.waitKey(0)
cv2.destroyAllWindows()
