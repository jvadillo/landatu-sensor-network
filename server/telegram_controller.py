# -*- coding: utf-8 -*-
 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import random
import datetime
import token
import os

from main_controller import *
import serial #Para hablar con Arduino por el puerto serial

TOKEN = '237825928:AAHmGwQzR71fCny9yjAbxT0vaAMY5O-AhOA' #Nuestro token del bot
 
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
#Listener
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
	for m in messages: # Por cada dato 'm' en el dato 'messages'
		cid = m.chat.id # Almacenaremos el ID de la conversación.
		if m.content_type == 'text':
			print(m.text) 
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
#############################################
#Funciones
@bot.message_handler(commands=['help']) 
def command_ayuda(m): 
	cid = m.chat.id 
	bot.send_message( cid, "Comandos Disponibles: /help, /temp, /saludo")


@bot.message_handler(commands=['getdata'])
def command_getdata(m):
	cid = m.chat.id
	print("Comando: "+m.text) 
	
	data = getData()
	print("Send data: "+str(data))
	bot.send_message( cid, data)

	

@bot.message_handler(commands=['activar'])
def command_activar(m):
	cid = m.chat.id
	print("Comando: "+m.text)

	# split the text
	words = m.text.split()
	# TODO: comprobar si el length es 3 y si no lo es devolver mensaje de error
	pin = words[1]
	mode = words[2]
	
	setData(pin,mode)


@bot.message_handler(commands=['desactivar'])
def command_activar(m):
	cid = m.chat.id
	print("Comando: "+m.text) 
	arduino = serial.Serial('COM3', 9600, timeout=0)
	time.sleep(2) #Ncesario antes de escribir en el puerto serie
	
	
	# split the text
	words = m.text.split()
	pin = words[1]
	print("Desactivar: "+pin) 
	arduino.write('0'.encode('ascii'))
	time.sleep(2) #Ncesario antes de escribir en el puerto serie
	#arduino.write(pin.encode('ascii'))

	arduino.close() #Finalizamos la comunicacion

@bot.message_handler(commands=['kaixo'])
def command_temp(m):
	cid = m.chat.id

	bot.send_message(cid, "Kaixo, zer moduz?")

#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algun fallo.