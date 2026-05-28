from fastapi import FastAPI

from backend.routes.attendance import router as attendance_router

from backend.routes.analytics import router as analytics_router

from backend.utils.recognizer import start_recognition

app = FastAPI()

app.include_router(attendance_router)

app.include_router(analytics_router)

@app.get("/")
def home():

    return {
        "message": "Smart Attendance System Running"
    }

@app.get("/start-attendance")
def start_attendance():

    start_recognition()

    return {
        "message": "Attendance Completed"
    }