from Libs.simpleRC522 import SimpleMFRC522
import RPi.GPIO as GPIO
reader = SimpleMFRC522()

try:        
    text = input('New data:')
    print("Now place your tag to write")
    reader.write(text)
    print("Written")

except KeyboardInterrupt:
    GPIO.cleanup()
    raise