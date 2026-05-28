import cv2
import os

student_name = input("Enter Student Name: ")

# Absolute project root path
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

path = os.path.join(
    BASE_DIR,
    "dataset",
    student_name
)

os.makedirs(path, exist_ok=True)

camera = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

count = 0

while True:

    ret, frame = camera.read()

    if not ret:
        print("Camera not working")
        break

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = face_detector.detectMultiScale(
        gray,
        1.3,
        5
    )

    for (x, y, w, h) in faces:

        face = frame[y:y+h, x:x+w]

        count += 1

        file_path = os.path.join(
            path,
            f"{count}.jpg"
        )

        cv2.imwrite(file_path, face)

        print(f"Saved: {file_path}")

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

    cv2.imshow("Capture Faces", frame)

    if cv2.waitKey(1) == 13 or count >= 30:
        break

camera.release()

cv2.destroyAllWindows()

print(f"{student_name} face dataset saved successfully")
