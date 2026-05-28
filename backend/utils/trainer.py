import os
import cv2
import numpy as np
import joblib

from keras_facenet import FaceNet

embedder = FaceNet()

dataset_path = "dataset"

embeddings = []
names = []

for person_name in os.listdir(dataset_path):

    person_folder = os.path.join(dataset_path, person_name)

    for image_name in os.listdir(person_folder):

        image_path = os.path.join(person_folder, image_name)

        image = cv2.imread(image_path)

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        detections = embedder.extract(rgb, threshold=0.95)

        if len(detections) > 0:

            embedding = detections[0]['embedding']

            embeddings.append(embedding)

            names.append(person_name)

# Save embeddings
data = {
    "embeddings": embeddings,
    "names": names
}

os.makedirs("models", exist_ok=True)

joblib.dump(data, "models/embeddings.pkl")

print("Embeddings saved successfully")
