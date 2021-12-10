import sqlite3
from TimeFunctions import getWeekDay, getDay, getTime

connection = sqlite3.connect('Cabina.db')
cursor = connection.cursor()

temperatura = input("\n\t Ingrese la temperatura")

cmd = f"""INSERT INTO EntradasClientes (day, time, temperature) VALUES ('{getDay()}','{getTime()}','{temperatura}')"""
cursor.execute(cmd)
connection.commit()