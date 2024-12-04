# Virtual Hand-Gesture Keyboard

## Project Description
A virtual keyboard that allows users to type using hand gestures via webcam, implemented with OpenCV and CVZone. The application uses hand tracking to detect finger positions and enables typing by hovering and pinching gestures.

## Features
- Real-time hand tracking
- Virtual keyboard layout
- Typing through hand gestures
- Interactive visual feedback

## Prerequisites
- Python 3.7+
- OpenCV
- CVZone
- NumPy

## Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/virtual-hand-gesture-keyboard.git
cd virtual-hand-gesture-keyboard
```

2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install required dependencies
```bash
pip install -r requirements.txt
```

## Dependencies
- opencv-python
- cvzone
- numpy

## Usage
Run the script with:
```bash
python main.py
```

## How It Works
- Hover your hand over a key to highlight it
- Pinch (bring thumb and ring finger close) to select a key
- The selected text appears in the text box at the bottom

## Limitations
- Requires good lighting
- May need calibration for different hand sizes
- Dependent on webcam quality

## Acknowledgments
- OpenCV
- CVZone
- Inspired by computer vision interaction techniques

## MediaPipe: Quick Overview
MediaPipe is a Google-developed, open-source framework for building cross-platform AI-powered multimedia solutions. For hand tracking, it:
- Detects up to 2 hands simultaneously
- Tracks 21 hand landmarks in real-time
- Provides 3D coordinate tracking
- Works across different platforms
- Offers high accuracy (95%+)
- Low computational requirements

Key Uses:
- Gesture recognition
- Virtual interfaces
- Computer vision applications
- Interactive experiences

How It Works in Our Virtual Keyboard:
- Tracks index finger for hovering
- Measures thumb-index distance for clicks
- Enables touchless typing through hand gestures

The framework simplifies complex machine learning tasks, making advanced computer vision accessible and efficient.
![MediaPipe-Hands-21-landmarks-13](https://github.com/user-attachments/assets/082d25f9-a1ec-4022-8938-dc184119182b)
