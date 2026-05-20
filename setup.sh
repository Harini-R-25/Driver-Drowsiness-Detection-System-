#!/bin/bash

# Driver Drowsiness Detection System - Raspberry Pi Setup Script

echo "===================================="
echo " Driver Drowsiness Detection Setup"
echo "===================================="

# Update system
echo "[1/5] Updating system packages..."
sudo apt-get update -y

# Install system dependencies
echo "[2/5] Installing system dependencies..."
sudo apt-get install -y python3-pip cmake libopenblas-dev liblapack-dev libx11-dev espeak

# Install Python libraries
echo "[3/5] Installing Python libraries..."
pip3 install -r requirements.txt

# Download dlib face landmark model
echo "[4/5] Downloading shape_predictor_68_face_landmarks.dat..."
wget -q http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
bzip2 -d shape_predictor_68_face_landmarks.dat.bz2
echo "Model downloaded and extracted."

# Enable camera on Raspberry Pi
echo "[5/5] Enabling Raspberry Pi camera..."
sudo raspi-config nonint do_camera 0

echo ""
echo "===================================="
echo " Setup Complete!"
echo " Run the system with:"
echo "   python3 drowsiness.py"
echo "===================================="
