# Alexandra Fuhs
# 12/19/17


import RPi.GPIO as GPIO
import time

# variable for the GPIO pin number
LED_pin_red = 21
LED_pin_green = 22
LED_pin_blue = 23

# Tell the Pi we are using the breakout board pin numbering
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin for output
GPIO.setup(LED_pin_red, GPIO.OUT)
GPIO.setup(LED_pin_green, GPIO.OUT)
GPIO.setup(LED_pin_blue, GPIO.OUT)

GPIO.output(LED_pin_red, GPIO.LOW)
GPIO.output(LED_pin_green, GPIO.LOW)
GPIO.output(LED_pin_blue, GPIO.LOW)

# Loop to blink our led
while True:
    #GPIO.output(LED_pin_red, GPIO.HIGH)
    #GPIO.output(LED_pin_green, GPIO.HIGH)
    GPIO.output(LED_pin_blue, GPIO.HIGH)
    print ("On")
    time.sleep(1)
    #GPIO.output(LED_pin_red, GPIO.LOW)
    #GPIO.output(LED_pin_green, GPIO.LOW)
    GPIO.output(LED_pin_blue, GPIO.LOW)
    print ("Off")
    time.sleep(1)
    
