#! /usr/bin/env python3
# Author: Ninad Sachania

# TODO:
#    - Move this to a class
#    - Investigate how far can the delay can be lowered
#    - Add digits and punctuation marks to `letters' dict

from time import sleep
import sys

try:
    import RPi.GPIO as GPIO
except ImportError:
    print("Error importing RPi.GPIO.", file=sys.stderr)
    sys.exit(1)

# Use physical pin numbering
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

PIN = 8

# Set pin 8 on output mode (By default every GPIO pins are in input mode)
GPIO.setup(PIN, GPIO.OUT)

ditLength = 1
dashLength = ditLength * 3
pauseBetweenWords = 2 * dashLength
pauseBetweenChars = dashLength
pauseBetweenElements = ditLength

delay = 0.05

letters = {
    "a": [0, 1],
    "b": [1, 0, 0, 0],
    "c": [1, 0, 1, 0],
    "d": [1, 0, 0],
    "e": [0],
    "f": [0, 0, 1, 0],
    "g": [1, 1, 0],
    "h": [0, 0, 0, 0],
    "i": [0, 0],
    "j": [0, 1, 1, 1],
    "k": [1, 0, 1],
    "l": [0, 1, 0, 0],
    "m": [1, 1],
    "n": [1, 0],
    "o": [1, 1, 1],
    "p": [0, 1, 1, 0],
    "q": [1, 1, 0, 1],
    "r": [0, 1, 0],
    "s": [0, 0, 0],
    "t": [1],
    "u": [0, 0, 1],
    "v": [0, 0, 0, 1],
    "w": [0, 1, 1],
    "x": [1, 0, 0, 1],
    "y": [1, 0, 1, 1],
    "z": [1, 1, 0, 0],
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
        if char == " ":
            sleep(pauseBetweenWords * delay)
            print([0] * 7)
        else:
            morseChar(char, pinNum)


morseWords("ninad sachania", PIN)
