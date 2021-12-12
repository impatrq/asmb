print(1)
from Libs.SQLFunctions import logEmployee
print(2)
from MainClass import ASMB
print(3)
asmb = ASMB()
print(4)
lectorTarjetas = asmb.LectorDeTarjetas()
print(5)
_, id = lectorTarjetas.readCard()
print(6)
logEmployee(id, 36)