from Libs.SQLFunctions import logEmployee
from MainClass import ASMB

asmb = ASMB()
mlx = asmb.Temperatura()
lectorTarjetas = asmb.LectorDeTarjetas()

_, temp = mlx.readTemp()
_, id = lectorTarjetas.readCard()

logEmployee(id, temp)