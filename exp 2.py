import cv2

img = cv2.imread(r"C:\Users\kasir\Downloads\download (1).jpg")

blur = cv2.blur(img, (15, 15))

cv2.imshow("Original Image", img)
cv2.imshow("Blur Image", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
