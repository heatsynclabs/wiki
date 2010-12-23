## Professional Options

American Circuit Technology(http://www.act-cw.com) - Quick Turn arounds, cost-effective pricing and quality boards. Does prototypes and offers articles on many PCB related topics.

batchpcb for fairly quackish and cheap turnaround - 1 month seedstudio for opening your product up and/or cheap as low as 30 bucks for 5 boards

otherwise find a deal with the big boys advanced pcb (4pcb.com) has 2 layer 33 each at 33each.com (min 4+1free comes to like 150 shipped) a and they have a decent system for checking your design at freedfm.com

One problem you should already have noticed is these places have 100 domains so its hard to know if you're dealing with the same shop.

haven't tried them but <http://www.goldphoenixpcb.biz> <http://www.expresspcb.com/ExpressPCBHtm/HowWorks.htm> <http://www.sunstone.com/QuoteQT.aspx> (pcbexpress, pcb123) www.batesquote.com

some good but perhaps outdated info from ladyada <http://www.ladyada.net/library/pcb/manufacturers.html>

## HOMEMADE

Several options, but they all boil down to covering up the copper you DONT want to take off, and bathing the rest in acid

photo resist-using light to affix your pattern heat transfer-using heat straight sharpie on copper-yep sharpie will resist etching, too

youll need some copper clad, available at fry, radio shack, elsewhere (several places are also selling flexible pcb material called Kapton!)

yowl also need some chemicals

etching chemicals ferric chloride-radio shack --don't get powder and deal with mixing it--realize you cant just toss this stuff down the drain when you're done with it (after a bunch of etches mind you)-- hence: cupric chloride <http://www.instructables.com/id/Stop-using-Ferric-Chloride-etchant!--A-better-etc/> <http://members.optusnet.com.au/~eseychell/PCB/etching_CuCl/index.html> more…

Im a fan of the heatsync transfer. method.

Youll need a laserjet printer, not the common home inkjet kind, but the kind you have at work and kinks

You typically buy a transfer paper from someone, I like pulsar prefix but I've seen reference to pressnpeel as well

press-n-peel <http://www.techniks.com/>

pulsarprofx-LOTS of info on the process on their site <http://www.pulsarprofx.com/>

Because toner doesn't apply densely enough, you probably want to seal as well, pulsar sells a green foil for this too.

Youll need some non metal container to etch in, and some gloves as ferric chloride at least stains your hands. I do small work so I can agitate in a dixie cup

bubble tank <http://www.instructables.com/id/Build-your-own-PCB-bubble-tank!/>

You generally then apply the transferred image over to your board. The cheap way is with an iron, I prefer the pulsarprofx laminator method. I found their laminator on ebay for 20-30 shipped

with pulsarprofx .032 boards a Simple paper cutter from staples works well for cutting, though I think the blade is degrading quickly

Now you etch!

Theres been a lot of hullabo about etching with just a sponge--MEH My results have been very messy and annoying and slow like this. I find the main lesson to learn here is to break the surface tension with your gloved finger occasionally while you're regularly agitating in order to speed up the process. <http://www.instructables.com/id/Sponge-Ferric-Chloride-Method-Etch-Circuit-Bo/>

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
