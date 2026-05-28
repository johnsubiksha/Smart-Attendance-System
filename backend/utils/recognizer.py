import cv2
import numpy as np
import joblib

from keras_facenet import FaceNet
from sklearn.metrics.pairwise import cosine_similarity

from backend.routes.attendance import mark_attendance

# Load FaceNet
embedder = FaceNet()

# Load embeddings
data = joblib.load("models/embeddings.pkl")

known_embeddings = data["embeddings"]
known_names = data["names"]

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    detections = embedder.extract(rgb, threshold=0.95)

    name = "User Not Found"

    for detection in detections:

        x, y, w, h = detection['box']

        embedding = detection['embedding']

        similarities = cosine_similarity(
            [embedding],
            known_embeddings
        )[0]

        best_match_index = np.argmax(similarities)

        best_similarity = similarities[best_match_index]

        # Threshold
        if best_similarity > 0.7:

            name = known_names[best_match_index]

            success = mark_attendance(name)

            if success:
                message = "Attendance Registered"
            else:
                message = "Already Registered"

            cv2.putText(frame,
                        message,
                        (50,50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0,255,0),
                        2)

            cv2.imshow("Attendance System", frame)

            cv2.waitKey(2000)

            cap.release()
            cv2.destroyAllWindows()

            exit()

        cv2.rectangle(frame,
                      (x,y),
                      (x+w,y+h),
                      (0,255,0),
                      2)

        cv2.putText(frame,
                    name,
                    (x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    2)

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
