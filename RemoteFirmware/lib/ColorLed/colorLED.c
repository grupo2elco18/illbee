/*
@file: colorLED.c

Copyright (C) 2018 by Alejandro Vicario and the IllBee contributors.

This file is part of the IllBee project.

IllBee is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

IllBee is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with IllBee.  If not, see <http://www.gnu.org/licenses/>.
*/

#include "colorLED.h"
#include <Arduino.h>

#if defined(LED_COMMON_ANODE) && defined(LED_COMMON_CATHODE)
#warning "LED configured for common cathode and anode simultaneously"
#endif

void colorLED_begin(){
	pinMode(LED_RED_PIN, OUTPUT);
	pinMode(LED_GREEN_PIN, OUTPUT);
	pinMode(LED_BLUE_PIN, OUTPUT);
}

void colorLED_set(long color){
	uint8_t r = (color & 0xFF0000) >> 16;
	uint8_t g = (color & 0x00FF00) >> 8;
	uint8_t b = (color & 0x0000FF) >> 0;
	colorLED_setByte(r, g, b);
}

void colorLED_setByte(uint8_t r, uint8_t g, uint8_t b){

#ifdef LED_COMMON_ANODE
	r = 255-r;
	g = 255-g;
	b = 255-b;
#endif

	analogWrite(LED_RED_PIN, r);
	analogWrite(LED_GREEN_PIN, g);
	analogWrite(LED_BLUE_PIN, b);
}

void colorLED_off(){
	colorLED_setByte(0, 0, 0);
}

// TODO Adjust with real light values
/* TODO
void sqrtLED(uint8_t r, uint8_t g, uint8_t b){
	double rr = sqrt(((uint16_t)r)*255);
	double gg = sqrt(((uint16_t)g)*255);
	double bb = sqrt(((uint16_t)b)*255);
	char buffer[20];
	colorLED_setByte((uint8_t) rr, (uint8_t) gg, (uint8_t) bb);
}*/
