/*
@file: xbee.cpp

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

#include "xbee.h"
#include <Arduino.h>
#include <string.h>

#define CTS_BUFFER_LEFT 16

static int conf = 0;
static const char* str_OK = "OK";
static const char* sn;

static int startConf();
static int endConf();
static int recvOK();
static int checkOK(const char* recv);
static int recvData(char* recv, size_t recv_len);
static int sendCTS(const char* str);
static int sendBuffer(const char* str);

static int startConf(){
	Serial.write("+++");
	if(recvOK() == XBEE_SUCCESS){
		conf = 1;
		return XBEE_SUCCESS;
	}
	return XBEE_ERROR;
}

static int endConf(){
	int status = xbee_sendAtForOk("CN");
	if(status == XBEE_SUCCESS){
		conf = 0;
		return XBEE_SUCCESS;
	}
	return XBEE_ERROR;
}

static int recvOK(){
	char recv[3];
	int status = recvData(recv, sizeof(recv));
	if(status == 2){
		return checkOK(recv);
	} else if(status < 0){

		return status;
	} else {
		return XBEE_ERROR;
	}
}

static int recvData(char* recv, size_t recv_len){
	unsigned long end_time = millis() + XBEE_TO_TIME;
	size_t p = 0;
	while (p < recv_len) {
		if(end_time < millis()) {
			return XBEE_TO_ERR;
		}
		if(Serial.available()){
			char c = Serial.read();
			if(c == '\r'){
				recv[p] = '\0';
				return p;
			}
			recv[p++] = c;
		}
	}
	return XBEE_OVF;
}

static int checkOK(const char* recv){
	if(strcmp(recv, str_OK) == 0){
		return XBEE_SUCCESS;
	} else {
		return XBEE_ERROR;
	}
}

/*
static int checkPAN(){
	char id_pan[17];
	char op_pan[17];
	int status = xbee_getPANID(id_pan, NULL);
	if(status != XBEE_SUCCESS) return XBEE_ASSOCIATION_NO_SUCCESS;
	status = xbee_getOpPAN(op_pan, NULL);
	if(status != XBEE_SUCCESS) return XBEE_ASSOCIATION_NO_SUCCESS;
	if(strcmp(id_pan, op_pan) == 0) return XBEE_ASSOCIATION_SUCCESS;
	return XBEE_ASSOCIATION_NO_SUCCESS;
}
*/

int xbee_init(){
	Serial.begin(9600); // TODO increase baud rate
	pinMode(XBEE_CTS_PIN, INPUT);
	int status = xbee_getSN();
	if(status != XBEE_SUCCESS) return status;
	sn = xbee_getSN_pchar();
	return XBEE_SUCCESS;
}

int xbee_wait_connect(uint16_t timeout){
	// TODO return error info
	int status = xbee_sendAtForOk("NR");
	if(status != XBEE_SUCCESS){
		return status;
	}

	unsigned long end = millis() + timeout;
	while(millis() < end){
		status = xbee_getAssociation();
		if(status == 0) return XBEE_ASSOCIATION_SUCCESS;
	}
	return XBEE_ASSOCIATION_NO_SUCCESS;
}

int xbee_sendAtForResponse(const char* at, char* resp, size_t resp_len){
	if(!conf) {
		int status = startConf();
		if(status != XBEE_SUCCESS) return status;
	}
	Serial.write("AT ");
	Serial.write(at);
	Serial.write("\r");
	return recvData(resp, resp_len);
}

int xbee_sendAtForConfig(const char* at, const char* arg){
	int len = strlen(at) + strlen(arg) + 2;
	char send[len];
	strcat(strcat(strcpy(send, at), " "), arg);
	return xbee_sendAtForOk(send);
}

int xbee_sendAtForOk(const char* at){
	char recv[3];
	int status = xbee_sendAtForResponse(at, recv, sizeof(recv));
	if(status == 2) return checkOK(recv);
	return status;
}

int xbee_send(const char* str){
	if(conf) {
		int status = endConf();
		if(status != XBEE_SUCCESS) return status;
	}
	int len = 0;
	int status = 0;
#ifdef XBEE_SEND_SERIAL
	status = sendCTS(sn);
	if(status < 0) return status;
	len += status;
#endif
	status = sendCTS(" {");
	if(status < 0) return status;
	len += status;
	status = sendCTS(str);
	if(status < 0) return status;
	len += status;
	status = sendCTS("}\r");
	if(status < 0) return status;
	len += status;
	return len;

}

int xbee_send_byte(uint8_t* c, size_t len){
	return XBEE_ERROR; // TODO
}

int xbee_changeBR(){
	int status = xbee_sendAtForConfig("BD", "7");
	if(status != XBEE_SUCCESS) return status;
	status = xbee_ac();
	if(status != XBEE_SUCCESS) return status;
	Serial.begin(115200);
	return XBEE_SUCCESS;
}


static int sendCTS(const char* str){
	unsigned long to = millis() + XBEE_TO_TIME;

	for(uint16_t i = 0;; i += CTS_BUFFER_LEFT){
		Serial.flush();
		while(digitalRead(XBEE_CTS_PIN)){
			if(millis() > to) return XBEE_TO_ERR;
		}
		uint16_t len = sendBuffer(str + i);
		if(len != 16) return i + len;
	}
}

static int sendBuffer(const char* str){
	for(uint8_t i = 0; i < CTS_BUFFER_LEFT; ++i){
		char c = str[i];
		if(c == '\0') return i;
		Serial.write(c);
	}
	return CTS_BUFFER_LEFT;
}
