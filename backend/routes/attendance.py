import pandas as pd
import os
from datetime import datetime

EXCEL_FILE = "attendance.xlsx"

if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame(columns=["Name", "Date", "Time"])
    df.to_excel(EXCEL_FILE, index=False, engine="openpyxl")


def mark_attendance(name):

    df = pd.read_excel(EXCEL_FILE, engine="openpyxl")

    today = datetime.now().strftime("%Y-%m-%d")

    # Already exists check
    already_exists = (
        (df["Name"] == name) &
        (df["Date"] == today)
    ).any()

    if already_exists:
        print("Already Registered")
        return False

    new_row = {
        "Name": name,
        "Date": today,
        "Time": datetime.now().strftime("%H:%M:%S")
    }

    df = pd.concat([df, pd.DataFrame([new_row])],
                   ignore_index=True)

    df.to_excel(EXCEL_FILE,
                index=False,
                engine="openpyxl")

    print("Attendance Registered")

    return True