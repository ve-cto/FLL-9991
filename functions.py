from setup import *


def GYRO_HOLD(time):
    # get starting angle and starting time (milis)
    straight_angle = gyro_sensor.angle()
    starting_time = stopwatch.time()
    # get ending time
    ending_time = starting_time + time
    
    # loop until ending time is reached
    while stopwatch.time() <= ending_time:
        # drive forward, correcting angle.   multiply gyro_sensor.angle for sensitivity
        robot.drive(0, -straight_angle + (gyro_sensor.angle() * 4))
    robot.stop()

# -----------------------------------------------------------------------------------

# time is in miliseconds
def GYRO_STRAIGHT(speed, time):
    # get starting angle and starting time (milis)
    straight_angle = gyro_sensor.angle()
    starting_time = stopwatch.time()
    # get ending time
    ending_time = starting_time + time
    
    # loop until ending time is reached
    while stopwatch.time() <= ending_time:
        # drive forward, correcting angle.   multiply gyro_sensor.angle for sensitivity
        robot.drive(-speed, -straight_angle + (gyro_sensor.angle() * 4))
    robot.stop()
# -----------------------------------------------------------------------------------

# time is in miliseconds
def GYRO_STRAIGHT_DISTANCE(speed, distance):
    # get starting angle
    straight_angle = gyro_sensor.angle()
    starting_distance = robot.distance()
    desired_distance = starting_distance + distance
    print(starting_distance)
    print(desired_distance)
    # loop until distance is achieved
    while -robot.distance() <= desired_distance:
        # drive forward, correcting angle.   multiply gyro_sensor.angle for sensitivity
        robot.drive(-speed, -straight_angle + (gyro_sensor.angle() * 4))
        print(-robot.distance())
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
