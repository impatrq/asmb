import sqlite3

conn = sqlite3.connect('EmployeeLogs.db')
cursor = conn.cursor()

if False:
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

        cmd = """CREATE TABLE IF NOT EXISTS Employees(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT,
                Surname TEXT,
                Email TEXT,
                PhoneNumber TEXT,
                Address TEXT,
                ZipCode TEXT,
                Position TEXT
                )"""
        cursor.execute(cmd)

        cmd = """CREATE TABLE IF NOT EXISTS WatchlistIO(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                EmployeeName TEXT,
                EmployeeID INTEGER,
                Date DATE,
                Time TIME,
                ExpectedCheckIn TIME,
                EstimatedCheckOut TIME,
                Temperature REAL,
                InOut TEXT,
                AdminName TEXT
                )"""
        cursor.execute(cmd)

        cmd = """CREATE TABLE IF NOT EXISTS Watchlists(
                AdminName TEXT,
                EmployeeName TEXT
                )"""
        cursor.execute(cmd)