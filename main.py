#!/usr/bin/env pybricks-micropython
from setup import *
from functions import *

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

PLAY_NOTES("confirm")


while True:
    # Get pressed buttons
    ev3ButtonsPressed = ev3.buttons.pressed()

    # Run run1.py on Up Button
    if Button.UP in ev3ButtonsPressed:
        with open("run1.py") as file:
            exec(file.read())

    # Run run5.py on Down Button
    elif Button.DOWN in ev3ButtonsPressed:
        with open("run5.py") as file:
            exec(file.read())

    # Run run2.py on Left Button
    elif Button.LEFT in ev3ButtonsPressed:
        with open("run2.py") as file:
            exec(file.read())

    # Run run4.py on Right Button
    elif Button.RIGHT in ev3ButtonsPressed:
        with open("run4.py") in ev3ButtonsPressed:
            exec(file.read())

    # Run run3.py on Center Button
    elif Button.CENTER in ev3Buttons.Pressed:
        with open("run3.py") as file:
            exec(file.read())

    else:
        wait(50)

