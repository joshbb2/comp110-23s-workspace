"""EX02 - One-Shot Wordle"""

__author__ = "730406136"

secret: str = "python"

guess: str = input("What is your 6-letters guess? ")

if len(guess) != 6:
    print("That was not 6 letters! " + input("Try again: "))

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")