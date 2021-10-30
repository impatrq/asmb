import sqlite3

conn = sqlite3.connect('EmployeeLogs.db')
cursor = conn.cursor()


cmd = """CREATE TABLE IF NOT EXISTS EmployeeIO(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        EmployeeName TEXT,
        EmployeeID INTEGER,
        Date DATE,
        Time TIME,
        ExpectedCheckIn TIME,
        EstimatedCheckOut TIME,
        Temperature REAL,
        InOut TEXT
        )"""
cursor.execute(cmd)