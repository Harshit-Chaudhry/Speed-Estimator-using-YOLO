# 🚗 Speed Estimation Project using YOLO Models  

## 📌 Description  

This project involves the development of a **speed estimation system** using **YOLO (You Only Look Once)** object detection models. The system is designed to **detect vehicles in real-time** and estimate their speed based on successive video frames.  

The primary goal is to create an **efficient and accurate speed estimation tool** for **traffic monitoring and analysis**.  

## 🔥 Features  

✅ **Real-time vehicle detection** using YOLO models  
✅ **Speed estimation** based on frame-by-frame analysis  
✅ Works with **live webcam feeds** and **video files**  
✅ **Visualization** of detected vehicles and their estimated speeds  
✅ Supports **custom YOLO models** for better accuracy  

---

## 🛠️ Requirements  

Ensure you have the following installed:  

- **Python 3.x**  
- **OpenCV** (`cv2`)  
- **YOLOv8 pre-trained weights** (`ultralytics`)  
- **NumPy**  
- **Matplotlib**  

To install the required dependencies, follow the installation steps below.  

---

## ⚡ Installation  

1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/yourusername/speed-estimator-using-yolo.git
cd speed-estimator-using-yolo
```

2️⃣ **Create a Virtual Environment**  
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt
```

4️⃣ **Run the Project**  
Run one of the following based on your use case:

- **For Webcam Live Detection**:  
  ```bash
  python webcam.py
  ```
- **For Video File Processing**:  
  ```bash
  python video_capture.py
  ```

---

## 📽️ Demo Representation  

### 🎥 **Video Demo**  
[![Watch the demo](readmejunks/download.mp4)](readmejunks/output_video.mp4)  

Click the image above to watch the **full demo video** (`output_video.mp4`).  

---

## 📂 File Structure  

```
SPEED-ESTIMATOR-USING-YOLO/
│── .venv/                     # Virtual environment files
│── readmejunks/               # Folder containing demo representation files
│   ├── download.mp4           # Thumbnail (or sample video for README)
│   ├── output_video.mp4       # Final processed video showing vehicle detection
│── .gitignore                  # Git ignore file
│── LICENSE                     # Project license
│── README.md                    # This file
│── requirements.txt             # Required dependencies
│── trials.ipynb                 # Jupyter Notebook for testing
│── video_capture.py             # Script for processing video files
│── webcam.py                    # Script for real-time webcam detection
│── yolov8n.pt                   # YOLOv8 pre-trained weights
```

---

## 📝 How It Works  

### **1️⃣ Object Detection with YOLO**  
The system uses **YOLOv8** to detect vehicles in **real-time** from a video stream (webcam or file).  

### **2️⃣ Speed Calculation**  
The speed is estimated by tracking the **change in position** of detected vehicles over **successive frames** and applying a **conversion factor (pixels to real-world units).**  

### **3️⃣ Visualization**  
Detected vehicles are **highlighted with bounding boxes**, and their **estimated speeds** are displayed on the video.  

---

## 📌 Code Files Explanation  

- **`webcam.py`** → Runs **real-time vehicle detection** using a **live webcam feed**.  
- **`video_capture.py`** → Processes **pre-recorded video files** to **detect vehicles** and **estimate speed**.  
- **`trials.ipynb`** → Jupyter Notebook for **testing and debugging** detection logic.  

---

## 🔗 References  

- [YOLOv8 Official Documentation](https://docs.ultralytics.com)  
- [OpenCV Library](https://opencv.org/)  

---

## 💡 Notes  

- The **YOLO model can be trained** on a **custom dataset** to improve accuracy.  
- If you encounter **errors** in webcam mode, check that your camera is properly connected.  
- You can **replace `output_video.mp4` and `download.mp4`** with your **own demo files**.  

---

## 🚀 Future Improvements  

- 📈 **Improve accuracy** with custom YOLO training  
- 🛣️ **Support multi-lane detection** for highways  
- 📊 **Store speed data** for analytics and reporting  

---

## 🎯 Contributing  

Contributions are welcome! Feel free to submit a pull request or open an issue.  

---

## 📜 License  

This project is licensed under the **MIT License**.  
