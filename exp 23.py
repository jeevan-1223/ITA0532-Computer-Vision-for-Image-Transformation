import cv2

img = cv2.imread(r"C:\Users\kasir\Downloads\download (1).jpg")

blur = cv2.GaussianBlur(img, (9, 9), 10.0)

sharpened = cv2.addWeighted(img, 1.5, blur, -0.5, 0)

cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blur)
cv2.imshow("Unsharp Masking", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
