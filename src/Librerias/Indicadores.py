import RPi.GPIO as GPIO
from time import sleep

PINCARTEL = 0   # Pin del indicador de funcionamiento
GPIO.setup(PINCARTEL, GPIO.OUT)

PINESCARTEL = [0,1] # [Desocupado(x), Ocupado(y)]; A definir
for p in PINESCARTEL:
    GPIO.setup(p, GPIO.OUT)



def cartelFuncionando() -> None:      # Una funcion con la unica funcion, valga la redundancia, de apagar el cartel de no funcionando
    '''Hace que el indicador de funcionamiento indique que la cabina está funcionando'''
    GPIO.output(PINCARTEL, GPIO.LOW)

def cartelNoFuncionando() -> None:    # Lo mismo q la de arriba solo que al revés
    '''Hace que el indicador de funcionamiento indique que la cabina no está funcionando'''
    GPIO.output(PINCARTEL, GPIO.HIGH)

def desocupar():
    '''Hace que el indicador de ocupado de la cabina indique que la caibna ya no está ocupada'''
    GPIO.output(PINESCARTEL[0], 0)
    GPIO.output(PINESCARTEL[1], 1)
    return False       # A definir

def ocupar():
    '''Hace que el indicador de ocupado de la cabina indique que la caibna está ocupada'''
    GPIO.output(PINESCARTEL[1], 1)
    GPIO.output(PINESCARTEL[1], 0)
    return True        # A definir