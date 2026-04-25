📌 Overview

This project presents a real-time Driver Drowsiness Detection System developed using Raspberry Pi and Computer Vision techniques. It continuously monitors the driver’s eye activity and detects signs of fatigue using the Eye Aspect Ratio (EAR) method. When drowsiness is detected, the system triggers an instant voice alert through a wired headset, helping prevent road accidents.

Key Features:

🔍 Real-time face and eye detection
👁️ Facial landmark-based eye tracking (Dlib – 68 points)
📉 EAR (Eye Aspect Ratio) based drowsiness detection
🔊 Voice alert using eSpeak (via wired headset)
⚡ Lightweight and efficient Raspberry Pi implementation
🚫 No wearable devices required (non-intrusive system)

🛠️ Tech Stack

Programming Language: Python
Libraries/Frameworks: OpenCV, Dlib, SciPy
Alert System: eSpeak (Text-to-Speech)
Hardware: Raspberry Pi 4, Pi Camera Module (8MP), Wired Headset
IDE: Thonny

⚙️ System Architecture

Camera → Raspberry Pi → Face Detection → Eye Landmark Detection → EAR Calculation → Drowsiness Detection → Voice Alert

How It Works:

The Pi Camera captures real-time video of the driver.
Dlib detects the face and extracts 68 facial landmarks.
Eye landmarks are used to compute the Eye Aspect Ratio (EAR).
If EAR falls below a threshold for consecutive frames → driver is drowsy.
A voice alert is generated using eSpeak through a headset.

🖥️ Output

Detects face (green rectangle)
Monitors eye movement
Displays “DROWSINESS ALERT!” on screen
Generates voice alert via headset

🚀 Applications

Driver safety systems in cars, buses, trucks
Transportation and logistics monitoring
Smart vehicle systems

📈 Future Enhancements

Night vision (IR camera support)
Mobile app integration
AI/Deep Learning-based detection
Vehicle control integration (auto braking, alerts)

⚠️ Limitations

Performance affected by low lighting
Reduced accuracy with glasses/occlusions
Requires proper camera positioning

Conclusion:

This project demonstrates an effective and affordable solution for detecting driver drowsiness in real time. By combining computer vision and embedded systems, it enhances road safety without requiring complex or expensive hardware.
