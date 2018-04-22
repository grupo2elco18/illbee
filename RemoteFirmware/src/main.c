#include <Arduino.h>
#include <xbee.h>

extern void Error_Handler();

void setup() {
	pinMode(9, OUTPUT); //Green
	pinMode(10, OUTPUT); //Blue
	pinMode(11, OUTPUT); //Red
	xbee_begin();
	digitalWrite(11, HIGH);
	delay(500);
	digitalWrite(11, LOW);
	delay(1000);
}

void loop() {

	int rc = xbee_send("Hola, Mundo!\r");
	if(rc != 13){
		Error_Handler();
	}
	delay(1000);
}

void Error_Handler(){
	digitalWrite(9, LOW);
	digitalWrite(10, LOW);
	digitalWrite(11, LOW);
	while(1){
		digitalWrite(11, HIGH);
		delay(500);
		digitalWrite(11, LOW);
		delay(500);
	}
}
