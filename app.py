# app.py

import cv2
import numpy as np
from tensorflow.keras.models import load_model
from utils.attendance_manager import mark_attendance
import os


# Load trained CNN model
model = load_model("models/face_cnn_model.h5")

# Class labels
class_names = os.listdir("dataset")

# Load Haar Cascade for face detection
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Start webcam
video_capture = cv2.VideoCapture(0)

while True:

    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:

        face = gray[y:y+h, x:x+w]

        # Resize for CNN input
        face = cv2.resize(face, (100, 100))

        # Normalize
        face = face / 255.0

        # Reshape for model
        face = face.reshape(1, 100, 100, 1)

        # Predict
        prediction = model.predict(face)

        class_index = np.argmax(prediction)

        confidence = prediction[0][class_index]

        if confidence > 0.7:
            name = class_names[class_index]
            mark_attendance(name)
        else:
            name = "Unknown"

        # Draw rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(
            frame,
            f"{name} ({confidence:.2f})",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("Smart Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()