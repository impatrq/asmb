import socket
import threading
import json
from SQLFunctions import logEstadoCabina, logEmployeeIO

HEADER = 16
IP = "192.168.0.132"
PORT = 8080
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
ADDR = (IP, PORT)


def handle_client(conn, addr):

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            msg = json.loads(msg)
            print(msg)
            if msg['Type'] == 'In' or msg['Type'] == 'Out':
                data = msg['Data']
                logEmployeeIO(data['EmployeeID'], data['ExpectedCheckIn'], data['ExpectedCheckOut'], data['Temperature'], msg['Type'])
            elif msg['Type'] == 'Sensors':
                data = msg['Data']
                logEstadoCabina(data['MAC'], data['Estates'])
    conn.close()

def server_init():
    print("[STARTING SERVER]")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    print("[SERVER STARTED]")
    server.listen(10)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
    

