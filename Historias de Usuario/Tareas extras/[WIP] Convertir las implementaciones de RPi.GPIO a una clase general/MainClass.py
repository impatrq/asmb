import adafruit_mlx90614 as mlx90614
import RPi.GPIO as GPIO
import busio as io
import board
from time import sleep
from SQLFunctions import logSensors

enUso:bool = False
enFuncionamiento:bool = True

#GPIO.setmode(GPIO.BOARD)

def setUso(v:bool):
    global enUso
    enUso = v
def setFuncionamiento(v:bool):
    global enFuncionamiento
    enFuncionamiento = v
def getFuncionamiento():
    return enFuncionamiento
def getUso():
    return enUso

class ASMB:
    def __init__(self, ) -> None:
        '''Clase general de la cabina'''
        pass
    class Pin:
        def __init__(self, pin, mode=GPIO.OUT, state=0) -> None:
            '''Constructor para los pines'''
            self.__pin = pin
            self.__modes = {'output':GPIO.OUT, 'input':GPIO.IN}
            self.__mode = mode
            self.__state = state 
            GPIO.setup(self.__pin, self.__modes[mode])
      
        def toggleState(self) -> None:
            '''Alterna el estado del pin'''
            if self.__mode == 'output':
                GPIO.output(self.__pin, not self.__state)
                self.__state = not self.__state
            else:
                raise Exception(f'Modo del pin {self.__pin}:{self.__mode}')

        def setState(self, state) -> None:
            '''Cambia el estado del pin'''
            if self.__state != state:
                if self.__mode == 'output':
                    GPIO.output(self.__pin, state)
                    self.__state = state
                else:
                    raise Exception(f'Modo del pin {self.__pin}:{self.__mode}')

        def getState(self) -> bool:
            '''Devuelve el estado del pin'''
            if self.__mode == 'input':
                state = GPIO.input(self.__pin)
                return state
            raise Exception(f'Modo del pin {self.__pin}:{self.__mode}')

        def push(self, state):
            if self.__mode == 'output':
                    GPIO.output(self.__pin, state)
                    GPIO.output(self.__pin, not state)
            else:
                raise Exception(f'Modo del pin {self.__pin}:{self.__mode}')

    class IO:       # Revisar nombre
        def __init__(self, entrada, salida, led) -> None:
            '''Constructor para los sensores de entrada y salida'''
            self.__entrada:ASMB.Pin = entrada
            self.__salida:ASMB.Pin = salida
            self.__led:ASMB.Pin = led

        def checkEntry(self,) -> None:
            ''''Verifica la entrada de un usuario'''
            while 1:
                e = self.__entrada.getState()
                if e:
                    setUso(True)
                    break
                self.__led.setState(0)
                sleep(0.1)

        def checkExit(self,) -> None:
            '''Verifica la salida del usuario'''
            while 1:
                e = self.__salida.getState()
                if e:
                    setUso(False)
                    break
                self.__led.setState(1)
                sleep(0.1)

    class CartelFuncionamiento:     # Revisar nombre
        def __init__(self, pin) -> None:
            '''Constructor para el cartel de funcionamiento'''
            self.__pin:ASMB.Pin = pin
        def setState(self, state) -> None:
            '''Cambia el estado del cartel de funcionamiento'''
            print(f'getFuncionamiento()={getFuncionamiento()}')
            if getFuncionamiento() != state:
                self.__pin.setState(state)
                setFuncionamiento(bool(state))

    class Temperatura:      # Revisar nombre
        def __init__(self, freq=100e3) -> None:
            '''Constructor para el mlx90614'''
            self.__i2c = io.I2C(board.SCL, board.SDA, frequency=freq)
            self.__mlx = mlx90614.MLX90614(self.__i2c)
        def readTemp(self,) -> list:
            '''Lee la temperatura en un intervalo de 25s maximos, de ser valida devuelve (True, temp) y en caso contrario (False, temp)'''
            mlx = self.__mlx
            while 1:
                temp = mlx.object_temperature
                if temp>=28:
                    break
            for _ in range(101):
                temp = mlx.object_temperature
                if 36<=temp<=37:
                    return True, temp 
                sleep(0.25)
            return False, temp
    class PanelEstado:
        def __init__(self, testPin, sh_cp, ds, st_cp, pinEntrada, pinAlcohol, pinSalida) -> None:
            self.testPin:ASMB.Pin = testPin
            self.sh_cp:ASMB.Pin = sh_cp
            self.ds:ASMB.Pin = ds
            self.st_cp:ASMB.Pin = st_cp

            self.pinEntrada:ASMB.Pin = pinEntrada
            self.pinAlcohol:ASMB.Pin = pinAlcohol
            self.pinSalida:ASMB.Pin = pinSalida
            
        def logSensors(self, states:tuple) -> None:
            registerRefreshPin = self.sh_cp
            serialOut = self.ds
            outputRefreshPin = self.st_cp
            for e in states:    
                serialOut.setState(e)
                registerRefreshPin.push(1)
            outputRefreshPin.push(1)
            logSensors(states)
        def getSensorStatus(self,) -> list:
            estados = [False]*8
            '''[temperatura, tarjetas, entrada, alcohol, salida, ]'''
            try:
                i2c = io.I2C(board.SCL, board.SDA, frequency=100e3)
                mlx = mlx90614.MLX90614(self.__i2c)
            except:
                estados[0] = True

            try:
                # Poner lo mismo q arriba pero para el lector de tarjetas
                pass
            except:
                estados[1] = True
            
