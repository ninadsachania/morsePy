#! /usr/bin/python3
# Author: Ninad Sachania

# for delay
from time import sleep

try:
    import RPi.GPIO as GPIO
except:
    print("Error importing RPi.GPIO.")

# Use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# Ignore warnings
GPIO.setwarnings(False)

# pin number 
PIN = 8

ditLength = 1 
dashLength = ditLength * 3
pauseBetweenWords = ditLength * 7
pauseBetweenChars = ditLength * 3
pauseBetweenElements = ditLength 

# delay of 0.1 ms 
delay = 0.05 

letters = {
    'a': [0,1],
    'b': [1, 0, 0, 0],
    'c': [1, 0, 1, 0],
    'd': [1, 0, 0],
    'e': [0],
    'f': [0, 0, 1, 0],
    'g': [1, 1, 0],
    'h': [0, 0, 0, 0],
    'i': [0, 0],
    'j': [0, 1, 1, 1],
    'k': [1, 0, 1],
    'l': [0, 1, 0, 0],
    'm': [1, 1],
    'n': [1, 0],
    'o': [1, 1, 1],
    'p': [0, 1, 1, 0],
    'q': [1, 1, 0, 1],
    'r': [0, 1, 0],
    's': [0, 0, 0],
    't': [1],
    'u': [0, 0, 1],
    'v': [0, 0, 0, 1],
    'w': [0, 1, 1],
    'x': [1, 0, 0, 1],
    'y': [1, 0, 1, 1],
    'z': [1, 1, 0, 0]
}

def morseChar(char, pinNum):
    global letters
    global delay
    morseCode = letters[char]
    # TODO: Delete or comment this out
    print(morseCode)

    for digit in morseCode:
        if digit == 0:
            GPIO.output(pinNum, GPIO.HIGH)
            sleep(ditLength * delay)
            GPIO.output(pinNum, GPIO.LOW)
        elif digit == 1:
            GPIO.output(pinNum, GPIO.HIGH)
            sleep(dashLength * delay)
            GPIO.output(pinNum, GPIO.LOW)

        sleep(pauseBetweenElements * delay)
    
    sleep(pauseBetweenChars * delay)

def morseWords(string, pinNum):
    characters = list(string)
    print(characters)

    for char in characters:
        if char == ' ':
            sleep(pauseBetweenWords * delay)
            print([0] * 7)
        else:
            morseChar(char, pinNum)


GPIO.setup(PIN, GPIO.OUT)

morseWords('ninad sachania', PIN)
