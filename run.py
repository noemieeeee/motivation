import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


motor1_pin1 = 11
motor1_pin2 = 12
motor2_pin1 = 13
motor2_pin2 = 15
enable_pin1 = 33
enable_pin2 = 35


GPIO.setup(motor1_pin1, GPIO.OUT)
GPIO.setup(motor1_pin2, GPIO.OUT)
GPIO.setup(motor2_pin1, GPIO.OUT)
GPIO.setup(motor2_pin2, GPIO.OUT)
GPIO.setup(enable_pin1, GPIO.OUT)
GPIO.setup(enable_pin2, GPIO.OUT)


pwm1 = GPIO.PWM(enable_pin1, 100)
pwm2 = GPIO.PWM(enable_pin2, 100)


pwm1.start(0)
pwm2.start(0)


def move_forward():
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.HIGH)
    GPIO.output(motor2_pin2, GPIO.LOW)
    pwm1.ChangeDutyCycle(50)
    pwm2.ChangeDutyCycle(50)

def move_backward():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.HIGH)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.HIGH)
    pwm1.ChangeDutyCycle(50)
    pwm2.ChangeDutyCycle(50)

def turn_left():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.HIGH)
    GPIO.output(motor2_pin1, GPIO.HIGH)
    GPIO.output(motor2_pin2, GPIO.LOW)
    pwm1.ChangeDutyCycle(50)
    pwm2.ChangeDutyCycle(50)

def turn_right():
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.HIGH)
    pwm1.ChangeDutyCycle(50)
    pwm2.ChangeDutyCycle(50)

def stop():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.LOW)
    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)


move_forward()
time.sleep(2)
stop()
time.sleep(1)
move_backward()
time.sleep(2)
stop()
time.sleep(1)
turn_left()
time.sleep(1)
stop()
time.sleep(1)
turn_right()
time.sleep(1)
stop()


pwm1.stop()
pwm2.stop()


GPIO.cleanup()
