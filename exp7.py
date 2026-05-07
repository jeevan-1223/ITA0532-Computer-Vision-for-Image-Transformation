import cv2

# Start webcam
cap = cv2.VideoCapture(0)

# Set video size (important)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define codec and create output file
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture")
        break

    # Save the frame to file
    out.write(frame)

    # Show video
    cv2.imshow("Webcam", frame)

    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()
