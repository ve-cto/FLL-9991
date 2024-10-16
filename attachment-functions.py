from setup import *
from functions import *

# This file is for attachment-specific functions, such as moving a specific attachment a custom amount, or at a specific speed.

# -----------------------------------------------------------------------------------

def ATTACHMENT_LEVER1(direction):
    if direction == "up":
        left_attachment_motor.run_until_stalled(300)
    else: 
        left_attachment_motor.run_until_stalled(-300)

# -----------------------------------------------------------------------------------

def ATTACHMENT_SCOOP(direction):
    if direction == "up":
        right_attachment_motor.run_target(500, 320)
        print(right_attachment.angle())
    else:
        right_attachment_motor.run_target(500, 0)
        print(right_attachment.angle())

# -----------------------------------------------------------------------------------

def RESET_ATTACHMENT(attachment):
    if attachment == "left":
        left_attachment_motor.run_until_stalled(-600)
        right_attachment_motor.reset_angle(0)
    else: 
        right_attachment_motor.run_until_stalled(-600)
        wait(100)
        right_attachment_motor.run_time(200, 400)
        right_attachment_motor.reset_angle(0)

# -----------------------------------------------------------------------------------

def RIGHT_ATTACHMENT(speed, angle):
    desired_angle = (angle * 0.833) * 2
    right_attachment_motor.run_target(speed, desired_angle)

# -----------------------------------------------------------------------------------

def LEFT_ATTACHMENT(speed, angle):
    desired_angle = (angle * 0.833) * 2
    left_attachment_motor.run_target(speed, desired_angle)

# -----------------------------------------------------------------------------------