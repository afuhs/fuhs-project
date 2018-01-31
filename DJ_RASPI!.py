# DJ Raspi
# Alexandra Fuhs
# January 16th, 2018
# A music playing DJ machine!!!

# import needed libraries
import RPi.GPIO as GPIO
import time
import random
import os

# Folders with sound files
path_music = "/usr/share/scratch/Media/Sounds/Music Loops/"
path_vocals = "/usr/share/scratch/Media/Sounds/Vocals/"
path_effects = "/usr/share/scratch/Media/Sounds/Effects/"

# Returns a list of mp3 sound files for the path given
def get_MP3_sounds(sound_path):
    sound_filesound_files = os.listdir(sound_path)
    sound_filesound_files = [sound_file for sound_file in sound_filesound_files if sound_file.endswith('.mp3')]
    return sound_filesound_files

# Plays a random sound from a list of mp3s for the path given
def play_random_sound(sound_path, sound_files):
    sound_file = random.choice(sound_files)
    os.system("omxplayer -o local '" + sound_path + "/" + sound_file + "' &")

# Get the list of music loops and vocals (mp3s only)
sounds_music = get_MP3_sounds(path_music)
sounds_vocals = get_MP3_sounds(path_vocals)
sounds_effects = get_MP3_sounds(path_effects)
# Variables for button pins
button_pin1 = 6
button_pin2 = 19

# Set pin numbering
GPIO.setmode(GPIO.BCM)

# setup GPIO for input
GPIO.setup(button_pin1, GPIO.IN)
GPIO.setup(button_pin2, GPIO.IN)

# Creating two lists w/ the files in the folders
sounds_music = os.listdir(path_music)
sounds_vocals = os.listdir(path_vocals)

# Removing .wav files
sounds_music = [sound for sound in sounds_music if sound.endswith('.mp3')]
sounds_vocals = [sound for sound in sounds_vocals if sound.endswith('.mp3')]

# Clear the screen
os.system("clear")

# Title
title = """
    DJ RASPI!!!
    Press Button 1 for Music Sounds
    Press Button 2 for Vocal Sounds
    Press Ctrl + C to exit
"""

# Start an infinite loop (must use Ctrl + C to stop it)
while True:
    if GPIO.input(button_pin1):
        print("You pressed #1")
        play_random_sound(path_music, sounds_music)
        time.sleep(.1)
    if GPIO.input(button_pin2):
        print("You pressed #2!")
        play_random_sound(path_vocals, sounds_vocals)
        time.sleep(.1)
    if GPIO.input(button_pin1) and GPIO.input(button_pin2):
        print("You pressed #1 and #2! Easter Egg!")
        play_random_sound(path_effects, sounds_effects)
        time.sleep(.1)
    time.sleep(.1)
    



