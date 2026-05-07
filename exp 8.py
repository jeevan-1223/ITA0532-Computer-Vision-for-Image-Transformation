import cv2

# 🔹 Step 1: Give correct image path
img = cv2.imread(r"C:\Users\kasir\Downloads\download (1).jpg")

# 🔹 Step 2: Check image loaded or not
if img is None:
    print("Error: Image not loaded. Check file path or file.")
    exit()

# 🔹 Step 3: Get original size
height, width = img.shape[:2]
print("Original Size:", width, "x", height)

# -------------------------------
# 🔹 Step 4: Scale to Bigger Size
# -------------------------------
bigger = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# -------------------------------
# 🔹 Step 5: Scale to Smaller Size
# -------------------------------
smaller = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# -------------------------------
# 🔹 Step 6: Show all images
# -------------------------------
cv2.imshow("Original Image", img)
cv2.imshow("Bigger Image (2x)", bigger)
cv2.imshow("Smaller Image (0.5x)", smaller)

# 🔹 Step 7: Wait & close
cv2.waitKey(0)
cv2.destroyAllWindows()
