I will try to keep track of my project and certifications on this page!

## Projects

### Current

List my current projects. Order can be somewhat random.

### Done

#### Laser cut 3d box for my previous LED project

**Date:** 2022-01-28

**Materials:**

- Scrap of 3mm plywood from the lab

**Detail:**

- Speed: 10mm/s
- Power: 50%

**What I learned:**

- I wanted something quickly because we were getting close to the end of public time, but next time I should definitely take into consideration the kerf

#### LED lighting for my office shelf

**Started:** 2022-12-31

**Ended:** 2023-01-21

**Materials:**

- WS2812B LED (~2.5m) 30led/m
- NodeMCU (ESP8266) on which I flashed WLED
- 5v 4A power supply
- A capacitor (can't remember the capacitance)
- Some wire

**Detail:**

- I've cut 5 strips of 15led, soldered them together (using ~50cm between each)
- Flashed WLED on my NodeMCU
- The power supply:
  - feeds the NodeMCU on VIN and GND. The capacitor is placed on this connection. The idea is that if I turned from dim green to bright white, the power supply might be slow to adjust and the NodeMCU might reset (lose power). But with the capacitor, this one will "discharge", providing power to the NodeMCU while the power supply adjust. Thanks David for the tip!
  - feeds the LED Strip

In theory, I would need a maximum of 4.5A=75led \* 0.06A (60mA) for the strips, that's the theoretical maximum for full-brightness white. But I didn't have one handy, so I'll probably set WLED to use max 3.5A, I believe that'll give enough brightness and it leaves 0.5A for my NodeMCU which I believe is enough.

**What I learned:**

- everything above :-) Soldering was.. difficult. Everything seems very small haha.

## Certifications

2023-09-01: Laser cutting certification by Eric

## Templates

### Project

` ==== Name ====`\
` `\
` '''Started:''' 2022-12-31`\
` `\
` '''Ended:''' current`\
` `\
` '''Materials:'''`\
` `\
` * A`\
` * B`\
` * C`\
` `\
` '''Detail:'''`\
` `\
` * give`\
` * some`\
` * details`\
` ** sublist`\
` `\
` '''What I learned:'''`\
` `\
` * list`
