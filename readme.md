# ✋ Real-Time Hand Gesture Recognition System

<p align="center">
  <img src="demo.gif" width="750">
</p>

<p align="center">
A real-time computer vision application that detects a human hand through a webcam and accurately counts the number of fingers being displayed using OpenCV and MediaPipe.
</p>

---

## 📌 Overview

The **Real-Time Hand Gesture Recognition System** is a computer vision project developed using **Python**, **OpenCV**, and **MediaPipe**.

The application captures live video from a webcam, detects the user's hand in real time, extracts hand landmarks, analyses finger positions, and finally determines how many fingers are raised.

The project demonstrates the practical use of computer vision for real-time gesture analysis without requiring any specialized hardware.

This project serves as an excellent beginner implementation of:
- Hand Detection
- Hand Landmark Tracking
- Finger State Detection
- Real-Time Image Processing
- Human-Computer Interaction (HCI)

---

## 🎥 Demo

> Replace this image with your demo GIF.

![Demo](demo.gif)

*(You can convert your screen recording into a GIF and upload it as `demo.gif`.)*

---

# ✨ Features

- 📹 Real-time webcam processing
- ✋ Accurate hand detection
- 👆 Counts raised fingers instantly
- ⚡ Fast frame processing
- 🖥️ Live visualization
- 📌 Landmark tracking using MediaPipe
- 🎯 Beginner-friendly implementation
- 💻 Lightweight and easy to run

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| OpenCV | Video Processing |
| MediaPipe | Hand Landmark Detection |
| NumPy | Numerical Operations |

---

# 📂 Project Structure

```
Real-Time-Hand-Gesture-Recognition-System/
│
├── Finger Counter.py
├── requirement.txt
├── README.md
└── demo.gif
```

---

# ⚙️ How It Works

The complete workflow consists of several stages.

### Step 1 — Webcam Initialization

The program first opens the webcam using OpenCV and continuously captures frames.

```
Camera
   ↓
Video Frames
```

---

### Step 2 — Hand Detection

Each frame is processed by MediaPipe's Hand Tracking model.

```
Frame
   ↓
MediaPipe
   ↓
Hand Detected
```

---

### Step 3 — Landmark Extraction

MediaPipe generates **21 hand landmarks** for every detected hand.

These landmarks correspond to joints such as:

- Wrist
- Thumb
- Index Finger
- Middle Finger
- Ring Finger
- Little Finger

Example:

```
Thumb Tip
Index Tip
Middle Tip
Ring Tip
Little Tip
```

---

### Step 4 — Finger Position Analysis

The program compares the position of each fingertip with its lower joint.

If

```
Tip.y < Joint.y
```

the finger is considered **Raised**.

Otherwise

```
Tip.y > Joint.y
```

the finger is considered **Folded**.

The thumb is detected differently using the x-coordinate because of its sideways orientation.

---

### Step 5 — Finger Counting

Each raised finger contributes a value of **1**.

Example:

```
Thumb   = 1
Index   = 1
Middle  = 1
Ring    = 0
Little  = 0

Total = 3
```

The total count is displayed live on the webcam window.

---

# 🧠 Algorithm

```
Start

↓

Open Webcam

↓

Capture Frame

↓

Detect Hand

↓

Extract Landmarks

↓

Check Thumb Position

↓

Check Remaining Fingers

↓

Count Raised Fingers

↓

Display Count

↓

Repeat Until Exit
```

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Real-Time-Hand-Gesture-Recognition-System.git
```

Move into the directory

```bash
cd Real-Time-Hand-Gesture-Recognition-System
```

Install dependencies

```bash
pip install -r requirement.txt
```

Run

```bash
python "Finger Counter.py"
```

---

# 📋 Requirements

Python 3.9+

Libraries

```
opencv-python
mediapipe
numpy
```

or simply

```bash
pip install -r requirement.txt
```

---

# 🖥️ Output

The application displays

- Live webcam feed
- Hand landmarks
- Finger count
- Real-time processing

Example

```
Finger Count : 0

Finger Count : 1

Finger Count : 3

Finger Count : 5
```

---

# 🚀 Applications

This project can be extended for various real-world applications:

- Gesture-based computer control
- Touchless Human Computer Interaction
- Smart classroom systems
- Sign language preprocessing
- Robotics control
- Interactive games
- Virtual presentations
- IoT device control
- Smart home automation

---

# 🔮 Future Improvements

- Multiple hand detection
- Dynamic gesture recognition
- Volume control using gestures
- Virtual mouse
- Virtual keyboard
- Gesture-controlled media player
- Brightness control
- AI-based gesture classification
- American Sign Language recognition

---

# 📸 Screenshots

Add screenshots like:

```
screenshots/
    image1.png
    image2.png
    image3.png
```

---

# 🤝 Contributing

Contributions are welcome.

If you'd like to improve the project:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 👨‍💻 Author

**Ayush Kumar Jha**

Electronics and Communication Engineering Student

Interested in:

- Computer Vision
- Artificial Intelligence
- Embedded Systems
- Cybersecurity

GitHub:
https://github.com/AyushKJha

LinkedIn:
(Add your LinkedIn URL)

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository

It motivates me to build more open-source projects.

---

## 📜 License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2025 Ayush Kumar Jha

Permission is hereby granted...
```

---
