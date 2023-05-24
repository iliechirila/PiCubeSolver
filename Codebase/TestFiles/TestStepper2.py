import RPi.GPIO as GPIO
import time

DIR = 4
STEP = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

GPIO.output(STEP, GPIO.LOW)

# clockwise rotation
GPIO.output(DIR, GPIO.LOW)


steps = 50
delay = 0.01

for i in range(steps):
    print(f"Step {i}")
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(delay)

# counter clockwise
GPIO.output(DIR, GPIO.HIGH)
for i in range(steps):
    print(f"Step {i}")
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(delay)

GPIO.cleanup()