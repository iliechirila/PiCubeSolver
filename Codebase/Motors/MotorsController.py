import time
import RPi.GPIO as GPIO

ENABLE_INDEX = 2
STEP_INDEX = 1
DIR_INDEX = 0

class MotorsController:
    def __init__(self):
        self.pins_config = dict()
        self.rot_steps = {"cw": 50, "ccw": 50, "dt": 100}

    def add_pins_configuration(self, motor_name: str, dir_pin: int, step_pin: int, enable_pin: int):
        GPIO.setup(dir_pin, GPIO.OUT)
        GPIO.setup(step_pin, GPIO.OUT)
        GPIO.setup(enable_pin, GPIO.OUT)
        GPIO.output(step_pin, GPIO.LOW)
        GPIO.output(enable_pin, GPIO.HIGH)
        GPIO.output(dir_pin, GPIO.LOW)
        self.pins_config.update({motor_name: [dir_pin, step_pin, enable_pin]})

    def command_stepper(self, move, RPM):
        face, rot_type = move
        steps_per_rev = 200
        delay = 60 / (RPM * steps_per_rev)
        ENABLE = self.pins_config[face][ENABLE_INDEX]
        DIR = self.pins_config[face][DIR_INDEX]
        STEP = self.pins_config[face][STEP_INDEX]
        rotation_pol = GPIO.LOW
        if rot_type == "cw":
            rotation_pol = GPIO.LOW
        elif rot_type == "ccw":
            rotation_pol = GPIO.HIGH

        GPIO.output(ENABLE, GPIO.LOW)
        GPIO.output(DIR, rotation_pol)
        for i in range(self.rot_steps[rot_type]):
            print(f"Step {i}")
            GPIO.output(STEP, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            time.sleep(delay)
        GPIO.output(ENABLE, GPIO.HIGH)

    def solve_cube(self, solution_tuples: list, rpm: int):
        for move in solution_tuples:
            self.command_stepper(move, RPM=rpm)
            time.sleep(0.1) # let the motors breathe