import sqlite3

conn = sqlite3.connect('EmployeeLogs.db', check_same_thread=False)
cursor = conn.cursor()


def getAllInOut():
    cursor.execute("SELECT * FROM EmployeeIO")
    return cursor.fetchall()

def getInOut(id):
    cursor.execute(f"SELECT * FROM EmployeeIO WHERE id='{id}'")

    return cursor.fetchall()