/*
@file: irCam.h

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

#ifndef IR_CAM_H
#define IR_CAM_H

#include <stdint.h>

#define IR_ADDR 0xB0
#define IR_SLAVE (IR_ADDR >> 1)

#ifdef __cplusplus
extern "C" {
#endif

void irCam_init();
void irCam_read(uint16_t* points);

#ifdef __cplusplus
}
#endif

#endif // IR_CAM_H

// TODO check if everything is rigth
