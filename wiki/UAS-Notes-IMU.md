# Inertial Measurement Unit (IMU)

The IMU was are going to create will consist of an 3 axis acceleration, a 3axis gyroscope, a 3 axis magnetometer, and a barometer. These combined will give us 10 degrees of freedom.

**6 dof algorithm**\
Here is what our algorithm will do:\
\- accelerometer tells us: "You are now at position Racc"\
\- we say "Thank you, but let me check",\
\- then correct this information with gyroscope data as well as with past Rest data and we output a new estimated vector Rest.\
\- we consider Rest to be our "best bet" as to the current position of the device.\

some algorithum i found

- Read the 3 axis magnetometer data

<!-- -->

- Calculate the "tilt compensated" x and y magnetic component (standard formulation):
  - CMx = mag_x\*cos(pitch) + mag_y\*sin(roll)sin(pitch) + mag_z\*cos(roll)sin(pitch) CMy = mag_y\*cos(roll) - mag_z\*sin(roll)

<!-- -->

- Calculate the magnetic heading with this compensated components:
  - MAG_Heading = Atan(CMy/CMx)

<http://code.google.com/p/sf9domahrs/> might have the code we are looking for.
