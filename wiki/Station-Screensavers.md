## Overview

The idea is to have a screensaver at the stations with a computer that shows projects people have made using the tools at that station. This was the easy part.

- Made folders C:\Photo Screensaver \_StationName\_
- Added photos from our Flickr or google photos collections
- Set the screensaver to photo and that folder
- Set the screensaver to 10 minutes thinking that was short enough to be annoying.

## Over Complicating Things

That was pretty much it and it worked good. I wanted the screensavers to be running when open hours starts, but the monitors turn off (which is good). To solve this I wrote a simple AutoHotkey script that checks if the computer has been idle for 5 minutes and will start the screensaver if it has. I use Windows taks scheduler to run this script when the open hours begins. This doesn't seem to work 100% of the time. If anyone knows how to solve this let me know.

---
*Categories: [Projects](Category-Projects)*
