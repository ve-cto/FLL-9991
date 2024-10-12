#!/usr/bin/env pybricks-micropython
from setup import *
from functions import *

ev3.speaker.beep()
wait(20)

GYRO_LEFT(90)
wait(500)
GYRO_RIGHT(90)
# GYRO_RIGHT(180)
# print(gyro_sensor.angle())
# wait(500)
# GYRO_LEFT(180)
# print(gyro_sensor.angle())


ev3.speaker.beep()
wait(20)
ev3.speaker.beep(frequency=1000, duration=100)
