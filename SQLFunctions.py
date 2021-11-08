import sqlite3

conn = sqlite3.connect('EmployeeLogs.db', check_same_thread=False)
cursor = conn.cursor()


def getAllInOut():
    cursor.execute("SELECT * FROM EmployeeIO ORDER BY id DESC")
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

def getNInOut(n):
    cursor.execute("SELECT * FROM EmployeeIO ORDER BY id DESC")
    return cursor.fetchmany(n)

def getInOutFromWatchlist(nombreAdmin, n):
    cursor.execute(f"SELECT ID, EmployeeName, EmployeeID, Date, Time, ExpectedCheckIn, EstimatedCheckOut, Temperature, InOut FROM WatchlistIO WHERE AdminName='{nombreAdmin}' ORDER BY id DESC")
    return cursor.fetchmany(n)

