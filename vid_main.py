import cv2
import numpy as np
import time
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("yolov8n.pt")

# Initialize previous position and time
prev_x, prev_y = None, None
prev_time = None

# Define scale: Pixels to centimeters conversion
pixels_per_cm = 5  

def calculate_speed(cx, cy, prev_x, prev_y, prev_time):
    """Calculates speed in cm/s based on object movement."""
    if prev_x is not None and prev_y is not None and prev_time is not None:
        distance = np.sqrt((cx - prev_x) ** 2 + (cy - prev_y) ** 2) / pixels_per_cm
        time_elapsed = time.time() - prev_time

        if time_elapsed > 0:
            return distance / time_elapsed  # Speed in cm/s
    return None

def draw_bounding_box_and_label(frame, x1, y1, x2, y2, label, speed=None):
    """Draws bounding boxes and labels on detected objects."""
    # Dark Green Thick Rectangle
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 100, 0), 4)

    # Larger Bold Label Text
    cv2.putText(frame, label, (x1, y1 - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 100, 0), 3)

    if speed is not None:
        cv2.putText(frame, f"Speed: {speed:.2f} cm/s", (x1, y1 - 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 150), 3)

def detect_objects(frame, model):
    """Runs YOLO object detection on a frame."""
    results = model(frame)
    return results

def process_frame(frame, model):
    """Processes a frame: detects objects, calculates speed, and draws boxes."""
    global prev_x, prev_y, prev_time

    results = detect_objects(frame, model)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  
            label = r.names[int(box.cls[0])]  

            speed = calculate_speed(cx, cy, prev_x, prev_y, prev_time)

            draw_bounding_box_and_label(frame, x1, y1, x2, y2, label, speed)

            # Update previous position and time
            prev_x, prev_y = cx, cy
            prev_time = time.time()

    return frame

# Input and Output Video Paths
video_path = "samples/2.mp4"  # Change this to your video file path
output_path = "output_video.mp4"  # Save output as MP4

# Open video file
cap = cv2.VideoCapture(video_path)

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Debugging prints
print(f"Video Properties: Width={frame_width}, Height={frame_height}, FPS={fps}")

# Ensure valid video
if frame_width == 0 or frame_height == 0:
    print("Error: Could not read video file. Check the file path and format.")
    cap.release()
    exit()

# Create VideoWriter for saving output
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (frame_width, frame_height))

# Process video frame by frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("End of video or read error.")
        break

    # Process frame (detect objects and draw bounding boxes)
    frame = process_frame(frame, model)
    out.write(frame)  # Save processed frame to output video

    # Show the processed frame
    cv2.imshow("Object Speed Detection", frame)

    # Press 'Esc' to exit early
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
print(f"Processing complete. Saved output to: {output_path}")
