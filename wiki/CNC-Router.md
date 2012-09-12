The last time we cleaned out the upstairs, I happened upon a treasure trove of servo motors, drivers, linear bearings, etc. that would be perfect for a CNC Router. We have the parts for 2 of the 3 axis, and 3 AC servo motors (but only two servo controllers). This is excellent because those are all normally VERY expensive pieces of hardware. AC servos are beefy, efficient, and can put out a constant torque over a broad range of speeds. These will be able to make the router fly at high feed rates while keeping excellent precision.

## Stuff we have on hand

Electronics:

- 1x Klinger CC1.2.A2 2 axis stepper motor controller
- 2x Reliance Electric HR2000 AC servo controllers
  - These were origionally sold with motors to match, which we do not have.
  - Also note that these require a 3 phase power supply

Motors:

- Kollmorgan Silverline AC Motors:
  - - These were origionally sold bundled with a servo controller, which we do not have.
  - H-232-C-0000 with LPRTP40 rotary encoder
  - H-342-C-0200 with E3-1000-315-I rotary encoder
  - H-344-L0802 with (probably) a LPRTP40 rotary encoder
- EC Electro-craft Corp. permanent magnet servo motor-tachometer
  - Part \# 0576.01.012
- 2x Motak motors with 90 degree gearboxes
  - 30:1 gear ratio
  - 24V
  - part 47-003901-OO1112-103

Rotary Encoders:

- Largish one with P/N 77676-163
- smaller one with P/N 77822-291

Hardware:

- 1x Z axis stage with two sliding units, and a space for a leadscrew
- 2x Linear ball bearings for 3/4" rod
- 1x 3/4" rod, about 4 feet long for use with above linear bearings
- 2x end caps for the 3/4" rod
- 3 bearing blocks with ball bearings and axels
- 1x Electronic break
  - This is normally closed, but opens to allow rotation when given 12V

## What we still need

- Linear bearings and rails for the third axis.
  - The best option is probably a MakerSlide: <http://makerslide.com/> The MakerSlide is MUCH cheaper than any other linear movement system I have seen in my research, that can be expected to maintain any reasonable precision.
- A table
  - Aluminum or steel with T-slots is what most mills use. Could be a bit expensive for a router this size however.
- A frame
  - Extruded aluminum with T-slots is the solution here. It is very sturdy and we can get parts to create just about any frame you could imagine. They are super-versatile. And not that expensive either.
- Linear movement system
  - I think timing belts would be the most practical solution. They are reinforced with fiberglass or steel, so they don't stretch much at all under load. And they are very cheap.
  - Leadscrews are precise, but extremely expensive, espectially in lengths of several feet as would be required here
  - For one axis we could use a rack and pinion movement. Though how accurate this would be is uncertain.
- Spindle
  - Chinese high frequency spindles are about \$300 each plus an inverter for \$200 or so. Some are liquid cooled. But we could get a 1500+ watt (~2 horsepower) motor that could spin at 24k rpm. That would be a very nice things to have indeed!
  - The cheaper option would be to use a standard wood router.

## TO-DO

- The first thing that really needs to be done is to get the servos and the servo controllers working together.
- The other first thing to do is create solidworks models of all the parts we have, and then design the rest of the machine around those in Solidworks. When that design is fleshed out and finalized, we can order parts and assemble!
- Next comes setting up a computer to control the machine.
