"""EX03 - Structured Wordle."""

__author__ = "730406136"

secret: str = "codes"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

result: str = ""

i = 0
j = 0
c = 0

def contains_char(word: str, char: str) -> bool:
    "Determines if char is found at any index of word."
    assert len(char) == 1
    i = 0
    while i < len(word):
        if word[i] == char:
            return True
        else:
            i = i + 1
    else:
        return False

def emojified(guess: str, secret: str) -> str:
    "Determines if any index of guess is equal to any index of secret."
    assert len(guess) == len(secret)
    j = 0
    c = 0
    while j < len(secret):
        if contains_char == True:
            return result + GREEN_BOX
        else:
            contains_char == False
        while contains_char == False and c < len(secret):
            if guess[j] == secret[c] and (j != c):
                return result + YELLOW_BOX
            else:
                c = c + 1
        else:
            return result + WHITE_BOX
    j = j + 1
    

