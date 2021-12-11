import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)


def setupPines():
    GPIO.setup(24, GPIO.IN,pull_up_down=GPIO.PUD_DOWN) ###Prox entrada
    GPIO.setup(23, GPIO.IN,pull_up_down=GPIO.PUD_DOWN) ###Prox salida
    GPIO.setup(15, GPIO.OUT)                            ###Ocupado
    GPIO.setup(17, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)   ##TEST Estado
    GPIO.setup(22, GPIO.OUT)                            ##SHCP
    GPIO.setup(27, GPIO.OUT)                            ##DC
    GPIO.setup(4,  GPIO.OUT)                            ##STCP
    GPIO.setup(10, GPIO.OUT)                             ##Motor gel
    GPIO.setup(18, GPIO.IN)                              ##Sensor alkohol
    GPIO.setup(11, GPIO.OUT)                             ##Motor Desinf

#Funcion para Envia los estados de los sensores al panel de estado
def logSensors(states):

    P = 0
    while(P < 8):  
        GPIO.output(27, states)  
        GPIO.output(22, 1)
        P=P+1
        GPIO.output(22, 0)
    GPIO.output(4, 1)


setupPines()
#Variables globales para definir tiempos
    a = 0
    Entro = 0
    TimaMiler = 0
    Test = 10050
    proxen = 1000
    proxsa = 10000 
    alcol = 100300
    desinf = 5000000
    panel = 500000
while(1):

    TimaMiler = TimaMiler + 1
    if(TimaMiler == desinf):

        TimaMiler = 0
        Test = 10050
        proxen = 1000
        proxsa = 10000
        alcol = 100300
        desinf = 5000000
        panel = 500000
        if(Entro):

            GPIO.output(11, 1)
            
            a = a + 1
            if(a == 3):

                a = 0
                GPIO.output(11, 0)
                
        else:

            a = 0
            GPIO.output(11, 0)

    if(TimaMiler == proxen):

        if(GPIO.input(24)):

            GPIO.output(15, 1)
            entro = 1

        proxen = proxen + 1000

    if(TimaMiler == alcol):

        if(GPIO.input(18)):

            a = a + 1
            if(a <= 100):
                GPIO.output(10, 1)

        if(not GPIO.input(18)):

            a = 0
            GPIO.output(10, 0)

        alcol = alcol + 1000000

    if(TimaMiler == Test):

        if(GPIO.input(17)):

            logSensors(1)

        Test = Test + 10000
    if(TimaMiler == proxsa):

        if(GPIO.input(23)):

            Entro = 0
            GPIO.output(15, 1)
            GPIO.output(11, 0)

        proxsa = proxsa + 10000

    if(TimaMiler == panel):

        if(not GPIO.input(17)):

            logSensors(0)

        panel = panel + 500000
