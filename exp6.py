import cv2

# Load video
cap = cv2.VideoCapture(r"C:\Users\kasir\Downloads\ram.mp4")

if not cap.isOpened():
    print("Error: Cannot open video")
else:
    delay = 30

    print("Press s = Slow | f = Fast | n = Normal | q = Quit")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("End of video")
            break

        # Show video
        cv2.imshow("Video", frame)

        key = cv2.waitKey(delay) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('s'):
            delay = 100
        elif key == ord('f'):
            delay = 10
        elif key == ord('n'):
            delay = 30

cap.release()
cv2.destroyAllWindows()
