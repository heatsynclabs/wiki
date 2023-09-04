On this page I will start listing all the questions people have and attempt to answer them or link to answers. This will serve as a single searchable page for questions.

## Misc

- Who should come to the Laser Meetup?
  - Anyone who is interested or curious even if you don't have a design in mind.
  - Anyone wanting to get help on a design or time cutting a project (you don't need to be certified ahead of class)
  - Kids can come as well, but anyone under 18 must have an adult parent or guardian with them.
- What size material can I cut in the laser.
  - See here; [ 80W](Large-80W-Laser#sizesize), [ 60W](Mini-60W-Laser#size)
- How thick of material can I cut. This largely depends on the material. See the laser logs [ 80W](Large-80W-Laser#logs), [ 60W](Mini-60W-Laser#size) for examples of what people cut. It lists the dimensions.

## Laser Operation

- Why doesn't anything happen when pressing xy, or z to move the laser.
  - Press the Download button to regain communications. You can close the window.
- How do I make the laser go to a specific place on the laser bed?
  - LightBurn has a setting called absolute coordinates, the other option is current position.
  - LaserCut has a similar setting labelled immediate. Uncheck that for absolute coordinates.
- Why doesn't the laser start my job or run the box and instead beeps 10 times?
  - Check the control panel and see if it says soft stop. If that happened it means the job was going to cut out of bounds so it terminated the job.
  - Look at your options for origin point, and if immediate was checked or not.
- Why did the laser start cutting as soon as I shut the lid.
  - This is a known problem. When you press pause on the LaserCut 5.3 software then open the lid it starts for some reason.

## File questions

- What types of files do I need?
  - LaserCut5.3 (80 Watt Laser) takes .dxf format
  - Lighburn (60 Watt Laser) takes [various file types;](https://docs.lightburnsoftware.com/BasicUsageEssentials.html#importing-artwork) Vector / mixed formats .ai, .svg, .dxf, .pdf, .plt, .hpgl. Image formats: .png, .jpg / .jpeg, .bmp, .gif, .tif / .tiff.
- Why are some parts of my design are missing when I import dxf into Lasercut?
  - Often those elements were not paths, but objects like basic shapes or fonts. Convert those objects to paths so they can be converted.
  - Also grouped items may not be converted to paths when saving as .dxf

<!-- -->

- Is it better to use a raster image to engrave or to use a vector?
  - This answer highly depends on the artwork in question. For images with gradients engraving in LightBurn works great. For black and white designs one reason to change to vector may be time. Engraving a clock face for instance will result in a lot of travel between the numbers that isn't cutting. If they are all separate layers it'll go quicker. Alternately in Lightburn you may try the "Offset Fill" option especially for thinner fonts. Functionally there should be no difference with a black and white image engrave of high enough quality so it really is only a matter of time.

<!-- -->

- My file imports with lots of segments of lines and curves that aren't connected. How do I make them all connected.
  - For LaserCut 5.3 you use the Tools menu then Unite Lines.
  - For Lightburn you use Edit Auto-Join Selected Shapes.
- Why is the text in my file coming up wrong.
  - Possibly the font that you used is not on the laser computer. You may need to convert the font to a path before importing it.

## Cleaning questions

- Where is the isopropyl (rubbing alcohol)?
  - On the table in the wood box unless someone moved it. There is more in the admin lockers. Ask whoever is hosting if you need help getting something from the lockers.

---
*Categories: [Laser](Category-Laser)*
