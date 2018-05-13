#ifndef XBEE_H
#define XBEE_H

#include "stdlib.h"
#include "stdint.h"
#include "xbeeConf.h"

#ifdef __cplusplus
extern "C" {
#endif

//#define XBEE_SEND_SERIAL

#define XBEE_CTS_PIN A3

#define XBEE_SUCCESS 0
#define XBEE_ERROR -1
#define XBEE_TO_ERR -2
#define XBEE_OVF -3

#define XBEE_TO_TIME 5000

int xbee_init();
int xbee_wait_connect(uint16_t timeout);
int xbee_sendAtForResponse(const char* at, char* resp, size_t resp_len);
int xbee_sendAtForConfig(const char* at, const char* arg);
int xbee_sendAtForOk(const char* at);
int xbee_send(const char* str);
int xbee_send_byte(uint8_t* c, size_t len);
int xbee_changeBR(); // TODO select baudrate



#ifdef __cplusplus
}
#endif

#endif // XBEE_H
