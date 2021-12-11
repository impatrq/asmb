import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

ProxEnt = 24
ProxSal = 23
CartelOcupado = 15
PanelTest = 17
PanelSHCP = 22
PanelDC = 27
PanelSTCP = 4
MotorGel = 10
MotorDesinfectante = 11
ProxAlcohol = 18
def setupPines():
    GPIO.setup(ProxEnt, GPIO.IN,pull_up_down=GPIO.PUD_DOWN) ###Prox entrada
    GPIO.setup(ProxSal, GPIO.IN,pull_up_down=GPIO.PUD_DOWN) ###Prox salida
    GPIO.setup(CartelOcupado, GPIO.OUT)                            ###Ocupado
    GPIO.setup(PanelTest, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)   ##TEST Estado
    GPIO.setup(PanelSHCP, GPIO.OUT)                            ##SHCP
    GPIO.setup(PanelDC, GPIO.OUT)                            ##DC
    GPIO.setup(PanelSTCP,  GPIO.OUT)                            ##STCP
    GPIO.setup(MotorGel, GPIO.OUT)                             ##Motor gel
    GPIO.setup(ProxAlcohol, GPIO.IN)                              ##Sensor alkohol
    GPIO.setup(MotorDesinfectante, GPIO.OUT)                             ##Motor Desinf
  # Funcion para Envia los estados de los sensores al panel de estado
def logSensors(states):
      # Declaro variable para bucle
    P = 0
      # Inicio buble
    while(P < 8):
          # Cargo estado p   
        GPIO.output(27, states)  
        GPIO.output(22, 1)
          # Aumento P
        P = P + 1
          # Bajo flag de carga
        GPIO.output(22, 0)
      # Subo estados cargados
    GPIO.output(4, 1)


setupPines()
# Variables globales para definir tiempos
# Declaro cada cuanto tiempo se repiten segun las necesidades de la cabina
a = 0
Entro = 0
TimaMiler = 0
Test = 10050
ProxEnntrada = 1000
ProxSalida = 10000 
Alcohol = 100300
Desinf = 5000000
Panel = 500000
# Bucle Principal, cada N-tiempo realizo N-tarea
while 1:
      # Bucle de tiempo
    TimaMiler += 1

      # Si estiempo maximo(Accion desinfectante)
    if TimaMiler == Desinf:
        
          # Reset Tiempos
        TimaMiler = 0
        Test = 10050
        ProxEnntrada = 1000
        ProxSalida = 10000 
        Alcohol = 100300
        Desinf = 5000000
        Panel = 500000

          # Si se esta dentro
        if Entro:
              # Activo el desinfectante
            GPIO.output(MotorDesinfectante, 1)
              # Cuento un pulso
            a += 1
              # Si llego a 3 pulsos
            if a == 3:
                  # Paro el desinfectante y reseteo pulsos
                a = 0
                GPIO.output(MotorDesinfectante, 0)
          # si salio   
        else:
              # Apago desinfectante y reseteo pulsos
            a = 0
            GPIO.output(MotorDesinfectante, 0)

      # Si es tiempo de leer Proximidad de entrada
    if TimaMiler == ProxEnntrada:
          # Si Senso la entrada
        if GPIO.input(ProxEnt):
              # Enciendo cartel de ocupado
            GPIO.output(CartelOcupado, 1)
              # Declaro que "Esta dentro de la cabina"
            entro = 1
          # Declaro proximo tiempo de Lectura
        ProxEnntrada += 1000

      # si es tiempo de leer el alcohol
    if TimaMiler == Alcohol:
          # Si pone las manos
        if GPIO.input(ProxAlcohol):
              # Cuento tiempo de dispenser
            a += 1
              # Si el tiempo de dispenser es menor al maximo
            if a <= 60:
                  #Activo dispenser
                GPIO.output(MotorGel, 1)
              # Si se paso de tiempo
            else:
                  #Paro el dispenser
                GPIO.output(MotorGel, 0)
          # Si no tiene las manos
        if not GPIO.input(ProxAlcohol):
              # Reseteo el contador
            a = 0
              # Apago el dispenser
            GPIO.output(MotorGel, 0)
          # Declao proximo tiempo de lectura
        Alcohol += 1000000

      # Si es tiempo de Testear
    if TimaMiler == Test:
          # Si toca el boton de test
        if GPIO.input(PanelTest):
              # Carga todos los estados en 1
            logSensors(1)
          # Declaro proximo tiempo de testeo
        Test += 10000
    
      # Si es tiempo de leer la salida
    if TimaMiler == ProxSalida :
          # Si esta saliendo
        if GPIO.input(ProxSal):
              # Declaro que esta fuera
            Entro = 0
              # Apago cartel de ocupado
            GPIO.output(CartelOcupado, 1)
              # Apago Motor desinfectante(en caso que este activado)
            GPIO.output(MotorDesinfectante, 0)
          # Declaro proximo tiempo de Lectura de salida
        ProxSalida += 10000

      # Si es tiempo de actualizar el panel
    if(TimaMiler == Panel):
          # Si no esta haciendo un test
        if not GPIO.input(PanelTest):
              # Carga los estados al panel
            logSensors(0)
          # Declaro proximo tiempo de actualizacion del panel
        Panel += 500000
