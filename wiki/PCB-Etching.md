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
- non-metal container(s) and/or bubble tank larger than your board
  - <http://www.instructables.com/id/Build-your-own-PCB-bubble-tank!/>
- protective gloves
  - latex or nitrile
- paper cutter to trim board (optional)
  - only use for thinner boards (0.032-)
  - abuses blade

### Print

When printing your design, there are two critical things to keep in mind.

- Print a mirror image.
- Set printer to maximum density. Use Transparency setting, if available.

These instructions assume you're using toner transfer paper.

1.  Mark top sheet in paper tray for side and orientation.
2.  Print circuit.
3.  Cut transfer paper slightly larger than image.
4.  Tape transfer paper over image, shiny side exposed.
    - Be sure not to cover important parts with tape!
    - Cover entire leading edge with tape to avoid jams.
5.  Place paper back in tray, noting orientation.
6.  Print image again with darkest setting.
7.  Remove transfer paper.

### Transfer

1.  Scour copper surface
    - Use scouring pad and a dab of soap
    - Use very light pressure. You're trying to roughen the copper, not remove it.
    - Surface should be slightly dull, with no gouges.
2.  Rinse/dry board.
3.  Partially fill one container with clean, cool tap water.
4.  Align image on transfer paper with board.
5.  Carefully trim excess paper with a razor or sharp scissors.
6.  Maintaining alignment, apply heat with either laminator or iron.
    - Laminator - Depending on the power of your machine, run your board through 2-6 times.
    - Iron - I have no experience with this method. The more heat and pressure, the better.
7.  Place board in water. Paper will release after a few seconds.
8.  Remove board from water, ensuring all paper has been removed.
    - Be careful not to remove toner.
9.  Inspect traces for excess/light toner.
    - If small amounts of toner are missing, use fine-point permanent marker to carefully draw them in.
    - If large amounts of toner are missing, wipe the toner off and restart.

If not using sealing foil, proceed to Etch section.

If using sealing foil:

1.  Allow board to dry. (Do NOT wipe dry!)
2.  Cut piece of foil slightly narrower, and 1"-2" longer than board.
3.  Place foil such that all the toner is covered, and a large flap is folded under the board. This will prevent slipping when applying heat.
4.  Being careful to avoid folds and wrinkles, run foil-wrapped board through laminator ONCE.

Traces should now be covered in green. If there are still black portions, this should be fine. Toner is sufficient to mask; the sealant is merely added protection.

### Etch

Some prefer using a sponge to apply the etchant. This is messy and slow, so we will use the submersion method. If you're interested in the sponge method, more information is at [Instructibles](http://www.instructables.com/id/Sponge-Ferric-Chloride-Method-Etch-Circuit-Bo/)

1.  If only using one container, dump water out.
2.  Fill container with enough etchant to cover board.
3.  Place board in etchant bath.
    - Be careful to avoid splashing. This stuff stains, and is a skin/eye irritant. Reading the MSDS for unfamiliar chemicals is always a great idea.
4.  Agitate bath 5-10 minutes. (unless using bubble tank)
    - Shake container
    - Gently rub board with (gloved!) finger.
    - Check board frequently.
    - Most of the visible etching happens very quickly toward the end of the process.
5.  Submerge board in water or rinse in sink to remove all etchant.
6.  Pour used etchant back into bottle for reuse.
    - You can get several boards from a single batch of etchant.
    - Do not dispose of used etchant down drain.
7.  Dry board.

Congratulations! Your board is now ready for drilling, if necessary, and population.

## The Homemade Process

Design:

- Create your eagle design, use 10-12 mil spacing in your DRU, route to 5mil, you may also find you need to alter your footprints to get the spacing between, say, smd pins to somewhere the process can handle it

Setup:

- 30 minutes prior to wanting to create your board, turn on lamintor making sure 5mil switch is turned on for hotter operation
- set your printer to ink density 5, mark the page which will print so you know how to position

Print:

- print gtl layer (top or bottom, pads and vias), make sure you mirror and make the scale 1 with no caption
- check that all your individual components fit on their footprints properly and that all your traces and components are sufficiently distinct
- cut out blue transfer paper larger than printed design and scotch tape over top of printed design
- place back in printer properly so blue gets printed on(shiny side printed on)
- when it comes out, remove tape

Transfer:

- cut a peice of board with the paper cutter to the size of your design, but make sure board is long enough to be fed through laminator. (a couple inches long--you could attempt multiple designs at a time to fill the space or just trim this off later before etching)
- buff board a little bit with green scotch pad and a little detergent and clean and dry any residue
- ready some water deep enough to later submerse your completed copper with fused transfer paper
- put printed blue face down on copper and insert into laminator and when it comes out the other side, insert again same face up but from the other direction
- when it comes out immediately submerse in water and agitate until the blue paper falls off
- remove from water and carefully dry
- again check that your traces are distinct, you may want to carefully clean them up with a razor blade or add to them with a sharpie

Seal:

- cut a peice of green foil not quite as wide as your copper but several inches longer than your design
- place it dull side over the design overlapping the forward edge an inch or 2, and feed this edge to the laminator
- when it comes out again, feed the exact same way again
- when it comes out second time slowly remove green foil, wrinkles are what we were attempting to avoid, if you get wrinkles you may just try your etch anyway, but in future I find best way to remove wrinkles is to overlap more foil over the front so you can feed it tightly, and making sure foil does NOT overlap on the sides
- the green foil I find tends to blur traces together a bit more even, so I tend to use a razor blade to very carefully make all traces and pads distinct again if need be

Etch:

- you should now cut the copper down to the smallest size to speed up etching and avoid wasting etchant
- put not used up acid in a tub or cup deep enough to submerge design
- put gloves on as etchant stains permanently
- you may want to use electrical tape on the edge of your copper to give yourself something to hold on to when you submerge design
- you should then agitate the design in the etchant for several minutes
- the design will etch from the outside in so you can help the process along by lifting it out of the acid and gently rubbing your finger over the design, breaking hte surface tension and mixing up the etchant
- eventually all visible copper will be eaten away and all your traces and pads are distinct
- drop finished design back into water bath to nuetralize acid

Cleanup:

- return printer to ink density 3
- if etch went fine and acid still seems fresh, replace etchant back into a container for reuse, we need to find disposal method for non fresh acid, please dont dump down drain as it contains copper heavy metals and is toxic
- dump water and clean any spilled acid thoroughly
