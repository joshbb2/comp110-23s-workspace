"""EX02 - One-Shot Wordle"""

__author__ = "730406136"

SECRET: str = "python"

guess: str = input("What is your 6-letter guess? ")

while len(guess) != 6:
        input("That was not 6 letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

counter = 0

result: str = ""

in_word: bool = False

i: int = 1
       
while counter < len(SECRET):
        if guess[counter] == SECRET[counter]:
                result = result + GREEN_BOX
                counter = counter + 1
        else:
                while in_word == False and i < len(SECRET):
                        if guess[0] == SECRET[i]:
                                in_word = True
                                result = result + YELLOW_BOX
                                i = i + 1
                        else:
                               result = result + WHITE_BOX
                               i = i + 1
print(result)
if guess == SECRET:
       print("Woo! You got it! ")
else:
       print("Not quite. Play again soon! ")

#check if alternate index of secret word is equal to current index of guessed word
