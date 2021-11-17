import sqlite3
from TimeFunctions import getDay, getTime

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
    cursor.execute(f"SELECT Name, Surname FROM Employees WHERE ID='{idEmpleado}'")
    return cursor.fetchone()

def getEmployeeData(idEmpleado):
    cursor.execute(f"SELECT * FROM Employees WHERE id='{idEmpleado}'")
    return cursor.fetchall()

def getNInOut(n):
    cursor.execute("SELECT * FROM EmployeeIO ORDER BY id DESC")
    return cursor.fetchmany(n)

def getInOutFromWatchlist(nombreAdmin, n):
    cursor.execute(f"SELECT ID, EmployeeName, EmployeeID, Date, Time, ExpectedCheckIn, EstimatedCheckOut, Temperature, InOut FROM WatchlistIO WHERE AdminName='{nombreAdmin}' ORDER BY id DESC")
    return cursor.fetchmany(n)

def getEmployeesInWatchListFrom(nombreAdmin):
    cursor.execute(f"SELECT EmployeeID FROM Watchlists WHERE AdminName='{nombreAdmin}'")
    empleados = cursor.fetchall()
    r = []
    for empleado in empleados:
        r.append(getEmployeeData(empleado[0])[0])
    return r

def getEmployeesIDInWatchList():
    cursor.execute(f"SELECT EmployeeID FROM Watchlists")
    return cursor.fetchall()

def getAdminNameFromWatchlist(employeeId):
    cursor.execute(f'''SELECT AdminName FROM Watchlists WHERE EmployeeID="{employeeId}"''')
    try:
        return cursor.fetchone()[0]
    except TypeError:
        return None

def getAdminChanges(n):
    cursor.execute("SELECT * FROM AdminChanges ORDER BY ID DESC")
    return cursor.fetchmany(n)


def getAllCabinas():
    cursor.execute("SELECT DISTINCT(MAC) FROM estadosCabinas")
    return cursor.fetchall()

def getEstadoCabina(mac):
    cursor.execute(f'''SELECT * FROM estadosCabinas WHERE MAC="{mac}" ORDER BY Date DESC''')
    return cursor.fetchmany(1)
    
def getAllEstadosCabinas():
    macs = getAllCabinas()	
    r = list()
    for mac in macs:
        r.append(getEstadoCabina(mac[0])[0])
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

def getEmployeeId(name, surname):
    cursor.execute(f'''SELECT ID FROM Employees WHERE Name="{name}" AND Surname="{surname}"''')
    return cursor.fetchone()[0]


def addEmployeeToWatchlist(adminName, employeeId):
    cursor.execute(f'''INSERT INTO Watchlists (AdminName, EmployeeID) VALUES ('{adminName}', '{employeeId}')''')
    conn.commit()

def removeEmployeeFromWatchlist(adminName, employeeId):
    cursor.execute(f'''DELETE FROM Watchlists WHERE AdminName="{adminName}" AND EmployeeID="{employeeId}"''')
    conn.commit()


#################################################################################

def getLastCabinasID():
    cursor.execute("SELECT DISTINCT(id) FROM estadosCabinas ORDER BY id ASC")
    return cursor.fetchone()[0] if cursor.fetchone() is not None else None

def getCabinaID(mac):
    cursor.execute(f'''SELECT id FROM estadosCabinas WHERE MAC="{mac}" ORDER BY id DESC''')
    return cursor.fetchone()

def logEstadoCabina(mac, estado):
    id = getCabinaID(mac)
    if id is not None:
        cursor.execute(f'''INSERT INTO EstadosCabinas VALUES ("{mac}", "{getTime()}", "{getDay()}", "{estado}", {id})''')
        conn.commit()    
    else: 
        cursor.execute(f'''INSERT INTO EstadosCabinas VALUES ("{mac}", "{getTime()}", "{getDay()}", "{estado}", {getLastCabinasID()+1})''')
        conn.commit()  


def logEmployeeIO(employeeID, expectedCheckIn, expectedCheckOut, temperature, inOut):
    first, last = getEmployeeName(employeeID)
    cursor.execute(f'''INSERT INTO EmployeeIO(EmployeeName, EmployeeID, Date, Time, ExpectedCheckIn, EstimatedCheckOut, Temperature, InOut) 
                                       VALUES ("{first + " " + last}",{employeeID},"{getDay()}","{getTime()}","{expectedCheckIn}","{expectedCheckOut}",{temperature},"{inOut}")''')
    conn.commit()
    ids = getEmployeesIDInWatchList()
    for id in ids:
        if id[0]==employeeID:
            cursor.execute(f'''INSERT INTO WatchlistIO (EmployeeName, EmployeeID, Date, Time, ExpectedCheckIn, EstimatedCheckOut, Temperature, InOut, AdminName) 
                                                VALUES ("{first + " " + last}",{employeeID},"{getDay()}","{getTime()}",
                                                "{expectedCheckIn}","{expectedCheckOut}",{temperature},"{inOut}","{getAdminNameFromWatchlist(employeeID)}")''')
            conn.commit()
            break
    

