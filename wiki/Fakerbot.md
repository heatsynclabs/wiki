# The Makerbot is currently \[working\]

# About

The machine is called a FakerBot, because it's not quite a MakerBot, but there is a direct lineage. Since we didn't have access to a laser-cutter and we wanted to do it on the cheap, the frame was slightly redesigned by Corey so that it could be cut on a tablesaw from inch material. The tongue and groove construction was replaced with dado-cut slots. All holes were made with a 7/8" forstner bit, this allows them to take a skate board bearing (a paper shim is required) or anything else that we wanted through the use of adapter plates since we knew that mods were likely. Total cost of the enclosure was \$13 for a sheet of 1/4" (actually 5.2mm) Luan from Home Despot which provided enough material to make four FakerBots even though we only made one. MakerBot specified precision shafting for the X&Y axis which is completely unnecessary for a low-tech motion control system like this one. Drill rod was substituted for all linear shafting at a total cost of about \$3 which is another \$20 or \$30 reduction. Similarly, low-cost nylon bushings were substituted for the more expensive MakerBot spec'd parts.

The X and Y stages on the MakerBot are pretty good aside from being too tall, however the Z-stage is a horrible design. It is overly complex, wobbly, prone to jamming, etc. A replacement z-stage was designed by Corey with the goal of making Z simple and reliable:

**The following parts from the Makerbot design were removed:**

- \(1\) Belt
- \(8\) Bearings
- \(1\) Driving Pulley
- \(4\) Driven Pulleys
- \(2\) Idler Pulleys
- \(1\) Platform
- \(2\) Extruder Mounts (Dragons)
- \(4\) All-thread Rods
- \(4\) Driven nuts
- assorted screws and hardware

**That giant pile of hardware was replaced with:**

- \(1\) 1/4-20 Acme leadscrew
- \(1\) Antibacklash nut
- \(1\) shaft coupler
- \(1\) Cantilever arm (laser cut)
- \(1\) Linear rail with truck

**So an overall reduction from (27) functional components down to (5)!**

If you count every nut and screw the reduction is even greater, but you get the idea. The new Z-stage is a big improvement and has eleminated all of the jamming and wobbling problems that we had previously. It also looks better.

The extruder is Corey's design hosted at <http://www.thingiverse.com/thing:4579>. It is a clean-sheet of paper design that sprang from the frustration of dealing with the shortcomings of earlier designs. So far the CoreyStruder and its derivatives have been downloaded on Thingiverse over 250 times.

# Usage

## Get a file

The best source online for files is probably [Thingiverse](http://www.thingiverse.com/) If you're feeling up to it you can design your own file!! You need some sort of cad program. Some free possibilities include:

- [Google Sketchup](http://sketchup.google.com/)
- [Blender](http://www.blender.org)
- [OpenScad](http://openscad.org) - This is neat because its not googlehical, its a 3d compiler! Its a programming language.

Whatever you use you need to export or save to STL format

## Turn on

Make sure fakerbot is turned on (switch on power supply in back). The usb cable should be plugged in to your computer and the power supply should of course be plugged in.

Boot the laptop on the desk and open replicatorg which should automatically connect to the board. Otherwise there is a connect button.

## Warm up

We need to heat up the tip for ~5 minutes and extrude some plastic in order to get the machine operational.

Click the Control panel button (arrows) and set Motor Speed PWM to 255, target temp to 240. You must press enter or click your cursor outside of that input box in order to make this take effect. You're probably using a heated bed as well so set that temperature to 100. Note: You'll need to wait quite a while for this to reach its final temperature.

The machine should immediately begin moving towards temp (theres a temperature graph below, with red as your temperature) and reach it within a minute or two tops.

While this happens get comfortable with the X, Y and Z controls. They move for the distance set in the Jog Size column. Be careful not to jam the head into the table or the sides!

Move the extruder at least 10 or 20mm off the table. No need to be perfect(you can eyeball this). Go ahead and click forward on the motor control which is under the pinch wheel extruder tab. Watch the bearing and the gear on the extruder. Both should be turning. If not stop the motor and wait for the barrel to heat up more and or help the extruder along by twisting the filament.

By now you should be freely flowing plastic or you've got a blocked heater barrel or your pinch wheel setup is not adjusted properly. You should find help or start googling (try the makerbot and or fakerbot sites).

Run the plastic for at least a few minutes, making sure the plastic doesn't pile up and touch the tip.

## Zero machine

fakerbot doesn't know or care where it starts, you pick your zero before you print.

Set the X and Y so the extruder is right in the center. Put a piece of paper down on the platform and slowly move the toolhead down. As you get closer you should lower the jog size to make sure you don't crash into the bed. You want to have the toolhead touch the paper and have a bit a drag, but still be able to remove the paper.

When you think you have it, and your toolhead is in the middle of your x and y axis as well, press set zero. Finally move back up 20 in the z.

## Generate GCode

Open your stl file if you haven't already. Take a look at it in the preview window. It shouldn't be hovering off the ground or spilling outside of the box. Click the model tab, and then click the large "generate g code" button on the right. This generates your tool paths. Next select the coreybot profile and click 'Generate'. When this finishes youll see some code in your window.

## Print!

Your machine should still be at temperature from your previous setup. You'll want to run the plastic out again as the chamber can empty from ooze. Clear the nozzle, click to zero the z, and click 'Build' from the main makerbot menu.

The build may take a bit to start while it achieves optimal temperatures. Note where the stop button is on the control panel in case anything looks bad. Presumably the print will start, adhere to the bed well, and you can simply stick around until your print finishes.

# Status Updates

## 3/29/2010

We will hope to keep updates here. Most recently Jacob adjusted the z and one of the x/y reference voltages down to keep the motors coolor. So far everything seems fine. Will want to adjust the other X/Y voltage down as well if everything remains awesome. I've also restricted the build envelope a bit more to hopefully match the machine. Finally we had an issue with Z stage binding during prints. I found the feedrate was set to 1000 in the machines.xml file, and I've moved this down to 100. I'm sure we can bump this a bit eventually but for now its good.
