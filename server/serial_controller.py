# -*- coding: utf-8 -*-

import time # Librería para hacer que el programa que controla el bot no se acabe.
import random
import datetime
import token
import os

import serial #Para hablar con Arduino por el puerto serial


def setData(pin,mode):
	
	print("setData: "+pin+" - "+mode) 
	arduino = serial.Serial('COM3', 9600, timeout=0)
	time.sleep(2) #Ncesario antes de escribir en el puerto serie
	
	arduino.write(pin+''+mode.encode('ascii'))
	
	arduino.close() #Finalizamos la comunicacion

def getData:
	
