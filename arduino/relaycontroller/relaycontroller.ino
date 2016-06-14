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


#define RELAY1  6                        
#define RELAY2  7 

int command;
int state = 0; //TODO: define states.

void setup() {
  // Initialise the Arduino data pins for OUTPUT
  pinMode(RELAY1, OUTPUT);       
  pinMode(RELAY2, OUTPUT);
  digitalWrite(RELAY1,HIGH);   // Turns Relay Off

  Serial.begin(9600);
}

void loop() {

  if(Serial.available() > 0) {

    char mode = Serial.read();
    
    switch(mode) {
      case '1':
        digitalWrite(RELAY1,HIGH);   // Turns Relay Off
        break;
      case '0':
        digitalWrite(RELAY1,LOW);    // Turns ON Relays 1
        break;
    }
  }
  delay(500);
}
