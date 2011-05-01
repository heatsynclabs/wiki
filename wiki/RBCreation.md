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

### Twitter Parsing

We created a Twitter account, @TweetToSmoke, which could be used to send @replies to. Using some code based on the open-source Ruby-based retjilp retweeting bot, we were able to set up an oath-enabled application to view TweetToSmoke's @replies on an Ubuntu cloud server using plain Ruby CGI over Apache (no Rails needed). The CGI script returned the latest reply's text.

### Web-to-Morse

An Arduino with an ethernet shield was programmed to connect to the cloud server via HTTP and parse out the text (handily delimited with a \$) and convert each character into morse code. From there, text-to-morse-code scripts were found and the Arduino Tone library was used to translate the tweet into an audio tone which would be sent out via a normal 3.5mm headphone jack.

### Audio-to-Smoke

The Arduino output 100 Hz tones of varying lengths to a large subwoofer speaker placed inside a trash can with a fog machine stuffed on top. The frequencies used and the placement of the sound system allowed us to generate small rings and long puffs of smoke which were viewable indoors, but not so thick that we would fill our Fire Department visit quota for the week.

#### Room for improvement

Scale up this model into something that would actually communicate well over long distances, we would need much more smoke and a more pronounced method of releasing dots and dashes into the sky. With some high-power relays and either servo motors, solenoids, or hydraulics we could build a bonfire-sized canopy system that would gather smoke inside the canopy and release it by opening the canopy.

#### Further ideas

- Using a series of smaller smoke apertures, emulate an LED matrix in smoke and thereby "print" actual letters instead of morse code.
- Scale it down to tabletop size or smaller, with a different type of "smoke", and put it in front of a webcam so people can communicate with it and see the results 24/7.
  - Or better yet, implement a larger one in a remote location with a 24/7 bonfire, thus realizing the dream of mass public communication in smoke (and possibly attracting the attention of the EPA!)
