# Inertial Measurement Unit (IMU)

The IMU was are going to create will consist of an 3 axis acceleration, a 3axis gyroscope, a 3 axis magnetometer, and a barometer. These combined will give us 10 degrees of freedom.

some algorithum i found

- Read the 3 axis magnetometer data

<!-- -->

- Calculate the "tilt compensated" x and y magnetic component (standard formulation):
  - CMx = mag_x\*cos(pitch) + mag_y\*sin(roll)sin(pitch) + mag_z\*cos(roll)sin(pitch) CMy = mag_y\*cos(roll) - mag_z\*sin(roll)

<!-- -->

- Calculate the magnetic heading with this compensated components:
  - MAG_Heading = Atan(CMy/CMx)

<http://code.google.com/p/sf9domahrs/> might have the code we are looking for.
