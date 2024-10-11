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


# Create your objects here.
ev3 = EV3Brick()

# define the attachment motors
motor_a = Motor(Port.A)
motor_d = Motor(Port.D)

# define the drive motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# group left_motor and right_motor into the drive base (robot)
robot = DriveBase(left_motor, right_motor, wheel_diameter=60, axle_track=115)

# default driving settings
robot.settings(500, 200, 90, 200)




# set the gyro to 1
gyro_sensor = GyroSensor(Port.S1)
gyro_sensor.reset_angle(0)


# put the two attachment motors in an array
attachment_motors = [motor_a, motor_d]



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def GYRO_STRAIGHT(speed):
    straight_angle = gyro_sensor.angle()
    print(straight_angle)
    while True:
        robot.drive(speed, straight_angle - gyro_sensor.angle())


def GYRO_LEFT(angle):
    # get desired turn angle derived from base gyro angle
    starting_angle = gyro_sensor.angle()    
    desired_angle = starting_angle - angle
    # print desired to console for debugging
    

    # coarse turn
    while gyro_sensor.angle() >= desired_angle:
        robot.drive(0, 80)
    
    # fine, slower turn for correction
    while gyro_sensor.angle() <= desired_angle: 
        robot.drive(0, -20)

    # stop
    robot.stop()

def GYRO_RIGHT(angle):
    # get desired turn angle derived from base gyro angle
    starting_angle = gyro_sensor.angle()    
    desired_angle = starting_angle + angle
    # print desired to console for debugging

    # coarse turn
    while gyro_sensor.angle() <= desired_angle:
        robot.drive(0, -80)
    
    # fine, slower turn for correction
    while gyro_sensor.angle() >= desired_angle: 
        robot.drive(0, 20)

    # stop
    robot.stop()


# Write your program here.
ev3.speaker.beep()




GYRO_LEFT(90)



ev3.speaker.beep(frequency=1000, duration=500)