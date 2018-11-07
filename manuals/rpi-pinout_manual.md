# Raspberry PI 2 model B pinout

## PinOut
```shell-session:pinout
$ pinout
,--------------------------------.
| <5V>oooooooooooooooo J8     +====
| <3V3>ooooooooooooooo        | USB
|                             +====
|      Pi Model 2B V1.1          |
|      +----+                 +====
| |D|  |SoC |                 | USB
| |S|  |    |                 +====
| |I|  +----+                    |
|                   |C|     +======
|                   |S|     |   Net
| pwr        |HDMI| |I||A|  +======
`-| |--------|    |----|V|-------'

Revision           : a01041
SoC                : BCM2836
RAM                : 1024Mb
Storage            : MicroSD
USB ports          : 4 (excluding power)
Ethernet ports     : 1
Wi-fi              : False
Bluetooth          : False
Camera ports (CSI) : 1
Display ports (DSI): 1

J8:
   3V3  (1) (2)  5V    
 GPIO2  (3) (4)  5V    
 GPIO3  (5) (6)  GND   
 GPIO4  (7) (8)  GPIO14
   GND  (9) (10) GPIO15
GPIO17 (11) (12) GPIO18
GPIO27 (13) (14) GND   
GPIO22 (15) (16) GPIO23
   3V3 (17) (18) GPIO24
GPIO10 (19) (20) GND   
 GPIO9 (21) (22) GPIO25
GPIO11 (23) (24) GPIO8
   GND (25) (26) GPIO7
 GPIO0 (27) (28) GPIO1
 GPIO5 (29) (30) GND   
 GPIO6 (31) (32) GPIO12
GPIO13 (33) (34) GND   
GPIO19 (35) (36) GPIO16
GPIO26 (37) (38) GPIO20
   GND (39) (40) GPIO21

For further information, please refer to https://pinout.xyz/
```
![rpi-pinout](raspberry-pi-pinout.png)
reference: [https://pinout.xyz/](https://pinout.xyz/)

## 今回使用するpin
- LED
    - describe_fire: 4
    - describe_fire_truck: 17
    - describe_explosion: 18
- Motor
    - move_conveyor: 5
    - destroy_coveyor: 6
    - remove_stopper: 12
    - describe_explosion: 13
    - launch_balls: 16
- Button
    - first_button: 27
    - second_button: 22
