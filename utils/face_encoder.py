import cv2
import os
import pickle

KNOWN_FACES = []
KNOWN_NAMES = []

DATASET_PATH = "dataset"

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

for person_name in os.listdir(DATASET_PATH):

    person_folder = os.path.join(DATASET_PATH, person_name)

    for image_name in os.listdir(person_folder):

        image_path = os.path.join(person_folder, image_name)

        image = cv2.imread(image_path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:

            face = gray[y:y+h, x:x+w]

            face = cv2.resize(face, (100, 100))

            KNOWN_FACES.append(face)
            KNOWN_NAMES.append(person_name)

data = {
    "faces": KNOWN_FACES,
    "names": KNOWN_NAMES
}

with open("models/face_data.pkl", "wb") as file:
    pickle.dump(data, file)

print("Face data saved successfully")