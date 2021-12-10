import RPi.GPIO as GPIO
from time import sleep

def buzz(pin, f):   
    buzzing = False
    GPIO.output(pin, buzzing)
    time = (f*2)**-1
    sleep(time)
        
    buzzing = True
    GPIO.output(pin, buzzing)
    sleep(time)

def sonidoBueno():
    BUZZER = 10 # A definir
    f1 = 100    # A definir
    f2 = 90     # A definir
    buzz(BUZZER,f1)
    sleep(0)    # Espera opcional
    buzz(BUZZER,f2)
    

def sonidoMalo():
    BUZZER = 10 # A definir
    f1 = 50     # A definir
    f2 = 5      # A definir
    buzz(BUZZER,f1)
    sleep(0)    # Espera opcional
    buzz(BUZZER,f2)


    
    