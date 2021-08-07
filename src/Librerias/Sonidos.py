import RPi.GPIO as GPIO
from time import sleep

BUZZER = 10
GPIO.setup(BUZZER, GPIO.OUT)

def buzz(pin, f):   
    buzzing = False
    GPIO.output(pin, buzzing)
    time = (f*2)**-1
    sleep(time)
    buzzing = True
    GPIO.output(pin, buzzing)
    sleep(time)

def sonidoBueno():
    f1 = 100    # A definir
    f2 = 90     # A definir
    buzz(BUZZER,f1)
    sleep(0)    # Espera opcional
    buzz(BUZZER,f2)
    

def sonidoMalo():
    f1 = 50     # A definir
    f2 = 5      # A definir
    buzz(BUZZER,f1)
    sleep(0)    # Espera opcional
    buzz(BUZZER,f2)

# Hay que rehacer esta libreria, ya que es conveniente usar un
# parlante antes que un buzzer, ademas de que el codigo se traba cuando se ejecuta el buzz   
# No lo voy a documentar, ya que esto se va a tener que cambiar.