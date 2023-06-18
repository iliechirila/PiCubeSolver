import RPi.GPIO as GPIO
import time

#=================== STEPPER 1 =============

DIR = 4
STEP = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

GPIO.output(STEP, GPIO.LOW)

# clockwise rotation
GPIO.output(DIR, GPIO.LOW)

#=================== STEPPER 2 =============
DIR2 = 17
STEP2 = 27

GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)

GPIO.output(STEP2, GPIO.LOW)

# clockwise rotation
GPIO.output(DIR2, GPIO.LOW)



def stepper_command(steps=100, delay=0.01, dir_pin=4, step_pin=3, rotation="CW"):
    rotation_pol = GPIO.LOW
    if rotation=="CW":
        rotation_pol = GPIO.LOW
    elif rotation=="CCW":
        rotation_pol = GPIO.HIGH
    
    GPIO.output(dir_pin, rotation_pol)
    for i in range(steps):
        print(f"Step {i}")
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(delay)

# stepper_command(steps=10, dir_pin=4, step_pin=3, rotation="CW")
# stepper_command(steps=10, dir_pin=4, step_pin=3, rotation="CCW")

stepper_command(steps=10, dir_pin=DIR2, step_pin=STEP2, rotation="CW")
stepper_command(steps=10, dir_pin=DIR2, step_pin=STEP2, rotation="CCW")

# stepper_command(steps=10, dir_pin=17, step_pin=27, rotation="CCW")


GPIO.cleanup()