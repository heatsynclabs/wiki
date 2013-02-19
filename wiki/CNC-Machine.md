## The Nature of the Beast

The CNC Mill is a rather powerful machine. It is also dumber than a heap of bricks, and needs to be babysat.

Keep in mind that:

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

## Certification

Before you can use the CNC machine, you must take our CNC machine certification class, so you can learn all the ins and outs of our specific machine.

Being certified on the blue manual mill is a prerequisite to being certified on the CNC mill.

Each of the following sections contains lists of the things you need to know to make safe use of the machine.

## Safety Rules

To keep yourself, others, and the machine safe, please follow these safety rules:

- Stay within quick reach of the E-STOP while the machine is running.
- Always wear safety glasses while the spindle is turning.
  - Safety glasses must protect the sides of your eyes. Prescription glasses do not count.
- Keep fingers clear of all moving parts.
- Do not run hand-edited G-code.
- Do not open the power supply.
- Unplug the spindle when you are not using it.

## [Parts of the Mill](Parts-of-the-Mill)

To be certified, you need to be able to identify all the following parts of the mill:

- E-STOP
- Stepper motors
- Spindle
- Belts
- Ways
- Power Supply
- Table
  - T-slots
- Control computer
- MACH3 Manual

## [Maintenance Tasks](Maintenance-Tasks)

To keep the machine in working order, you need to:

- Vacuum up ALL chips and debris
- Clean and oil the ways

## [Operating the Machine](Operating-the-Machine)

Know how to:

- Recover from an E-STOP
- Home the machine
- Manually jog the table
- Touch off the tools
- Set material offsets
- Change tools
- Fix materials to the table
- Move table by hand
- Power up the machine
- Start and stop spindle
- Manually raise and lower Z axis
- Load a G-code program

## Software Toolchain

To be certified, you need to know MACH3 at a minimum.

But you will need to learn all the programs in the toolchain to design, code, and mill a part.

### CAD

You need to use a CAD program to create the actual design of the part you wish to mill. This can be done in either SolidWorks or AutoCad. Basic CAD functionality is also available in CamBam. For basic projects, that will mean one less program to have to use.

### CAM

CAM software takes the part you created with your CAD software, and generates the necessary G-code to actually mill the part. The G-code is then executed by the machine, creating the part.

There are two CAM programs we will be providing:

- HSMXpress is a SolidWorks plugin for doing g-code generation from within solidworks directly on a part. The express version only comes with the documentation that is in its help file, accessed in the plugin itself.

<!-- -->

- CamBam is the CAM program that can handle most everything, and the manual can be found at <http://www.cambam.info/doc/>
  - A printed CamBam manual is also kept at the CNC workstation.

Both CAM programs are currently installed on the HP workstation on the large wooden table near the electronics station and laser. That computer also has Autocad, which is also very useful for designing parts.

### MACH3

MACH3 is the control software we have chosen to do the actual running of the machine. It reads G-code and executes it on the machine, controlling the stepper motors and spindle in according to the instructions in the G-code

The manual for MACH3 can be downloaded here: <http://www.machsupport.com/documentation.php>

There is also a printed copy in a binder at the CNC workstation.

## Setup Information

Put everything about how the machine should be setup here, especially the settings used in the control software.

LinuxCNC Config Files

[LinuxCNC Inches ini file](LinuxCNC-Inches-ini-file)

[LinuxCNC Pinout](LinuxCNC-Pinout)

## Tips and best practices

Practice manual milling on the blue mill. Certification on the blue mill will be a prerequisite for being certified on the CNC mill.
