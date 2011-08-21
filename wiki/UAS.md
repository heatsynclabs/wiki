<div style="float: right">

</div>

UAS is either **Unmanned Aerial Sensor** or **Unmanned Aircraft System**

## What

The goal of this project is to create an Automatic Flight System for use, initially, on inexpensive R/C aircraft. We intend to do this using low cost Arduino (or Arduino-like) development boards, an [IMU](http://en.wikipedia.org/wiki/Inertial_navigation_system), and GPS. As our confidence in the system grows, we intend to grow the project to control larger drones capable of greater range and payload.

### Demonstration Goals

- Command surfaces.
- Command throttle.
- Demonstrate RTS/preflight.
- Unpowered straight line flight coupled with "safe" landing.
- Powered, short straight line flight coupled with "safe" landing.
- Fly an oval retaining a static altitude
- Circle up to altitude, then circle back down and land.
- Circle up to altitude, then dive down and land.
- Perform multiple "Go Around" test landing passes.
- Fly a longer flight plan.
- Test failure modes.
- Bonus: attempt to fly thermals!
- Bonus: aerobatics!

## Why

Because it interests us.

Of course, this is nothing new. It's all been done before, but not by us.

### Practical Uses

This are some interesting, potentially practical uses:

- RF data repeater
- Search drone (e.g. missing hikers)
- Wildfire spotter

## Who

- Scott B.
- Jeremy M.
- Mike M.

## Design

See [UAS/Design](UAS-Design)

## Implementation

- Hardware [UAS/Initial_BOM](UAS-Initial-BOM)
- Software [UAS/Software](UAS-Software)

#### Assumptions

# See Also

- [INS](http://en.wikipedia.org/wiki/Inertial_navigation_system) @ Wikipedia
- [American Model Aircraft](https://www.modelaircraft.org)
- [DIYDrones Regulator page](http://diydrones.com/profiles/blog/show?id=705844%3ABlogPost%3A28583)
