use https://pybricks.com/ev3-micropython/ev3devices.html for reference

## Driving Functions
GYRO_HOLD(time)
GYRO_LEFT(angle) 
GYRO_RIGHT(angle) 
GYRO_STRAIGHT(speed, time) 
GYRO_STRAIGHT_DISTANCE(speed, distance) 
GYRO_HOLD(time) 

## Motor Controls: 
motor.stop() 
motor.hold() 
motor.run(speed) 
motor.run_time(speed,time) 
motor.run_target(speed, angle) 
motor.run_until_stalled(speed)

## Sensors:
### Touch Sensor: 
sensor.pressed() 

### Color Sensor 
sensor.color() 
sensor.ambient() 
sensor.reflection() 
sensor.rgb() 

### Ultrasonic Sensor: 
sensor.distance(silent=True/False) 
sensor.presence() 

### Gyroscopic Sensor 
sensor.speed() 
sensor.angle() 
sensor.reset_angle(angle) 

## Attachment Functions:
RESET_ATTACHMENT(side) {left / right} 
ATTACHMENT_SCOOP(direction) {up / down} 
ATTACHMENT_LEVER1(direction) {up / down} 
RIGHT_ATTACHMENT(speed, angle) 
LEFT_ATTACHMENT(speed, angle)
