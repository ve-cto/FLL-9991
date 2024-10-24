from setup import *
import math

def DRIVE_STOP():
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
    DRIVE_STOP()

# -----------------------------------------------------------------------------------

def GYRO_STRAIGHT(time, speed):
    # reset robot distancd and gyro
    robot.reset()
    gyro_sensor.reset_angle(0)
    ending_time = time + stopwatch.time()

    # define gain, increase this value to be more sensitive to interactions
    # excessively high gain may cause wobbling
    PROP_GAIN = 2.0
    while stopwatch.time() <= ending_time:
        angle_compensate = -PROP_GAIN * gyro_sensor.angle()
        robot.drive(speed, angle_compensate)
    DRIVE_STOP()
    
# -----------------------------------------------------------------------------------

def GYRO_STRAIGHT_DISTANCE(distance, speed):
    # reset robot distancd and gyro
    robot.reset()
    gyro_sensor.reset_angle(0)

    # define gain, increase this value to be more sensitive to interactions
    # excessively high gain may cause wobbling
    PROP_GAIN = 2.0
    if distance > 0:
        while robot.distance() < distance:
            angle_compensate = PROP_GAIN * gyro_sensor.angle()
            robot.drive(speed, angle_compensate)
        DRIVE_STOP()
    elif distance < 0:
        while robot.distance() > distance:
            angle_compensate = PROP_GAIN * gyro_sensor.angle()
            robot.drive(speed, angle_compensate)
        DRIVE_STOP()

# -----------------------------------------------------------------------------------
        
def GYRO_TURN(angle, speed):
    gyro_sensor.reset_angle(0)
    desired_angle = angle + 3
    if angle < 0:
        while gyro_sensor.angle() >= angle:
            robot.drive(0, speed)
            wait(10)
            
        while gyro_sensor.angle() <= desired_angle: 
            robot.drive(0, -20)
            wait(10)
    elif angle > 0:
        while gyro_sensor.angle() < angle:
            robot.drive(0, -speed)
            wait(10)
            
        while gyro_sensor.angle() >= desired_angle: 
            robot.drive(0, 20)
            wait(10)
    else:
        print("Error! you did an oopsie and didn't define a speed")

    # robot.brake()
    DRIVE_STOP()

# -----------------------------------------------------------------------------------

# play a sequence of notes as action responses
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
        
# -----------------------------------------------------------------------------------
