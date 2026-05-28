# Smart Attendance System

AI-based attendance system using Face Recognition.

## Features

* Face Detection using OpenCV
* Face Recognition using FaceNet
* Automatic Attendance Marking
* Duplicate Prevention
* Unknown User Detection
* Excel Attendance Storage

---

# Technologies Used

* Python
* OpenCV
* FaceNet
* TensorFlow
* Pandas
* FastAPI

---

# Project Workflow

```text id="dj6pph"
Register Face
    ↓
Generate Embeddings
    ↓
Recognize Face
    ↓
Mark Attendance
```

---

# Run Project

## Register Face

```bash id="o0v8op"
python backend/capture_faces.py
```

## Generate Embeddings

```bash id="r5l12d"
python backend/utils/trainer.py
```

## Start Recognition

```bash id="svw8kq"
python -m backend.utils.recognizer
```

---

