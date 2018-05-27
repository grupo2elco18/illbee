/*
@file: colorLED.h

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

#ifndef COLOR_LED_H
#define COLOR_LED_H

#include "stdint.h"

//#define LED_COMMON_CATHODE
#define LED_COMMON_ANODE

#define LED_RED      0xFF0000
#define LED_GREEN    0x00FF00
#define LED_BLUE     0x0000FF
#define LED_YELLOW   0xFFFF00
#define LED_CYAN     0x00FFFF
#define LED_MAGENTA  0xFF00FF
#define LED_WHITE    0xFFFFFF
#define LED_ORANGE   0xDF9400

#define LED_RED_PIN 11
#define LED_GREEN_PIN 10
#define LED_BLUE_PIN 9

void colorLED_begin();
void colorLED_set(long color);
void colorLED_setByte(uint8_t r, uint8_t g, uint8_t b);
void colorLED_off();


#endif // COLOR_LED_H
