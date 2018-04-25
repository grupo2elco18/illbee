#include <Arduino.h>
#include <xbee.h>
#include <colorLED.h>
#include <stdio.h>
#include <irCam.h>
#include <stdlib.h>

extern void Error_Handler();

void setup() {
	colorLED_begin();
	colorLED_set(LED_BLUE);

	irCam_init();

	if(xbee_init() != XBEE_SUCCESS){
		Error_Handler();
	}

	colorLED_set(LED_ORANGE);
	if(xbee_wait_connect(2000) != XBEE_ASSOCIATION_SUCCESS){
		Error_Handler();
	}

	colorLED_set(LED_GREEN);
}

void loop() {
	uint16_t points[8];
	irCam_read(points);

	char buffer[50];
	sprintf(buffer, "%d, %d, %d, %d, %d, %d, %d, %d",
		points[0], points[1], points[2], points[3],
		points[4], points[5], points[6], points[7]
	);

	if(xbee_send(buffer) <= 0){
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
