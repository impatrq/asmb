from MainClass import ASMB
from time import sleep 

asmb = ASMB()
ledCartel = asmb.Pin(37, 'output', 0) 
cartel = asmb.CartelFuncionamiento(ledCartel)

while 1:
    cartel.setState(1)
    sleep(0.5)
    cartel.setState(0)
    sleep(0.5)
