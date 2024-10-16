from setup import *
import math

def DRIVE_STOP():
    robot.stop()
    robot.stop()
    left_drive_motor.brake()
    right_drive_motor.brake()
    wait(100)
    left_drive_motor.stop()
    right_drive_motor.stop()
# -----------------------------------------------------------------------------------

def GYRO_HOLD(time):
    # get starting angle and starting time (milis)
    straight_angle = gyro_sensor.angle()
    starting_time = stopwatch.time()
    # get ending time
    ending_time = starting_time + time
    sensitivity = 4
    # loop until ending time is reached
    while stopwatch.time() <= ending_time:
        # drive forward, correcting angle.   multiply gyro_sensor.angle for sensitivity
        current_angle = gyro_sensor.angle()
        error = current_angle - straight_angle
        drive_angle = -error * sensitivity  # multiply error by sensitivity
        robot.drive(0, -drive_angle)
    robot.stop()

# -----------------------------------------------------------------------------------

# time is in miliseconds
def GYRO_STRAIGHT(speed, time):
    starting_time = stopwatch.time()
    robot.reset()
    print("straight")
    # get starting angle
    straight_angle = gyro_sensor.angle()
    print(straight_angle)
    
    ending_time = starting_time + time
    
    sensitivity = 5  # adjust this value to change the sensitivity
    # loop until distance is achieved
    while -robot.distance() <= ending_time:
        # drive forward, correcting angle
        current_angle = gyro_sensor.angle()
        error = current_angle - straight_angle
        drive_angle = -error * sensitivity  # multiply error by sensitivity
        robot.drive(-speed, -drive_angle)
        print(drive_angle)
    robot.stop()

# -----------------------------------------------------------------------------------

# time is in miliseconds
def GYRO_STRAIGHT_DISTANCE(speed, distance):
    robot.reset()
    print("straight")
    # get starting angle
    straight_angle = gyro_sensor.angle()
    print(straight_angle)
    
    starting_distance = robot.distance()
    desired_distance = starting_distance + distance
    sensitivity = 8  # adjust this value to change the sensitivity
    # loop until distance is achieved
    while robot.distance() >= -desired_distance:
        # drive forward, correcting angle
        current_angle = gyro_sensor.angle()
        error = current_angle - straight_angle
        drive_angle = -error * sensitivity  # multiply error by sensitivity
        robot.drive(-speed, -drive_angle)
        print(robot.distance())
    robot.stop()

# -----------------------------------------------------------------------------------


def GYRO_LEFT(angle):
    # get desired turn angle derived from base gyro angle
    starting_angle = gyro_sensor.angle()    
    desired_angle = starting_angle + angle

    # coarse turn
    while gyro_sensor.angle() <= desired_angle:
        robot.drive(0, -120)

    # fine, slower turn for correction
    while gyro_sensor.angle() >= desired_angle: 
        robot.drive(0, 20)



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


def PLAY_NOTES(event):
    if event == "confirm":
        ev3.speaker.beep(frequency=1000, duration=50)
        wait(20)
        ev3.speaker.beep(frequency=800, duration=50)
        wait(20)
        ev3.speaker.beep(frequency=1000, duration=50)
        wait(20)
        ev3.speaker.beep(frequency=1200, duration=50)
    elif event == "cancel":
        ev3.speaker.beep(frequency=400, duration=50)
        wait(20)
        ev3.speaker.beep(frequency=600, duration=50)
        wait(20)
        ev3.speaker.beep(frequency=400, duration=50)
        wait(20)
        ev3.speaker.beep(frequency=200, duration=50)
    elif event == "warning":
        ev3.speaker.beep(frequency=400, duration=50)
        wait(20)
        ev3.speaker.beep(frequency=400, duration=50)
        wait(20)
        ev3.speaker.beep(frequency=400, duration=50)
        wait(20)
    else:
        wait(20)