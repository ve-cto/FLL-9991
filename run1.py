#!/usr/bin/env pybricks-micropython
from setup import *
from functions import *
from attachmentfunctions import *

# GYRO_LEFT(angle)
# GYRO_RIGHT(angle)
# GYRO_STRAIGHT(speed, time)
# GYRO_STRAIGHT_DISTANCE(speed, distance)
# GYRO_HOLD(time)

# Motor Controls:
# motor.stop()
# motor.hold()
# motor.run(speed)
# motor.run_time(speed,time)
# motor.run_target(speed, angle)
# motor.run_until_stalled(speed)

# Touch Sensor:
# sensor.pressed()

# Color Sensor
# sensor.color()
# sensor.ambient()
# sensor.reflection()
# sensor.rgb()

# Ultrasonic Sensor:
# sensor.distance(silent=True/False)
# sensor.presence()

# Gyroscopic Sensor
# sensor.speed()
# sensor.angle()
# sensor.reset_angle(angle)

# RESET_ATTACHMENT(side) {left / right}
# ATTACHMENT_SCOOP(direction) {up / down}
# ATTACHMENT_LEVER1(direction) {up / down}

# RIGHT_ATTACHMENT(speed, angle)
# LEFT_ATTACHMENT(speed, angle)
# ---------------------------------------------------------------

PLAY_NOTES("confirm")
RESET_ATTACHMENT("right")
right_attachment_motor.run_target(200, -200)
GYRO_STRAIGHT_DISTANCE(-590, -200)
right_attachment_motor.run(-150)
robot.drive(-75,-180)
wait(4000)
DRIVE_STOP()
right_attachment_motor.stop()
GYRO_STRAIGHT_DISTANCE(-590, -400)