import adafruit_mlx90614 as mlx90614
import RPi.GPIO as GPIO    
import busio as io
import board
from time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


class ASMB:
    def __init__(self, ) -> None:
        '''Clase general de la cabina'''
        self.enUso:bool = False
        self.enFuncionamiento:bool = True
    class Pin:
        def __init__(self, pin, mode=None, state=0) -> None:
            '''Constructor para los pines'''
            self.__pin = pin
            self.__mode = mode or 'output'
            self.__states = {'output':GPIO.OUT, 'input':GPIO.IN}
            self.__state = state or 0
            GPIO.setup(self.__pin, self.__states[mode])

        def toggleState(self) -> None:
            '''Alterna el estado del pin'''
            if self.__mode == 'output':
                GPIO.output(self.__pin, not self.__state)
                self.__state = not self.__state
            else:
                raise f'Modo del pin {self.__pin}:{self.__mode}'

        def setState(self, state) -> None:
            '''Cambia el estado del pin'''
            if self.__state != state:
                if self.__mode == 'output':
                    GPIO.output(self.__pin, state)
                    self.__state = state
                else:
                    raise f'Modo del pin {self.__pin}:{self.__mode}'

        def getState(self) -> bool:
            '''Devuelve el estado del pin'''
            if self.__mode == 'input':
                state = GPIO.input(self.__pin)
                self.__state = not self.__state
                return state
            raise f'Modo del pin {self.__pin}:{self.__mode}'

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
                    ASMB.enUso = True
                    break
                self.__led.setState(0)
                sleep(0.1)

        def checkExit(self,) -> None:
            '''Verifica la salida del usuario'''
            while 1:
                e = self.__salida.getState()
                if e:
                    ASMB.enUso = False
                    break
                self.__led.setState(1)
                sleep(0.1)
    
    class CartelFuncionamiento:     # Revisar nombre
        def __init__(self, pin) -> None:
            '''Constructor para el cartel de funcionamiento'''
            self.__pin:ASMB.Pin = pin
        def setState(self, state) -> None:
            '''Cambia el estado del cartel de funcionamiento'''
            state = bool(state)
            if ASMB.enFuncionamiento != state:
                self.__pin.setState(state)
                ASMB.enFuncionamiento = state

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
                if temp>=40:
                    break
            for _ in range(101):
                temp = mlx.object_temperature
                if 36<=temp<=37:
                    return True, temp 
                sleep(0.25)
            return False, temp

          