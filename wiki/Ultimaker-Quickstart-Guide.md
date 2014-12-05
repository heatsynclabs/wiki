**The Ultimaker is Currently Running at 100%**

The Ultimaker is our wonderful fancy Dutch 3D printer. Much like their shoes, the Dutch chose to build the 3D printer using a wood frame. Using the Ultimaker isn't entirely difficult, it just takes a quick walkthrough to get it running.

We are currently using Cura for our slicing, because its quick and easy to use. If you get more into 3d printing you will find that using Slic3r through Repetier host will give you more control over the parameters of the slicing than Cura.

## Getting your STL

If you're downloading your model from [Thingiverse](http://thingiverse.com), it'll probably have an STL file available. If they don't, match their file types with the sections below, or [ask the internet](http://google.com).

If you have your own file say from Solidworks or Autodesk Inventor, make sure you export it as an .stl. you can then load it onto a flash drive and bring it over to the 3d printing station computer. Another way to move the file to the 3d printing computer from your own is using the shared file network that we have at the lab. If you are going to use the shared file network i would recommend making yourself a folder in this location \\\files\shared\users. Once you are logged onto the Wifi you can export your files onto our shared network by exporting them to \\\files\shared\users\\"your name here". using the file networking can save you a lot of time if you are editing your file and checking it on the 3d printing computer.

The Ultimaker slicing programming (Cura) will only import STL files currently. Getting STLs out of your program of choice depends on your program of choice. If yours is not documented [ask the internet](http://google.com) and then document it here.

Place your downloaded STL on the HSL 3D Printing Station Computer in the Downloads/ folder, in a directory with Your Name. Files floating around freely in Downloads will be mercilessly deleted.

### OpensCAD (\*.scad) (0\$)

OpenSCAD natively exports STL files after building. Construct your model, and then go to the Design menu and hit "Compile and Render (CGAL)". After that, hit the "Export as STL" option in that same menu.

## Slicing

Slicing is what turns the STL model (consisting of a list of the triangles in the model), into a list of commands that the printer understands. This list is called [GCode](http://linuxcnc.org/docs/html/gcode/overview.html).

- Open the model in Cura by double clicking on it
- Here you can rotate, move, and resize the model,
  - Your model will print as it appears in the build preview. Make sure that

it is centered and on the build platform, laying flat, using the move, rotate and resize tools.

- - If your print has crazy overhangs or intricate details, it may **not**

print well on our machine. :(

- Select 'Switch to full settings' on the tools menu. This allows you to select

the print profile for the filament you are using

- Select 'Open Profile' on the 'File' menu and navigate

to the '\\\files\shared\Cura Profiles' folder. Choose the \*standard.ini file

- Cura has many helpful view modes, available in the upper right corner of the

screen

- - 'Layers' allows you to preview how it will print, layer by layer, showing

shells, fill, support, etc. in different colors

- - 'Overhang' highlights overhanging areas in red, suggesting the need for

support

- - 'Normal' allows for resizing and rotating the object

<!-- -->

- Click the "Save Toolpath" button (floppy disk icon) to save the gcode to the

SD card.

### Adjusting print profile settings

If your just printing a bracket or something simple with no overhangs, the stock settings will work fine. However If your printing something like a skeleton or a small model of a person, you will probably need some custom settings to make it work right. A good rule of thumb is anything that is organic in shape or has overhangs will need some custom cura settings to work.

If those defaults don't make sense to you for some reason (You're printing a structural piece for example and need a stronger infill) you can adjust the settings, but realize that will probably affect print time and final weight and will make Moheeb cry.

If you do modify the print settings make sure you reload the standard.ini profile once you are done so other people dont waste their time using your settings which are probably really crappy and wont work.

**DO NOT OVERWRITE DEFAULT PROFILES!**

Please name your profile in the following format: TMP \$YOURNAME \$REMINDER or \$YOURNAME \$REMINDER, where reminder is something like 10% or hollow infill, or something like that so that you don't forget. Temporary profiles may be deleted when I am cleaning the machine up, UM profiles will stay.

## 3D Printing Station Donations

- While we dont charge to use the ultimaker or the TAZ, some people choose to donate a

few dollars whenever they print things so the lab can get more plastic for the printer and maintain it.

## Getting GCode on the Printer

**CURRENTLY THE SD CARD ON THE 3D PRINTING STATION COMPUTER IS NOT WORKING, FOR NOW YOU NEED TO FIND ANOTHER WAY TO GET THE GCODE TO THE PRINTER, USING A USB STICK TO TRANSFER TO ANOTHER COMPUTER WITH A WORKING SD CARD IS THE BEST WAY**

- Pull the SD card out of the left side of the UltiController and put it in

the computer

- If it doesn't pop up just pull it out and try again until it works for you.
- In Cura, Click the "Save Toolpath" button (floppy disk icon) to save the

gcode to the SD card.

- Put the SD card back in to the printer.

Our UltiMaker has an [UltiController](https://shop.ultimaker.com/en/parts-and-upgrades/ulticontroller-ultipanel.html) installed on it, a marvel of Dutch engineering which allows you to, using the amazing power of LCD displays and Secure Digital cards control the printer without the use of a PC computer. While this may sound limiting, there are huge benefits to printing this way:

- Because the USB serial link is slower, you cannot get the printer to do

crazy things like print at 700% speed

- Prints can pause or hang due to high load on the computer causing an

interrupt in USB serial communications. This usually ends up with nasty globs of plastic on the model or, commonly, print failures.

Seriously follow this, don't use USB serial. It's just as easy and less painful.

## Print

Make sure the build platform is clean, if necessary use the alcohol spray to clean the surface. Also if the glass is loose the small black clips need to be slid over it using some tweezers, the glass only fits one way.

The UltiController has a scroll knob on the left end, it's also a button.

- Push the button to get in to the menu
- Navigate to "SD Card Menu" and push the button
- Navigate to your print and push the button

The machine will zero itself and begin heating the machine for the print. When it has reached temperature it will begin printing.

## Oh noes!

When something goes wrong on your print, don't panic, even if the heated nozzle is crashing in to the Heated glass build platform.

### Stop the Print

If it's not a "HOLY SHIT THE MACHINE IS BROKEN/REPRODUCING" issue, i.e. your print messed up or the hot end stopped extruding, you can just stop the print.

- Press the button to enter the device menu
- Scroll the button all the way down to "STOP PRINT" and press the knob

Your print will stop within 30 seconds and you can home The Nozzle and peel your failed print off.

### KILL IT WITH FIRE

If something is going haywire, i.e. the machine has generated a small mushroom cloud, is crashing uncontrollably, or has started to make another 3d printer on its own, shut the machine off using the switch on the right side and move the bed down, by spinning the large screw under the bed counter clockwise, then you can push the head out of the way by hand. If the machine is not in order to print after this, don't worry unless its trying to make another printer, please make a note on it and inform [User:Dfarms](User-Dfarms) ASAP so we can get the printer back in working order again.

## Cleaning Up

Now my favourite part, when you're done, clean up the build area, deposit any excess plastic into a trashcan, it was once believed you could reuse the plastic and make it into new filament, this is not true unfortunately. Do three cartwheels and clap your shoes together in the air. Make sure the machine is turned off, and you're done.

### Logging your Work (WIP)

Much like the laser cutter, we like to track usage of the Ultimaker for assessing wear and tear and statistics on prints. Please fill out the log when you are finished by clicking the "3D Printer Log" icon on the desktop.

This includes tracking failed prints, just record how far the machine got before it failed, and the reason why.

# But Wait!

There's more! Take a look at the [Ultimaker](Ultimaker) page for more information about the printer and how you can get more involved in 3D printing at HeatSync Labs.
