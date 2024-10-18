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


# initialize the ev3
ev3 = EV3Brick()

# initialize the stopwatch
stopwatch = StopWatch()

# define the attachment motors
left_attachment_motor = Motor(Port.A)
right_attachment_motor = Motor(Port.D)
# put the two attachment motors in an array for sequencial control
attachment_motors = [left_attachment_motor, right_attachment_motor]

# define the two drive motors
left_drive_motor = Motor(Port.B)
right_drive_motor = Motor(Port.C)

# group left_motor and right_motor into the drive base (robot) and define specifications
robot = DriveBase(left_drive_motor, right_drive_motor, wheel_diameter=60, axle_track=115)

robot_brake = [left_drive_motor, right_drive_motor]

# initialize default driving settings
ROBOT_SPEED = 400
ROBOT_ACCELERATION = 100
ROBOT_TURN_SPEED = 90
ROBOT_TURN_ACCELERATION = 80
robot.settings(ROBOT_SPEED, ROBOT_ACCELERATION, ROBOT_TURN_SPEED, ROBOT_TURN_ACCELERATION)


# define the gyro sensor on port 3 and reset it's angle
gyro_sensor = GyroSensor(Port.S3)
gyro_sensor.reset_angle(0)

