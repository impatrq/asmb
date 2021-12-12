from Libs.SQLFunctions import logClient
from MainClass import ASMB

asmb = ASMB()
mlx = asmb.Temperatura()

_, temp = mlx.readTemp()

logClient(temp)