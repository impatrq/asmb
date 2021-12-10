import RPi.GPIO as GPIO    
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

BUZZER = 29
GPIO.setup(BUZZER, GPIO.OUT)

def buzz(pin, f):   
    buzzing = False
    GPIO.output(pin, buzzing)
    time = (f*2)**-1
    sleep(time)
    
    buzzing = True
    GPIO.output(pin, buzzing)
    sleep(time)

while 1:
    buzz(BUZZER,0.166)
    