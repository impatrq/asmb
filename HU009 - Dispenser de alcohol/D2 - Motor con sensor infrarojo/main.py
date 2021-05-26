from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.IN)

lastState = 0

while 1:
    currentState = GPIO.input(10)

    if currentState!=lastState:
        if currentState:
            GPIO.output(8, GPIO.HIGH)
            sleep(2)
            GPIO.output(8, GPIO.LOW)
        lastState = currentState

    sleep(0.1)
