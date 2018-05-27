/*
@file: xbeeConf.h

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
int xbee_getOpPAN(char* sdc, uint8_t* sdb);

int xbee_isCoordinator();
int xbee_setCoordinator(int c);

int xbee_wr();
int xbee_ac();

#ifdef __cplusplus
}
#endif


// TODO baudrate



#endif // XBEE_CONF_H
