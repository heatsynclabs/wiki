The software for the laser cutter is usable, but certainly not a best case scenario. The software is tied to the motherboard of the machine which is OEM'ed from another company. Our machine has the MPC6515 Motion Controller from Leetro, as do most of the laser machines out of china apparently. This board is tied to the LaserCut software (and Corel and Autocad drivers which utilize it) This is btw why all laser cutters out of China use this LaserCut software. Another popular machine using this combo is [Rabbit USA](http://www.rabbitlaserusa.com/) who attempt to do support and documentation in english making them a good resource.

# Alternate Solutions to Lasercut/MCPC6515

## Closed Source

Solustan have created a [system driver](http://www.solustan.com/linkmotion_and_leetro.php) for the laser freeing it from lasercut allowing you to print from basically anything. They charge \$400 but [feedback](http://www.sawmillcreek.org/showthread.php?77344-Converting-a-Rabbit-user-interface) in 2008 was pretty rough for their solution.

We contacted them on July 18th and they say they've basically given up on that driver and are instead about to release a new driver and a whole new motherboard for driving the machine for around \$400-500. We're in talks with to them about evaluating this solution.

## New Open Source Engineering

- Think Haus [created](http://www.thinkhaus.org/2010/06/24/howto-turn-a-cheap-chinese-laser-engraver-into-a-pretty-good-laser-cutter-2/) their own stepper driver board and are using linuxcnc to drive it with a custom inkscape plugin!
- [Open source Laser Interface Driver](http://www.boingboing.net/2011/07/11/diana-engs-laser-cut.html)

## Reverse Engineering

\[www.hackspace.org.uk Hackspace\] are [reverse engineering](http://wiki.hackspace.org.uk/wiki/Projects/RELaserSoftware) their machine and the MOL document spec. They were more active back in Feb of 2011 but I see a few commits recently.

---
*Categories: [Laser](Category-Laser)*
