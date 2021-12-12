import sqlite3
from TimeFunctions import getWeekDay, getDay, getTime

connection = sqlite3.connect('Cabina.db')
cursor = connection.cursor()

def getScheduleByName(nombre):
    if type(id) != str:
        raise TypeError("La funcion toma como parametro un string")

    cmd = f"""SELECT Horarios.{getWeekDay()}
            FROM Empleados LEFT OUTER JOIN Horarios
            ON Empleados.workschedule == Horarios.workschedule
            WHERE Empleados.name == '{nombre}'"""
    cursor.execute(cmd)
    horario = cursor.fetchone()[0]

    #print(f"\n\t Bienvenido {nombre} tu horario hoy es de: {horario}")
    return horario

def getSchedule(id):
    if type(id) != int:
        raise TypeError("La funcion toma como parametro un entero positivo")

    cmd = f"""SELECT Horarios.{getWeekDay()}
            FROM Empleados LEFT OUTER JOIN Horarios
            ON Empleados.workschedule == Horarios.workschedule
            WHERE Empleados.id == '{id}'"""
    cursor.execute(cmd)
    horario = cursor.fetchone()[0]

    #print(f"\n\t Bienvenido empleado {id} tu horario hoy es de: {horario}")
    return horario


def logSensors(sensorStatus):
    if not len(sensorStatus)==8:
        raise TypeError("La lista ingresada debe contener 8 valores")

    cmd = f"""INSERT INTO Sensores (date, time, estados) VALUES ('{getDay()}', '{getTime()}', '{sensorStatus}')"""
    cursor.execute(cmd)
    connection.commit()


def logEmployee(empleadoid, temp):
    if type(id) != str:
        raise TypeError("La funcion toma como primer parametro un string ")
    if type(temp) != int:
        raise TypeError("La funcion toma como segundo parametro un entero positivo")

    cmd = f"""INSERT INTO EntradasEmpleados (empleadoid, day, checkin, pretendedcheckin, temperature) 
            VALUES ('{empleadoid}','{getDay()}','{getTime()}','{getSchedule(empleadoid)}','{temp}')"""
    cursor.execute(cmd)
    connection.commit()

def logClient(temp):
    if type(temp) != int:
        raise TypeError("La funcion toma como parametro un entero positivo")

    cmd = f"""INSERT INTO EntradasClientes (day, time, temperature) VALUES ('{getDay()}','{getTime()}','{temp}')"""
    cursor.execute(cmd)
    connection.commit()

