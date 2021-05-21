import sqlite3
import datetime

connection = sqlite3.connect('Cabina.db')
cursor = connection.cursor()

cmd = """CREATE TABLE IF NOT EXISTS Sensores(
         date DATE NOT NULL,
         time TIME NOT NULL,
         estados TEXT NOT NULL
     )"""
cursor.execute(cmd)

def logSensors(sensorStatus):
    assert len(sensorStatus)==8, 'La lista ingresada debe contener 8 valores'

    today = datetime.date.today()
    now = datetime.datetime.now().time()

    cmd = f"""INSERT INTO Sensores (date, time, estados) VALUES ('{today}', '{str(now)[0:8]}', '{sensorStatus}')"""
    cursor.execute(cmd)
    connection.commit()


