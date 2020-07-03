The software for the laser cutter is usable, but certainly not a best case scenario. The software is tied to the motherboard of the machine which is OEM'ed from another company. Our machine has the [MPC6515 Motion Controller](files/MPC6515_Manual-2.pdf) from Leetro, as do most of the laser machines out of China apparently. This board is tied to the LaserCut software (and Corel and Autocad drivers which utilize it) This is btw why all laser cutters out of China use this LaserCut software. Another popular machine using this combo is [Rabbit USA](http://www.rabbitlaserusa.com/) who attempt to do support and documentation in english making them a good resource.

## to add

- colors work
- layers don't
- only s2p letters

### LaserCut Software

- Top right menu with layers (colors): Each layer can cut or engrave, with its own speed, power, output/hidden, and number of times to run.
- In the cut options menu (when you double click on speed or power) the blower options are not applicable.
- The Up/Down buttons let you sequence cuts/engraves in the order you want.
- The Compute button allows you to then use the Simulate or Estimate Work Time buttons. Make sure nothing is selected beforehand in order to be accurate.
- X, Y, and Z control buttons operate as expected. Datum and Z Datum also work.
- Never push the Laser button on the computer. Once you push it, the laser will fire until you push the stop button on the physical machine. The computer can't stop the laser from firing.
- Run Box and Clip Box outline the outer rectangle of your project. Run is with the laser off, Clip is with the laser on.
- The Pause button has the same problem as the machine; never use it, as the laser will fire.
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

# Alternate Solutions to Lasercut/MCPC6515

## Closed Source

Solustan have created a [system driver](http://www.solustan.com/linkmotion_and_leetro.php) for the laser freeing it from lasercut allowing you to print from basically anything. They charge \$400 but [feedback](http://www.sawmillcreek.org/showthread.php?77344-Converting-a-Rabbit-user-interface) in 2008 was pretty rough for their solution.

We contacted them on July 18th and they say they've basically given up on that driver and are instead about to release a new driver and a whole new motherboard for driving the machine for around \$400-500. We're in talks with to them about evaluating this solution.

## New Open Source Engineering

- Think Haus [created](http://www.thinkhaus.org/2010/06/24/howto-turn-a-cheap-chinese-laser-engraver-into-a-pretty-good-laser-cutter-2/) their own stepper driver board and are using linuxcnc to drive it with a custom inkscape plugin!
- [Open source Laser Interface Driver](http://www.boingboing.net/2011/07/11/diana-engs-laser-cut.html)

## Reverse Engineering

[Hackspace](http://www.hackspace.org.uk) are [reverse engineering](http://wiki.hackspace.org.uk/wiki/Projects/RELaserSoftware) their machine and the MOL document spec. They were more active back in Feb of 2011 but I see a few commits recently.

# Manuals

- [MPC6515 Motion Controller](files/MPC6515_Manual-2.pdf)

---
*Categories: [Laser](Category-Laser)*
