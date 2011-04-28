- using existing, or a new, board to make lights on makerbot heated build platform also provide information display on readiness of platform.

Would be interesting to know 4 states

- at room temperature
- rising
- at build temperature
- falling

This could be as many as 4 leds (ughhh)

Also interesting concept, how about telling temperature with the platform lights. IE temp of 32C is two or 3 leds on... all the way up to max temp is 3/4 to all leds on. Only need maybe even one color for this, but much more control logic to be able to control all leds individually unless theres a better way...

# Existing Design

5 connections on heated bed

- 12v power for platform
- 12v gnd
- 5v power to therm
- gnd to therm
- therm signal

## Utilize extruder

The extruder has a plenty powerful processor to do this small calculation. We would have to send another signal line or something over to platform to do signaling. Also we'd have to patch makerbot software and/or hope to one day be included. Will be harder to 'productize' the innovation as well as people might buy our kit, but they wont continually patch the software.

- single signal line to board
- control a mux?
- can i embed this signal in power somehow?

if switch to thermocouple reduce 2 wires. This only really makes sense if Im not doing something locally on heated board as Id need 5v + - for a micro anyway.

# Keep all alterations on heated board

This means no code changes which is good. I have to calc the temp, or approxamate, or even just a + or - delta at the board and control the lights.

`Just pull the 5,gnd,signal and put some very small micro (tiny44 or something) and duplicate temps inside of it.`

- 95 means hot
- \<95 (and rising) means yellow
- \<95 and falling means?
- room temp (under 30c?) blue? white?

Or better really just want comparator for rising, lowering, maintaining. If were maintaining at bottom (room temp) or maintaining towards top (at temp)
