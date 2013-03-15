This page should contain everything you need to know to be allowed to touch the CNC machine:

## Pre-requisites:

Before you can be certified on the CNC mill, you need to be certified on the big Blue Mill. Practice manual milling first.

## Safety

### The Mill Is Dangerous!

The CNC Mill is a rather powerful machine. It is also dumber than a heap of bricks, and needs to be babysat. It can harm, maim, or kill you in a variety of different ways:

- The lead screw and motors are capable of producing up to 2356 lbs of linear force, on the X and Y axis. Combined, that is a peak force of 3331 lbs diagonally.

<!-- -->

- At 1000 RPM, with a 1/4" diameter tool, the 2 horsepower motor can apply as much as 500 lbs of force at the point where the teeth contact the material. This can be even higher with larger gear ratios.

<!-- -->

- The end mills are hard enough and sharp enough to cut steel. Human flesh is butter in comparison.

<!-- -->

- These peak forces are enough to severely damage the machine itself, let alone any stray fingers or foreign objects.

<!-- -->

- The computer has no way of sensing what the machine is actually doing. It cannot tell whether the tool is being crashed into the table, vise, or other obstacle. It can only sense via limit switches when the table is at the extreme of its operating range.

<!-- -->

- The power supply contains very high voltages, charged capacitors full of electricity, and sensitive electronics.

### Safety Rules

To keep yourself, others, and the machine safe, please follow these safety rules:

- Stay within quick reach of the E-STOP while the machine is running.
- Always wear safety glasses while the spindle is turning.
  - Safety glasses must protect the sides of your eyes. Prescription glasses do not count.
- Keep fingers clear of all moving parts.
- Do not run hand-edited G-code.
- Do not open the power supply.
- Unplug the spindle when you are not using it.

## Understand how the mill works

### E-STOP

- Know where it is, know when to press it.

### Stepper Motors

- Know how to move the axis by hand

### Spindle

- Know how to power on, and off
- Know how to adjust belt tension with

### Belts

- Know what gear ratio to be using
- Know how to change the belts

### Ways

- Know how to clean and oil them

### Power Supply

- How to power on, off
- How the motors and sensors should be connected to
- How to never open it up.

### Table

- Know how to securely mount material to the table

## Operating the Mill

### E-STOP Recovery

- Recover from an E-STOP

### Home the Axis

- Home the machine

=== Manually Jogging the Table

- Manually jog the table

### Touch off Tools

- Touch off the tools
- Set any necessary offsets

### Secure Materials to table

### Change Tools

### Power up the machine

## Using MACH3

### How to simulate your G-code program

### How to load G-code

### How to job the table

### How to home the machine

## Checklists!

### BEFORE running a job

1.  Run your G-code in the simulator
2.  Mount the material on the table
3.  Power up the machine controller

### AFTER running a job

1.  Vacuum up any debris
2.  Clean, oil the ways
3.  Put away all tooling, material mounts
4.
