### Safety

- Fire, Inhalation, Pinch, Electrical, and Eye/Laser Hazards
- HeatSync certified adults only, no exceptions.
- Safety zone around laser, keep people out.
- Location of fire extinguisher and water bottle.
- The Emergency Stop button will always stop everything. Memorize its location.
- Pressing the laser button will always fire the laser even if the lid is up.
- Pressing pause and then lifting the lid will resume, and fire the laser. If you want to truly pause, simply lift the lid. Never press pause, because leaving the machine paused is actually leaving the laser armed and will fire on anyone who lifts the lid.
- The Z axis has no limit switches and is a pinch hazard. It will keep going and not stop, stripping the screws and crashing the head into the bed. Keep hands free of the unit when anyone is near the control panel or computer.

### Control Panel

- Main thing to remember is that the speed and the power are in reference to what you set them to in your file. If it's at 100% on the control panel, that's 100% of whatever you've set on the computer. I.e. you can slow it down or decrease it on the panel, not increase it.
- The Datum button is "Home". It'll bring the laser back to the top right based on the limit switches. (the "laser origin" not the "program origin" which is the bottom left.)
- To "Home" to the z-axis (bed) enter Z mode by pressing the center Z button. You can then press the Datum button to home or the up/down arrows to adjust the bed. To exit, press the Z button again.
- The Laser button is always live and will fire at 100% power for as long as you hold the button. Treat it carefully and never push it with the lid up to avoid eye damage.
- The Stop button will stop any cutting from happening while in the main menu. There are two modes where the Stop button will not function immediately: when in Z-axis mode, or if you've got a "soft stop" error (i.e. you've gone off the edge, corrected the error, and continue to cut, but still made a mistake and wish to stop, you'll have to press Esc and then Stop.) In other words, clear any errors on the screen before cutting.
- The Test button moves the laser along the rectangular perimeter of your project.
- To run a project, highlight it under the File menu option and press the the Start button. Beware of pressing the pause button, because if you open the lid it will automatically resume and cause a hazardous situation for your eyes.
- The Esc button will exit all screens with one exception, which is the Z-axis mode. To exit the Z-axis mode, simply press the Z-axis button again.
- The Menu button should not be used. All of the settings on the screen will not actually do anything; change all your settings within the computer program. Don't go hunting around in the menu or other options, because you'll put the machine in a weird mode.
- To move the laser, press Esc to ensure nothing on the screen is highlighted. Then, press the arrow keys.

<!-- -->

- The temperature display on the laser is set up in order to work properly with the chiller. In the event that the chiller fails and the system heats up, this will shut down the system and prevent damage to the laser. It's normal to see temperatures below 30', and you can ignore any blinking or alarm lights on the temperature display. If the temperature gets above 30' it will shut down the system.

### Turn Off / Turn On

- To turn on, get key from lockbox.
  - Plug in the big extension cord (twist before pulling)
  - The chiller and ventilation blower will have power supplied
  - When the laser key is turned, the laser will boot up and the air assist compressor will start.
  - Do not play with the electrical wiring; don't plug anything into the wall, everything is 220v volt.
- To turn off, wait for 5 minutes to let the laser tube cool, and then turn off the key and unplug the big twist extension cord.
  - Place key in lockbox.

### File Design

- Place any engrave ("raster/etch") projects towards the middle of the bed. Placing an engraving project along the edge of the bed will result in gouging the laser against the side of the bed because the laser will overrun a bit in engrave mode.

### Computer

- Ensure you're using the correct config file so the laser knows how big its bed is and doesn't crash into the side.

### LaserCut Software

- Top right menu with layers (colors): Each layer can cut or engrave, with its own speed, power, output/hidden, and number of times to run.
- In the cut options menu (when you double click on speed or power) the blower options are not applicable.
- The Up/Down buttons let you sequence cuts/engraves in the order you want.
- The Compute button allows you to then use the Simulate or Estimate Work Time buttons. Make sure nothing is selected beforehand in order to be accurate.
- X, Y, and Z control buttons operate as expected. Datum and Z Datum also work.
- Never push the Laser button on the computer. Once you push it, the laser will fire until you push the stop button on the physical machine. The computer can't stop the laser from firing.
- Run Box and Clip Box outline the outer rectangle of your project. Run is with the laser off, Clip is with the laser on.
- The Pause button has the same problem as the machine; never use it, as the laser will fire as soon as the lid is opened.
- The Start button starts cutting the file currently displayed on the laser's display screen.
- The Stop button, unlike on the machine, only restarts the cut. It goes back to the program's origin and begins again. To stop, press the stop button on the machine or the Emergency Stop button in an emergency.
- The DownLoad button opens the file manager.
  - Don't press the Download CFG. It will replace the laser's config and possibly mess it up.
  - The Download File takes the current config on the laser and saves it to your computer.
  - The Download Current takes the project currently open and transfers it to the laser, ready for cutting.
  - The Export File button gives you a .MOL file which can be read directly by the laser via a USB storage device.
  - The Export CFG button allows you to save the computer's config file elsewhere.
  - The Export file button lets you save a project file from the laser elsewhere.
  - The Del and Del All buttons delete files from the laser.

### Maintenance

- Store spares inside left panel, DO NOT TOUCH \*\* contact laser team if
- Every use
  - Write in the logfile
  - Empty the bucket and clean up any debris
  - Clean the residue from the slats and from the z-limit switch with rubbing alcohol
- Every 30 days, trained people should:
  - Water
  - Chiller air filters (both sides, just wash them)
  - Laser air filter
