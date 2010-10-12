To compliment our 3D printer(Rep Rap)that we created it would be great if we had our very own affordable and accurate 3D scanning setup. At the moment we can create 3D models in software and print them or we can download pre-made models from websites like instructables.com. Having a 3D scanner would speed up the replication process for us if we have an object already.

## Method

There is a community surrounding some free 3D scanner software called David LaserScanner. We'll acquire a web cam and laser level. And then install the David 3D scanner software to do a scan of a small object.

Once getting a basic functional setup we'll move towards commercial methods of doing multi-scans at the same time and combine the results after processing to ensure that we have the least amount of noise possible and the cleanest scan from the cheapest materials.

## Budget

Goal is to have the ultimate cost for this project to be less than commercially available products. The lowest that I've found so far is:

**NextEngine** - \$2,995

or

**David 3D Package w/ Camera** - circa \$1,418.67

## Trials

### First Scan Setup

Tried my first scan using the following materials:

- Free Version of David LaserScanner Software
- MacBook Pro Intel Core 2 Duo 2.6GHz
- Built-in iSight - USB 2.0, Plastic Lense, Fixed Focus, CMOS Active pixel sensor instead of a CCD(Apple has moved to using a sensor capable of 1280x1024 pixels, but when accessed using provided APIs, the image is re-sampled to 640x480 pixels.) Frame Rate? Possibly 15fps-30fps
- Black and Decker Laser Level Held Horizontally- <http://www.blackanddecker.com/ProductGuide/Product-Details.aspx?ProductID=10968> (Class II Red Laser - Maximum Output \<1mW at 630nm-670nm) - \$17.47
- 90 degree calibration corner using the .pdf printout included with David Laser Scanner and a Poster Board

**Conclusion** - This was successful and surprisingly satisfying seeing the results pop up on the screen immediately. Scanned one side of a spray bottle and it was distinguishable in the resulting render. The precision and detail wasn't that great with hand holding the laser. Skipping around a bit. I would like to fix that in the second revision. Also, the laser is not diffracted as well as I would like. The laser line varies from a bright spot to very thin line. Looks like the background poster board could be made larger to fill the full frame of the camera's field of vision. The tape I used to tape down the calibration points ended up being detected by the software as calibration points. I need the tape not to show up in the frame or to use alternative adhesives. Lastly, I will need to play with controlled lighting in the scanning environment so that we don't have any stray shadows that take away from the scan. Possibly an enclosed environment? Possibly up the quality with an external firewire camera.

### Second Scan Setup

With this revision I would like to attempt to create a rotational base for the objects that we want to scan. This time I can set up the laser in a fixed setup scanning vertically and taking out the user error of the scanning. With the steps from the motor we should get finer detail. For the laser itself I am upgrading to a 10mw Green Laser that will be diffracted through a line generator lens or a stem from a wine glass. Apparently green shows up better on camera CCDs(need to look a bit more into optics to verify this as I know green is at the peak of the optical spectrum for human beings). Finally, as the object we are scanning is no longer static we will need to take video instead of still shots and then stitch the frames together to create our object. The use of white paint on objects being scanned seems to heighten the quality of the scan as well.

**Equipment Sources:**

- 5mw Green(532nm) Laser - <http://www.dealextreme.com/details.dx/sku.91>
- Parts to create something similar to this commercial base - <http://ortery.com/products/photocapture360-360-degree-photo-animation-turntable.php>
- White Spray Paint(Washable?)

## Links

### Commercial Models

NextEngine:\
<https://www.nextengine.com/indexSecure.htm>

RapMan Is Selling a David Laser Scanner Package:\
<http://www.rap-man.com/david3d.asp>

### Open Source Projects

MakerBot Industries Attempt at a Scanner <http://www.makerscanner.com/>\
<http://wiki.makerbot.com/makerscanner>

MakerBot Cyclops - 3D Scanner Mount:\
<http://www.thingiverse.com/thing:4271>

### Current News

<http://blog.makezine.com/archive/2010/03/letters_from_the_fab_academy_part_4.html>

### Forums

Primary Forums for David 3D Scanning Software:\
<http://www.david-laserscanner.com/forum/>

A lot of people have tried different combinations of camera, laser, and software to improve upon the scans. Saves time by cutting out things you don't have to try.

MakerBot has a group discussing a MakerScan device that would be cost affordable and in a nice package:\
<http://groups.google.com/group/makerscan/>

### Instructables

<http://www.instructables.com/id/3-D-Laser-Scanner/>\
<http://www.instructables.com/id/Make-your-own-3d-scanner/>\
<http://www.instructables.com/id/Structured-Light-3D-Scanning/>\
<http://www.instructables.com/id/David-3D-scanner/>\

### Software

The actual scanning software(David 3D):\
<http://www.david-laserscanner.com/>

A point cloud can be brought into MeshLab as a PLY file, a simple ASCII format for 3D object description:\
<http://meshlab.sourceforge.net/>

From here you can merge scans together. The merging process is sometimes easier if you mark certain areas of the object with sharpy so you can align the dots from different scans.

### Videos

systm Covered Cheap 3D Scanning in this Episode:\
<http://revision3.com/systm/laserscan>

### Links Pages

The MakerBot Community Has Their Own Link Page For 3D Scanning Projects:\
<http://wiki.makerbot.com/laser-scanner-links>
