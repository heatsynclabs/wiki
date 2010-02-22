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

Blackjack II cell phone has a built-in GPS. We can use the free software Mologogo to track the phone.

#### Radio

Blackjack II cell phone IS a radio. It even has two way radio capabilities. Mologogo can use the phone's data network to send the phone's GPS coordinates back to a website. We can then track the balloon by browsing to this website with other cell phones or cell phone enabled laptops.

#### Camera

We can potentially use a used or donated digital camera. Some of these have built in time-lapse functions. If we can't find one that does, we can built a simple timer circuit to push the shutter button every few minutes. We may also be able to write an app for the Blackjack II cell phone to use the camera's built-in camera.

#### Flight Computer

Paul has a Blackjack II cell phone he is willing to donate to this project. The phone has the capabilities to be our computer, GPS, radio, and possibly our camera

#### Batteries

The cell phone already has a battery. If this battery is in good condition it may be sufficient to provide enough power in the cold weather for the length of the mission. It may be a good idea to construct an external battery pack for the phone. The pack can hook up to the phone via it's charging port. This will allow us to drain the external batteries before switching to the phone battery as a backup.

#### Weatherproof container

Can use a styrofoam cooler with insulation. Other's have also used insulated lunch boxes. We can also construct something from scratch if we want.

#### Parachute

Can purchase or construct from scratch

## Pricing

Actual Cost is how much we actually pay for an item. In some cases an item may be donated to us, but the competition states that all items must have a price associated with them. In that case, we must find the donated item for sale somewhere, and record that price in the "Recorded cost" column.

#### Cell Phone Balloon

| Item | Quantity | Actual Cost | Total | Recorded Cost | Source |
|----|----|----|----|----|----|
| 1200 Gram Balloon | 2 | \$45 est | \$90 | \$45 | <http://www.kaymont.com/pages/cold-weather-balloons.cfm> |
| 55CF Helium | 1 | \$38.50 | \$38.50 | \$38.50 | <http://www.azairboutique.com/index.php?option=com_content&view=article&id=52&Itemid=71> |
| Cell Phone | 1 | 0 | 0 | \$40 | Paul R |
| GoPhone (For the prepaid sim card) | 1 | \$30 | \$30 | \$30 | <http://tinyurl.com/y9yxpe3> |
| Cell Phone Antenna | 1 | \$12 | \$12 | \$12 | <http://www.primecellular.com/CM200> |
| Digital Camera | 1 | 0 | 0 | ? | <http://tinyurl.com/ydynpk2> |
| Lunchbox | 1 | \$10 | \$10 | \$10 | <http://tinyurl.com/y85dl4y> |
| Parachute | 1 | \$25 | \$25 | \$25 | <http://rocketchutes.com/> |

#### Ham Radio Balloon

| Item | Quantity | Actual Cost | Total | Recorded Cost | Source |
|----|----|----|----|----|----|
| 1200 Gram Balloon | 2 | \$45 est | \$90 | \$45 | <http://www.kaymont.com/pages/cold-weather-balloons.cfm> |
| 55CF Helium | 1 | \$38.50 | \$38.50 | \$38.50 | <http://www.azairboutique.com/index.php?option=com_content&view=article&id=52&Itemid=71> |
| Radio | 1 | \$40-\$50est | \$40-\$50est | \$40-\$50est | ebay.com (Search "Realistic HTX-202") |
| TNC | 1 | 0 | 0 | \$33 | <http://www.byonics.com/tinytrak/> |
| GPS | 1 |  |  |  |  |
| Digital Camera | 1 | 0 | 0 | ? | <http://tinyurl.com/ydynpk2> |
| Lunchbox | 1 | \$10 | \$10 | \$10 | <http://tinyurl.com/y85dl4y> |
| Parachute | 1 | \$25 | \$25 | \$25 | <http://rocketchutes.com/> |

## Ideas

1.  High Altitude Rendevous
    - Collaborate with another nearby hackerspace to launch balloons simultaneously. These balloons should communicate with each other somehow.
2.  Live Video
    - Use a video transmitter to send live video to ourselves on the ground
    - <http://www.mfjenterprises.com/Product.php?productid=MFJ-8704>
3.  TCP/IP via Radio
    - <http://www.febo.com/hamdocs/intronos.html>

## See Also

[Nearspace_Balloon](Nearspace-Balloon)
