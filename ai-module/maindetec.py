import cv2
from ultralytics import YOLO
import serial
import time

# Serial Setup 
ser = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)

# Load YOLO Model
model = YOLO("best.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access camera.")
    exit()

CONFIDENCE_THRESHOLD = 0.7
last_detected_state = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, conf=CONFIDENCE_THRESHOLD, save=False)
    result = results[0]
    boxes = result.boxes

    current_state = None

    if boxes is not None:
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = float(box.conf[0])
            class_id = int(box.cls[0])
            label = model.names[class_id]

            current_state = label

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            text = f"{label} {confidence:.2f}"
            cv2.putText(frame, text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (0, 255, 0), 2)

    # Decision + Serial Logic
    if current_state == "Diseased" and last_detected_state != "Diseased":
        print("⚠ Diseased leaf detected → Sending signal")
        ser.write(b'1')

    if current_state is None and last_detected_state is not None:
        print("No leaf detected")

    last_detected_state = current_state

    cv2.imshow("Smart AgroSpray - Detection v4", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()