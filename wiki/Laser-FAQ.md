On this page I will start listing all the questions people have and attempt to answer them or link to answers. This will serve as a single searchable page for questions.

## Misc

- How do I make the laser go to a specific place on the laser bed?
  - LightBurn has a setting called absolute coordinates, the other option is current position.
  - LaserCut has a similar setting labelled immediate. Uncheck that for absolute coordinates.

## File questions

- What types of files do I need?
  - LaserCut5.3 (80 Watt Laser) takes .dxf format
  - Lighburn (60 Watt Laser) takes [various file types;](https://docs.lightburnsoftware.com/BasicUsageEssentials.html#importing-artwork) Vector / mixed formats .ai, .svg, .dxf, .pdf, .plt, .hpgl. Image formats: .png, .jpg / .jpeg, .bmp, .gif, .tif / .tiff.
- Why are some parts of my design are missing when I import dxf into Lasercut?
  - Often those elements were not paths, but objects like basic shapes or fonts. Convert those objects to paths so they can be converted.
  - Also grouped items may not be converted to paths when saving as .dxf

<!-- -->

- Is it better to use a raster image to engrave or to use a vector?

This answer highly depends on the artwork in question. For images with gradients engraving in LightBurn works great. For black and white designs one reason to change to vector may be time. Engraving a clock face for instance will result in a lot of travel between the numbers that isn't cutting. If they are all separate layers it'll go quicker. Alternately in Lightburn you may try the "Offset Fill" option especially for thinner fonts. Functionally there should be no difference with a black and white image engrave of high enough quality so it really is only a matter of time.

## Cleaning questions

- Where is the isopropyl (rubbing alcohol)?
  - On the table in the wood box unless someone moved it. There is more in the admin lockers. Ask whoever is hosting if you need help getting something from the lockers.
