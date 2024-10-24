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

GYRO_STRAIGHT_DISTANCE(-230, -500)
DRIVE_STOP()
GYRO_TURN(33, 300)
GYRO_STRAIGHT_DISTANCE(-125, -300)
DRIVE_STOP()
wait(100)
GYRO_STRAIGHT_DISTANCE(125, 150)
GYRO_TURN(-55, 200)
GYRO_STRAIGHT_DISTANCE(-300, -600)
DRIVE_STOP()
GYRO_STRAIGHT_DISTANCE(700, 400)
DRIVE_STOP()