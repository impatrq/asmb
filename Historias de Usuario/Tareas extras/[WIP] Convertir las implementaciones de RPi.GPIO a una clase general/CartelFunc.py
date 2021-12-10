#!/u#!/usr/bin/python
# -*- coding:windows-1252 -*-

from MainClass import ASMB
from time import sleep 

#GPIO.setmode(GPIO.BOARD)
#GPIO.setwarning(False)
asmb = ASMB()
ledCartel = asmb.Pin(37, 'output', 0) # Cambiar el n de pin 
cartel = asmb.CartelFuncionamiento(ledCartel)

while 1:
    ledCartel.setState(1)
    sleep(0.5)
    ledCartel.setState(0)
    sleep(0.5)
