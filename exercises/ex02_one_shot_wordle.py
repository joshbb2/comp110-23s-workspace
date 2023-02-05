"""EX02 - One-Shot Wordle"""

__author__ = "730406136"

SECRET: str = "python"

guess: str = input("What is your 6-letter guess? ")

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
                result = GREEN_BOX
                count = count + 1
while (in_word == False) and i < len(SECRET):
        if guess[0] == SECRET[i]:
                in_word = True
                result = YELLOW_BOX
                i = i + 1   
        else:
                result = WHITE_BOX
                i = i + 1
        if guess[1] == SECRET[i]:
                in_word = True
                result = YELLOW_BOX
                i = i + 1   
        else:
                result = result + WHITE_BOX
                i = i + 1           
print(result)