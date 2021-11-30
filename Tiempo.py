import RPi.GPIO as GPIO
from time import sleep, time
import datetime
a=0
while(a<20000000):
    a=a+1
    if(a==10000):
        print("10000=",datetime.datetime.now())
    if(a==10000000):
        print("10000000=",datetime.datetime.now())
    if(a==1000):
        print(datetime.datetime.now())
    if(a==40000):
        print("10000=",datetime.datetime.now())
    if(a==20000):
        print("10000=",datetime.datetime.now())
    if(a==30000):
        print("10000=",datetime.datetime.now())
        
