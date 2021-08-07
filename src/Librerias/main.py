from FaceDetection import detectClosedEyesAndMouth
from SQLFunctions import logClient
from SQLFunctions import logEmployee
from SQLFunctions import logSensors
from Indicadores import cartelFuncionando
from Indicadores import cartelNoFuncionando
from Indicadores import ocupar
from Indicadores import desocupar
from Sonidos import sonidoBueno
from Sonidos import sonidoMalo
from time import sleep

# GPIO libres (2-27)
# 5, 6, 6, 8, 9, 10, 11, 13, 14, 15, 25, 26

pinProximidadAlcohol = 18
pinProximidadEntrada = 23
pinProximidadSalida = 24
pinBuzzer = 12
pinTesteoPanelEstado = 4
pinesLectorTarjetas = {
    'Sda': 19,
    'Sck': 16,
    'Miso': 20,
    'Irq': 21 
}
pinesSensorTemperatura = {
    'Sda': 2,
    'Sck': 3 
}
pinesPanelEstado = {
    'SH_CP': 17,
    'DS': 22  ,
    'ST_CP': 27 
}

def leerTemperatura():
    return 36.5
def leerTarjeta():
    return 1
def leerEntrada():
    return True
def leerPosicionAlfombra():
    return True
def titilarLed():
    print('Led titilando')
    pass
def getEstadoSensores():
    pass


def main():
    while True:
        temperatura = leerTemperatura()
        if 36 <= temperatura <= 37:
            sonidoBueno()
            break 
        else:
            sonidoMalo()
            # Ni idea, falta decidir q haria si se pasa de temperatura

    while True: # Cuidado que acá el if se evalua como true si id tiene literalmente cualquier cosa
        id = leerTarjeta()
        if id:
            logEmployee(id, temperatura)
            break

    estadoCabina = ocupar()

    while True:
        if leerEntrada():
            sonidoBueno()
            break
        else:
            continue

    while True:
        if leerPosicionAlfombra():
            sonidoBueno()
            titilarLed()
            break
        else:
            continue
    
    detectClosedEyesAndMouth() # Falta implementar el boton para pasar este proceso
    sonidoBueno()
    

    

    








    estadoCabina = desocupar()



def otro():
    estadoSensores = getEstadoSensores()
    logSensors(estadoSensores)
    if any(estadoSensores):    
        # Esto se ejecuta si hay algun sensor fallando
        cartelNoFuncionando()
    else:
        cartelFuncionando()



if __name__=='__main__':
    main()
