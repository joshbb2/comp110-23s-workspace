"""EX02 - One-Shot Wordle"""

__author__ = "730406136"

SECRET: str = "python"

guess: str = input("What is your 6-letters guess? ")

while len(guess) != 6:
    input("That was not 6 letters! Try again: ")

if guess == SECRET:
        print("Woo! You got it!")
else:
        print("Not quite. Play again soon!")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

counter: int = 0

result: str = ""

if SECRET[0] == guess[0]:
    result = GREEN_BOX
    counter = counter + 1
else:
    result = WHITE_BOX
    counter = counter + 1
if SECRET[1] == guess[1]:
    result = result + GREEN_BOX
    counter = counter + 1
else:
    result = result + WHITE_BOX
    counter = counter + 1
if SECRET[2] == guess [2]:
    result = result + GREEN_BOX
    counter = counter + 1
else:
    result = result + WHITE_BOX
    counter = counter + 1
if SECRET[3] == guess[3]:
    result = result + GREEN_BOX
    counter = counter + 1
else:
    result = result + WHITE_BOX
    counter = counter + 1
if SECRET[4] == guess[4]:
    result = result + GREEN_BOX
    counter = counter + 1
else:
    result = result + WHITE_BOX
    counter = counter + 1

print(result)
