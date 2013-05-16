See [CNC Mill Notes](CNC-Mill-Notes) for notes made in preparation for teaching a class.

## Certification

Before you can use the CNC machine, you must take our **CNC Machine [Certification Class](Certification-Class)**, so you can learn all the ins and outs of our specific machine.

Being certified on the blue manual mill is a prerequisite to being certified on the CNC mill.

**You will need to know the information outlined in the sections titled Safety Rules, Parts of the Mill, Maintenance Tasks, Operating the Machine, and Software Toolchain.**

## Safety Rules

To keep yourself, others, and the machine safe, please follow these safety rules:

- Stay within quick reach of the E-STOP while the machine is running.
- Always wear safety glasses while the spindle is turning.
  - Safety glasses must protect the sides of your eyes. Prescription glasses do not count.
- Keep fingers clear of all moving parts.
- Do not run hand-edited G-code.
- Do not open the power supply.
- Unplug the spindle when you are not using it.

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

## Miscellaneous Information

LinuxCNC is also installed on the computer, which is setup as a dual-boot. These are the config files:

LinuxCNC Config Files

[LinuxCNC Inches ini file](LinuxCNC-Inches-ini-file)

[LinuxCNC Pinout](LinuxCNC-Pinout)
