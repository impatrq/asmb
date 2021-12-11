from MainClass import ASMB
from time import sleep

asmb = ASMB()
mlx = asmb.Temperatura()

e, temp = mlx.readTemp()

print(f"Estado: {e}")
print(f"Temperatura: {temp}")