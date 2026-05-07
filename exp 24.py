import cv2

img = cv2.imread(r"C:\Users\kasir\Downloads\download (1).jpg")

blur = cv2.GaussianBlur(img, (9, 9), 10)

mask = cv2.subtract(img, blur)

A = 2.0
high_boost = cv2.addWeighted(img, A, blur, -(A - 1), 0)

cv2.imshow("Original Image", img)
cv2.imshow("High Boost Mask", mask)
cv2.imshow("High Boost Sharpened Image", high_boost)

cv2.waitKey(0)
cv2.destroyAllWindows()
