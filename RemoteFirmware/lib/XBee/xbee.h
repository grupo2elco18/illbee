/*
@file: xbee.h

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
