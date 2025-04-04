import cv2
import numpy as np
import time
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Speed Calculation Variables
prev_x, prev_y = None, None
prev_time = None
pixels_per_cm = 5  # Adjust based on real-world calibration

def calculate_speed(cx, cy, prev_x, prev_y, prev_time):
    """Calculate the speed of detected objects."""
    if prev_x is not None and prev_y is not None:
        distance = np.sqrt((cx - prev_x) ** 2 + (cy - prev_y) ** 2) / pixels_per_cm
        time_elapsed = time.time() - prev_time

        if time_elapsed > 0:
            return distance / time_elapsed
    return None

def draw_bounding_box_and_label(frame, x1, y1, x2, y2, label, speed=None):
    """Draw bounding box and speed label on detected objects."""
    overlay = frame.copy()
    cv2.rectangle(overlay, (x1, y1), (x2, y2), (0, 0, 255), -1)  # Dark Red filled rectangle
    alpha = 0.4  # Transparency factor
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 4)  # Thick bounding box
    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)

    if speed is not None:
        cv2.putText(frame, f"Speed: {speed:.2f} cm/s", (x1, y1 - 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 3)
        
def detect_objects(frame, model):
    """Run YOLO detection on the frame."""
    results = model(frame)
    return results

def process_frame(frame, model):
    """Process each frame for object detection and speed estimation."""
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

# Choose Input (Webcam or Video)
mode = input("Enter 'w' for Webcam, 'v' for Video file: ").strip().lower()

if mode == "w":
    cap = cv2.VideoCapture(0)  # Webcam
elif mode == "v":
    cap = cv2.VideoCapture("readmejunks/download.mp4")  # Change to your video file
else:
    print("Invalid input. Exiting...")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = process_frame(frame, model)
    cv2.imshow("Object Speed Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
