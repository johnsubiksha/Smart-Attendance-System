import pandas as pd
from datetime import datetime


def mark_attendance(name):
    file_path = "attendance/attendance.csv"

    try:
        df = pd.read_csv(file_path)
    except:
        df = pd.DataFrame(columns=["Name", "Date", "Time"])

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    if not ((df['Name'] == name) & (df['Date'] == date)).any():
        new_entry = {
            "Name": name,
            "Date": date,
            "Time": time
        }

        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(file_path, index=False)
        print(f"Attendance marked for {name}")