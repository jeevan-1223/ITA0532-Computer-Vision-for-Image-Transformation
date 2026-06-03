import cv2

video_path = r"C:\Users\kasir\Downloads\traffic.mp4"

cap = cv2.VideoCapture(video_path)

car_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_car.xml"
)

if car_cascade.empty():
    print("Car cascade file not found.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, (700, 500))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3
    )

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Vehicle", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
