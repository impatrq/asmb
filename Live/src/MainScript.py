from MainClass import ASMB
from threading import Thread
from Libs.SQLFunctions import logEmployee, logSensors
from time import sleep


# Creo una instancia de la clase ASMB
asmb = ASMB()

############################################################################################################

# Creo el objeto del sensor de temperatura
sensorTemperatura = asmb.Temperatura()

############################################################################################################

# Creo el bojeto del lecto de tarjetas
lectorTarjetas = asmb.LectorDeTarjetas(bus=1, device=0)

############################################################################################################

# Creo los pines necesarios para el sistema de entrada y salida
pinProximidadEntrada = asmb.Pin(24, 'input')
pinProximidadSalida = asmb.Pin(23, 'input')
pinPanelOcupado = asmb.Pin(15, 'output')

# Creo el objeto de los sensores de entrada y salida
io = asmb.IO(pinProximidadEntrada, pinProximidadSalida, pinPanelOcupado)

############################################################################################################

# Creo el objeto de la detección facial
faceDetection = asmb.FaceDetection()

############################################################################################################

# Creo los pines necesarios para el panel de estado
testPin = asmb.Pin(17, 'input')
sh_cp = asmb.Pin(22, 'output')
ds = asmb.Pin(27, 'output')
st_cp = asmb.Pin(4, 'output')
pinHallEntrada = asmb.Pin(7, 'input')
pinHallAlcohol = asmb.Pin(8, 'input')
pinHallSalida = asmb.Pin(25, 'input')

# Creo el objeto del panel de estado
panelEstado = asmb.PanelEstado(testPin, sh_cp, ds, st_cp, pinHallEntrada, pinHallAlcohol, pinHallSalida)

############################################################################################################

# Creo el pin necesario para el cartel de funcionamiento
pinCartelFuncionamiento = asmb.Pin(14, 'output')

# Creo el objeto del cartel de funcionamiento
cartelFuncionamineto = asmb.CartelFuncionamiento(pinCartelFuncionamiento)

############################################################################################################

# Creo los pines necesarios para el dispenser de alcohol en gel
pinMotorAlcoholGel = asmb.Pin(10, 'output')
pinProximidadAlcohol = asmb.Pin(18, 'input')

# Creo el objeto del dispenser de alcohol en gel
dispenserAlcohol = asmb.DispenserAlcohol(pinProximidadAlcohol, pinMotorAlcoholGel, .3)

############################################################################################################

# Creo el pin del motor para el desinfectante
pinMotorDesinfectante = asmb.Pin(11, 'output')

############################################################################################################



estados = panelEstado.getSensorStatus()
panelEstado.logSensors(estados)

if any(estados):
    cartelFuncionamineto.setState(0)

else:    
    def iniciarAlcoholGel():
        thread = Thread(target=dispenserAlcohol.verMano)
        thread.start()

    def main():

        while 1:
            # Prendo el cartel de funcionamiento
            cartelFuncionamineto.setState(1)


            # Espero a la temperatura del usuario
            e, temperatura = sensorTemperatura.readTemp()
            

            # Detecto la entrada de un usuario
            io.checkEntry()


            # Apago el cartel de funcionamiento (Para indicar que está ocupada)
            cartelFuncionamineto.setState(0)


            # Leo la tarjeta de identificación
            _, employeeID = lectorTarjetas.readCard()


            # Registro la entrada de alguien en la base de datos
            logEmployee(employeeID, temperatura)


            # Si la temperatura excede el limite
            if not e:
                cartelFuncionamineto.setState(0)
                sleep(10)
                continue


            # Detecto la cara/barbijo
            faceDetection.detect()


            # Pulverizo el desinfectante
            pinMotorDesinfectante.setState(1)
            sleep(.5)
            pinMotorDesinfectante.setState(0)


            # Detecto la salida de un usuario
            io.checkExit()

    if __name__ == '__main__':
        iniciarAlcoholGel()
        main()