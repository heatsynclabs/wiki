# Ablating copper directly

So far we've had no luck with our \<60 watt laser in ablating copper directly. Nothing happens lasering on straight copper. We've also tried masking the copper with basic spray paint. Best case scenario the copper sort of melts and bubbles a bit oddly. We have access to a 4000W Laser though, would that do anything different??

# Transferring Gerber

Typically to transfer an image to a gerber you have to utilize something like toner transfer process which works ok, but gets tedious. We've been testing transferring our gerber file to the copper by spray painting a copper board with basic black paint and lasering off an inversion of our gerber. The results seem rather promising. There tends to still be a bit of paint left afterwards which can easily be removed with a cotton swab and some alcohol. Here's a (test board)transfer after etching. <http://www.flickr.com/photos/60827818@N07/5563081269/in/photostream> And heres the paint cleaned off. <http://www.flickr.com/photos/60827818@N07/5563081269/in/photostream>

# Soldermask

We wanted to attempt solder mask as well. Theres a huge problem with home made boards in that the solder wicks down the non soldermasked traces. Apparently people have use yellow oche to paint over traces, but that sounds boring. We came up with the idea of re-spraying our board again after etching, then re-lasering the soldermask layer. This re-exposes our pads, but not our traces, and finally destroys the enemy that is wicking!
