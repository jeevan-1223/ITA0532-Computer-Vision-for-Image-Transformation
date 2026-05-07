import cv2

# Load images
img1 = cv2.imread(r"C:\Users\kasir\Downloads\butter fly image (2).jpg")
img2 = cv2.imread(r"C:\Users\kasir\Downloads\butter fly image (2).jpg")

# Check image loaded
if img1 is None or img2 is None:
    print("Error loading image")
    exit()

# Crop image
crop = img1[20:120, 20:120]

# Resize cropped image
crop = cv2.resize(crop, (80, 80))

# Paste cropped image inside another image
img2[50:130, 50:130] = crop

# Display images
cv2.imshow("Original Image", img1)
cv2.imshow("Cropped Image", crop)
cv2.imshow("Pasted Image", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
