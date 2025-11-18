# AI-Pose-Based-Workout-Assistant

A real-time computer vision system for automatic exercise analysis and repetition counting.

📌 Overview

This project implements an AI-powered personal trainer using MediaPipe Pose, OpenCV, and Python.
It detects human pose landmarks, computes joint angles in real-time, and tracks exercise progress (e.g., bicep curls) with automatic repetition counting.

The system is capable of:

- Detecting the user’s pose
- Calculating elbow joint angles
- Mapping angles to exercise progression
- Counting reps using direction logic
- Displaying progress bars and visual feedback

🚀 Features

✅ Real-time pose estimation using MediaPipe BlazePose
✅ Automatic joint-angle computation (shoulder–elbow–wrist)
✅ Exercise progression tracking using interpolation
✅ Intelligent repetition counter based on movement direction
✅ Real-time UI overlays (progress bar, rep counter)
✅ Works on any video or webcam feed
✅ Modular, reusable pose detection class (PoseModule.py)

🧠 How It Works

1. Pose Detection
- The poseDetector class wraps MediaPipe Pose.
- Each frame is converted to RGB and processed.
- All body landmarks are extracted.

2. Joint Angle Calculation
Using 3 landmarks:
p1 = shoulder
p2 = elbow
p3 = wrist

Find the desired landmarks here:
https://github.com/UFTHaq/Motion-Capture-Leg-Limp-with-Python-OpenCV-MediaPipe

The angle is computed using: atan2 vectors + degree conversion

3. Exercise Progress Mapping
- Using np.interp():
- Angle range → 0–100%
- Used for progress bar + rep logic

4. Rep Counting Logic
A bidirectional movement system:
- When angle reaches 100% → half rep
- When it drops to 0% → half rep
- Combine to form full rep counts

5. UI Feedback
- Vertical progress bar
- Percentage text
- Rep counter
- FPS display

📁 Project Structure
AITrainer/
│
├── AI_Trainer.py           # Main script (trainer logic)
├── PoseModule.py           # Pose detection + utilities
├── resource/
│    ├── Pose1.mp4          # Sample workout video
│    └── test.jpg           # Optional test image
└── README.md               # Documentation
