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

#Bucle Principal, cada N-tiempo realizo N-tarea
while(1):
    #Bucle de tiempo
    TimaMiler = TimaMiler + 1

    #si estiempo maximo(Accion desinfectante)
    if(TimaMiler == desinf):
        
        #Reset Tiempos
        TimaMiler = 0
        Test = 10050
        proxen = 1000
        proxsa = 10000
        alcol = 100300
        desinf = 5000000
        panel = 500000

        #Si se esta dentro
        if(Entro):
            #Activo el desinfectante
            GPIO.output(11, 1)
            #Cuento un pulso
            a = a + 1
            #si llego a 3 pulsos
            if(a == 3):
                #Paro el desinfectante y reseteo pulsos
                a = 0
                GPIO.output(11, 0)
        #si salio   
        else:
            #Apago desinfectante y reseteo pulsos
            a = 0
            GPIO.output(11, 0)

    #si es tiempo de leer Proximidad de entrada
    if(TimaMiler == proxen):
        #si Senso la entrada
        if(GPIO.input(24)):
            #Enciendo cartel de ocupado
            GPIO.output(15, 1)
            #Declaro que "Esta dentro de la cabina"
            entro = 1
        #Declaro proximo tiempo de Lectura
        proxen = proxen + 1000

    #si es tiempo de leer el alcohol

    if(TimaMiler == alcol):
        #si pone las manos
        if(GPIO.input(18)):
            # Cuento tiempo de dispenser
            a = a + 1
            #si el tiempo de dispenser es menor al maximo
            if(a <= 60):
                #Activo dispenser
                GPIO.output(10, 1)
            #si se paso de tiempo
            else:
                #Paro el dispenser
                GPIO.output(10, 0)
        #si no tiene las manos
        if(not GPIO.input(18)):
            #Reseteo el contador
            a = 0
            #apago el dispenser
            GPIO.output(10, 0)
        #Declao proximo tiempo de lectura
        alcol = alcol + 1000000

    #Si es tiempo de Testear
    if(TimaMiler == Test):
        #si toca el boton de test
        if(GPIO.input(17)):
            #Carga todos los estados en 1
            logSensors(1)
        #Declaro proximo tiempo de testeo
        Test = Test + 10000
    
    #si es tiempo de leer la salida
    if(TimaMiler == proxsa):
        #si esta saliendo
        if(GPIO.input(23)):
            #Declaro que esta fuera
            Entro = 0
            #Apago cartel de ocupado
            GPIO.output(15, 1)
            #Apago Motor desinfectante(en caso que este activado)
            GPIO.output(11, 0)
        #declaro proximo tiempo de Lectura de salida
        proxsa = proxsa + 10000

    #si es tiempo de actualizar el panel
    if(TimaMiler == panel):
        #si no esta haciendo un test
        if(not GPIO.input(17)):
            #Carga los estados al panel
            logSensors(0)
        #declaro proximo tiempo de actualizacion del panel
        panel = panel + 500000
