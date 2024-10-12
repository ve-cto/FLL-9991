#!/usr/bin/env pybricks-micropython
from setup import *
from functions import *


# GYRO_LEFT(angle)
# GYRO_RIGHT(angle)
# GYRO_STRAIGHT(time, speed)
# GYRO_STRAIGHT_DISTANCE(time, distance)
# GYRO_HOLD(time)


ev3.speaker.beep()
wait(20)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
GYRO_LEFT(180)
wait(20)
GYRO_STRAIGHT_DISTANCE(300, 2000)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

ev3.speaker.beep()
wait(20)
ev3.speaker.beep(frequency=1000, duration=100)
