This page contains developers notes on the L3G4200D 3 axis gyro

A lot of the information of this page comes from the datasheets, but it has been interrupted and filtered to how it can and should be used on this project.

this units provides dps (degrees per seconds) as well as temperature

## Registers

### WHO_AM_I (0x0F)

writing to register 0x0f should return the value 0xD3 11010011(binary) D3(hex) or 211 (dec)

### Register 4 (0x23)

control register

this is how we are configuring the device\
BDU BLE FS1 FS0 --- ST1 ST0 SIM\
0 0 1 1 0 0 0 0
