# Alexandra Fuhs
# 10/18/2017
# Norwegian Blue Guessing Game
# A guessing game
import random


# Display title and instructions
print ("*" * 80)
print ("THE NORWEGIAN BLUE GUESSING GAME")
print ("*" * 80)

instructions = """ You walk into a pet store and the pet
shop owner greets you. You see a parrot and ask
how much it is. He says the only way to take the parrot home
is by guessing his age. The parrot is a rare Norwegian Blue, so
you take the chance.


You only get five guesses!!!
"""

print (instructions)
# Make up the parrot's age
parrot_age = random.randint (1, 20)

# Set the number of guesses to 0
number_of_guesses = 0

while number_of_guesses < 5:
        # Get a guess from the user
        guess = input ("Guess the age of the parrot [1 to 20]:")
        guess = int (guess) # Converts a string to an integer
        number_of_guesses = number_of_guesses + 1
        print (number_of_guesses)
        if guess == parrot_age:
                print ("Congratulations! You win the parrot!")
                break
        else:
            # TODO: Add higher or lower
            if guess < parrot_age:
                print ("Too low")
            else:
                print ("Too high")
            print ("That was a horrible guess! Maybe you don't deserve the parrot!")
print ("Thank you for playing! The parrot was " , parrot_age, " years old. ")
        




