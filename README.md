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

## ⚙ Installation

Clone the repository

```
git clone https://github.com/DurgeshGowda-HB/smart-agrospray-ai-iot.git
```

Navigate to the project folder

```
cd smart-agrospray-ai-iot
```

Install the required dependencies

```
pip install -r requirements.txt
```

---

## ▶ Running the System

Run the AI detection script

```
python ai-module/main_detec.py
```

Make sure:

* The camera is connected
* The trained YOLO model (`best.pt`) is available
* The ESP8266 device is connected to the correct serial port

The system will start detecting tomato leaf diseases and trigger pesticide spraying when a diseased leaf is detected.

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

## 🔌 Hardware Wiring

The hardware components are connected as follows:

- **ESP8266 NodeMCU**
  - Acts as the main controller for the spraying system.

- **HC-05 Bluetooth Module**
  - TX → RX (ESP8266)
  - RX → TX (ESP8266)
  - Used for communication between the AI detection system and the robot.

- **Relay Module**
  - IN → GPIO5 (ESP8266)
  - VCC → 5V
  - GND → GND

- **Pesticide Pump**
  - Connected to the relay output.
  - Activates when a diseased leaf is detected.

- **Power Supply**
  - Provides power to ESP8266 and pump system.

## 📊 Performance

- Detection Accuracy: 90–92%
- Real-time response (<1 second delay)
- Selective spraying

## 📚 Research Publication

This project is published in:
International Journal of Recent Development in Engineering and Technology (Dec 2025)

Certificate included in docs folder.
