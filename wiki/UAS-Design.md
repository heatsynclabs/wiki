## Architecture

Maybe the following subsystems exist:?

### Navigation (NAV)

This subsystem calculates location, orientation, and--maybe--HAGL.

### Return to Service (RTS) and Preflight

This subsystem should perform RTS (return to service)/preflight testing of the craft. I suppose it will come with a checklist so the maintenance person knows when to invert it, etc, so it can test it's various sensors.

RTS should not pass if Maintenance has stored a fault. Until formally cleared.

### Maintenance (MAINT) and Logger

This subsystem should capture and store faults (e.g. failure of a sensor).

### Flight Plan (FP)

This subsystem should feed the flight plan to the Pilot.

This should interface w/ COMS to enable flight plan updating.

### Pilot

This is the thing that takes inputs from NAV and FP and commands servos and throttles. This flys the craft.

### Auto Land

The auto land subsystem takes over (when directed) to provide inputs to the Pilot to create a safe, clean landing.

### Communications (COMS)

This is a 2 part subsystem: USB and RF. behavior shall be different in USB vs RF mode. Also will be different if we are on ground.

COMS should generally provide a way for the base station to talk to the various subsystems of the drone. This should allow for things like:

- querying the DATALOG.
- querying the FP.
- Changing the FP
- subscribing to data (e.g. telemetry information, %to next waypoint)
- return to base

## Random Thoughts

What do our emergency modes look like and where do they go?

How do we monitor the battery? (Shut the engine off and glide in for a landing?)
