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

def getEmployeesInWatchList(nombreAdmin):
    cursor.execute(f"SELECT EmployeeID FROM Watchlists WHERE AdminName='{nombreAdmin}'")
    empleados = cursor.fetchall()
    r = []
    for empleado in empleados:
        r.append(getEmployeeData(empleado[0])[0])
    return r

def getAdminChanges(n):
    cursor.execute("SELECT * FROM AdminChanges ORDER BY ID DESC")
    return cursor.fetchmany(n)


def getAllCabinas():
    cursor.execute("SELECT DISTINCT(MAC) FROM estadosCabinas")
    return cursor.fetchall()

def getEstadoCabina(mac):
    cursor.execute(f"SELECT * FROM estadosCabinas WHERE MAC='{mac}' ORDER BY Date DESC")
    return cursor.fetchone()
    
def getAllEstadosCabinas():
    cursor.execute("SELECT DISTINCT(MAC) FROM estadosCabinas")
    macs = cursor.fetchall()
    r = []
    for mac in macs:
        r.append(getEstadoCabina(mac[0]))
    return r


def getEmployees():
    cursor.execute("SELECT * FROM Employees")
    return cursor.fetchall()

def createEmployee(name, surname, email, phone, address, zip, position):
    cmd = f'''INSERT INTO Employees (Name, Surname, Email, PhoneNumber, Address, ZipCode, Position)
    VALUES ('{name}', '{surname}', '{email}', '{phone}', '{address}', '{zip}', '{position}')'''
    cursor.execute(cmd)
    conn.commit()

def checkEmployee(name, surname, email, phone):
    cursor.execute(f'''SELECT * FROM Employees WHERE (Name="{name}" AND Surname="{surname}") OR Email="{email}" OR PhoneNumber="{phone}"''')
    user = cursor.fetchone()
    return False if user is None else True
