**<span style="color: green  ">The Ultimaker 2 is working!... </span>**

**<span style="color:#009900">The <s>Coocheer</s> Choocher (Prusa i3 clone) is working!</span>**

**<span style="color:#DD0000">The Ultimaker 1 is Currently Out of Commission =(</span>**

# I WANT TO USE THE UM2

**Are you familiar with the Cura workflow? Skip down to [\#Common Issues](#common-issues)**

The Ultimaker 2 is our wonderful fancy Dutch 3D printer. Due to increasing globalization and lost traditional values, the UM2, much like their shoes, is no longer made of wood as it used to be.

We are currently using Cura for our slicing, because its quick and easy to use. If you get more into 3d printing you will find that using another program, such as Repetier host, will give you more control over the parameters of the slicing than Cura does.

## Getting your STL

If you're downloading your model from [Thingiverse](http://thingiverse.com), it'll probably have an STL file available. If they don't, match their file types with the sections below, or [ask the internet](http://google.com).

If you have your own file say from Solidworks or Autodesk Inventor, make sure you export it as an .stl. you can then load it onto a flash drive and bring it over to the 3d printing station computer. Another way to move the file to the 3d printing computer from your own is using the shared file network that we have at the lab. If you are going to use the shared file network i would recommend making yourself a folder in this location \\\files\shared\users. Once you are logged onto the Wifi you can export your files onto our shared network by exporting them to \\\files\shared\users\\"your name here". using the file networking can save you a lot of time if you are editing your file and checking it on the 3d printing computer.

The Ultimaker slicing programming (Cura) will only import STL files currently. Getting STLs out of your program of choice depends on your program of choice. If yours is not documented [ask the internet](http://google.com) and then document it here.

Place your downloaded STL on the HSL 3D Printing Station Computer in the Downloads/ folder, in a directory with Your Name. Files floating around freely in Downloads will be mercilessly deleted.

### OpensCAD (\*.scad) (0\$)

OpenSCAD natively exports STL files after building. Construct your model, and then go to the Design menu and hit "Compile and Render (CGAL)". After that, hit the "Export as STL" option in that same menu.

## Slicing with cura

Slicing is what turns the STL model (consisting of a list of the triangles in the model), into a list of commands that the printer understands. This list is called [GCode](http://linuxcnc.org/docs/html/gcode/overview.html).

- Open the model in Cura by double clicking on it
- Here you can rotate, move, and resize the model,
  - Your model will print as it appears in the build preview. Make sure that

it is centered and on the build platform, laying flat, using the move, rotate and resize tools.

- Cura has many helpful view modes, available in the upper right corner of the

screen

- - 'Layers' allows you to preview how it will print, layer by layer, showing

shells, fill, support, etc. in different colors

- - 'Overhang' highlights overhanging areas in red, suggesting the need for

support

- - 'Normal' allows for resizing and rotating the object
- Click the "Save Toolpath" button (floppy disk icon) to save the gcode to the

SD card.

### Adjusting print profile settings

If your just printing a bracket or something simple with no overhangs, the stock settings will work fine. However If your printing something like a skeleton or a small model of a person, you will probably need some custom settings to make it work right. A good rule of thumb is anything that is organic in shape or has overhangs will need some custom cura settings to work.

This is an example of the type of 3d print that will need custom settings.

![isis-one-desktop-3d-printer-5.jpg](files/Isis-one-desktop-3d-printer-5.jpg)\
If those defaults don't make sense to you for some reason (You're printing a structural piece for example and need a stronger infill) you can adjust the settings, but realize that will probably affect print time and final weight and will make Moheeb cry.

If you do modify the print settings make sure you switch back to 'quick print' when you are done.

## 3D Printing Station Donations

- While we dont charge to use our printer(s), some people choose to donate a

few dollars whenever they print things so the lab can get more plastic for the printer and maintain it. You can also donate a roll of 3mm filament of any type!

## Getting GCode on the Printer

- Pull the SD card out of the front of the UM2 and put it in

the computer

- In Cura, Click the "Save Toolpath" button (floppy disk icon) to save the

gcode to the SD card.

- Press the eject (up arrow) that just popped up at the bottom of the screen to eject the SD card
- Put the SD card back in to the printer.

## Print

We use hairspray to make PLA stick to the bed, and gluestick to make ABS stick to the bed.

PLEASE DO NOT USE ABS JUICE AS THIS MAKES A DISASTER AREA OF A MESS

- Push the button to get in to the menu
- Navigate to "SD Card Menu" and push the button
- Navigate to your print and push the button

The machine will zero itself and begin heating the machine for the print. When it has reached temperature it will begin printing.

## Oh noes!

When something goes wrong on your print, don't panic, even if the heated nozzle is crashing in to the Heated glass build platform.

### Stop the Print

If it's not a "HOLY SHIT THE MACHINE IS BROKEN/REPRODUCING" issue, i.e. your print messed up or the hot end stopped extruding, you can just stop the print.

- Scroll the button to 'Tune'
- Scroll the button to "Abort" and press the knob

Your print will stop within 30 seconds and you can peel your failed print off.

### KILL IT WITH FIRE

If something is going haywire, i.e. the machine has generated a small mushroom cloud, is crashing uncontrollably, or has started to make another 3d printer on its own, shut the machine off using the switch on the right side and move the bed down, by spinning the large screw under the bed counter clockwise, then you can push the head out of the way by hand. If the machine is not in order to print after this, don't worry unless its trying to make another printer, please make a note, place it on the bed, and inform PBorJ ASAP so we can get the printer back in working order again.

## Cleaning Up

Now my favourite part, when you're done, clean up the build area, deposit any excess plastic into a trashcan, it was once believed you could reuse the plastic and make it into new filament, this is not true unfortunately. Do three cartwheels and clap your shoes together in the air. Make sure the machine is turned off, and you're done.

## Common Issues

- If you cut the filament flat when loading it, it will sometimes catch at the exit of the bowden tube. To avoid this, please cut the filament at an angle, to make a shape that looks like a sharpened pencil. This will guide the filament around the shoulder and reduce your frustration.
- If you pause before you abort, the filament will retract twice. This is a known bug.
  - If this happens, you can either start a print and wait for the filament to come out, knowing you will need to abort said print and start it again WITHOUT pausing first
  - Or you can just reload the filament.

## If the machine doesn't go goodly

1.  Read the above common issues first
2.  Reload the filament once, twice, even maybe three times if you think it might help
    1.  Make sure to check for filament breakage. If the filament breaks inside the bowden tube, see next step
3.  At this point, please email PBnJ (contact info is on the sign)

- The machine is rarely actually clogged. Please \*\*do not\*\* take any actions beyond reloading the filament.
- DO NOT REMOVE THE HOTEND SCREWS
- DO NOT ATTEMPT TO INSERT SMALL OBJECTS INTO THE NOZZLE (EVER)
