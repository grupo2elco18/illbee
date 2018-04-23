#ifndef XBEE_CONF_H
#define XBEE_CONF_H

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

#define XBEE_ASSOCIATION_SUCCESS 0
#define XBEE_ASSOCIATION_NO_SUCCESS 1

int xbee_getSN();
const char* xbee_getSN_pchar();
const uint8_t* xbee_getSN_pbyte();
int xbee_getAssociation(); //AI

int xbee_getPANID(char* sdc, uint8_t* sdb);
int xbee_setPANID(const char* sdc);

int xbee_isCoordinator();
int xbee_setCoordinator(int c);

int xbee_wr();

#ifdef __cplusplus
}
#endif


// TODO baudrate



#endif // XBEE_CONF_H
