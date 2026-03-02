import cv2
from ultralytics import YOLO
import serial
import time

CONFIDENCE_THRESHOLD = 0.7
SERIAL_PORT = 'COM7'
BAUD_RATE = 9600


def initialize_serial():
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
    return ser


def initialize_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not access camera.")
        exit()
    return cap


def load_model():
    return YOLO("best.pt")


def process_frame(frame, model):
    results = model.predict(source=frame, conf=CONFIDENCE_THRESHOLD, save=False)
    result = results[0]
    return result.boxes


def draw_boxes(frame, boxes, model):
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

    return current_state


def main():
    ser = initialize_serial()
    cap = initialize_camera()
    model = load_model()

    last_detected_state = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        boxes = process_frame(frame, model)
        current_state = draw_boxes(frame, boxes, model)

        # Serial trigger logic
        if current_state == "Diseased":
            if last_detected_state != "Diseased":
                print("Diseased leaf detected → Sending signal")
                ser.write(b'1')
        else:
            if last_detected_state == "Diseased":
                print("Leaf cleared → System reset")

        last_detected_state = current_state

        cv2.imshow("Smart AgroSpray - Detection v5", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ser.close()


if __name__ == "__main__":
    main()