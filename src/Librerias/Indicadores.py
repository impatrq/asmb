import RPi.GPIO as GPIO
from time import sleep

PINESCARTEL = [0,1] # [Desocupado(x), Ocupado(y)]; A definir
for p in PINESCARTEL:
    GPIO.setup(p, GPIO.OUT)

def desocupar():
    GPIO.output(PINESCARTEL[0], 0)
    GPIO.output(PINESCARTEL[1], 1)
    return False       # A definir

def ocupar():
    GPIO.output(PINESCARTEL[1], 1)
    GPIO.output(PINESCARTEL[1], 0)
    return True        # A definir


# USO:
# estado = ocupar()
# estado = desocupar()
# 
# El primero se debe ejecutar cuando alguien entra a la cabina, la variable asociada 
# se usa para verificar el estado de la cabina en todo momento.
# El segundo se usa cuando se desocupa la cabina.