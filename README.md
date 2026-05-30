# ☀️ Solar Panel Fire & Environment Monitoring System

This project is an intelligent monitoring system for solar panels that collects temperature, humidity, and smoke data through an Arduino board and displays them on a graphical dashboard.

## 🛠 Technologies Used
- **Hardware:** Arduino UNO R4 WiFi, SHT20 Sensor, MQ Smoke Sensor
- **Database:** InfluxDB 2.7 (Time-series database)
- **Visualization:** Grafana
- **Backend:** Python (Ingestion Service)
- **Deployment:** Docker & Docker Compose

## 🚀 Installation and Setup Guide

To run this project inside the university's local network, follow these steps:

### 1. Hardware Setup
Make sure the Arduino is connected to Wi-Fi and has a static IP address on the network.

### 2. Software Setup
First, clone the repository:
```bash
git clone https://github.com/Hamid-Khoeini/solar-monitoring-system.git
cd solar-monitoring-system
