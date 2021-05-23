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

def logCheckIn(empleadoid):
    cmd = f"""INSERT INTO Entradas (empleadoid,day,checkin,pretendedcheckin) 
            VALUES ('{empleadoid}','{getDay()}','{getTime()}','{getSchedule(empleadoid)}')"""
    cursor.execute(cmd)
    connection.commit()

def logSensors(sensorStatus):
    assert len(sensorStatus)==8, 'La lista ingresada debe contener 8 valores'

    cmd = f"""INSERT INTO Sensores (date, time, estados) VALUES ('{getDay()}', '{getTime()}', '{sensorStatus}')"""
    cursor.execute(cmd)
    connection.commit()

