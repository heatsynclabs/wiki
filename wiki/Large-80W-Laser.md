# Overview

This is the main quick guide for the large laser cutter (aka PewPew9000 for reasons I'm sure the old-timers can explain). It will likely get rearranged, but in phases.

## Size

The largest material that will fit in the laser is 48" x 32" but the cutting area is smaller.

## What you can cut

These lists are not exhaustive. If your material is not on either list, ask first!

- See the [Laser Material Guidelines](Laser-Material-Guidelines) for a list of materials and common speed and power settings.

## Operation

### Turn on the laser

1.  Turn on the machine
    1.  Turn on the switch
    2.  be sure to disengage the E-STOP
    3.  Verify the following are up and running
        1.  Laser Cutter
        2.  Chiller
        3.  Exhaust fan
        4.  Air compressor

### Start the software

1.  Start the [LaserCut 5.3](LaserCut-5.3)
    1.  Communication Problem?
        1.  Click download to regain communication
        2.  Save work
        3.  Exit LaserCut
        4.  Restart LaserCut
    2.  “SoftDog” dongle errors
        1.  These are usually random
        2.  retry

### Load your files

1.  Create your design
    1.  For more detailed discussion, checkout [Inkscape](Inkscape)
2.  Shapes, Text, Graphics
    1.  Use [LaserCut 5.3](LaserCut-5.3) for simple work, or
    2.  Import from Adobe Illustractor, [Inkscape](Inkscape), Corel, AutoCad, etc
3.  Assign objects to layers then values for:
    1.  Speed
    2.  Power
    3.  Frequency
    4.  Output
4.  Set drawing origin (Choose intelligently based on your design)
5.  Click Calculate
6.  Simulate (this can help you spot problems)

### Prepare the material

1.  Lower the table so that material doesn't hit the laser head
    1.  Position material in center of bed (use squaring blocks if necessary)
    2.  Jog laser head over to the material using computer or keypad
    3.  Set the Z-axis
        1.  Focus will be 6mm below air cone (this is what you use the little "puck" for)
        2.  Place the puck near, but not under, the laser and on the material
        3.  Move the bed up and down and try to get the puck to slide under the laser
            1.  Do **not** simply put the puck on the material and raise the table until it hits the laser. That's how you'll crash it. Do it to the side and try to slide it in so that head crash isn't as likely.
        4.  **If you run the head through the table hit the E-STOP and see [Laser Cutter Emergency Guidelines](Laser-Cutter-Emergency-Guidelines)**

### Send your design to the laser

1.  Download the design to the laser cutter
    1.  Click “Download” then “Download Current”
    2.  Close the download window

### Make sure your design fits on your material

1.  Check design boundary
    1.  Click "Run Box" to outline the extent of your design area without the laser powering on
        1.  Don't use Clip Box or it will power on the laser

### Safety

1.  Remember your [Laser Cutter Safety Training](Laser-Cutter-Safety-Training)
    1.  Locate water spray bottle
    2.  Locate fire extinguisher
    3.  Most flare-ups will self-extinguish when the laser stops
    4.  Stay at the laser while it is running. If you must leave, someone else trained must take your place.
    5.  If you need to suspend your job quickly, raise the hood. Cutting will resume when you lower the hood.
    6.  Due to software bugs, do not use the Pause or Stop buttons on either the machine or software

### Fire in the hole!

1.  Start the Laser
    1.  Click 'Start'
    2.  If you must suspend you can open the hood or click 'Start' again.
    3.  Avoid using "Stop" or "Pause" if possible.

### Finishing

1.  Finished?
    1.  Wait for cooldown and exhaust to clear
        1.  Temperature display should be below 25°C
    2.  Turn off the key lock switch
2.  Verify the following are off:
    1.  1.  Laser Cutter
        2.  Chiller
        3.  Exhaust
        4.  Air Compressor

#### Clean up the machine

1.  Rails
    1.  Clean each rails with a rag and alcohol. Gloves are recommended.
2.  Scraps
3.  Drawer
4.  Hood

#### Document!

1.  Add your results to [logbook](https://docs.google.com/forms/d/1ld4T9pDXP6uqZbYmlebe9SxATHcP436kMobnhSQEKPI/viewform). These are visible [here](https://docs.google.com/spreadsheet/ccc?key=0AoBMPvlNCqvldHl5SERwRHVjN09wRHEtODZzd2RXNWc&usp=sharing)
2.  Log any issues. Redtag device if necessary.

---
*Categories: [Laser](Category-Laser)*
