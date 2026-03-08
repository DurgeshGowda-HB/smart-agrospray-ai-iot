# Smart AgroSpray 🌱🤖  

AI-Driven Precision Pesticide Spraying using YOLO and IoT

## 📌 Project Overview

Smart AgroSpray is an AI–IoT integrated robotic system designed for real-time tomato leaf disease detection and automated pesticide spraying.

The system uses:
- YOLOv11 for disease detection
- ESP8266 for IoT control
- HC-05 Bluetooth for communication
- Blynk app for robot navigation

## 🎯 Objectives

- Detect diseased tomato leaves in real time
- Trigger automatic pesticide spraying
- Reduce chemical wastage
- Minimize farmer exposure
- Promote sustainable farming

## 🏗 System Architecture

![image alt](https://github.com/DurgeshGowda-HB/smart-agrospray-ai-iot/blob/a3f3716248d956baff0db2952e8e625b85e61306/images/system_architecture.png.png)

Camera → YOLO Model → Bluetooth → ESP8266 → Relay → Pump

## 🛠 Tech Stack

- Python
- OpenCV
- Ultralytics YOLO
- ESP8266
- Arduino IDE
- Blynk IoT

## 🔧 Hardware Components

The Smart AgroSpray system integrates computer vision with embedded hardware to perform automated pesticide spraying.
Main components used:

- ESP8266 NodeMCU – Controls the spray mechanism
- Relay Module – Switches the pesticide pump
- Water Pump – Sprays pesticide when disease is detected
- Camera – Captures live tomato leaf images
- HC-05 Bluetooth Module – Communication between AI system and robot
- Power Supply – Provides power to the system

## ⚙ System Workflow

1. Camera captures real-time tomato leaf images.
2. YOLO model analyzes the frame and detects leaf condition.
3. Python detection module determines whether the leaf is healthy or diseased.
4. A signal is sent through serial communication.
5. ESP8266 receives the signal and activates the relay.
6. Relay turns on the pesticide pump to spray the infected plant.
7. System resets and waits for the next detection cycle.

## 📊 Performance

- Detection Accuracy: 90–92%
- Real-time response (<1 second delay)
- Selective spraying

## 📚 Research Publication

This project is published in:
International Journal of Recent Development in Engineering and Technology (Dec 2025)

Certificate included in docs folder.
