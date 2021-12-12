from MainClass import ASMB
import threading

asmb = ASMB()
pinSensorProx = asmb.Pin(1,  'input')  
pinMotor = asmb.Pin(2, 'output')
dispenserAlcohol = asmb.DispenseAlcohol(pinSensorProx, pinSensorProx, .25)

thread = threading.Thread(target=dispenserAlcohol.verMano)
thread.start()