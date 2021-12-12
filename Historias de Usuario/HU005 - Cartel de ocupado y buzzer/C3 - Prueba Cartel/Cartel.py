import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

IN = 29
OUTO = 31
OUTD = 32

GPIO.setup(IN, GPIO.IN)
GPIO.setup(OUTO, GPIO.OUT)
GPIO.setup(OUTD, GPIO.OUT)#, pull_up_down=GPIO.PD_DW)


while 1:
    GPIO.output(OUTD, GPIO.input(IN))
    GPIO.output(OUTO, not GPIO.input(IN))
    sleep(0.1)