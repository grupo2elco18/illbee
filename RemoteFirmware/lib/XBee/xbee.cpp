#include "xbee.h"
#include <Arduino.h>
#include <string.h>

static int conf = 0;
static const char* str_OK = "OK";
static const char* sn;

static int startConf();
static int endConf();
static int recvOK();
static int checkOK(const char* recv);
static int recvData(char* recv, size_t recv_len);

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

int xbee_init(){
	Serial.begin(9600);
	int status = xbee_getSN();
	if(status != XBEE_SUCCESS) return status;
	sn = xbee_getSN_pchar();
	return XBEE_SUCCESS;
}

int xbee_wait_connect(uint16_t timeout){
	// TODO return error info
	unsigned long end = millis() + timeout;
	int status;
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
	len += Serial.write(sn);
	len += Serial.write(" {");
	len += Serial.write(str);
	len += Serial.write("}\r");
	return len;

}

int xbee_send_byte(uint8_t* c, size_t len){
	return XBEE_ERROR; // TODO
}
