#include <Arduino.h>
#include <xbee.h>
#include <colorLED.h>
#include <stdio.h>

extern void Error_Handler();

void setup() {
	colorLED_begin();
	xbee_begin();
	for(int i = 0; i < 256; ++i){
		colorLED_setByte(255 - i, i, 0);
		delay(10);
	}
	for(int i = 0; i < 256; ++i){
		colorLED_setByte(0, 255 - i, i);
		delay(10);
	}
	for(int i = 0; i < 256; ++i){
		colorLED_setByte(i, 0, 255 - i);
		delay(10);
	}

	colorLED_setByte(255, 255, 255);
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
