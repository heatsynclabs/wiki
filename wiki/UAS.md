<div style="float: right">

</div>

## What

Arduino based auto-flight, auto-land drone.

### Goals

- Command surfaces.
- Command throttle.
- Demonstrate RTS/preflight.
- Short, straight line flight coupled with "safe" landing.
- Fly an oval retaining a static altitude
- Circle up to altitude, then circle back down and land.
- Circle up to altitude, then dive down and land.
- Perform multiple "Go Around" test landing passes.
- Fly a longer flight plan.
- Test failure modes.
- Bonus: attempt to fly thermals!

## Why

Because it interests us.

Of course, this is nothing new. It's all been done before, but not by us.

## Who

## Design

going to take an arduino, or arduino like system, and have it control a model airplane. This drone will have an on board GPS for position (3D), heading, and speed. Will need the Gyro to know if we are level, or to hold a certain position in a bank or turning maneuver.

See [Drone/Design](Drone-Design)

## Bill of Materials (BOM)

### Auto Pilot

- [Maple Mini](http://leaflabs.com/devices/#Maple-Mini) as the in craft controller?
- [GPS Receiver](http://www.sparkfun.com/products/465) ~\$60.00
- accelerometer or Gyro (3 axis)
- Proximity sensors (for autoland)

### Aircraft

- [Bixler](http://www.hobbyking.com/hobbyking/store/__18083__Hobbyking_Bixler_EPO_1400mm_ARF_USA_Warehouse_.html) Looks like a good place to start. Lots of surfaces to control, plenty of room for avionics, and reasonably priced.

Some other fun aircraft:

- [HobbyKing SkyFun](http://www.hobbyking.com/hobbyking/store/uh_viewItem.asp?idProduct=9614) as the craft
  - Note: make sure to get a redundant craft. I, or my s/w defect, will surely crash and destroy one...
- [Servos](http://www3.towerhobbies.com/cgi-bin/wti0001p?&I=LXHHB0&P=0) X 3 (two control surfaces plus throttle)
- [Predator](http://www.hobbyking.com/hobbyking/store/__5455__Predator_UAV_74in_Spy_Plane_ARF.html) Fairly large. Lots of goodness?
  - [review](http://www.hobbyking.com/hobbyking/forum/forum_posts.asp?TID=719) great info.
- [Reaper](http://www.hobbyking.com/hobbyking/store/__17988__MQ_9_Reaper_Fiberglass_2500mm_FPV_ARF_.html) cool.

### Coms

- XBee PRO 900 XSC? or...?

### Misscelaneous

- [Camera?](http://www.hobbyking.com/hobbyking/store/uh_viewItem.asp?idProduct=13987)

#### Assumptions

# See Also

- [INS](http://en.wikipedia.org/wiki/Inertial_navigation_system) @ Wikipedia
