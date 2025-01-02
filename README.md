# Automated Car Management System

This project is an **Automated Car Management System** built using Python and Raspberry Pi. It leverages IR sensors connected via GPIO pins to detect vehicle presence and monitor parking spaces in real-time. The system processes sensor inputs and outputs relevant data through a command-line interface.

---

## Features

- **Real-Time Vehicle Detection**:
  - Detects vehicle entry and exit using IR sensors connected to GPIO pins.
  - Outputs detection status in the console with timestamps.

- **Sensor Monitoring**:
  - Continuously monitors two sensors for changes in input.
  - Provides detailed logs of sensor states.

- **Modular Design**:
  - Utilizes multiprocessing for efficient parallel execution of sensor monitoring tasks.

- **Safe Exit**:
  - Handles interruptions gracefully and cleans up GPIO states before exiting.

---

## Hardware Requirements

- **Raspberry Pi**:
  - A Raspberry Pi board with GPIO pin support.

- **IR Sensors**:
  - Two IR sensors connected to GPIO pins (Pin 3 and Pin 5 in BOARD mode).

- **Power Supply**:
  - A stable power source for the Raspberry Pi and sensors.

---

## Software Details

- **Programming Language**: Python 3.x
- **Libraries Used**:
  - `RPi.GPIO`: For GPIO pin control and interaction.
  - `multiprocessing`: To manage parallel processes.
  - `time`: For timestamp generation and delays.

---

## How It Works

1. **GPIO Pin Setup**:
   - Configures Pin 3 and Pin 5 in BOARD mode for sensor input.

2. **Sensor Monitoring**:
   - Reads sensor inputs in a continuous loop.
   - Detects changes in sensor states and logs them with timestamps.

3. **Parallel Execution**:
   - Runs the sensor monitoring process in parallel using the `multiprocessing` library.

4. **Safe Termination**:
   - Cleans up GPIO settings on program exit or keyboard interruption.

---


## Limitations and Future Enhancements

- **Current Limitations**:
  - Limited to two sensors for vehicle detection.
  - Requires manual script execution.

- **Future Enhancements**:
  - Add more sensors for better coverage.
  - Implement a web-based interface for real-time monitoring.
  - Integrate database logging for persistent storage of sensor data.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
- Video attached for sample purposes

https://github.com/user-attachments/assets/170bf967-f16e-44da-8e30-814cb6f7f3d7

