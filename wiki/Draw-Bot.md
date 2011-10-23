## Concept

Initially, the plan was to duplicate the Der Kritzler; however, one of the design goals was affordability. Der Kritzler's toothed belts and pulleys add significant cost, but seem to deliver little advantage over a spooled line design.

Also, a goal is to co-locate the motors with the embedded controller and pen on the chassis. The thought is that the system will be simpler and cleaner.

Prototype plans call for an Arduino Uno and breadboard, with the final device as a custom PCB w/ ATMega328 or maybe ATTiny? Anyway, the PCB might be part of the chassis?

Also, we'd like to change the design so the DrawBot reads it's commands from an SD card instead of a command station.

## Bill of Materials

- Chassis/pen holder
  - custom part, will need to build in house
- 2 x suction cups (mount points for belts)
  - [10 lb suction cups?](http://www.mcmaster.com/#suction-cups/=e59uu8)
- 2 x stepper drivers
  - H Bridge power control [TI 1320](http://octopart.com/sn754410ne-texas+instruments-1320)
- 2 x stepper motors
  - [2.4 kg-cm 4 Wire NEMA 17 Stepper Motor / 42BYGH011](http://www.circuitspecialists.com/nema_17_stepper_motor_42bygh011.html)
- 1 x servo (for controlling pen?)
- 1 x Arduino
- Monofilament, 30# test?

### Deprecated

- 2 x stepper motors
  - go w/ 5mm shaft
  - need 40ish oz/in?
- 2 x toothed belt pulleys
  - go w/ 5mm shaft
- 20 ft toothed belt

## Motor Control

<http://arduino.cc/en/Reference/StepperBipolarCircuit>\
<http://www.arduino.cc/en/Tutorial/MotorKnob>

# Links

- [Der Kritzler](http://tinkerlog.com/2011/09/02/der-kritzler/)
  - [source](https://github.com/tinkerlog/Kritzler)
- [Project3, Drawbot](http://makezine.com/makeitlast/) Uses monofillament
- [Hector](http://hektor.ch/) -- the inspiration for DK
- [Gates Mectrol](http://www.gatesmectrol.com/mectrol/brochure.cfm?brochure=5199&location_id=4947) -- possible source for the Polyurethane (PU) timing belts (aka linear motion belt)
