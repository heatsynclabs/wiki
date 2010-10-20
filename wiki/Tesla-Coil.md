# Project Synopsis

We would like to build a tesla coil for the mustache laser party (and beyond!)

## Design Summary

Traditional Basic Tesla Coil Configuration:\
![basictc.jpg](files/Basictc.jpg)

Our configuration:\
![Our_coil.png](files/Our_coil.png)

## Estimated Voltage Output

The energy in the cap bank is 1/2 \*C \* V^2 when the spark gap fires. For our capacitor bank and a 12KVRMS transformer that will be 0.5 \* 35nF \* 16968V^2 = 5joules Assuming that the energy is coupled 100% to the secondary, which it will not be, the voltage gain can be calculated using the same equation on the secondary capacitance; A 16" pumpkin has a free space capacitance of 45.607pf. Solving for voltage using 5 joules, we now get: E = 1/2 \*C \* V^2 5 = 1/2 \* 45.6pF\*V^2 V = 468,292 Volts

Ballpark estimate as electric field shape and coupling to everything in the room will cause shifts from the ideal case.

# Components

## Secondary Coil

  
A secondary wound on an 8" piece of green PVC is already available for use. Actual coil measurements are 6.25" diameter, 22" high, and approx 28turns per inch.

## Primary Coil (Harry)

  
A flat inductor used as a resonator within the LC tank circuit which is magnetically coupled to the secondary. Needs to be tuned with the main capacitor to the resonant frequency of the secondary LC circuit.

#### Build Notes

**Acquired Materials:**

::\*50' of 1/4" copper tubing (Lowes ~\$25).

::\*A large 20"x12" HDPE kitchen cutting board (Frys \$10)

::\*10' of 3/8" copper tube for strike rail (Lowes \$12)

::\*Medium battery clips for tapping point connection (Lowes \$3)

::\*2 ft square of plywood to mount. (Jasper)

::\*6 x 1/4" nylon nuts and bolts for strike rail (Lowes approx \$4.86)

::\*12 x zip ties

::\*Black spray paint

  
**Notes:** See [DeepFriedNeon](http://deepfriedneon.com/tesla_f_primary.html) Primary Coil Page for example with images.

<!-- -->

  
Cut the cutting board into six 20"x1" strips and drilled with 5/16" holes at .75" intervals for coil support rods.

<!-- -->

  
To wind the copper tube through the rods place the tubing on a flat surface and arrange the tube into an approximation of the coil first.Then working from the innermost end of the coil and the outermost hole of the rods, thread the rods around the tube. It's important to pay attention to the inner ring diameter. This method may expand the inner diameter as you turn.

<!-- -->

  
An additional series of holes were added to allow the creation of a strike rail to absorb any stray streamers that might hit the primary and damage the primary circuit components.

For the strike rail cut off excess length of support rods, leaving 1 extra hole, turn perpendicular to the rest of the rods, and drill a 3/8" hole for the copper tube. Attach these smaller rods to the main supports with nylon nuts and bolts through the extra hole in the end of the support rods.

<!-- -->

  
In the plywood: holes drilled at locations around the plywood to zip tie the support rods down, 1 hole for the primary connection, and a center hole for secondary coil ground wire.

<!-- -->

  
**Measurements:**Inner Diameter 11", Turn spacing .5", Number of Turns 10

## Transformer

<div style="text-indent:75px">

A 12KV 30mA neon sign transformer and an 12KV 60mA transformer are available for use.

#### Building Notes

We killed the 12KV 60mA NST after about 10 seconds of total use and the protection inductors shorted and caught fire. A very old unit, the tar is very dry. Its not surprising that it died. It was depotted and brought back to life. An oven re-heat killed the shorted coil again, though a tar-paper unwrap and fishing out some broken windings brought it back again. The output current was increased to ~123mA by knocking out some of the magnetic shunts and the whole thing was submerged in mineral oil. An additional "kick in the ass" by connecting to a 27nF capacitive load which revealed some weak spots in the form of a nice fat explosive arc. After some short circuit testing revealed small luminous discharges between adjacent winding layers, it was decided to sever the top winding layer as there appears to be a short to the core somewhere in the layer. The second winding layer was used as the output sacrificing a small amount of voltage. The transformer showed no corona or arcing either with the capacitive load nor under tesla coil conditions.

</div>

## Spark Gap (Harry)

<div style="text-indent:75px">

Discharges the energy stored in the main capacitor into the tank circuit. Forms the trigger for the relaxation oscillator once the capacitor charges to a specific voltage.

#### Materials needed

10x 1/2" to 1" copper pipe sections attached to a flat surface lain in parallel to form multiple small gaps of 1/8" to 1/4". Tuneable to using aligator clips to select different sections of pipe.

Aligator clips

**Note: Zach has supplied 2ft of 1/2" copper pipe.**

</div>

## Main Capacitor

<div style="text-indent:75px">

Stores energy until a certain voltage is reached, then discharges through the main spark gap and sets up a resonance between the primary coil.

An exponentially decaying RF waveform is produced until the energy is dissapated, recharging begins at the next 60Hz peak (discharge is therefore at 120Hz).

We already have a 30nF 35KV maxwell pulse capacitor designed for high frequency use.

</div>

## Protection Inductors (Jasper / Paul)

<div style="text-indent:75px">

Provides a high impedance to RF in order to contain the RF within the tank circuit. Allows 60hz to pass unimpeded.

#### Materials needed

Magnet wire and wooden dowel. Target 10mH. Separate winding layers with an insulator to keep arcs from forming between the input and the output (which will have kilovolt potential differences)

**Note: Will has supplied dowels of about 1/2" dia. left near the lathe, and Zach has magnet wire on the floor near the lathe. Zach has supplied 3ft of 5/8" dowel as well.**

  
  
question: how many winding layers of how many turns each?

  
As many side-by-side turns as you can fit in a 4 inch length, make three layers and measure the inductance. We will go from there!

#### Building Notes

The original inductors actually melted and caught fire during the first wave of 100% power testing for the tesla coil. 26 AWG magnetic wire per pound was \$18 and each roll has a total inductance of 163mH. These should make very nice chokes as long as they don't start arcing. If they do, they can be submerged in mineral oil or vaseline.

</div>

## Protection Capacitors (Jasper)

<div style="text-indent:75px">

These shunt any RF energy that passes the RF chokes to ground instead of injecting it into the transformer secondary.

#### Materials needed

Two Old English 800 beer bottles, salt water, AL foil. **Note: Jeremy Leung has supplied two OE 800 bottles**

</div>

## Protection Spark Gap (Jasper)

<div style="text-indent:75px">

A simple tunable spark gap consisting of a grounded middle section with a gap on either side to each leg of the transformer's differential output.

#### Materials needed

Three pieces of threaded rod, 1 to 2" long and polished as round as possible (to provide an even E field and predictable breakdown voltage).

Set each into a small wooden slat and use the threaded nature of the rods to tune the gaps. Or something like that.

  
  
Question: please elaborate on the construction/arrangement of the pieces, I.e. what do you mean by slat, how should the threading work, where do the rods go in relation to each other.

  
All three pieces will be end to end with a support in the center of each piece and a gap between the sections. The support will have a hole in it to match the rod,

so that it may be adjusted back and forth simply by rotating. It might make sense to center and tightly affix the centeral section.

**Note: Zach has supplied 1/4"-20 threaded rod.** **Note: Jasper has finished the protection spark gap as of 10/10/2010**

</div>

## Discharge Terminal (Paul)

<div style="text-indent:75px">

A smooth conductive surface to use as a capacitor in the LC secondary resonator assembly. A jack-O-electrons. Let's carve a freakin' pumpkin!

#### Materials needed

Pumpkin, knife, evil

</div>

# Reference

Wireless World - March 1995 - by Malcolm Watts\
<http://www.scribd.com/doc/12711857/tesla1>

How Tesla Coils Work by Chris from The Geek Group:\
<http://www.youtube.com/watch?v=W_7fgcnzhmw>

and

A Little Bit More In Depth on Resonance and Tesla Coil Basics by Chris:\
<http://www.youtube.com/watch?v=fT5_MmeSeDU&NR=1>
