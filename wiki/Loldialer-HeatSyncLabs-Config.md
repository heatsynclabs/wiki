Welcome traveler!

You're attempting to troubleshoot your Loldialer (tm) brand trolling device. If you have another brand trolling device or suspect your device might be counterfeit, please contact your manufacturer for support.

Note 1: When in doubt reboot it, duh. Note 2: I've seen the loldialer not be able to run the ethernet (ie ping, etc) while also powering the lcd and or backlight. You'll want to be plugged into a dc adapter for this.

The loldialer with current code from \[Jacob's Repo <https://github.com/jacobrosenthal/loldialer>\] will get DHCP and will report if it can't get an IP.

- Is internet up at hsl?
- Is the network cable still in good? Easiest things first, right? Swap it!

Does it say contact manufacturer?

- Is the loldialer server up and responding? Heatsync labs server is up at rs1.zyphon.com. You can actually initiate a loldial from your computer. Insert your 10 digit phonenumber below to troll yourself and guarantee the server is up <http://50.56.124.136/~huertanix/cgi-bin/invoke_lulz.cgi?phone=XXXXXXXXXX&clip=rickroll>

Other than that

- Maybe it was dropped and wires are loose? I've labeled everything inside
- Is the LCD functioning? This hardware version (1?) uses the sparkfun lcd <https://www.sparkfun.com/tutorials/246>
- Does the button pad work? You need its library from in here, and theres test code in here. From the schematic you'll notice we use the default pins so the test sketch should just run <http://playground.arduino.cc/code/Keypad>
- Can you reflash/update the code? You should already have the libraries (mainly the keypad) from above The v1 software is the master branch over at github <https://github.com/huertanix/loldialer>
