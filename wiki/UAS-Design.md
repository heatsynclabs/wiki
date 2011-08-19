<div style="float: right">

</div>

Return to [UAS](UAS)

## Architecture

Maybe the following subsystems exist:?

### Navigation (NAV)

This subsystem calculates location, orientation, and--maybe--HAGL.

### Return to Service (RTS) and Preflight

This subsystem should perform RTS (return to service) and preflight testing of the craft.

RTS is only available via USB and should include instructions for the operator (e.g. invert the aircraft, visually confirm the elevator moves to maximum down position).

RTS should not pass if Maintenance has stored a fault. Until formally cleared. Also, the aircraft should not take off with an active RTS fault.

Preflight should be a standard, on ground operation of all control surfaces. It is activated via push button and cycles the test (with a few second timeout) until the operator pushes the button again, but only after a full preflight cycle.

### Maintenance (MAINT) and Logger

This subsystem should capture and store faults (e.g. failure of a sensor).

### Flight Plan (FP)

This subsystem should feed the flight plan to the Pilot.

This should interface w/ COMS to enable flight plan updating.

### Pilot (AP)

This is the thing that takes inputs from NAV and FP and commands servos and throttles. This flys the craft.

### Auto Land (AL)

The auto land subsystem takes over (when directed) to provide inputs to the Pilot to create a safe, clean landing. In all likely hood, AL is a mode inside AP, NOT a full subsystem...

### Communications (COMS)

This is a 2 part subsystem: USB and RF. behavior shall be different in USB vs RF mode. Also will be different if we are on ground.

COMS should generally provide a way for the base station to talk to the various subsystems of the drone. This should allow for things like:

- querying the DATALOG.
- querying the FP.
- Changing the FP
- subscribing to data (e.g. telemetry information, %to next waypoint)
- return to base
- Take Off
- Go Around

## Random Thoughts

What do our emergency modes look like and where do they go?

How do we monitor the battery? (Shut the engine off and glide in for a landing?)

## Software Design

How they system is layout in software. [UAS/Design/Software](UAS-Design-Software)
