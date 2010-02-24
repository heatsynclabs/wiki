## Team Members

| Name    | Email                      |
|---------|----------------------------|
| Rick O  | ricko@heatsynclabs.org     |
| David H | huertanix@heatsynclabs.org |
| Paul H  | paulhickey@gmail.com       |
| Will B  | bradley.will@gmail.com\>   |
| Nate P  | nate@coffeebot.net         |
| Bobby M | bwmetz@gmail.com           |
|         |                            |

## Tasks

| Task      | Name           | Completed? |
|-----------|----------------|------------|
| Balloon   | Paul H         | No         |
| Camera    | Will B         | No         |
| Helium    | Paul H         | Yes        |
| Parachute | Casey D        | No         |
| Container | Rick O / Bobby | No         |
| Radio     | Rick O         | No         |
| GPS       | Zach           | Yes        |
|           |                |            |

## Synopsis

This project will involve sending a weather balloon into near space. Near space is typically considered to be above 65,000 feet above sea level. A near space balloon typically consists of the following major components:

1.  Balloon + helium (duh)
2.  GPS for tracking the balloon
3.  One way radio communication
    1.  This is for sending us the GPS coordinates
4.  Camera on a timer
    1.  Must take pictures every X minutes and have enough space to store them all
5.  Flight computer
    1.  This coordinates all of the other parts and makes them work together
6.  Batteries
    1.  Need to handle extreme cold and last long enough for the flight and for you to find it
7.  Weatherproof container
    1.  This must keep out the cold as much as possible
    2.  Needs a hole for the camera to take pictures through
    3.  Must be able to open, but latch it shut securely
    4.  The electronics must be secured inside somehow
    5.  Balloon has to attach to this, but be able to release somehow after it pops.
8.  Parachute
    1.  This slows the balloon down so it doesn't slam into the ground at terminal velocity, but it's not huge enough that it takes forever for the payload to return to earth.

## Balloon

### Components

#### Balloon and Helium

Purchase balloons most likely on line. Rent helium tanks locally. May need to put a hefty deposit on the tanks.

#### GPS

Zach's hacked Palm GPS mapper. Outputs serial data which should work great for the TinyTrak and fits into an Altoids tin.

#### Radio

RadioShack Realistic HTX-202. It's a pretty rugged hand held radio. It has a BNC connector which will allow us to easily add an external antenna. The rechargeable battery is shot but the radio can be powered externally by a separate battery pack. The radio is capable of 2-meter transmission only, but that should work just fine and includes the APRS frequency. Maximum output power is 5 watts which should be sufficient with an external antenna. <http://www.eham.net/reviews/detail/1296>

#### Camera

We can potentially use a used or donated digital camera. Some of these have built in time-lapse functions. If we can't find one that does, we can built a simple timer circuit to push the shutter button every few minutes.

#### Flight Computer

I have a TinyTrak3 that can be used to take serial GPS data and send it out of the radio automatically.

#### Batteries

The cell phone already has a battery. If this battery is in good condition it may be sufficient to provide enough power in the cold weather for the length of the mission. It may be a good idea to construct an external battery pack for the phone. The pack can hook up to the phone via it's charging port. This will allow us to drain the external batteries before switching to the phone battery as a backup.

#### Chassis

Can use a styrofoam cooler with insulation. Other's have also used insulated lunch boxes. We can also construct something from scratch if we want.

#### Parachute

Can purchase or construct from scratch

## Launch Site

- Grabbed this info from UAT's nearspace wiki: <http://nearspace.0x58.com/index.php?title=Launch_Sites>

### Primary

<div style="float:right">

\<googlemap version="0.9" lat="32.84503" lon="-112.31748" type="terrain" width="400" height="400" selector="no" controls="small"\>32.84503, -112.31748Primary Launch Site\</googlemap\>

</div>

- Lauch Site 1
  - Cord (decimal): 32.84503 by -112.31748 at 1801.2ft MSL
  - Cord (deg/minute): 32° 50' 42.108" N by 112° 19' 2.928" W at 1801.2ft MSL

<div style="clear: both">

</div>

### Secondary

<div style="float:right">

\<googlemap version="0.9" lat="32.69635" lon="-111.49202" type="terrain" width="400" height="400" selector="no" controls="small"\> 32.69635, -111.49202 \</googlemap\>

</div>

- Lauch Site 2
  - Cord (decimal): 32.69635 by -111.49202 at 1630.6ft MSL
  - Cord (deg/minute): 32° 41' 46.86" N by 111° 29' 31.2714" W at 1801.2ft MSL

The closest major airport is Eloy Municipal with is about 9 miles to the NW.

<div style="clear: both">

</div>

## Pricing

Actual Cost is how much we actually pay for an item. In some cases an item may be donated to us, but the competition states that all items must have a price associated with them. In that case, we must find the donated item for sale somewhere, and record that price in the "Recorded cost" column.

#### Ham Radio Balloon

| Item | Quantity | Actual Cost | Total | Recorded Cost | Source |
|----|----|----|----|----|----|
| 1200 Gram Balloon | 2 | \$45 est | \$90 | \$45 | <http://www.kaymont.com/pages/cold-weather-balloons.cfm> |
| 90CF Helium | 1 | \$40.00 + \$100 deposit | \$40.00 | \$40.00 | <http://www.azfunparty.com/helium.html> |
| Radio | 1 | \$40-\$50est | \$40-\$50est | \$40-\$50est | ebay.com (Search "Realistic HTX-202") |
| TNC | 1 | 0 | 0 | \$33 | <http://www.byonics.com/tinytrak/> |
| GPS | 1 | 0 | 0 | \$15 |  |
| Digital Camera | 1 | 0 | 0 | ? | <http://tinyurl.com/ydynpk2> |
| Chassis | 1 | ? | ? | ? | ? |
| Parachute | 1 | \$25 | \$25 | \$25 | <http://rocketchutes.com/> |

## Competition

### Rules

- One team per hackerspace. Any size build team, but only 10 people for the launch and retrieval team.
- Payload must be under 4 pounds.
- Parts cost limit of \$250.00. Must show receipts or have other proof of purchase.
- Payload must return with pictures taken from the flight.
- Only one official launch per team allowed. Notice of official launches must be given by 8 a.m., and a judge must be present for the launch to count.
- All local laws and ordinances must be followed throughout the entire competition.
- The Event Board may judge any other conduct considered outside “the spirit” of the event and disqualify a team that does not adhere to it by majority vote.

### Scoring

- Retrieval Time Base: 50 points. 1 point off for every minute past 45 minutes.
- Weight of Payload 5 points added for every 1/2 pound under 4 lb.
- Cost of Setup Base: 50 points. 0.5 points off for every dollar over \$150.
- Total Points Base 100 + 5 per each -1/2 pound.

### Judging

- Judges are members of each hackerspace, and will be submitted to the Event Board. They will ensure all rules are followed.
- One person from each hackerspace will be on the Event Board. The Event Board will oversee the event, judge each applicant, and declare winners.

### Dates

- Competition starts immediately upon challenges going out.
- Teams will indicate acceptance of challenge by March 1, 2010 (at workshop88.com/space).
- Launches will be held between June 1, 2010 and August 31, 2010.
- Results of the official launch must be sent in by September 7, 2010.
- Winner will be announce on or before September 30, 2010.

## See Also

[Nearspace Balloon 2](Nearspace-Balloon-2)
