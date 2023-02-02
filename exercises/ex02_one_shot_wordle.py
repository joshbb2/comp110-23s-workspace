"""EX02 - One-Shot Wordle"""

__author__ = "730406136"

SECRET: str = "python"

guess: str = input("What is your 6-letters guess? ")

if len(guess) != 6:
    print(input("That was not 6 letters! Try again: "))

if guess == SECRET:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")