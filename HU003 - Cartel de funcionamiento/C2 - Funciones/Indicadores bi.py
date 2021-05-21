import RPi.GPIO as GPIO
from time import sleep

PINCARTEL = 0   # Pin del indicador de funcionamiento

GPIO.setup(PINCARTEL, GPIO.OUT)

def funcionando():      # Una funcion con la unica funcion, valga la redundancia, de apagar el cartel de no funcionando
    GPIO.output(PINCARTEL, GPIO.LOW)

def noFuncionando():    # Lo mismo q la de arriba solo que al revez
    GPIO.output(PINCARTEL, GPIO.HIGH)
