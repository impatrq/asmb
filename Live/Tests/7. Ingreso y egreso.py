from MainClass import ASMB

asmb = ASMB()

pinEntrada = asmb.Pin(3,'input')
pinSalida = asmb.Pin(4,'input')
pinLED = asmb.Pin(5, 'output')

IO = asmb.IO(pinEntrada, pinSalida, pinLED)

IO.checkEntry()
print("Persona dentro de la cabina")
IO.checkExit()
print("Persona fera de la cabina")