## Minutes

    owner: oliver
    cnc experts: greg, aaron
    this machine's experts: austin k, tim m, nate c, bought from joe
    other: jeff, alex, larry

    todo:
    buy new wrench for big clamping kit bolts (7/8")
    mod emergency switch to stop spindle (austin - weekends, after thu - deadline nov 3)
     - 24v relay, contactor, etc
    build lid for power supply
    run separate circuit for spindle?
    get ups for cnc computer
    figure out toolchange procedure (possibly run them as separate programs? common reference point issues. reference off the vice?)
    figure out how do display file inside mach3

    warnings:
    make sure head is above everything on bed
    if reset is flashing, undo e-stop?
    spindle motor takes awhile to stop!
    if the microcontroller board freezes, the kill switch may not work
    once the z axis is homed, don't adjust the manual knob

    info:
    cnc table and computer table can be redone (smaller)
    limit switches redone
     (mach3 doesn't know which switch has been hit! total stop)
     "soft limits" button on mach3
    gecko stepper motor controllers - custom controller board
    spindle speed controlled manually, via pulleys (run aluminum/wood/etc mainly instead of steel for simplicity?)
    lower link belt has reduced chatter (possibly due to bump in regular belt)
    return spindle to top in order to access drawbar

## Notes for Future CNC Mill Class

### TODO

- Contact MCC instructors or retirees? summer?
- Enhance safety signage and plastic shield

### Maintenance Responsibilities

- fixing problems
- answering questions
- engaging professionals, local students to help absorb the class and maintenance workload
- keeping accountability / ownership (card access control?)
- define default configurations, write scripts to help automate
- create a checklist for posting at the tool before usage

### Class Ideas

- prerequisite: mill and 3d printer
- demonstrate skill? make a gauge block?
- do we teach operator versus programmer versus designer? teach a combination of all three?
- must know how to read g-code to manually verify validity, or identify problems.
- identify workflow – solidworks/autocad, hsm express versus other cad/cambam. Mach3, CNC.
- possibly distribute materials to study – written – and then only do one-on-one instruction afterwards.
- there's a relatively high barrier to entry – cost, time, approval
- regular meetups might be a good idea to establish a CNC community, reach critical mass, and get community participation instead of offering a “class” per se
- option to outsource to MCC? We'd have to write up which classes to take
- create a class waiting/signup list?
- class sizes should be small, 1-3 people, and customized to each student. Probably about 10 hours of instruction per person.

### Class Outline

- feeds/speeds/flutes
- changing belts
- changing tools, setting up tools
- clamping/vice/mounting
- materials
- safety issues incl. Earplugs, e-stops, spindle stops, vices
- g-code/m-code (study simulator?)
- make a standardized part within spec – demo corners, radiuses, directions, up/down/drill/mill
- create g-code in cambam

` * save your cad files and g-code in millimeters for mach3`

- starting mach3
- go over each tool and run part – teach in three stages: explain/watch, instruct/do, do/verify
- touch off part, correct height, offset by appropriate value (quick change height issues)
- jog, change jog speed, change feed rate during cut, diagnose surface quality issues, diagnose diagnoal x/y issues
- touching off/zeroing

` * going to coords, jogging`\
` * don't change machine coordinates`

### Mill Notes (source material for class)

Mill needs:

- tool selection
- speeds and feeds
- mounting, locks, clamping, pulleys

Design notes:

- It's possible to change parameters in your CAD/CAM software to fine-tune the algorithm, i.e. to avoid using inefficient z-axis moves or routines.

CNC special notes:

- raising and lowering the head in the back with a lug wrench (23mm, written on the bolt)
- the bolts are poor quality and tend to stretch; we need to get decent replacement bolts
  - - Corey's had to hacksaw the bolt out in the past
- inside the top lid door is the chart that shows the pulley speeds (look at 60hz column, change the belts to the speeds you need)
  - you must loosen the wingnut on the back right and adjust the back-left bolts to loosen the motor so you can adjust pulleys.
  - you must also loosen the bolts up top to loosen the middle pulley (and re-tighten!)
- some belts are junk, causing poor surface finish and vibration. the B-33 belts from Grangier had visible imperfections in it. the shorter-length link belts (a-link-5) seem to induce higher-frequency vibrations which affect performance less.

<!-- -->

- There are normally bolts for locking down the axes, but that can strip out due to the CNC operation so the locks have been removed.
- All axes have limit switches, which improve safety; if the software is running right (which it usually does) then the mill will stop before running off the edge (and breaking things). For example Mach3 might freeze, which might cause the limit switches to be ignored (because they are implemented in software\*\*- Joe's CNC logic circuit board has separate grounds, which prevents the limit switches from stopping the motors both logically and physically.)
- Additionally, the red E-Stop button is software-only, it does not stop the spindle from spinning due to how our power is situated. It's a good idea to stop the X-Y motion with the E-stop first, and then shut down the spindle, to prevent breaking a bit. The spindle motor is stopped with the Fwd/Rev/Stop switch on the front-left of the machine. If in doubt, hit the E-Stop first so you don't throw something across the room.
  - - Ideally we'd built a box which stops all these things, or even better we'd use a VFD to control all items centrally.
    - Maybe in the short term we can build a kill switch in a more accessible location than the two existing switches.
- Finally, we need to cover the A/C power supply because it's currently open-air (with a warning sign.)

<!-- -->

- Use a vacuum or a chip brush to clean the chips as they come off.

<!-- -->

- Draw bar is 17mm. To tighten, hold the pulley while wrenching draw bar.
  - Recommend getting a torque wrench to gauge and avoid overtightening.

<!-- -->

- Make sure you only turn on the CNC after computer is already booted. Random parallel line noise may cause bad behavior.

<!-- -->

- Spindle motor is connected via red extension cord off to the left.

Vice:

- Screwless; it's got lugs underneath. Watch out that you're actually tightened against the material instead of tightened to the vice itself. Even things that appear tight can fly loose during milling.

CNC controller:

- Blinking light on turn-on waits 10 seconds to charge capacitors, to potentially avoid blowing a circuit breaker. Steppers are run via ~60 volts.

Mach3:

- It's possible to customize the menu, however we should keep it as generic as possible so it's easy to follow along with online guides.

<!-- -->

- This version has one setting file for the single machine. There's only one profile. You must run the "Mach3Mill" profile on the desktop because the main program profile doesn't have the correct settings for our machine.
- Normally you don't need to see debugging menu, but you can access it to easily see the various switch status.
- Each of the switches are wired together; any switch will stop motion. The machine knows which direction it's moving, if it hits while moving a certain direction
- Offsets menu is where you adjust tool offset. Read the manual for how to do the correct procedure. It stores the height at touch-off point, and it'll calculate the difference between touch-offs, and thus know how long the tools are. Make sure you touch off at the same tool/part. Make sure you don't adjust the tools, because you'll lose your calibration information.

<!-- -->

- MDI menu: you can manual data input and type g-code directly in; not recommended.
  - EXPERTS can quickly re-zero by inputting here, etc.
- If limit switches or E-Stop have been activated, the red RESET button blinks. Click that to enable steppers again. (The E-Stop button must be pulled back out.)

<!-- -->

- Jog mode is always on.
- To jog, use arrow keys. A pendant, controller, or USB keypad might be nice.
- To set tool height, an electronic probe at the spindle might be nice to automatically zero.
- Press tab to cycle to jog mode.
- Jog mode is currently set to 0.0010\*\*- be aware of this before jogging.
- Hold shift to jog at max, hold ctrl to jog at minimum speed.
- Soft limits are on; as you attempt to jog towards a limit switch, it'll slow down within 0.5 inch to avoid hitting a limit switch.
  - WARNING. IF YOU HIT RESET AT A STOP, IT IS POSSIBLE TO CONTINUE IN THE WRONG DIRECTION. PROCEED GINGERLY WHEN HITTING 'RESET.'

<!-- -->

- Click REF ALL HOME to re-zero all axes. Hold hand near E-Stop to quickly address any failures.
- Limit switches are accurate to about 3 thousandths when re-zeroing.
- You usually only need relative coordinates; Machine coordinates are mostly used for debugging.
- 5 inches Z, 5 inches Y, ~19 inches X.

When loading files:

- HSM express is pretty good about putting the tools needed at the top of the g-code.
- Wait until it selects the first tool, and then touch off the first tool. Then Mach3 will know the relative heights of the other pre-set tools.
- We could load up a macro where, when a tool change is encountered in the g-code, it'll run a routine so you can safely do a tool-change off to the side and then go back to the part once you're ready.

Before beginning:

- - Lay out the tools in the order you'll need them, and re-set all your tool height offsets in Mach3. NEVER ASSUME THEY ARE CORRECT! You don't want to go halfway through a part and realize the offset is wrong and part is ruined.
    - Touch off with any technique you like; gauge block, paper, di-chem, sharpie, etc\*\*- just be consistent between your tools.
    - Tools are not interchangeable! Just because Tool 5 and Tool 6 are both "the same", their z-height might not be the same!!!
    - Consider using nail polish to verify a bit hasn't been moved.
    - Some basic tools are \$30, be careful!
- Lubricate all lubrication points at the start of each job, and make sure you clean up everything when done. Double-check any chips on the backside.
- Spindle speed is not currently supported by our CNC. You have to set it by hand, the Mach3 setting isn't operable.

When beginning:

- There may be a softlimit warning; this is OK.
- Press the yellow FEED HOLD button to pause.

<!-- -->

- Tool changes are indicated by yellow flashing in the center of the screen. You can then use the arrow keys to change the tool and touch off the z-height. Whatever the height is, it'll then set the relative offsets of all other tools in memory.
- HSM express puts a nice comment saying exactly what tool to use (0.375 in 4-flute flat endmill)

<!-- -->

- G53 work offset may cause work to begin off to one side (see red line on table display at top-right of mach3 window)\*\*- proceed with caution.
- You may have to move the spindle and table to within the bounds of your program to avoid hitting limit switches. Hold hand over e-stop when beginning a file.

<!-- -->

- Watch g-code as it scrolls by to see what is happening (comments are good!)
- You can adjust the speed on the fly; 30% of what's specified, 130%, etc. HSM Express may make overly aggressive suggestions for our machine. See the FEED RATE pane.
- The table display at top right traces the path with the purple lines (notice the way the end of the line traces a lighter path.)

While running:

- Brush away chips
- Apply lubrication

Tool change:

- M1, T2 M6, tool description.
- You can simply touch off a tool and run with it for a simple operation. However with multiple tools, you don't want to touch off every time. In fact, you'll typically lose your reference point during running.
- See configuration, tool table. Each number, with name, and diameter. Height is the offset. (Part of Mach3 is in inches, part may be mm!)
- To create a tool height offset, go to offsets menu and enter the number in Tool Info. If using gauge block, set the height of it. Manually move the mill, and then click Set Tool Offset. Move on to new tools by typing in a new tool number. Make sure you click Save Tool at the end!
- Good idea to number each tool physically.
