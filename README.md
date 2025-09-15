# 🤖 Edge AI Object Detection Robot

An embedded systems project that brings together real-time **object detection**, **motor control**, and **machine learning on the edge**. This robot detects objects using a lightweight AI model and reacts in real time using an embedded microcontroller.

---

## 📸 Project Overview

This project uses a **Raspberry Pi** (or Jetson Nano) as the primary processing unit to run a **TensorFlow Lite model** (e.g., MobileNetV2) and a microcontroller (e.g., **Arduino Uno**, **ESP32**, or **RP2040**) to control the robot's motion. Detected object classes (like `person`, `car`, etc.) influence movement commands (e.g., `avoid`, `follow`, `stop`) sent over UART to the motor controller.

---

## 🧠 Features

- Real-time **object detection** using TensorFlow Lite
- Embedded firmware for **motor control via serial commands**
- Live video feed with detection overlays via OpenCV
- Modular firmware design in C++ (Arduino)
- Expandable: add ultrasonic sensors, BLE, or PID control

---

## 🧰 Tools & Stack

| Layer | Technology |
|-------|------------|
| **ML Inference** | TensorFlow Lite, Python |
| **Computer Vision** | OpenCV |
| **Hardware Interface** | Raspberry Pi 4 / Jetson Nano, Arduino Uno / RP2040 |
| **Firmware** | C++, Arduino IDE |
| **Communication** | UART (Serial) |
| **Motor Control** | H-Bridge Driver (e.g., L298N), PWM |

---

## 🔌 Hardware Required

- Raspberry Pi 4 / Jetson Nano
- Arduino Uno / RP2040 / ESP32
- USB or Pi Camera Module
- L298N motor driver
- DC Motors with wheels
- Power supply (battery pack or 5V wall adapter)
- Jumper wires, breadboard or custom PCB

---

## 🧾 File Structure

