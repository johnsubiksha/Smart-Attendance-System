from fastapi import APIRouter
import pandas as pd

router = APIRouter()

EXCEL_FILE = "attendance.xlsx"

@router.get("/analytics")
def analytics():

    df = pd.read_excel(EXCEL_FILE)

    total_students = df["Name"].nunique()

    total_records = len(df)

    attendance_count = (
        df["Name"]
        .value_counts()
        .to_dict()
    )

    return {
        "total_students": total_students,
        "total_attendance_records": total_records,
        "student_attendance_count": attendance_count
    }