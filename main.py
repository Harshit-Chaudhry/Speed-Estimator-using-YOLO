import cv2
import numpy as np
import time
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

prev_x, prev_y = None, None
prev_time = None
pixels_per_cm = 5 

def calculate_speed(cx, cy, prev_x, prev_y, prev_time):
    if prev_x is not None and prev_y is not None:
        distance = np.sqrt((cx - prev_x) ** 2 + (cy - prev_y) ** 2) / pixels_per_cm
        time_elapsed = time.time() - prev_time

        if time_elapsed > 0:
            return distance / time_elapsed
    return None

def draw_bounding_box_and_label(frame, x1, y1, x2, y2, label, speed=None):
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    if speed is not None:
        cv2.putText(frame, f"Speed: {speed:.2f} cm/s", (x1, y1 - 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        
def detect_objects(frame, model):
    results = model(frame)
    return results

def process_frame(frame, model):
    global prev_x, prev_y, prev_time

    results = detect_objects(frame, model)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2 
            label = r.names[int(box.cls[0])]  
            speed = calculate_speed(cx, cy, prev_x, prev_y, prev_time)
            draw_bounding_box_and_label(frame, x1, y1, x2, y2, label, speed)
            prev_x, prev_y = cx, cy
            prev_time = time.time()

    return frame

cap = cv2.VideoCapture(0)  

model = YOLO("yolov8n.pt")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = process_frame(frame, model)

    cv2.imshow("Object Speed Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:  
        break

cap.release()
cv2.destroyAllWindows()
