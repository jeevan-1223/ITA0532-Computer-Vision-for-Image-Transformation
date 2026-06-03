import cv2

# Change this path to your watch image
img = cv2.imread(r"C:\Users\kasir\Downloads\watch.jpg")

if img is None:
    print("Image not found. Check the file path.")
    exit()

img = cv2.resize(img, (600, 500))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=100,
    param1=50,
    param2=30,
    minRadius=30,
    maxRadius=200
)

output = img.copy()

if circles is not None:
    circles = circles[0].astype(int)

    for (x, y, r) in circles:
        cv2.circle(output, (x, y), r, (0, 255, 0), 3)
        cv2.putText(output,
                    "WATCH DETECTED",
                    (x - 50, y - r - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2)

cv2.imshow("Original Image", img)
cv2.imshow("Watch Recognition", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
