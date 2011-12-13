# Project Synopsis

CURRENT STATUS: In pieces, check out [Fakerbot](Fakerbot) instead.

We've been trying to brainstorm a good project idea that we can focus on to present to ASU for the \$2000 grant we're aiming for. One project that would definitely put us on the map and would also allow us to reach out to the local community would be procuring a Rapid-Prototyping device. The RepRap project is a prime example of one whose initial creator's intention was not only to make a device that was as inexpensive as possible but also one that can replicate itself. Seeing the cost benefits analysis, as well as, the vast improvements with version II of this device(Mendel) we're thinking about going with that design.

--Update - ASU did not fund us so we did it ourselves. Take that establishment.

## Design Summary

Check out the RepRap main site here:\
<http://reprap.org/bin/view/Main/WebHome>

They've got a great video/mini documentary explaining the background of the RepRap concept including an interview with the designer:\
<http://vimeo.com/5202148>

Check out the below link for a good video summary of what the "Mendel" is:\
<http://objects.reprap.org/wiki/Mendel_Overview>

## Construction

The RepRap team has done a pretty good job of ensuring that the design specs are open source so that the world wide community can participate in building and even bettering what they've started.

Below is their how to section on building a "Mendel" version of the RepRap:\
<http://objects.reprap.org/wiki/How_to_make_RepRap_Version_II_%22Mendel%22>

## Budget

This is a tally of costs so far, and providers used. You can see the original estimate on the rep rap site of \$520 was rather low. With all the various shipping charges (plus we got 15lbs of plastic) we will likely almost double this. They also do not mention the impossibility of finding the prototyped/printed parts for the rep rap. They are approximately 100 hours to print and thus we've found few rep rap/makerbot owners willing or able to print those parts for us. These parts can also be rapid prototyped for around \$1500 dollars which is slightly more than the advertised \$20 dollars.

### Located Parts

|  |  |  |
|----|----|----|
| **Item** | **US cost** | **Notes** |
| Bearings | \$76.14 shipped | TheBigBearingStore.com |
| Fasteners | 109.20 | Mcmaster.com |
| Belt | see Fasteners | Mcmaster.com |
| Extruder parts(machined) | \$32.40 shipped | reifsnyderb on rep rap forums |
| Motors | 302.85 shipped | Store.Makerbot.com |
| Plastic Stock | See motors | Store.Makerbot.com |
| PCBs | See Motors | Makerbot |
| Electronics | 169.16 | Parted out from Digikey, Allied,Arrow,Newark and Mouser |
| Thick sheet MDF, between 4mm and 6mm and at least 42cmx40cm | 57.15 | Lowes |
| Bar (smooth rod) BZP NOT BMS A2 Steel even better - at least 3m - M8 (8mm diameter) | See Thick Sheet | Lowes |
| Studding (threaded rod) -BZP M8 (8mm diameter) at least 9 meters | See Thick Sheet | Lowes |
| epoxy,ties | See Thick Sheet | Lowes |
| silicon grease, kapton tape | ~33.00 | Grainger |
| pcb strip board, heatshrink tubing, | n/a | Scrap |
| 12 PC or laptop Power Supply | n/a | Multiple units donated by various members |
| 5v FTDI | 19.04 shipped | Sparkfun |
| Extruder parts - 6-ohm length of fibreglass-insulated nichrome wire, | .50cents a foot | <http://store.makerbot.com/nichrome-wire-31-ga.html> |
| Extruder thermistor | 4.06 | <http://www.circuitspecialists.com/prod.itml/icOid/6136> |
| 2pin .1inch pitch connectors to replace rj45s | ~10 | Newark.com EC100F-2 CE100F22-2 |
| Thin sheet less than 2mm thick and at least 8cmx5cm | Free Scrap | Beer, Soda, Energy Drink Can |
| **Total** | **\$\>794.26** | '''''' |

## NEEDED PARTS

These are the parts we still need. Perhaps you can help?

|  |  |  |
|----|----|----|
| **Item** | **US cost** | **Notes** |
| [Printed Parts](Phoenix-RepRap-Printed-Parts) | Free From Local Printer Community | Laser Cut, Rapid Prototyped, or Printed? |
| Misc - oil, box cutter blades, more? | ? | Lowes, Home Depot |
| **Total** | **?** |  |
|  |  |  |

## Build Log

Sorting parts into 'kits' (whole lotta parts to sort) Soldering - 2 or 3 stations probably (12 boards of various complexity)

- Dip soldering and SMD soldering
- Toaster oven reflow

Testing Wiring

- ribbon data
- power

Mechanical construction

- Extruder building
- X, Y and Z
- Rods cut to length

## Status

Initial Build Done(ish)

- There's one electronics/firmware/software problem we've been watching the entire build. Our Z axis has always moved... oddly. When running Z through the X or Y axis it actuates properly, but the Z output from the motherboard makes the motor move oddly and only in one direction.--Swapped for another board which is working fine, still haven't determined problem on old board though

  
*Z-axis output issue fixed, now it just needs calibration.* --[Geekner](User-Geekner) 08:46, 10 March 2010 (UTC)

- We're having some jerky movements in the Z mechanical construction. We believe we have diagnosed this down to issues with metric and standard conversions on a certain z axis nut. --works well enough for now
- The Extruder motor board didn't appear to be able to drive the motor (and lots of thermistor problems)
  - Have more powerful motor hooked up now but the pinch wheel is such a pain and the software is so bad I don't l know if its any better.
  - Also have hooked up 'underpowered' motor through pololu A4983 and have seen it occasionally move in rep rap software, but it keeps crashing so not tested.
  - Moving back to rep g the more powerful stepper seems to work now but isn't extruding. Pinch wheel problems or still underpowered?(altered rep g to take stepper)
  - Havent yet found pinouts on the extruder board for repg firmware (different from rep rap firmware) to utilize the pololu stepper for use in rep g firmware

<strong>Try to print again in rep g, wait for David's design now that we have functioning stepper in repg, rewrite software to not crash and or try other extruder board to see if its more stable?, find pinouts on extruder board for stepper and direction pins (on rep rap they come off the mobo as sda and scl)</strong>

## Insufficiencies in Rep Rap Documentation

### Instruction issues

- Extruder page lists 5leds, but you actualyl need 9. (were 9 in partlist it would seem) Led1 and Led9 are actually named Power and Debug also.
- Need better documentation on Mendel modifications to build process. We accidentally did a lot of soldering we had to desolder.
- All mechanical construction steps don't actually give you any instructions, simply parts lists and completed pictures

### Problems in Schematics

- Motherboard schematic claims 100u for c6, should be 10u as in documentation wiki

### Missing from partslist

- 4 conductor ribbon for the extruder
- Thermistor for extruder
- 2 color 2 conductor 8amp guaged wire for power
- XLR connectors --which we're not using so thats fine
- We were short a length of 10 conductor ribbon
- Extruder lists 180ohm 1206 resistor as not required... I think? Or is it?
- Partslist doesn't list any of the mendel mobo modification parts --3v Voltage Regulator 78L33 or electrolytic cap - we don't need anyway as we went with a sparkfun 5v ftdi breakout which matches a breakout on the mobo and gives us our 3.3v and 5v both I believe

### Unnecessary on partslist

- 30 watt resistor - 30w-5-nd (digikey)
- SPDT Slide Switch - as atx header isnt used on mobo anymore, switch doesn't actually switch anything
- atx headers
- rj45

## Making Improvements

### What's Out There?

- Thingiverse Combined .stl Files: [<http://www.thingiverse.com/thing:1883>](http://www.thingiverse.com/thing:1883)
- Dremel Attachment: [<http://blog.makezine.com/archive/2010/02/dremel_attachment_for_makerbot.html>](http://blog.makezine.com/archive/2010/02/dremel_attachment_for_makerbot.html)

### New Ideas

- Be Able To Make It's Own Circuit Boards
- Means to Recycle Plastic
- Print on a finer scale
- Increase Print Speed
- Hot Plate for Print Consistency
- Larger Print Area
