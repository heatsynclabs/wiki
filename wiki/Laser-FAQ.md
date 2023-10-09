In this FAQ for the [Laser Cutters](Laser-Cutters) we will be listing all the questions people have and attempt to answer them or link to answers. This will serve as a single searchable page for questions.

## Misc

- Who should come to the Laser Meetup?
  - Anyone who is interested or curious even if you don't have a design in mind.
  - Anyone wanting to get help on a design or time cutting a project (you don't need to be certified ahead of class)
  - Kids can come as well, but anyone under 18 must have an adult parent or guardian with them.
- How do I keep my material in place?
  - Taping things to the rails with a bit of tension so it doesn't slide left and right.
  - You can use the honeycomb and put T pins in them. There should be some in the drawer. To access the drawer of the medical cart use the code 1234 to unlock.
- Why did I hear something beep 5 times?
  - That could be the medical cart locking. Not a problem.
- Is the 80 W laser log accessible on both computers?
  - Both of them can be accessed from anywhere on the internet [ 80W](Large-80W-Laser#logs), and [ 60W](Mini-60W-Laser#size).

## Materials and Cut Settings

- What materials can I cut or engrave with the laser?
  - The [ Laser Material Guidelines](Laser-Material-Guidelines) wiki page aims to cover that.
- What size material can I cut with the laser?
  - See here; [ 80W](Large-80W-Laser#sizesize), [ 60W](Mini-60W-Laser#size)
- How thick of material can I cut?
  - This largely depends on the material. See the laser logs for the [ 80W](Large-80W-Laser#logs), and [ 60W](Mini-60W-Laser#size) for examples of what people cut. It lists the dimensions.
- I'm at 100% for power and not cutting through; Should I use 2 passes to cut through my material or change my settings to go slower?
  - Typically you'll want to go slower. If you do multiple passes there may be debris left in the cut, and it may misaligned if heat causes warping to your material or anything else causes movement of the material.
- Is the MDF from Home Depot/Lowe's good enough or is there a better place to get MDF?
  - Big box stores will have the price advantage because of volume. Sourcing and quality are super subjective, so its up to you. An art store like Jerry's may have finer stuff but you will pay a premium.
- How finely can I engrave with the lasers?
  - If you are asking about how fine the line or kerf of the laser is; In my experience the 80W laser is 0.125mm or larger if out of focus due to height or warping. The 60W laser provides a finer point much closer to .1mm. (summarized Robert Douglas Slack response).

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
- What order is my design going to cut in?
  - The software will go from top to bottom in your layers (colors) for any that are set to output. Within those elements it will probably try to cut things that are near each other. Preview or simulate are going to show you more about what order things are happening in without actually cutting the job.
- Is there a rotary attachment?
  - Yes for the 80 W laser and it does require special training to use. Post on Slack asking to get help using it once have some experience using the 80 W laser.
- Can you vary power during an engrave? OR Can you engrave at different depths / Can you do a gray scale engrave?
  - Engraving gradients is done by dithering an image and Lightburn has some nice settings features for engraving images, but the laser power isn't adjusting. You can create separate engrave layers and cut them at different powers, but no true variable power cuts.

## File questions

- What types of files do I need?
  - LaserCut5.3 (80 Watt Laser) takes .dxf format.
    - In Adobe Illustrator to export a dxf go to the menu File, Export, Export As and choose DXF 2000.
    - Newer versions of DXF may pose problems. In Inkscape you can save as DXFR12 or DXFR14 one or both should work.
  - Lighburn (60 Watt Laser) takes [various file types;](https://docs.lightburnsoftware.com/BasicUsageEssentials.html#importing-artwork) Vector / mixed formats .ai, .svg, .dxf, .pdf, .plt, .hpgl. Image formats: .png, .jpg / .jpeg, .bmp, .gif, .tif / .tiff.
- "Why are some parts of my design missing when I convert to dxf for Lasercut?
  - Often those elements were not paths, but objects like basic shapes or fonts. Convert those objects to paths so they can be converted.
  - Also grouped items may not be converted to paths when saving as .dxf
- My file imports with lots of segments of lines and curves that aren't connected. How do I make them all connected.
  - For LaserCut 5.3 you use the Tools menu then Unite Lines.
  - For Lightburn you use Edit Auto-Join Selected Shapes.
- Is it better to use a raster image to engrave or to use a vector?
  - This answer highly depends on the artwork in question. For images with gradients engraving in LightBurn works great. For black and white designs one reason to change to vector may be time. Engraving a clock face for instance will result in a lot of travel between the numbers that isn't cutting. If they are all separate layers it'll go quicker. Alternately in Lightburn you may try the "Offset Fill" option especially for thinner fonts. Functionally there should be no difference with a black and white image engrave of high enough quality so it really is only a matter of time.
- Why is the text in my file coming up wrong.
  - Possibly the font that you used is not on the laser computer. You may need to convert the font to a path before importing it.
- Why does my design come in with the wrong dimensions (didn't scale correctly)?
  - This depends on how your design software assigns units of measurement which is outside the scope of this FAQ. However you can resolve most if not all of these problems by checking the total size of your design then scaling it once you bring it into the laser software.
    - For LaserCut5.3 you can go to Edit Size to adjust your design size.
    - For Lightburn the top bar has the size and you can adjust it there.
- I have lines that extend beyond the boundaries of the document. If I were to upload that file onto either of the laser cutting software, will the software include the lines that are outside the boundary?
  - Yes. Neither LaserCut 5.3 or Lightburn will care about what your page size is. Everything outside your page will still import.

## Cleaning questions

- Where is the isopropyl (rubbing alcohol)?
  - On the table in the wood box unless someone moved it. There is more in the admin lockers. Ask whoever is hosting if you need help getting something from the lockers.

---
*Categories: [Laser](Category-Laser)*
