"""EX02 - One-Shot Wordle"""

__author__ = "730406136"

SECRET: str = "python"

guess: str = input("What is your 6-letters guess? ")

while len(guess) != 6:
    input("That was not 6 letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

count: int = 0

result: str = ""

in_word: bool = False

i = 0
         
while count < len(SECRET):
        if guess[count] == SECRET[count]:
                result = result + GREEN_BOX
                count = count + 1
        else:
                result = result + WHITE_BOX
                count = count + 1  
print(result)