import cv2
import numpy as np

# Step 1: Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open camera")
    exit()

while True:
    # Step 2: Read video frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Cannot read frame")
        break

    # Step 3: Get frame size
    height, width = frame.shape[:2]

    # Step 4: Original 4 points
    pts1 = np.float32([
        [100, 100],
        [width - 100, 100],
        [100, height - 100],
        [width - 100, height - 100]
    ])

    # Step 5: Destination 4 points
    pts2 = np.float32([
        [0, 0],
        [width, 0],
        [0, height],
        [width, height]
    ])

    # Step 6: Perspective matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Step 7: Apply perspective transformation
    transformed = cv2.warpPerspective(frame, matrix, (width, height))

    # Step 8: Show output
    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformed Video", transformed)

    # Press q to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 9: Release camera
cap.release()
cv2.destroyAllWindows()
