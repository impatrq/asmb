import sqlite3
from time import sleep
from TimeFunctions import getDay, getTime
from Encrypter import Encrypter
from random import randint

conn = sqlite3.connect('EmployeeLogs.db', check_same_thread=False)
cursor = conn.cursor()


cmd = '''CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT,
    email TEXT,
    phone TEXT,
    country TEXT,
    last_login_day DATE,
    last_login_time TIME
)'''
cursor.execute(cmd)


cmd = '''CREATE TABLE IF NOT EXISTS encrypterData (
    times_encrypted INTEGER,
    encryter_key TEXT
)'''
cursor.execute(cmd)	


def getEncrypterData():
    cmd = '''SELECT * FROM encrypterData'''
    cursor.execute(cmd)
    data = cursor.fetchone()
    return (data[1], data[0]) if data is not None else (None, None)

def setEncrypterData(key, times):
    cmd = f'''INSERT INTO encrypterData (times_encrypted, encryter_key) VALUES ({times}, '{key}')'''
    cursor.execute(cmd)
    conn.commit()



key, times = getEncrypterData() 
encrypter = Encrypter(key)



if not all(getEncrypterData()):
    key = encrypter.regenerateKey()
    times = randint(20, 100)
    setEncrypterData(key, times)



def createAdmin(username, password):
    cmd = f'''INSERT INTO AdminAccounts (username, password)
    VALUES ('{username}', '{encrypter.encrypt(password, times)}')'''
    cursor.execute(cmd)
    conn.commit()

def checkAdmin(username):
    cmd = f'''SELECT * FROM AdminAccounts WHERE username = '{username}' '''
    cursor.execute(cmd)
    user = cursor.fetchone()
    return user if user is None else True

def loginAdmin(username, password):
    cmd = f'''SELECT * FROM AdminAccounts WHERE username = '{username}' AND password = '{encrypter.encrypt(password, times)}' '''
    cursor.execute(cmd)
    user = cursor.fetchone()
    print(user)
    return True if user is not None else False