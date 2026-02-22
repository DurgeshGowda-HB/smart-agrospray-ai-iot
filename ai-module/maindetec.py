import cv2
from ultralytics import YOLO

#Loades the trained YOLO model
model = YOLO("best.pt")

#Open webcam for capture the picture
cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    print("Error: Could not access camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    #Run detection
    results = model(frame)
    annotated_frame = results[0].plot()
    cv2.imshow("Smart AgroSpray - Basic Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()