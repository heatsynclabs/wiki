<div style="float: right">

</div>

## What

Arduino based auto-flight, auto-land drone.

## Why

Because it interests us.

Of course, this is nothing new. It's all been done before, but not by us.

## Who

## Design

going to take an arduino, or arduino like system, and have it control a model airplane. This drone will have an on board GPS for position (3D), heading, and speed. Will need the Gyro to know if we are level, or to hold a certain position in a bank or turning maneuver.

### Architecture

Maybe the following subsystems exist:?

#### Navigation (NAV)

This subsystem calculates location, orientation, and--maybe--HAGL.

#### Return to Service (RTS) / Preflight

This subsystem should perform RTS (return to service)/preflight testing of the craft. I suppose it will come with a checklist so the maintenance person knows when to invert it, etc, so it can test it's various sensors.

RTS should not pass if Maintenance has stored a fault. Until formally cleared.

#### Maintenance (MAINT)

This subsystem should capture and store faults (e.g. failure of a sensor).

#### Flight Plan (FP)

This subsystem should feed the flight plan to the Pilot.

This should interface w/ COMS to enable flight plan updating.

#### Pilot

This is the thing that takes inputs from NAV and FP and commands servos and throttles. This flys the craft.

Somehow, COMS should probably be allowed to command the craft. This might go through FP or may be an override.

#### Communications (COMS)

This is a 2 part subsystem: USB and RF. behavior shall be different in USB vs RF mode. Also will be different if we are on ground.

#### Random Thoughts

What do our emergency modes look like and where do they go?

How do we monitor the battery? (Shut the engine off and glide in for a landing?)

## Bill of Materials (BOM)

### Auto Pilot

- [Maple Mini](http://leaflabs.com/devices/#Maple-Mini) as the in craft controller?
- [GPS Receiver](http://www.sparkfun.com/products/465) ~\$60.00
- accelerometer or Gyro (3 axis)

### Plane

- [HobbyKing SkyFun](http://www.hobbyking.com/hobbyking/store/uh_viewItem.asp?idProduct=9614) as the craft
  - Note: make sure to get a redundant craft. I, or my s/w defect, will surely crash and destroy one...
- [Servos](http://www3.towerhobbies.com/cgi-bin/wti0001p?&I=LXHHB0&P=0) X 3 (two control surfaces plus throttle)

#### Assumptions
