# PIR Motion Test
# Alexandra Fuhs & Tony Yu
# 1/24/18

import RPi.GPIO as GPIO
import time

# Setting up the LED pins
GPIO.setmode(GPIO.BCM)
PIR_pin = 12
LED_pin = 22
button = 6

GPIO.setup(PIR_pin, GPIO.IN)
GPIO.setup(LED_pin, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

on_mode = False

while True:
    if on_mode == True:
        print ("Powered on!")
        time.sleep(0.1)
        if GPIO.input(PIR_pin):
            print ("Hello whatever's in front of me!")
            GPIO.output(LED_pin, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LED_pin, GPIO.LOW)
            time.sleep(0.1)
        if GPIO.input(button):
            if on_mode == False:
                on_mode = True
            else:
                on_mode = False
