"""EX03 - Structured Wordle."""

__author__ = "730406136"

secret: str = "codes"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
c: int = 0

def contains_char(word: str, char: str) -> bool:
    "Determines if char is found at any index of word."
    assert len(char) == 1
    i = 0
    in_word: bool = False
    while i < len(word):
        if word[i] == char:
            return True
        else:
            i += 1
    return False

def emojified(guess: str, secret: str) -> str:
    "Determines if any index of guess is equal to any index of secret."
    assert len(guess) == len(secret)
    c = 0
    result: str = ""
    while c < len(secret):
        if guess[c] == secret[c]:
            result += GREEN_BOX
        elif contains_char(secret, guess[c]) == True:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        c += 1
    return (result)

