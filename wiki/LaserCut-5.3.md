The software for the laser cutter is usable, but certainly not a best case scenario. The software is tied to the motherboard of the machine which is OEM'ed from another company. Our machine has the [MPC6515 Motion Controller](files/MPC6515_Manual-2.pdf) from Leetro, as do most of the laser machines out of China apparently. This board is tied to the LaserCut software (and Corel and Autocad drivers which utilize it) This is btw why all laser cutters out of China use this LaserCut software. Another popular machine using this combo is [Rabbit USA](http://www.rabbitlaserusa.com/) who attempt to do support and documentation in english making them a good resource.

### LaserCut Software

- Top right menu with layers (colors): Each layer can cut or engrave, with its own speed, power, output/hidden, and number of times to run.
- In the cut options menu (when you double click on speed or power) the blower options are not applicable.
- The Up/Down buttons let you sequence cuts/engraves in the order you want.
- The Compute button allows you to then use the Simulate or Estimate Work Time buttons. Make sure nothing is selected beforehand in order to be accurate.
- X, Y, and Z control buttons operate as expected. Datum and Z Datum also work.
- Never push the Laser button on the computer. Once you push it, the laser will fire until you push the stop button on the physical machine. The computer can't stop the laser from firing.
- Run Box and Clip Box outline the outer rectangle of your project. Run is with the laser off, Clip is with the laser on.
- The Pause button has the same problem as the machine; never use it, as the laser will fire.
- The Start button starts cutting the file that has been downloaded to the laser. (This may differ from what is displayed in the editor!)
- The Stop button, unlike on the machine, only restarts the cut. It goes back to the program's origin and begins again. To stop, press the stop button on the machine or the Emergency Stop button in an emergency.
- The DownLoad button opens the file manager.
  - Don't press the Download CFG. It will replace the laser's config and possibly mess it up.
  - The Download File takes the current config on the laser and saves it to your computer.
  - The Download Current takes the project currently open and transfers it to the laser, ready for cutting.
  - The Export File button gives you a .MOL file which can be read directly by the laser via a USB storage device.
  - The Export CFG button allows you to save the computer's config file elsewhere.
  - The Export file button lets you save a project file from the laser elsewhere.
  - The Del and Del All buttons delete files from the laser.

# Manuals

- [MPC6515 Motion Controller](files/MPC6515_Manual-2.pdf)

---
*Categories: [Laser](Category-Laser)*
