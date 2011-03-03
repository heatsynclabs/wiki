## Professional Options

batchpcb for fairly quackish and cheap turnaround - 1 month seedstudio for opening your product up and/or cheap as low as 30 bucks for 5 boards

otherwise find a deal with the big boys advanced pcb (4pcb.com) has 2 layer 33 each at 33each.com (min 4+1free comes to like 150 shipped) a and they have a decent system for checking your design at freedfm.com

One problem you should already have noticed is these places have 100 domains so its hard to know if you're dealing with the same shop.

haven't tried them but <http://www.goldphoenixpcb.biz> <http://www.expresspcb.com/ExpressPCBHtm/HowWorks.htm> <http://www.sunstone.com/QuoteQT.aspx> (pcbexpress, pcb123) www.batesquote.com

some good but perhaps outdated info from ladyada <http://www.ladyada.net/library/pcb/manufacturers.html>

## Homebrew

There are several options for home etching, but they all boil down to covering up the copper you DON'T want to take off, and bathing the rest in acid.

- photo resist - using light to affix your pattern
- heat transfer - using heat
- permanent marker - yep sharpie will resist etching, too

### Design

- spacing: 10-12mil
- route: 5mil
- Adjust routing and/or footprints as necessary.

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
    - Gently rub board with (gloved!) finger.
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
  - DO NOT dump down train. Etchant is toxic and contains heavy metals. Check MSDS for disposal instructions.
- Dump water down drain while running cold water.
- Thoroughly clean up any spilled etchant.
- Return printer to typical settings.
