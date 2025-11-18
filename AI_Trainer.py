import cv2
import numpy as np
import time
import PoseModule as pm

# ----------------------------------------------
# Load video and initialize pose detector
# ----------------------------------------------
cap = cv2.VideoCapture(r"Pose1.mp4")
detector = pm.poseDetector()

# ----------------------------------------------
# Variables for repetition counting
# ----------------------------------------------
count = 0       # Total reps counted
dir = 0         # Direction of movement: 0 = down, 1 = up
ptime = 0       # For FPS (if needed)

while True:
    # ------------------------------------------
    # Read frame from video
    # ------------------------------------------
    success, img = cap.read()
    if not success:
        break

    img = cv2.resize(img, (1280, 720))

    # ------------------------------------------
    # Detect pose and extract landmark positions
    # ------------------------------------------
    img = detector.findPose(img, draw=False)
    lmlist = detector.findPosition(img, draw=False)

    # ------------------------------------------
    # Calculate elbow angle + normalized % + bar
    # ------------------------------------------
    if len(lmlist) != 0:

        # Angle between Shoulder (11), Elbow (13), Wrist (15)
        angle = detector.findAngle(img, 11, 13, 15)

        # Convert angle range to percentage of curl (0% to 100%)
        per = np.interp(angle, (210, 310), (0, 100))

        # Vertical bar for UI feedback
        bar = np.interp(angle, (220, 310), (650, 100))

        # --------------------------------------
        # Repetition counting logic
        # --------------------------------------
        # When arm is fully contracted → per = 100
        if per == 100:
            if dir == 0:          # If movement was downward before
                count += 0.5       # Half rep completed
                dir = 1            # Now movement is upward

        # When arm is fully extended → per = 0
        if per == 0:
            if dir == 1:
                count += 0.5       # Full rep completed
                dir = 0

        print(count)

        # --------------------------------------
        # Draw vertical progress bar
        # --------------------------------------
        cv2.rectangle(img, (1100, 100), (1175, 650), (0, 255, 0), 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), (0, 255, 0), cv2.FILLED)

        # Curl percentage text
        cv2.putText(img, f'{int(per)} %', (1100, 75),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)

        # --------------------------------------
        # Draw repetition counter
        # --------------------------------------
        cv2.putText(img, str(int(count)), (45, 670),
                    cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    # ------------------------------------------
    # Show output frame
    # ------------------------------------------
    cv2.imshow("Image", img)
    cv2.waitKey(1)
