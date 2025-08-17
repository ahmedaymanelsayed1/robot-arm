# 🤖 Robotic Arm Controlled via Laptop Camera

## 🔹 Project Overview

This project is a **6-DOF robotic arm with servo motors** that can be controlled through **hand gestures detected by a laptop camera**, using **Python and Arduino**.

The robotic arm is designed to move precisely and can **pick and place objects** efficiently. It demonstrates the integration of **computer vision, robotics, and embedded systems**, creating an **interactive real-time robotic platform**.

The control system works by detecting **hand gestures** with the laptop camera. These gestures are processed using Python and then translated into servo motor commands, which are sent to the Arduino board via serial communication.

---

## 🛠️ Hardware Components

* **6 × MG995 Servo Motors** – for joint movements of the robotic arm.
* **Arduino Uno** – microcontroller for servo control.
* **12V Power Supply** – to provide stable power to the servos.
* **Buck Converter** – to step down voltage from 12V → 7V for servo motors.
* **3mm Screws & Bolts** – for mechanical assembly.
* **Jumper Wires** – for connections between Arduino, servos, and power.
* **Laptop Camera** – to capture hand gestures in real time.
* *(Optional)* External breadboard for wiring and testing.

---

## 💻 Software Requirements

### 🔹 Python Code

The Python script handles **gesture detection** and sends servo control signals to Arduino.

Required libraries:

* `opencv-python` → Image/video processing.
* `cvzone` → Simplifies hand tracking.
* `numpy` → Mathematical operations.
* `pyserial` → Serial communication with Arduino.
* `mediapipe` → Hand landmark detection.

Install dependencies:

```
pip install opencv-python cvzone numpy pyserial mediapipe
```

### 🔹 Arduino Code

The Arduino sketch receives commands from Python and controls the servo motors accordingly.

* Make sure the **Servo library** is installed in Arduino IDE.
* Adjust the **servo pin mapping** in the code to match your wiring.

---

## 🔧 Assembly Steps

1. Mount the **6 MG995 servos** onto the robotic arm frame using 3mm screws.
2. Connect each servo signal wire to the **Arduino digital pins** (D2–D7 recommended).
3. Connect the servo power lines to the **buck converter output (7V)**.
4. Connect the **buck converter input** to the **12V power supply**.
5. Connect Arduino to the laptop via **USB cable**.
6. Upload the Arduino code, then run the Python script.

---

## ⚙️ How It Works

1. Laptop camera captures real-time **hand gestures**.
2. Python processes the video feed and **detects hand landmarks**.
3. Gestures are mapped to **servo motor angles**.
4. Commands are sent to the Arduino via **serial communication**.
5. Arduino drives the **servo motors**, replicating the detected hand movements on the robotic arm.

---

## 🌟 Features

* Real-time control of robotic arm via **computer vision**.
* Smooth movement using **6-DOF servo configuration**.
* Fully customizable for new gestures or tasks (e.g., object tracking, automation).
* Combines **robotics, embedded systems, and AI-based vision**.
* Open-source and easy to replicate.

---

## 🔮 Future Improvements

* Add **inverse kinematics** for more precise control.
* Integrate **voice commands** alongside gesture recognition.
* Use **external depth camera (Intel RealSense / Kinect)** for better accuracy.
* Expand to **wireless control** (Bluetooth/WiFi module for Arduino).
* Enable **autonomous tasks** (e.g., object sorting, line following).

---

## 📂 Project Structure

```
├── Arduino/
│   └── robotic_arm.ino        # Arduino servo control code
├── Python/
│   └── gesture_control.py     # Python gesture detection & serial communication
├── Images/
│   └── demo.jpg               # Sample images/screenshots
├── README.md                  # Project documentation
```
