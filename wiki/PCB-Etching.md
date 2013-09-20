## Professional Options

### Local

- [Avanti Circuits](Local-Resources#electronics) - located in North Phoenix. You have to buy a full board apx 18in x 24in for a few hundred dollars, but it's completely panelizable and customizable, they work for your business and will do rapid turnaround or weird requests. Go in on it with some friends.

### Internet

- [BatchPCB](http://batchpcb.com/) for fairly quackish and cheap turnaround - 1 month
- [Seedstudio Fusion PCB](http://www.seeedstudio.com/depot/fusion-pcb-service-p-835.html?cPath=185) for qty10, relatively cheap for small sizes. 2-5 week turnaround typical.

otherwise find a deal with the big boys

- [Advanced PCB](http://4pcb.com) has 2 layer 33 each at 33each.com (min 4+1free comes to like 150 shipped) a and they have a decent system for checking your design at freedfm.com

One problem you should already have noticed is these places have 100 domains so its hard to know if you're dealing with the same shop.

haven't tried them but

- <http://www.goldphoenixpcb.biz>
- <http://www.expresspcb.com/ExpressPCBHtm/HowWorks.htm>
- <http://www.sunstone.com/QuoteQT.aspx> (pcbexpress, pcb123)
- <http://www.batesquote.com>

some good but perhaps outdated info from ladyada

- <http://www.ladyada.net/library/pcb/manufacturers.html>

## Homebrew

There are several options for home etching, but they all boil down to covering up the copper you DON'T want to take off, and bathing the rest in acid.

- [PCBLaserEtch](PCBLaserEtch) - using paint and a laser engraver
- photo resist - using light to affix your pattern
- heat transfer - using heat
- permanent marker - yep sharpie will resist etching, too

### Design

- spacing: 10-12mil
- route: 5-10mil
- Adjust routing and/or footprints as necessary.

### Laser Process

See also: [Stencil Etching](Stencil-Etching) -- for solder stencils.

- Single-sided only unless you're very handy with a jig. This means single-sided copper board, too, unless you feel like wasting a bunch of FeCl/time trying to get rid of a whole side of copper to avoid shorting out the whole board.
- Spray paint the copper with an even, not-goopy coat of matte spray paint. Let dry for awhile and then put on a second layer for best results. Glossy paint is somewhat elastic and will "curl" under the laser producing imprecise results.
- Make sure your image is mirrored so you end up etching your circuit "on the back" -- in other words, if you put all your traces and pads on the top layer without mirroring and then etch the board, you're going to have a hard time soldering your components on the top side, fitting your soldering iron in between the component and its tiny little lead. So just mirror it and solder on the back like a normal person. Also, test the whole process with cardboard first so you don't laser, etch, and drill, and realize you've wasted 4 hours.
- Our laser only accepts B&W images so you'll need to convert it to the right format. In Photoshop, you can convert an image to 2-bit (actually probably 1-bit) mode by going to Image\>Mode\>Grayscale and Image\>Mode\>Bitmap. Choose Diffusion Dither. Save as a .bmp and import into the laser. Double check that the dimensions are accurate. If it whines about being 2-bit bitmap, you likely didn't do the bitmap mode correctly and it's 1 or 2 bits of color stored in a 32-bit format or something.
- Make sure that the colors are right: I think our laser engraves away all black pixels, which means those pixels will be exposed to acid, which means black = "empty space" and white = "copper traces". Double-check by running a preview beforehand and making sure that the red "cut" areas are the areas you want to end up as "empty space".
- To get accurate sizing when importing into LaserCut, you'll also probably want to save your file at 254dpi / 100 dots per centimeter / 10 dots per millimeter. In other words, LaserCut seems to interpret a 254-pixel image as being 1 inch because (as far as I can tell) it doesn't respect DPI settings in files.
- Follow the normal laser cutter directions and precautions.
- Engrave ("raster") the image using power/speed settings recommended by the laser cutter job log. It's a good idea to test a small unused corner first; you want to ablate all the black paint leaving behind only the settled dust which can easily be wiped off. Avoid using too much power / too low speed because heating up the copper may "glue" the paint dust back on the board and the copper reflection may damage the laser.
- Clean up the paint dust using rubbing alcohol or water (not acetone)
- Follow the [Etch](#etch) instructions below.

### Preparation

You will need:

- copper clad board
  - Available at Fry's Electronics, Radio Shack, and other electronics supply shops.
  - Several places are also selling flexible PCB material called Kapton.
- transfer material
  - Some use magazines or transparencies.
  - Special-purpose toner transfer paper is available.
    - Pulsar Pro FX - <http://pulsarprofx.com>
    - Press'n'Peel - <http://www.techniks.com/>
- sealing foil (optional) - <http://pulsarprofx.com>
- source of either UV light or heat
  - Desktop paper laminator works great.
  - Clothes/craft iron also works.
- laser printer
  - Ink jet will NOT work.
- scouring pad (NOT steel wool)
- chemicals
  - dish soap
  - ferric chloride (FeCl)
    - Use this OR CuCl.
    - Get liquid so you don't have to mix the powder.
    - You can't just dump this down the drain when you're done with it (after several of etches).
  - cupric chloride (CuCl)
    - Use this OR FeCl
    - Easier to work with
    - <http://www.instructables.com/id/Stop-using-Ferric-Chloride-etchant!--A-better-etc/>
    - <http://members.optusnet.com.au/~eseychell/PCB/etching_CuCl/index.html>
  - vinegar, peroxide (H2O2, table salt (NaCl)
    - Inexpensive
    - Much less toxic
    - Easier cleanup
    - <http://www.stephenhobley.com/blog/2011/03/02/still-messing-with-forces-i-dont-understand-the-formula/>
- non-metal container(s) and/or bubble tank larger than your board
  - <http://www.instructables.com/id/Build-your-own-PCB-bubble-tank!/>
- protective gloves
  - latex or nitrile
- paper cutter to trim board (optional)
  - only use for thinner boards (0.032-)
  - abuses blade
- we also have a sheet metal brake/shear which can be used for boards

30 minutes prior to transfer, turn on laminator. Use thickest setting for highest heat.

### Print

When printing your design, there are two critical things to keep in mind.

- Print a mirror image, scale to 1.
- Set printer to maximum density. Use Transparency setting, if available.

These instructions assume you're using toner transfer paper.

1.  Mark top sheet in paper tray for side and orientation.
2.  Print circuit.
    - top OR bottom layer, pads, vias
    - no docu/caption
    - Verify components fit on their footprints.
    - Verify all traces are clear and distinct.
3.  Cut transfer paper slightly larger than image.
4.  Tape transfer paper over image, shiny side exposed.
    - Be sure not to cover important parts with tape!
    - Cover entire leading edge with tape to avoid jams.
5.  Place paper back in tray, noting orientation.
6.  Print image again with darkest setting.
7.  Remove transfer paper.

### Transfer

![](files/Pcb_transfer.jpg)

*pcb_transfer.jpg*

1.  Cut board to appropriate size
    - Leave enough board to push through laminator; At least two inches.
2.  Scour copper surface
    - Use scouring pad and a dab of soap
    - Use very light pressure. You're trying to roughen the copper, not remove it.
    - Surface should be slightly dull, with no gouges.
3.  Rinse/dry board.
4.  Partially fill one container with clean, cool tap water.
5.  Align image on transfer paper with board.
6.  Carefully trim excess paper with a razor or sharp scissors.
7.  Maintaining alignment, apply heat with either laminator or iron.
    - Laminator - Depending on the power of your machine, run your board through 2-6 times changing direction at least once.
    - Iron - I have no experience with this method. The more heat and pressure, the better.
8.  Place board in water. Paper will release after a few seconds.
9.  Remove board from water, ensuring all paper has been removed.
    - Be careful not to remove toner.
10. Inspect traces for excess/light toner.
    - If small amounts of toner are missing, use fine-point permanent marker to carefully draw them in.
    - If large amounts of toner are missing, wipe the toner off and restart.
    - Remove excess toner with a razor blade.

If not using sealing foil, proceed to Etch section.

If using sealing foil:

1.  Allow board to dry. (Do NOT wipe dry!)
2.  Cut piece of foil slightly narrower, and 1"-2" longer than board.
3.  Place foil, dull side down, such that all the toner is covered, and a large flap is folded under the board. This will prevent slipping when applying heat.
4.  Being careful to avoid folds and wrinkles, run foil-wrapped board through laminator twice.

Traces should now be covered in green. If there are still black portions, this should be fine. Toner is sufficient to mask; the sealant is merely added protection.

### Etch

![pcb_etched.jpg](files/Pcb_etched.jpg) Some prefer using a sponge to apply the etchant. This is messy and slow, so we will use the submersion method. If you're interested in the sponge method, more information is at [Instructibles](http://www.instructables.com/id/Sponge-Ferric-Chloride-Method-Etch-Circuit-Bo/)

1.  Trim excess copper board to avoid wasting etchant.
2.  If only using one container, dump water out.
3.  Fill container with enough etchant to cover board.
4.  Place board in etchant bath.
    - Be careful to avoid splashing. This stuff stains, and is a skin/eye irritant. Reading the MSDS for unfamiliar chemicals is always a great idea.
5.  Agitate bath 5-10 minutes. (unless using bubble tank)
    - Shake container
    - Gently rub board with (gloved!) finger. Avoid touching things afterwards, this stuff stains everything.
    - Check board frequently.
    - Most of the visible etching happens very quickly toward the end of the process.
6.  Submerge board in water or rinse in sink to remove all etchant.
7.  Pour used etchant back into bottle for reuse.
    - You can get several boards from a single batch of etchant.
    - Do not dispose of used etchant down drain.
8.  Dry board.

Congratulations! Your board is now ready for drilling, if necessary, and population.

### Cleanup

- Return used etchant to container for future reuse.
  - DO NOT dump down train. Etchant is toxic and contains heavy metals. Check MSDS or city hazardous waste department for disposal instructions.
- Thoroughly clean up any spilled etchant.
- Return printer to typical settings.
