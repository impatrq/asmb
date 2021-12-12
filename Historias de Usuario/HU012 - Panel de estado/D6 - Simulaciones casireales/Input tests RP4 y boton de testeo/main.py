import RPi.GPIO as GPIO
from time import sleep

def main():
	estados = [1,0,1,0,1,0,1,0]

	GPIO.setwarnings(False)

	GPIO.setmode(GPIO.BOARD)

	SH_CP = 29
	DS = 31
	ST_CP = 32
	MR = 33

	IN = [7,11,12,13,15,16,18,22]
	for p in IN:
		GPIO.setup(p, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		
	TEST = 19
	GPIO.setup(TEST, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

	GPIO.setup(SH_CP, GPIO.OUT)
	GPIO.setup(DS, GPIO.OUT)
	GPIO.setup(ST_CP, GPIO.OUT)
	GPIO.setup(MR, GPIO.OUT, initial=GPIO.HIGH)

	def refreshLEDs():
		GPIO.output(ST_CP, GPIO.HIGH)
		GPIO.output(ST_CP, GPIO.LOW)
	
	def refreshRegisters():
		GPIO.output(SH_CP, GPIO.HIGH)
		GPIO.output(SH_CP, GPIO.LOW)
	
	def clean():
		GPIO.output(MR, GPIO.HIGH)
		GPIO.output(MR, GPIO.LOW)
		refreshRegisters()
		refreshLEDs()


	def sendData(e):
		if e:
			GPIO.output(DS, GPIO.HIGH)
		else:
			GPIO.output(DS, GPIO.LOW)

	while 1:
		if GPIO.input(TEST) :
			for _ in IN:
				sendData(1)
				refreshRegisters()
				refreshLEDs()
		else:
			for p in IN:
				input = GPIO.input(p)
				sendData(input)
				refreshRegisters()
				refreshLEDs()
		sleep(1)


if __name__=='__main__':
	main()
