import socket
import threading 
import json
import getmac

HEADER = 16
IP = socket.gethostbyname(socket.gethostname())
PORT = 8080
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
ADDR = (IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg, sock):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)        
    send_length += b' ' * (HEADER - len(send_length))
    sock.send(send_length)
    sock.send(message)


datos = {
    'Type': 'In',
    'Data': {
        'EmployeeID': 1,
        'ExpectedCheckIn': '21:30:00',
        'ExpectedCheckOut': '22:30:00',
        'Temperature': 37.7
    }  
}    


paquete = {
    'Type': None,
    'Data': {
    }
}

print("Creador de paquetes artificiales para ASMB")

while 1:
    tipoPaquete = input("\nIngrese el tipo de paquete (In/Out/Sensors): ")
    if tipoPaquete in ("In","Out","Sensors"):
        break

paquete['Type'] = tipoPaquete

if tipoPaquete == "Sensors":
    while 1:
        estados = input("\nIngrese los estados de los sensores, separador \ncomo un espacio, siendo 1 o 0: ")
        estados = tuple(int(e) for e in estados.split(' '))
        print(estados)
        if len(estados) == 8: 
            break 
        
    paquete['Data']['MAC'] = getmac.get_mac_address().upper()   
    paquete['Data']['Estates'] = estados

if tipoPaquete == "In" or tipoPaquete == "Out":

    employeeID = int(input("\nIngrese el id del empleado: "))
    expectedCheckIn = input("\nIngrese el horario de entrada esperado: ")
    expectedCheckOut = input("\nIngrese el horario de salida esperado: ")
    temperatura = int(input("\nIngrese la temperatura: "))

    paquete['Type'] = tipoPaquete
    paquete['Data']['EmployeeID'] = employeeID
    paquete['Data']['ExpectedCheckIn'] = expectedCheckIn
    paquete['Data']['ExpectedCheckOut'] = expectedCheckOut
    paquete['Data']['Temperature'] = temperatura



send(json.dumps(paquete), client)