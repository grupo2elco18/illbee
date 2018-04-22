#ifndef COLOR_LED_H
#define COLOR_LED_H

#include "stdint.h"

#define LED_RED      0xFF0000
#define LED_GREEN    0x00FF00
#define LED_BLUE     0x0000FF
#define LED_YELLOW   0xFFFF00
#define LED_CYAN     0x00FFFF
#define LED_MAGENTA  0xFF00FF
#define LED_WHITE    0xFFFFFF

#define LED_RED_PIN 11
#define LED_GREEN_PIN 9
#define LED_BLUE_PIN 10

void colorLED_begin();
void colorLED_set(long color);
void colorLED_setByte(uint8_t r, uint8_t g, uint8_t b);
void colorLED_off();


#endif // COLOR_LED_H
