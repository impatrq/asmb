from MainClass import ASMB

asmb = ASMB()

pinCartel = asmb.Pin(0, 'output')
cartelFuncionamiento = asmb.CartelFuncionamiento(pinCartel)

testPin = asmb.Pin(1, 'input')

sh_cp = asmb.Pin(2, 'output') 
ds = asmb.Pin(3, 'output')
st_cp = asmb.Pin(4 , 'output')

pinHallEntrada = asmb.Pin(5, 'input')
pinHallAlcohol = asmb.Pin(6, 'input')
pinHallSalida = asmb.Pin(7, 'input')

panel = asmb.PanelEstado(testPin, sh_cp, ds, st_cp, pinHallEntrada, pinHallAlcohol, pinHallSalida)

e = panel.getSensorStatus()
if any(e):
    cartelFuncionamiento.setState(1)
else:
    cartelFuncionamiento.setState(0)

panel.logSensors(e)
