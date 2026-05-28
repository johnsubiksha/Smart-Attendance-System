import cv2

IMG_SIZE = 100

def preprocess_face(face):

    face = cv2.resize(face, (IMG_SIZE, IMG_SIZE))

    face = face / 255.0

    return face