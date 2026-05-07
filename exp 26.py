import cv2

img = cv2.imread(r"C:\Users\kasir\Downloads\download (1).jpg")

watermarked = img.copy()

text = "Jeevan Sai"

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(watermarked,
            text,
            (50, 50),
            font,
            1,
            (255, 255, 255),
            2,
            cv2.LINE_AA)

cv2.imshow("Original Image", img)
cv2.imshow("Watermarked Image", watermarked)

cv2.waitKey(0)
cv2.destroyAllWindows()
