import cv2

# Step 1: Load image
img = cv2.imread(r"C:\Users\kasir\Downloads\download (1).jpg")

# Step 2: Check image loaded
if img is None:
    print("Error: Image not loaded")
    exit()

# Step 3: Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 4: Apply Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Step 5: Display results
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Canny Edge Detection", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
