import serial #Para hablar con Arduino por el puerto serial
import logging
import telegram_controller
import time # Librería para hacer que el programa que controla el bot no se acabe.


#configure logging
logging.basicConfig(level=logging.INFO, 
					filename='myserver.log', # log to this file
					format='%(asctime)s %(message)s') # include timestamp


def __init__(self):
	logging.info('__init__ MainController')

def start(self):
	logging.info('start() MainController')
		
def getData():
	print("getData()")
	arduino = serial.Serial('COM3', 9600, timeout=0)
	time.sleep(2) #Ncesario antes de escribir en el puerto serie
	arduino.write('G'.encode('ascii')) #Le indicamos a Arduino que queremos hacer una lectura ('G')
	#time.sleep(2) #Ncesario antes de escribir en el puerto serie

	received = 0
	while (received == 0):
		if arduino.inWaiting() > 0:
			time.sleep(2) #Este sleep es necesario antes de leer, si no no se lee el mensaje completo.

			myData = arduino.readline()
			print("mydata...")
			print(myData.decode())
			arduino.close()
			received = 1
			return myData.decode()



	

def setData(pin,mode):
	print("setData: "+pin+" - "+mode) 
	arduino = serial.Serial('COM3', 9600, timeout=0)
	time.sleep(2) #Ncesario antes de escribir en el puerto serie

	arduino.write('G'.encode('ascii')) #Le indicamos a Arduino que queremos hacer una lectura ('G')
	time.sleep(0.1)

	message = str(pin)+''+str(mode)
	arduino.write(message.encode('ascii'))
	
	arduino.close() #Finalizamos la comunicacion

	



	