"""EX02 - One-Shot Wordle"""

__author__ = "730406136"

SECRET: str = "python"

guess: str = input(f"What is your {len(SECRET)}-letter guess? ")

while len(guess) != len(SECRET):
        guess = input(f"That was not {len(SECRET)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

result: str = ""


i = 0       
while i < len(SECRET):
        in_word: bool = False
        j = 0
        while (in_word == False) and (j < len(SECRET)):
                if guess[i] == SECRET[j] and (i == j):
                        result = result + GREEN_BOX
                elif guess[i] == SECRET[j] and (i != j):
                        in_word = True
                        result = result + YELLOW_BOX 
                j = j + 1
        i = i + 1
        
print(result)



if guess == SECRET:
        print("Woo! You got it! ")
else: 
        print("Not quite. Play again soon! ")