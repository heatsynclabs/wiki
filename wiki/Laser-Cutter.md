Notice: These documentations are being depreciated for [Laser Cutter Quick Guide](Laser-Cutter-Quick-Guide).

- Training is required to use the laser. Laser classes are by-request, just come to the lab and fill out the form to register (it's an icon on the bench computer called Laser Class Registration.)

### Documentation

- [Exlas_Machine_Manual.pdf](files/Exlas_Machine_Manual.pdf)
  *Exlas_Machine_Manual.pdf*
- [Laser_Cutter_Training_Slides.pdf](files/Laser_Cutter_Training_Slides.pdf)
  *Laser_Cutter_Training_Slides.pdf*
- [LaserCut5.3_Manual.pdf](files/LaserCut5.3_Manual.pdf)
  *LaserCut5.3_Manual.pdf*
- [MPC6515_User_Manual.pdf](files/MPC6515_User_Manual.pdf)
  *MPC6515_User_Manual.pdf*
- [Aligning the Beam](http://www.rabbitlaserusa.com/Manuals/BeamAlignment.html)

**BUT WAIT THERE'S MORE**

- [Acrylic_Cutting_Tips.pdf](files/Acrylic_Cutting_Tips.pdf)
  *Acrylic_Cutting_Tips.pdf*
- [Raster_to_Vector_in_Corel.pdf](files/Raster_to_Vector_in_Corel.pdf)
  *Raster_to_Vector_in_Corel.pdf*
- [Vector_Files_in_Corel.pdf](files/Vector_Files_in_Corel.pdf)
  *Vector_Files_in_Corel.pdf*
- [Recommended_Speed_Settings.pdf](files/Recommended_Speed_Settings.pdf)
  *Recommended_Speed_Settings.pdf*

### Safety

- Fire, Inhalation, Pinch, Electrical, and Eye/Laser Hazards
- HeatSync certified adults only, no exceptions.
- Safety zone around laser, keep people out.
- Location of fire extinguisher and water bottle.
- The Emergency Stop button will always stop everything. It turns off the machine's power. Memorize its location.
- Pressing the laser button will always fire the laser.
- If you want to pause a cut, simply lift the lid. Never press pause, because the machine will resume the job if the lid is lifted for some reason.
- The Z axis has no limit switches and is a pinch hazard. It will keep going and not stop, stripping the screws and crashing the head into the bed. Keep hands free of the unit when anyone is near the control panel or computer.

### Control Panel

- Main thing to remember is that the speed and the power are in reference to what you set them to in your file. If it's at 100% on the control panel, that's 100% of whatever you've set on the computer. I.e. you can slow it down or decrease it on the panel, not increase it.
- The Datum button is "Home". It'll bring the laser back to the top right based on the limit switches. (the "laser origin" not the "program origin" which is the bottom left.)
- To "Home" to the z-axis (bed) enter Z mode by pressing the center Z button. You can then press the Datum button to home or the up/down arrows to adjust the bed. To exit, press the Z button again.
- The Laser button is always live and will fire at 100% power for as long as you hold the button. Treat it carefully and never push it with the lid up.
- The Stop button will stop any cutting from happening while in the main menu. There are two modes where the Stop button will not function immediately: when in Z-axis mode, or if you've got a "soft stop" error (i.e. you've gone off the edge, corrected the error, and continue to cut, but still made a mistake and wish to stop, you'll have to press Esc and then Stop.) In other words, clear any errors on the screen before cutting.
- The Test button moves the laser along the rectangular perimeter of your project.
- To run a project, highlight it under the File menu option and press the the Start button. Beware of pressing the pause button, because if you open the lid it will automatically resume and cause a hazardous situation for your eyes.
- The Esc button will exit all screens with one exception, which is the Z-axis mode. To exit the Z-axis mode, simply press the Z-axis button again.
- The Menu button should not be used. All of the settings on the screen will not actually do anything; change all your settings within the computer program. Don't go hunting around in the menu or other options, because you'll put the machine in a weird mode.
- To move the laser, press Esc to ensure nothing on the screen is highlighted. Then, press the arrow keys.

<!-- -->

- The temperature display on the laser is set up in order to work properly with the chiller. In the event that the chiller fails and the system heats up, this will shut down the system and prevent damage to the laser. It's normal to see temperatures below 30', and you can ignore any blinking or alarm lights on the temperature display. If the temperature gets above 30' it will shut down the system.

### Turn Off / Turn On

- To turn on, get the key.
  - Plug in the big extension cord (twist before pulling)
  - The chiller and ventilation blower will have power supplied
  - When the laser key is turned, the laser will boot up and the air assist compressor will start. If not, twist the emergency stop button.
  - Do not play with the electrical wiring; don't plug anything into the wall, everything is 220v volt.
- To turn off, wait for 5 minutes to let the laser tube cool, and then turn off the key and unplug the big twist extension cord.
  - Place key back in its place.

### File Design

- Place any engrave ("raster/etch") projects towards the middle of the bed. Placing an engraving project along the edge of the bed will result in gouging the laser against the side of the bed because the laser will overrun a bit in engrave mode.
- To engrave, you'll likely want to invert the image unless un-engraved areas might actually be darker that engraved areas. Normally, engraving darkens the material which is why you'll want to invert.
- **To get accurate sizing from raster files:** You'll also want to resize to 254dpi / 100 dots per centimeter / 10 dots per millimeter. LaserCut will interpret a 254-pixel image as being 1 inch.
- In Photoshop, you can convert an image to 2-bit (actually probably 1-bit) mode by resizing to your desired inches at 254dpi (100 dots per centimeter.) Then go to Image\>Mode\>Grayscale and Image\>Mode\>Bitmap. Choose Diffusion Dither. Save as a .bmp and import into the laser, it should import at the correct inch dimensions you set in Photoshop. If it whines about being 2-bit bitmap, you likely didn't do the bitmap mode correctly and it's 1 or 2 bits of color stored in a 32-bit format.

### Computer

- Ensure you're using the correct config file so the laser knows how big its bed is and doesn't crash into the side.

### Maintenance

- Store spare parts inside left panel. DO NOT TOUCH. Contact laser team to do maintenance or repairs.
- Every use
  - Write in the logfile
  - Empty the bucket and clean up any debris
  - Clean the residue from the slats and from the z-limit switch with rubbing alcohol
- Every 30 days, trained people should:
  - Water
  - Chiller air filters (both sides, just wash them)
  - Laser air filter
- If there are major problems with the machine:
  - Place a lockout tag or out of order note on machine
  - Log the problem in the machine log
  - Contact a laser team member

---
*Categories: [Laser](Category-Laser)*
