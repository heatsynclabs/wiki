# Motivation

In continuing with adding senses to the human body, night vision (or near infrared vision) has been available commercially even at low prices for some time. Even now there are night vision toys and night vision goggles being given away with special edition video games. On top of this there are also many examples of DIY/Homebrew night vision. There is, however, to our knowledge no open source kit/collaboration on night vision. We intend to source and package a consistent high quality set of parts as a platform to build on.

# Theory

Night vision looks to illuminate a scene with light that is not visible to the human eye. Presumably we would like to illuminate the scene in such a way as to be discrete or we would use visible light.

<http://en.wikipedia.org/wiki/Infrared> Breaks the infrared spectrum to between 700-30,000nm. <http://electronics.howstuffworks.com/gadgets/other-gadgets/nightvision1.htm> Further breaks that down and explains its the applications. .7 to about 1.3 are generally consisered near infrared and are what we are talking about when we speak of night vision. Mid range is where IR remotes tend to function. Above that is thermal infrared.

Wikipedia explains 700nm is where the visible spectrum tends to fade, though focused light up to 880nm can be seen as a faint red light. As such we want to stay above 700nm and go even higher if we do any focusing.

## Theramal Infrared

A branch of infrared night vision is thermal imaging. (Heat Mapping) Thermal imaging would be of course amazing, but all research so far seems to indicate that currently available ccd/cmos technology is still incredibly expensive. Unless we can figure out a cheap way of imaging this seems out of reach for now.

# Literature survey

There are tons of homebrew/diy night vision out there. The majority of these instruct to take apart an old camcorder/camera to harvest the expensive lcd, lenses and imagers. These cameras generally remove IR as humans aren't used to seeing it and it would distort and wash out images. The homebrew guides generally then begin to look into adding more infrared light to the scene. The most common method of doing this is adding an array of IR leds. The Evil Genius series of books on Spy Gadgets suggest an interesting method of illuminating a scene by using a non focused (lens removd) IR laser. He also mentions that green lasers, ~530nm in the spectrum, aren't actually manufacturable and that they are actually composed of IR diodes.

# Process

We will generally want to use a cheap low resolution camera, probably black and white though maybe color. We will want a lens to focus light onto our imaging sensor (ccd,cmos) (sans any kind of infrared blocking filters, and possibly with the addition of white blocking filters). We will want some sort of infrared illuminator to bring (invisible) light to the scene. Finally we will want a comfortable and adjustable mounting for all this, hopefully made available on thingiverse.

## LED IR emitters

Frankly the options in LED illuminators is pretty poor. These diodes are generally so incredibly low in brightness (\<1 lumen) we can't expect to illuminate much more than in front of our faces. The general solution to this has been to create arrays of these leds and overdrive and pulse them like crazy to squeak out as much illumination as possible. There are exeptions, but they are expensive. So far I have sourced an emitter at digikey made expressly for IR CMOS illumination, but its \$82 dollars...

## Lasers

So we may want to look into the previously mentioned green and or IR lasers for illuminating the scene. Sadly IR lasers are indeed expensive as there seems to be little call for them in the consumer market. Green on the other hand are incredibly common. Apparently cheap Chinese green lasers on ebay are generally to be avoided by laser enthusiasts as they give less visible light bang for their buck and are more dangerous due to a lack of IR filtering. This lack of IR filtering is actually kind of good for us though. We could take out the green aspects of the laser, or we could simply filter it afterwards.

### Danger

Any light, focused, is dangerous to the human retina. Non visible spectrum light like Infrared and UV are, however, extremely dangerous to human vision. Welding goggles for instance are specifically designed to protect us from this part of the spectrum! Lasers for instance are classified generally into 3 classes. <http://en.wikipedia.org/wiki/Laser#Laser_safety> The idea is, by the time the light could damage your eye, you would look away and would know you were in danger during that time. Higher class lasers are so powerful by the time you knew you had damaged your retinas, they would already be damaged. IR (and UV) are however invisible to the human eye, so you would never know you were or had done damage to your or anyone else's eyes.

## Filters

A red filter will remove Violet, Blue, Green and part of Yellow. It will allow through Red, Orange and some Yellow which we don't care about. A red filter would remove any of the green laser left over if we didn't wish to modify it to remove the green logic within.

Also used heavily in commercial grade night vision are visible light filters at the ccd/cmos. By removing visible light you can remove any washing out of the image and apparently create a cleaner image. Wikipedia mentions polysulfone which we should look into.

## Sourcing IR Emitters

- <http://search.digikey.com/scripts/DkSearch/dksus.dll?Detail&name=475-2844-1-ND>
  - 120deg max dc 1amp 320mW/sr @ 1A but typically 530mW/Sr (mw/Sr is = to candela I believe)
  - \$12 interesting if not expensive

<!-- -->

- <http://search.digikey.com/scripts/DkSearch/dksus.dll?Detail&name=67-1001-ND>
  - 60deg 60 candela at 100ma
  - \$.27 much cheaper... but do NOTHING..sigh

<!-- -->

- <http://search.digikey.com/scripts/DkSearch/dksus.dll?Detail&name=475-1200-ND>
  - 6deg but 400mcd!--Wonder if smaller angle will help, many smaller angle emitters for more pinpoint viewing?
  - \$.69

<!-- -->

- <http://search.digikey.com/scripts/DkSearch/dksus.dll?lang=en&site=US&WT.z_homepage_link=hp_go_button&KeyWords=SFH4740&x=0&y=0>
  - \$82 1amp 1200mcd
  - Obviously too expensive. Apparently directly manufactured for this purpose. Will research to see what we're up against.
  - Also need to find mating connector to use this.

<!-- -->

- SFH4730 900mcd
  - \$82 and also 900 mcd, ahh, now I see different wavelength. Ill stick to brightness

<!-- -->

- <http://search.digikey.com/scripts/DkSearch/dksus.dll?Detail&name=475-2846-ND>
  - 4751 \$74 1amp 940nm \>630 900mcd typ
  - nah

<!-- -->

- <http://search.digikey.com/scripts/DkSearch/dksus.dll?Detail&name=475-2845-ND>
  - 4750 \$74 1amp 850nm \>630 1000mcd typ
  - nah

## Sourcing LCD's

The idea here would probably be to go BW and cheap. I would like to prototype a nicer display to begin to build up general purpose HUD on it, but am not sure how feasible that will be along side this project with the possible necessity of color filtering. Current sourcing through general electronics vendors such as digikey has led to very few promising results which are all very over priced. Sparkfun sells a few cheap lcd's including some knock off Nokia displays. I am currently thinking of going with these cheap cellphone displays from the source. There displays available through Chinese marketplaces such as aliexpress for \$5-15 dollars. A

# Todo

- test leds for illumination, difference in mcd and beam angle
- source cmos sensors
- source lenses
- source lcd
- prototype
- create a housing which is comfortable and adjustable
