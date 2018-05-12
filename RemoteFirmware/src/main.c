#include <Arduino.h>
#include <xbee.h>
#include <colorLED.h>
#include <stdio.h>
#include <irCam.h>
#include <stdlib.h>

#define LED_COLOR LED_GREEN

#define BUTTON_PIN 2
#define DEBOUNCE_TIME 50

extern void Error_Handler();
static void button_isr();

volatile uint8_t button;

void setup() {

	colorLED_begin();

	colorLED_set(LED_BLUE);


	irCam_init();

	if(xbee_init() != XBEE_SUCCESS){
		Error_Handler();
	}

	if(xbee_changeBR() != XBEE_SUCCESS){
		Error_Handler();
	}

	colorLED_set(LED_ORANGE);
	// TODO Configure xbee here
	if(xbee_wait_connect(30000) != XBEE_ASSOCIATION_SUCCESS){
		Error_Handler();
	}

	colorLED_set(LED_COLOR);

	pinMode(BUTTON_PIN, INPUT_PULLUP);
	attachInterrupt(digitalPinToInterrupt(BUTTON_PIN), button_isr, FALLING);
}

void loop() {

	uint16_t points[8];
	irCam_read(points);

	if(button){
		button = 0;
		if(xbee_send("button") <= 0){
			Error_Handler();
		}
	}

	char buffer[50];
	sprintf(buffer, "%d, %d, %d, %d, %d, %d, %d, %d",
		points[0], points[1], points[2], points[3],
		points[4], points[5], points[6], points[7]
	);

	if(xbee_send(buffer) <= 0){
		Error_Handler();
	}
	delay(20);
}

void Error_Handler(){
	colorLED_off();
	while(1){
		colorLED_set(LED_RED);
		xbee_send("Error");
		delay(500);
		colorLED_off();
		delay(500);
	}
}

static void button_isr(){
	static unsigned long last = 0;
	unsigned long now = millis();
	if(now < last + DEBOUNCE_TIME) return;

	last = now;

	button = 1;
}
