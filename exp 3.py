import cv2

img = cv2.imread(r"C:\Users\kasir\Downloads\download (1).jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

outline = cv2.Canny(gray, 100, 200)

cv2.imshow("Original Image", img)
cv2.imshow("Outline using Canny", outline)

cv2.waitKey(0)
cv2.destroyAllWindows()
