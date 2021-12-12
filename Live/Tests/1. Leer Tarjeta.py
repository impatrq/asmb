from time import sleep
import RPi.GPIO as GPIO
from Libs.simpleRC522 import SimpleMFRC522

reader = SimpleMFRC522(busa=0, devicea=0)

try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print(f"text= {text}")
        print(f"{id:=}")
        sleep(.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
