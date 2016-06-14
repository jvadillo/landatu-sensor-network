/* ===============================================================
      Project: Aldeano 24hrs
       Author: Jon Vadillo
      Created: 08/06/2016
  Arduino IDE: 1.0.5
      Website: http://www.jonvadillo.com
  Description: .....
  ================================================================== */

/*
  Connect 5V on Arduino to VCC on Relay Module
  Connect GND on Arduino to GND on Relay Module
  Connect GND on Arduino to the Common Terminal (middle terminal) on Relay Module. */

#include "DHT.h"
#define DHTPIN 8
#define DHTTYPE DHT11 
DHT dht(DHTPIN, DHTTYPE);

#define RELAY1  6                        
#define RELAY2  7 


void setup() {
  // Initialise the Arduino data pins for OUTPUT
  pinMode(RELAY1, OUTPUT);       
  pinMode(RELAY2, OUTPUT);

  Serial.begin(9600);
}

void loop() {

  if(Serial.available() > 0) {

    char action = Serial.read();
    if(action == 'G') {
      int hum = dht.readHumidity();// Lee la humedad
      int temp= dht.readTemperature();//Lee la temperatura

      String message = "Humedad Relativa: " + String(hum) + " -- Temperatura: " + String(temp) + "C";
      Serial.println(message);                           
    }
    else if(action == 'S') {
      char pin = Serial.read();
      char mode = Serial.read();
      Serial.print("PIN:");
      Serial.print(pin);
      Serial.print("MODE:");
      Serial.print(mode);
      
      switch(pin) {
        case '6':
          setDigialPin(RELAY1,mode);   // Turns Relay Off
          break;
        case '7':
          setDigialPin(RELAY2,mode);    // Turns ON Relays 1
          break;
      }
    }
  }
  delay(500);
}

void setDigialPin(int pin,int mode){
  switch(mode) {
    case '1':
      digitalWrite(pin,HIGH);   // Turns Relay Off
      break;
    case '0':
      digitalWrite(pin,LOW);    // Turns ON Relays 1
      break;
  }
}

