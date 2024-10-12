#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# define the EV3 as ev3 (duh).
ev3 = EV3Brick()

stopwatch = StopWatch()

# define the attachment motors
left_attachment = Motor(Port.A)
right_attachment = Motor(Port.D)
# put the two attachment motors in an array for easier control
attachment_motors = [left_attachment, right_attachment]

# define the drive motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# group left_motor and right_motor into the drive base (robot)
robot = DriveBase(left_motor, right_motor, wheel_diameter=60, axle_track=115)

# default driving settings
robot.settings(500, 200, 90, 200)


# identify the gyro sensor on port 1
gyro_sensor = GyroSensor(Port.S3)
gyro_sensor.reset_angle(0)


# identify the rangefinder on port 2
# distance_sensor = UltrasonicSensor(Port.S2)