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


# define the attachment motors
motor_a = Motor(Port.A)
motor_d = Motor(Port.D)
# put the two attachment motors in an array for easier control
attachment_motors = [motor_a, motor_d]

# define the drive motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# group left_motor and right_motor into the drive base (robot)
robot = DriveBase(left_motor, right_motor, wheel_diameter=60, axle_track=115)

# default driving settings
robot.settings(500, 200, 90, 200)


# identify the gyro sensor on port 1
gyro_sensor = GyroSensor(Port.S1)
gyro_sensor.reset_angle(0)


# identify the rangefinder on port 2
# distance_sensor = UltrasonicSensor(Port.S2)



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------


def GYRO_STRAIGHT(speed):
    straight_angle = gyro_sensor.angle()
    print(straight_angle)
    while True:
        robot.drive(speed, straight_angle - gyro_sensor.angle())

# -----------------------------------------------------------------------------------

def GYRO_LEFT(angle):
    # get desired turn angle derived from base gyro angle
    starting_angle = gyro_sensor.angle()    
    desired_angle = starting_angle + angle

    # coarse turn
    while gyro_sensor.angle() <= desired_angle:
        robot.drive(0, -120)
        print(gyro_sensor.angle())

    # fine, slower turn for correction
    while gyro_sensor.angle() >= desired_angle: 
        robot.drive(0, 20)
        print(gyro_sensor.angle())

    # stop
    robot.stop()


# -----------------------------------------------------------------------------------

def GYRO_RIGHT(angle):
    # get desired turn angle derived from base gyro angle
    starting_angle = gyro_sensor.angle()    
    desired_angle = starting_angle - angle

    # coarse turn
    while gyro_sensor.angle() >= desired_angle:
        robot.drive(0, 120)
        print(gyro_sensor.angle())

    # fine, slower turn for correction
    while gyro_sensor.angle() <= desired_angle: 
        robot.drive(0, -20)
        print(gyro_sensor.angle())
        
    # stop
    robot.stop()


# -----------------------------------------------------------------------------------


ev3.speaker.beep()

GYRO_RIGHT(180)
print(gyro_sensor.angle())
wait(500)
GYRO_LEFT(180)
print(gyro_sensor.angle())

ev3.speaker.beep()
wait(20)
ev3.speaker.beep()
# ev3.speaker.beep(frequency=1000, duration=500)