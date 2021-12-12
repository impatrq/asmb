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

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

F1 = 100    # Frecuencia buena
F2 = 50     # Frecuencia mala

IN = 29
OUTO = 31
OUTD = 32
BZ = 33

GPIO.setup(IN, GPIO.IN)
GPIO.setup(OUTO, GPIO.OUT)
GPIO.setup(OUTD, GPIO.OUT)
GPIO.setup(BZ,GPIO.OUT)

while 1:
    if GPIO.input(IN) == 1:
        GPIO.output(OUTD, 1)
        GPIO.output(OUTO, 0)
        buzz(BZ,F1)
    else:
        GPIO.output(OUTD, 0)
        GPIO.output(OUTO, 1)
        buzz(BZ,F2)
	


