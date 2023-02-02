"""EX02 - One-Shot Wordle"""

__author__ = "730406136"

SECRET: str = "python"

guess: str = input("What is your 6-letters guess? ")

while len(guess) != 6:
    input("That was not 6 letters! Try again: ")
    guess = input("That was not 6 letters! Try again: ")
else:
    if guess == SECRET:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")


