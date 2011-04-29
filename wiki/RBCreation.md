# Red Bull Creation Contest

Wat: Red Bull gave away mystery boxes to hackerspaces across the US, and challenged us to reverse-engineer them. HeatSync Labs did, and after many rick-rolls and dead ends, we found most of their easter eggs and registered a team, called

Original Ideas for projects:

- Virtual Babbage Difference Engine or Analytical Engine emulated in Arduino with historically accurate analog inputs and outputs
  - Virtual Enigma machine or Bombe (bonus points for Churchill tie in)
- Reinvented wheel that moves under its own power
- Virtual sun-dial (light sensors and an LCD display)
- Punchcard reader or compiler ( makes Arduino code and puts it on the chip?)
  - Old school census tabulation
- Arduino-powered radar

<!-- -->

- Vinyl-to-mp3 encoder

<!-- -->

- Spinning wheel with length calculator and/or red yellow green yarn consistency meter
- Sextant with Aruino and GPS
- Abacus with digital readout
- Tweet a smoke signal generator
- Suit of armor with damage sensors and HUD
- 8-Track-Duino
- Full room sized pong game
- Ice Box with LCD and tweet to tell you when it needs more ice
- Flintlock with laser targeting range finder

<!-- -->

- Retrofitting a paper stock ticker (like from the 1920s) to spit out hackerspace Twitter list tweets instead of stocks
- Retrofitting a phone to dial robot messages to people (via Twilio or Tropo, akin to loldialer)
- Old-style outdoor clothesline outfitted with a moisture sensor that buzzes or blinks or SMS texts when clothes are dry or fall off a clothes line
- Old-style typewriter outfitted to send e-mail (this will get really tedious given the mechanical nature of their keys)
- Arduino-powered open-hardware record (vinyl) player

## TweetToSmoke

Our project's aim is to provide a means to connect one of the newest forms of human mass-communication (Twitter) into the oldest (smoke signals). Our team, the Triad, was made up of a mix of different skillsets and talents which came in handy when dealing with both JSON parsing and fog machine smoke shaping. It boils down to a few steps:

We created a Twitter account, @TweetToSmoke, which could be used to send @replies to. Using some code based on the open-source Ruby-based retjilp retweeting bot, we were able to set up an oath-enabled application to view TweetToSmoke's @replies on an rackspace cloud instance using plain Ruby CGI (no Rails needed). The CGI script returned the latest reply's text. From there, an Arduino with an ethernet shield was programmed to parse out the text and convert each character into morse code and from there, into an audio tone which would be amplified and sent to a large bass subwoofer pointed in the center near the top of the inside of a trash can with a fog machine stuffed inside. The frequencies used and the placement of the sound system allowed us to generate small rings and long puffs of smoke which were viewable indoors, but not so thick that we would end up getting a visit from the Fire Department (again).
