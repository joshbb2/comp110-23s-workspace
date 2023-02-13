"""EX02 - One-Shot Wordle."""

__author__ = "730406136"

SECRET: str = "python"

guess: str = input(f"What is your {len(SECRET)}-letter guess? ")

while len(guess) != len(SECRET):
    guess = input(f"That was not {len(SECRET)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
word_idx: int = 0
result: str = ""
      
while word_idx < len(SECRET):
    if guess[word_idx] == SECRET[word_idx]:
        result = result + GREEN_BOX
    else:
        in_word: bool = False
        secret_idx: int = 0
        while not in_word and secret_idx < len(SECRET):
            if guess[word_idx] == SECRET[secret_idx]:
                in_word = True
            else:
                secret_idx = secret_idx + 1
        if in_word:
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
    word_idx = word_idx + 1

print(result)

if guess == SECRET:
    print("Woo! You got it! ")
else: 
    print("Not quite. Play again soon! ")