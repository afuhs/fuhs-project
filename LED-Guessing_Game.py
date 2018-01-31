# Alexandra Fuhs
# 1/3/18
# Light Up Guessing Game
# Guess the number, shows blue if too low, red if too high, green if correct.
# You get 5 tries.

import random
import time
import RPi.GPIO as GPIO

def easter_egg(LED_pin_green):
    for i in range (5):
        GPIO.output(LED_pin_green,GPIO.HIGH)
        time.sleep(.2)
        GPIO.output(LED_pin_green,GPIO.LOW)
        time.sleep(.2)
    

def game_over():
    '''My game over function'''
    print("You ran out of guesses! :(")
    time.sleep(1)
    print("yay!")

def blink_led(pin):
    for i in range (5):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(.2)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(.2)
# Setting up my LED pins
GPIO.setmode(GPIO.BCM) # Sets the number scheme to Broadcom numbering
LED_pin_red = 21
LED_pin_green = 22
LED_pin_blue = 23

GPIO.setup(LED_pin_red, GPIO.OUT)
GPIO.setup(LED_pin_green, GPIO.OUT)
GPIO.setup(LED_pin_blue, GPIO.OUT)

# Title and instructions
print ("*"*80)
print ("""
Welcome to the
 _        _______  ______  
( \      (  ____ \(  __  \ 
| (      | (    \/| (  \  )
| |      | (__    | |   ) |
| |      |  __)   | |   | |
| |      | (      | |   ) |
| (____/\| (____/\| (__/  )
(_______/(_______/(______/
Guessing Game!

""")

print ("*"*80)
time.sleep(1)
print ("""
You have 5 guesses to guess a number between 1 and 20
Too low --> Blue Blink
Too high --> Red Blink
Correct --> Green Blink
""")
print ("*"*80)

play_again = "Y"
    
while play_again == "Y":

    # Get a random number between 1 and 20
    num = random.randint(1,20) 

    # Start a loop and give them 5 tries
    guesses = 0
    while guesses < 5:
        # Get a guess from the user
        guess = input("Guess a number from 1 to 20: ")
        if guess == ("banana"):
            easter_egg(LED_pin_green)
            break
        else:
            guess = int(guess)
            guesses += 1
            # Check if correct, too low or too high
            if guess == num:
                print("Correct!")
                # TODO: Blink Green
                blink_led(LED_pin_green)
                
                break
            elif guess < num:
                print("Too low!")
                # TODO: Blink Blue
                blink_led(LED_pin_blue)
            else: # Must be too high
                print("Too high!")
                # TODO: Blink Red
                blink_led(LED_pin_red)
    else:
        game_over()

        play_again = input("Do you want to play again? (Y or N): ").upper()    

print ("Thank you for playing.")

            

    


