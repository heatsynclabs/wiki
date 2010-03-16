## Summary

The most basic concept that can explain an evoked potential device is that of a warm crackling fire: The calming effect of sitting in front of the fireplace, watching the flames flicker, hearing the sound, and feeling the pulsing heat all in tune of the same rhythm. One of the reasons for this effect (not discounting the many other psychological associations, basic warmth, etc.) is [Evoked Potential](http://en.wikipedia.org/wiki/Evoked_potential), the natural tendency of the brain to fire in sync with its sensory surroundings. Odds are good that fire is flickering at a slow 4-12 Hz, the [Theta](http://en.wikipedia.org/wiki/Theta_wave) and [Alpha](http://en.wikipedia.org/wiki/Alpha_waves) ranges associated with calm relaxation.

The goal of this project is to build a device that can induce these brain wave states using flashing LEDs and pulsing audio. Many other examples of this concept are currently out in the world, but one example near to the hearts of many in the Maker community is the Make [Brain Machine](http://blog.makezine.com/archive/2008/12/the_brain_machine.html) by [Mitch Altman](http://www.tvbgone.com/cfe_mfaire.php).\
The design goals of this model are as follows:

1.  Soft wearable design suitable for sleeping such as a face mask.
2.  Self programmable using a simple computer interface.
3.  Multiple programs stored on device for easy selection and playback.
4.  Rechargeable batteries.
5.  Option to plug in your portable music player and play over the pulsing beats. (reduces effectiveness but more pleasurable)
6.  Electronics removable for washing.

The chosen platform for the electronics is the [Lilypad Arduino](http://www.arduino.cc/en/Main/ArduinoBoardLilyPad) microcontroller board. After some experimentation with the open source Mitch Altman design I estimate that the ATMega328 controller will be overkill for this design, but will afford many future enhancement possibilities.

© Designs and Code under this project distributed under Creative Commons 3.0 Attribution Share-Alike License\
<http://creativecommons.org/licenses/by-sa/3.0/>

## Materials

1 x LilyPad Arduino Mainboard [SparkFun DEV-09266](http://www.sparkfun.com/commerce/product_info.php?products_id=9266)\
1 x FTDI-based USB Arduino programmer (I have an Arduino [MiniUSB](http://www.arduino.cc/en/Main/MiniUSB) which works with some minor [adjustments](http://web.media.mit.edu/~leah/LilyPad/01_comp_attach_text2.html#soldering).)\
1 x LilyPad LiPower [SparkFun DEV-08786](http://www.sparkfun.com/commerce/product_info.php?products_id=8786)\
1 x LiPoly Charger - Single Cell 3.7-7V Input [SparkFun PRT-00726](http://www.sparkfun.com/commerce/product_info.php?products_id=726)\
1 x Polymer Lithium Ion Batteries - 1000mAh [SparkFun PRT-00339](http://www.sparkfun.com/commerce/product_info.php?products_id=339)\
1 x Spool of Conductive Thread - 234/34 4ply [SparkFun DEV-08549](http://www.sparkfun.com/commerce/product_info.php?products_id=8549)\
1 x Surface Mount Navigation Switch [SparkFun COM-08184](http://www.sparkfun.com/commerce/product_info.php?products_id=8184)\
8 x Triple Output SMD LED RGB [SparkFun COM-07844](http://www.sparkfun.com/commerce/product_info.php?products_id=7844)\
2-8 x 4.7K SMD resistors (LEDs)\
2 x 2.7K SMD resistors (Audio)\
4 x 10K resistors (audio mixer)\
2 x 1μF SMD Capacitors\
1 x Stereo Headphone Jack [RadioShack 274-249](http://www.radioshack.com/product/index.jsp?productId=2103452)\
1 x Cheap set of headphones\
1 x Eye mask ([Make Your Own](http://www.ehow.com/video_4404865_making-pattern-sewing-sleeping-mask.html))\

## Design

[EPEM Source Code](EPEM-Source-Code)\
[EPEM Schematic](EPEM-Schematic)\

## Links

[LilyPad Home](http://web.media.mit.edu/~leah/LilyPad/index.html)\
[Arduino Forum: How to implement a soft-reset button](http://www.arduino.cc/cgi-bin/yabb2/YaBB.pl?num=1260037835)\
[BrainWave Machines](http://www.hackcanada.com/homegrown/wetware/brainwave/)\
