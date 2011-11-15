Software Design should be layout out here.

Should have an initial design that outlines the major components, and how they inter communicate.

In order to fully describe a motion status of an object, 6 variables are needed, 3 linear coordinate: x, y, z, and 3 angular coordinate α, β, γ. accelerometer can measure the x y z and gyro can measure the α, β, γ, so 6 variables are all measured by the 2 elements, you get the exact status.

## Implementation Considerations

- code will be implemented in c++
- application will be single threaded, design may or mayn't take this into consideration.
- 

## Main Loop

- Sensor Reading
- Sensor combing
- Position Control
- Telemetry & Datalogging

sensor the first three items will be run all the time, and the last will only be executed if there is enough time. We will put in ,some kind of check to ensure that telemetry is going out sometime, even if the timers are being overrun.
