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
