import pandas as pd
import os

EXCEL_FILE = "attendance.xlsx"

# CREATE EXCEL FILE
if not os.path.exists(EXCEL_FILE):

    df = pd.DataFrame(
        columns=["Name", "Date", "Time", "Status"]
    )

    df.to_excel(EXCEL_FILE, index=False)