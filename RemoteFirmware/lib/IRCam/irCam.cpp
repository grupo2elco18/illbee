#include "irCam.h"
#include <Arduino.h>
#include <Wire.h>
#include <string.h>

static void write2bytes(uint8_t d1, uint8_t d2);

void irCam_init(){
	Wire.begin();
	write2bytes(0x30,0x01); delay(10);
	write2bytes(0x30,0x08); delay(10);
	write2bytes(0x06,0x90); delay(10);
	write2bytes(0x08,0xC0); delay(10);
	write2bytes(0x1A,0x40); delay(10);
	write2bytes(0x33,0x33); delay(10);
	delay(100);
}

void irCam_read(uint16_t* points){
	Wire.beginTransmission(IR_SLAVE);
	Wire.write(0x36);
	Wire.endTransmission();

	uint8_t buffer[16];
	Wire.requestFrom(IR_SLAVE, 16);
	memset(buffer, 0, sizeof(buffer));

	for(size_t i = 0; i < sizeof(buffer); ++i){
		if(Wire.available() == 0) break;
		buffer[i] = Wire.read();
	}

	for(int i = 0; i < 4; ++i){
		points[2*i] = buffer[3*i+1];
		points[2*i] += (buffer[3*i+3] & 0x30) << 4;
		points[2*i+1] = buffer[3*i+2];
		points[2*i+1] += (buffer[3*i+3] & 0xC0) << 2;
	}
}

static void write2bytes(uint8_t d1, uint8_t d2) {
	Wire.beginTransmission(IR_SLAVE);
	Wire.write(d1); Wire.write(d2);
	Wire.endTransmission();
}

// TODO too many magic numbers
