import sqlite3
from TimeFunctions import getWeekDay, getDay, getTime

connection = sqlite3.connect('Recursos/Cabina.db')
cursor = connection.cursor()

def getScheduleByName(nombre:str):
    '''Devuelve el horario del empleado ingresado'''
    if type(id) != str:
        raise TypeError("La funcion toma como parametro un string")

    cmd = f"""SELECT Horarios.{getWeekDay()}
            FROM Empleados LEFT OUTER JOIN Horarios
            ON Empleados.workschedule == Horarios.workschedule
            WHERE Empleados.name == '{nombre}'"""
    cursor.execute(cmd)
    horario = cursor.fetchone()[0]

    return horario

def getSchedule(id:int):
    '''Devuelve el horario del la id ingresada'''
    if type(id) != int:
        raise TypeError("La funcion toma como parametro un entero positivo")

    cmd = f"""SELECT Horarios.{getWeekDay()}
            FROM Empleados LEFT OUTER JOIN Horarios
            ON Empleados.workschedule == Horarios.workschedule
            WHERE Empleados.id == '{id}'"""
    cursor.execute(cmd)
    horario = cursor.fetchone()[0]

    return horario


def logSensors(sensorStatus:tuple):
    '''Guarda el estado de los sensores actuales'''
    if type(sensorStatus) != tuple or type(sensorStatus) != list:
        raise TypeError("El parametro ingresado debe ser una lista/tupla")
    if len(sensorStatus)!=8:
        raise TypeError("El array ingresado debe contener 8 valores")

    cmd = f"""INSERT INTO Sensores (date, time, estados) VALUES ('{getDay()}', '{getTime()}', '{sensorStatus}')"""
    cursor.execute(cmd)
    connection.commit()


def logEmployee(empleadoid:int, temp:float):
    '''Guarda el horario de ingreso del empleado, a la par de su temperatura'''
    if type(empleadoid) != int:
        raise TypeError("La funcion toma como primer parametro un entero positivo")
    if type(temp) != float:
        raise TypeError("La funcion toma como segundo parametro un decimal positivo")

    cmd = f"""INSERT INTO EntradasEmpleados (employeeid, day, checkin, pretendedcheckin, temperature) 
            VALUES ('{empleadoid}','{getDay()}','{getTime()}','{getSchedule(empleadoid)}','{temp}')"""
    cursor.execute(cmd)
    connection.commit()

def logClient(temp:float):
    ''''Guarda el horario de ingreso de un cliente, con us temperatura'''
    if type(temp) != float:
        raise TypeError("La funcion toma como parametro un decimal positivo")

    cmd = f"""INSERT INTO EntradasClientes (day, time, temperature) VALUES ('{getDay()}','{getTime()}','{temp}')"""
    cursor.execute(cmd)
    connection.commit()
