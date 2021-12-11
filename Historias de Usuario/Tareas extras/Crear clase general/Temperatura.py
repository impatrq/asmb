#!/u#!/usr/bin/python
# -*- coding:windows-1252 -*-

from MainClass import ASMB
import RPi.GPIO as GPIO

asmb = ASMB()
temp = asmb.Temperatura()
val, lectura = temp.readTemp()

print(val)
print(lectura)
