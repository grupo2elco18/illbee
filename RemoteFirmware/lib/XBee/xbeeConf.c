#include "xbeeConf.h"
#include "xbee.h"
#include <string.h>
#include <stdlib.h>

static char* strcpy_size(char* dest, const char* src, size_t len);

static char sn_c[17];
static uint8_t sn_b[8];

const char* xbee_getSN_pchar(){
	return sn_c;
}

const uint8_t* xbee_getSN_pbyte(){
	return sn_b;
}

int xbee_getSN(){
	char buffer[10];
	int status = xbee_sendAtForResponse("SH", buffer, sizeof(buffer));
	if(status <= 0) return status;
	strcpy_size(sn_c, buffer, 9);
	status = xbee_sendAtForResponse("SL", buffer, sizeof(buffer));
	if(status <= 0) return status;
	strcpy_size(sn_c+8, buffer, 9);
	return XBEE_SUCCESS;
}

int xbee_getAssociation(){
	char buffer[10];
	int status = xbee_sendAtForResponse("AI", buffer, sizeof(buffer));
	if(status <= 0) return status;
	return (int) strtoul(buffer, NULL, 16);
}

int xbee_getPANID(char* sdc, uint8_t* sdb){
	char buffer[17];
	int status = xbee_sendAtForResponse("ID", buffer, sizeof(buffer));
	if(status <= 0) return status;
	strcpy_size(sdc, buffer, 17);
	return XBEE_SUCCESS;
}

int xbee_getOpPAN(char* sdc, uint8_t* sdb){
	char buffer[17];
	int status = xbee_sendAtForResponse("OP", buffer, sizeof(buffer));
	if(status <= 0) return status;
	strcpy_size(sdc, buffer, 17);
	return XBEE_SUCCESS;
}

static char* strcpy_size(char* dest, const char* src, size_t len){
	int diff = len - (strlen(src) + 1);
	if(diff < 0) return NULL;
	memset(dest, '0', len);
	strcpy(dest + diff, src);
	return dest;
}

int xbee_setPANID(const char* sdc){
	return xbee_sendAtForConfig("ID", sdc);
}

int xbee_wr(){
	return xbee_sendAtForOk("WR");
}

int xbee_ac(){
	return xbee_sendAtForOk("AC");
}

// TODO complete this driver
// TODO repeated code with get ids
