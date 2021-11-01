import sqlite3

conn = sqlite3.connect('EmployeeLogs.db', check_same_thread=False)
cursor = conn.cursor()


def getAllInOut():
    cursor.execute("SELECT * FROM EmployeeIO ORDER BY ID DESC")
    return cursor.fetchall()

def getInOut(idEntrada):
    cursor.execute(f"SELECT * FROM EmployeeIO WHERE id='{idEntrada}'")
    return cursor.fetchall()

def getInFrom(idEmpleado, n):
    cursor.execute(f"SELECT ID, Date, Time, ExpectedCheckIn, Temperature FROM EmployeeIO WHERE EmployeeId='{idEmpleado}' AND InOut='In'")
    return cursor.fetchmany(n)

def getOutFrom(idEmpleado, n):
    cursor.execute(f"SELECT ID, Date, Time, EstimatedCheckOut, Temperature FROM EmployeeIO WHERE EmployeeId='{idEmpleado}' AND InOut='Out'")
    return cursor.fetchmany(n)

def getEmployeeName(idEmpleado):
    cursor.execute(f"SELECT EmployeeName FROM EmployeeIO WHERE ID='{idEmpleado}'")
    return cursor.fetchone()[0]

def getEmployeeData(idEmpleado):
    cursor.execute(f"SELECT * FROM Employees WHERE id='{idEmpleado}'")
    return cursor.fetchall()

#def insert_picture(conn, picture_file):
#     with open(picture_file, 'rb') as input_file:
#        ablob = input_file.read()
#        sqlite3.Binary(ablob)
#        conn.execute("INSERT INTO EmployeeIO (Picture) VALUES (?)", (ablob,))


