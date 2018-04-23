#include <Arduino.h>
#include <xbee.h>
#include <colorLED.h>
#include <stdio.h>

extern void Error_Handler();

void setup() {
	colorLED_begin();
	colorLED_set(LED_BLUE);

	if(xbee_init() != XBEE_SUCCESS){
		Error_Handler();
	}

	colorLED_set(LED_GREEN);
}

void loop() {
	if(xbee_send("Hola, Mundo!") <= 0){
		Error_Handler();
	}
	delay(1000);
}

void Error_Handler(){
	colorLED_off();
	while(1){
		colorLED_set(LED_RED);
		delay(500);
		colorLED_off();
		delay(500);
	}
}
