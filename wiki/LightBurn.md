# Overview

This page needs a lot of work, so right now it's just a dumping ground for my notes. I'll work to improve it, or you can too.

There is a lot of good documentation on [lightburnsoftware.com](https://lightburnsoftware.com/).

The computer at the vinyl cutter station also has LightBurn. If the computer at the laser is busy you can prep your files from that machine. The LightBurn isn't for controlling the vinyl cutters.

One note of caution. On our version 1.2.01 you want to use the start button, not the send button. Sending your project has resulted in glitches in engravings.

# Details

Check the official Lightburn documentation for info on the user interface.

Some important portions to focus on:

The edit window: the displayed grid. This is the pattern that the laser will cut/engrave.

- You can import SVG files, or even just drag and drop them onto the edit window.

Layers: at the right.

- Different layers can be set to use different modes, with different power and speed settings.
  - Fill mode: used for engraving (breaking up the surface of the material for things like drawing images, without cutting through it).
  - Line mode: attempts to actually cut through the material. Success depends on whether you are using appropriate power and speed settings for your chosen material.
  - There are other modes, but Fill and Line are most important for starters.
- You can rearrange the order of layers; this is the order the laser will act on them in. Generally you want the Fill layers first, followed by any Line layers.
- Each layer has a corresponding Power and Speed setting; consult the binder for some tips on how to set these for the material you're cutting. Engraving can use a higher speed and lower power than cutting.

Laser window: at the right below Layers.

- Frame: *without* turning the laser on, causes the laser head to follow a rectangular or oval path around the area it will cut/engrave inside. Use this first to check that your material is positioned correctly!
- Cut selected graphics: causes the laser to cut/engrave just your selection, rather than everything in the edit window.
- Start: Start cutting/engraving!
- Pause: Pause cutting. As long as you don't move your material, you will not lose your job progress by using this.
- Stop: Stops the cut job. You will likely have to start over from the beginning with fresh material, but sometimes this is necessary.

Other notes:

- Middle button scroll
- adjusted laser position on the panel
- Upload
- Start -says "Send the current design to the laser" in the tool tip, but it really means, start the laser.
- Can choose "output" to only cut certain portions
- Upload failed - run "frame" to get reinitiate
- If you can get it to "frame" but you click start and it just beeps at you, make sure you have some output chosen. (Image below)
- If you get "no object selected" or some other item, there is a different check mark (image below)

![](files/Lightburn-screen.jpg)

*lightburn-screen.jpg*

---
*Categories: [Laser](Category-Laser)*
