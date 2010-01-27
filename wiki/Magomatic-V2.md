### Magomatic Overview

I have some information about the original Magomatic up on my site: <http://www.richardosgood.com/blog/projects/magomatic/> The Magomatic is a device that can read Track 2 of a magstripe card and temporarily store that information on a microcontroller. The Magomatic is then able to emulate that data using an electromagnet. This effectively allows you to temporarily "copy" the magstripe data on the fly.

### Why?

Magstripes are everywhere. Most people probably have at least 1 or 2 cards in their wallet that have magstripe data on them. Those same people probably have no idea what is encoded on the stripes and have no idea how simple it really is for someone to access that data. The Magomatic is a demonstration of how a regular person can easily copy this sensitive information and use it for their own purposes. The Magomatic illustrates that you don't even need a full computer to do these things.

### Version 2

The original Magomatic was capable of copying track 2 of a magnetic card and replaying that data. That was it. I wanted more functionality. I want to be able to read that data. I want to be able to alter the data before emulating it out. This could potentially allow for unauthorized access to areas using magnetic stripe key cards. What if you read the data on your hotel room key, and then altered the room number? Would it let you into another room? That is what I hope to find out through this project.

### Status

1/26/10 I've been working on this project a lot lately. I acquired a 2x16 character serial LCD from Parallax and I am using that as a display. The Magomatic can currently scan track 2 of a magnetic stripe and read that data back out to me on the LCD. I can also scroll through that data and manipulate each byte one by one. Next I have to go back and polish up a few things in the code. Once that is done, I have to re-implement the emulation function for the new code. Finally I will have to alter the circuit board and housing to accommodate the LCD screen and the 3-4 new buttons.

1/27/10 I took my dremel to the original Magomatic enclosure yesterday. There is now room for the LCD screen to fit. I also drilled out four holes and stuck momentary push button switches in them. I wired those all up so I could use them for testing. I polished up the code so it is less buggy. I also added support for up to 64 characters. The code as of yesterday only had support for 32 characters. Unfortunately I am finding that I am running out of code space on the SX chip. I believe it has a total of 2KB of memory, but I am still running out of room. I think that means my code is inefficient :/ . I am so close to being done with the code though. I am going to have to make some room somewhere so I can finish the LRC subroutine. Once that is complete, I should be completely done with the software side of things unless I find a bug somewhere or if the emulation function I wrote last night doesn't work for some reason. I believe I can test emulation by creating some temporary code at the start of the program to just output a test buffer I manually set inside the code. I can then hook up the reader to my computer instead of having to have it attached to the Magomatic. Assuming everything works as expected, I can then start adding components to the circuit board.
