import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)


def pin_on(pin_num):
    GPIO.output(pin_num, GPIO.HIGH)
    
def pin_off(pin_num):
    GPIO.output(pin_num, GPIO.LOW)


print("INITIAL DELAY")
time.sleep(5)


pin_on(3)
print("TURNED ON")
time.sleep(5)

pin_off(3)
print("TURNED OFF")
time.sleep(5)