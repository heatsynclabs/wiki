### Magomatic Overview

I have some information about the original Magomatic up on my site: <http://www.richardosgood.com/blog/projects/magomatic/> The Magomatic is a device that can read Track 2 of a magstripe card and temporarily store that information on a microcontroller. The Magomatic is then able to emulate that data using an electromagnet. This effectively allows you to temporarily "copy" the magstripe data on the fly.

### Why?

Magstripes are everywhere. Most people probably have at least 1 or 2 cards in their wallet that have magstripe data on them. Those same people probably have no idea what is encoded on the stripes and have no idea how simple it really is for someone to access that data. The Magomatic is a demonstration of how a regular person can easily copy this sensitive information and use it for their own purposes. The Magomatic illustrates that you don't even need a full computer to do these things.

### Version 2

The original Magomatic was capable of copying track 2 of a magnetic card and replaying that data. That was it. I wanted more functionality. I want to be able to read that data. I want to be able to alter the data before emulating it out. This could potentially allow for unauthorized access to areas using magnetic stripe key cards. What if you read the data on your hotel room key, and then altered the room number? Would it let you into another room? That is what I hope to find out through this project.

### Status

I've been working on this project a lot lately. I acquired a 2x16 character serial LCD from Parallax and I am using that as a display. The Magomatic can currently scan track 2 of a magnetic stripe and read that data back out to me on the LCD. I can also scroll through that data and manipulate each byte one by one. Next I have to go back and polish up a few things in the code. Once that is done, I have to re-implement the emulation function for the new code. Finally I will have to alter the circuit board and housing to accommodate the LCD screen and the 3-4 new buttons.
