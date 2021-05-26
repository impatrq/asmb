import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

p = GPIO.PWM(8, 50)  
p.start(0)

while 1:
    for dc in range(0, 101, 5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.5)
    for dc in range(100, -1, -5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.5)

pwm = GPIO.PWM(18, 1000)
pwm.start(50)

p.stop()
GPIO.cleanup()