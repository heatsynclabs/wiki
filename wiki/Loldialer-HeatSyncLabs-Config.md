Welcome traveler!

You're attempting to troubleshoot your Loldialer (tm) brand trolling device. If you have another brand trolling device or suspect your device might be counterfeit, please contact your manufacturer for support.

To test lets break it down into modules

Note 1: Substitute your network info into any of these

- byte mac\[\] = {0x90,0xA2,0xDA,0x00,0xDE,0x22};
- byte ip\[\] = {172,22,110,97};
- byte gateway\[\] = {172,22,110,1};
- byte subnet\[\] = {255,255,254,0};
- byte server\[\] = {108,166,54,238};

Note 2: I've seen the loldialer not be able to run the ethernet (ie ping, etc) while also powering the lcd and or backlight. You'll want to be plugged into a dc adapter for this.

- Is internet up at hsl?
- Is the network cable still in good? Easiest things first, right? Swap it!
- Can you ping the loldialer from your computer? (IP above)
- Can the loldialer ping something (google?) Grab the example from <http://arduino.cc/en/Reference/EthernetClient> You might have to change out their ip address for google as it changes occasionally. Use your system to ping google.com and replace whatever IP you get back to be sure
- Is the loldialer server up and responding? Heatsync labs server is up at rs1.zyphon.com. You can actually initiate a loldial from your computer. Insert your 10 digit phonenumber below to troll yourself and guarantee the server is up <http://50.56.124.136/~huertanix/cgi-bin/invoke_lulz.cgi?phone=XXXXXXXXXX&clip=rickroll>
- Is the LCD functioning? This hardware version (1?) uses the sparkfun lcd <https://www.sparkfun.com/tutorials/246>
- Does the button pad work? You need its library from in here, and theres test code in here. From the schematic you'll notice we use the default pins so the test sketch should just run <http://playground.arduino.cc/code/Keypad>
- Can you reflash/update the code? You should already have the libraries (mainly the keypad) from above The v1 software is the master branch over at github <https://github.com/huertanix/loldialer>
