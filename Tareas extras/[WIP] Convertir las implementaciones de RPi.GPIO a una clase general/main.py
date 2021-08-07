import RPi.GPIO as GPIO    
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class ASMB:
    def __init__(self, ) -> None:
        '''Clase general de la cabina'''
        self.enUso:bool = False
        
    class Pin:
        def __init__(self, pin, mode=None, state=0) -> None:
            '''Constructor para los pines'''
            self.__pin = pin
            self.__mode = mode or 'output'
            self.__states = {'output':GPIO.OUT, 'input':GPIO.IN}
            self.__state = state or 0
            GPIO.setup(self.__pin, self.__states[mode])
        def toggleState(self):
            '''Alterna el estado del pin'''
            if self.__mode == 'output':
                GPIO.output(self.__pin, not self.__state)
                self.__state = not self.__state
            else:
                raise f'Modo del pin {self.__pin}:{self.__mode}'
        def setState(self, state):
            '''Cambia el estado del pin'''
            if self.__mode == 'output':
                GPIO.output(self.__pin, state)
                self.__state = state
            else:
                raise f'Modo del pin {self.__pin}:{self.__mode}'
        def getState(self):
            '''Devuelve el estado del pin'''
            if self.__mode == 'input':
                state = GPIO.input(self.__pin)
                self.__state = not self.__state
                return state
            raise f'Modo del pin {self.__pin}:{self.__mode}'

    class IO:
        def __init__(self, entrada, salida, led) -> None:
            '''Constructor para los sensores de entrada y salida'''
            self.__entrada:ASMB.Pin = entrada
            self.__salida:ASMB.Pin = salida
            self.__led:ASMB.Pin = led
        def checkEntry(self,):
            while 1:
                e = self.__entrada.getState()
                if e:
                    ASMB.enUso = True
                    break
                self.__led.setState(0)
                sleep(0.1)
        def checkExit(self,):
            while 1:
                e = self.__salida.getState()
                if e:
                    ASMB.enUso = False
                    break
                self.__led.setState(1)
                sleep(0.1)