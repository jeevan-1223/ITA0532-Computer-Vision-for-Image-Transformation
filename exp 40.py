import cv2

img = cv2.imread(r"C:\Users\kasir\Downloads\butter fly image (2).jpg")

if img is None:
    print("Image not found. Check file path.")
    exit()

img = cv2.resize(img, (500, 400))

x, y, w, h = 120, 80, 250, 200

output = img.copy()

cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 3)

extracted_object = img[y:y+h, x:x+w]

cv2.imshow("Original Image", img)
cv2.imshow("Rectangle Drawn Image", output)
cv2.imshow("Extracted Object", extracted_object)

cv2.waitKey(0)
cv2.destroyAllWindows()
