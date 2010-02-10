# Project Synopsis

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
| silicon grease, kapton tape | ~47.36 | Grainger |
| pcb strip board, heatshrink tubing, | n/a | Scrap |
| 12 PC or laptop Power Supply | n/a | Multiple units donated by various members |
| 5v FTDI |  | Sparkfun |
| Extruder parts - 6-ohm length of fibreglass-insulated nichrome wire, |  | <http://store.makerbot.com/nichrome-wire-31-ga.html> |
| **Total** | **\$\>794.26** | '''''' |

## NEEDED PARTS

These are the parts we still need. Perhaps you can help?

|  |  |  |
|----|----|----|
| **Item** | **US cost** | **Notes** |
| Thin sheet less than 2mm thick and at least 8cmx5cm | ? | Beer can? |
| [Printed Parts](Phoenix-RepRap-Printed-Parts) | ? | Laser Cut, Rapid Prototyped, or Printed? |
| Misc - oil, box cutter blades, more? | ? | Lowes, Home Depot |
| **Total** | **?** | '''''' |

## Build Plan

Sorting parts into 'kits' (whole lotta parts to sort) Soldering - 2 or 3 stations probably (12 boards of various complexity) Testing Extruder building - going to be dependent on us getting prototyped parts in time Mechanical construction - going to be dependent on us getting prototyped parts in time

## Status

- \>60% prototyped parts constructed--shooting for completion or at least a subset we can start construction on for next meeting
- Extruder construction begun
- Need to heat gun reflow solder the micro on one extruder controller
- Mobo currently not passing e testing, all other boards waiting on this

## Problems found in Rep Rap Instructions

- Extruder lists 180ohm 1206 resistor as not required... I think? Or is it?
- Extruder page lists 5leds, but you actualyl need 9. (were 9 in partlist it would seem) Led1 and Led9 are actually named Power and Debug also.
- Need better documentation on Mendel modifications to build process. We accidentally did a lot of soldering we had to desolder.
- Partslist doesn't list any of the mendel modification parts
- For Mobo modifications - 3v Voltage Regulator 78L33 or electrolytic cap for - we don't need anyway as we went with a sparkfun 5v ftdi breakout which matches a breakout on the mobo and gives us our 3.3v and 5v both I believe
- Partlist doesn't list the need for 2 color 2 conductor 8amp guaged wire for power or the 3pin xlr connectors (and the xlr, as far as I can tell, aren't even needed anymore--we have molex on steppers and a terminal block on motherboard)
- We were short a length of 10 conductor ribbon, short on partslist?
- Motherboard schematic claims 100u for c6, should be 10u as in documentation wiki
- Unnecessary components on the rep rap sheet: (listed by vendor IDs not manufacturer IDs)
  - 30w-5-nd (digikey)
  - 10sp001 mouser
  - 538-26-48-1245 mouser
  - 538-39-29-3206 mouser
  - 538-08-52-0072 mouser
  - 970-0313 allied
  - rj45's ?
