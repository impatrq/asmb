import sqlite3
from TimeFunctions import getWeekDay, getDay, getTime

connection = sqlite3.connect('Cabina.db')
cursor = connection.cursor()

def getScheduleByName(nombre):

    cmd = f"""SELECT Horarios.{getWeekDay()}
            FROM Empleados LEFT OUTER JOIN Horarios
            ON Empleados.workschedule == Horarios.workschedule
            WHERE Empleados.name == '{nombre}'"""
    cursor.execute(cmd)
    horario = cursor.fetchone()[0]

    #print(f"\n\t Bienvenido {nombre} tu horario hoy es de: {horario}")
    return horario

def getSchedule(id):

    cmd = f"""SELECT Horarios.{getWeekDay()}
            FROM Empleados LEFT OUTER JOIN Horarios
            ON Empleados.workschedule == Horarios.workschedule
            WHERE Empleados.id == '{id}'"""
    cursor.execute(cmd)
    horario = cursor.fetchone()[0]

    #print(f"\n\t Bienvenido empleado {id} tu horario hoy es de: {horario}")
    return horario

def logCheckIn(employeeid, temperatura):
    cmd = f"""INSERT INTO Entradas (employeeid, day,checkin, pretendedcheckin, temperature) 
            VALUES ('{employeeid}','{getDay()}','{getTime()}','{getSchedule(employeeid)}','{temperatura}')"""
    cursor.execute(cmd)
    connection.commit()

logCheckIn(3,20)