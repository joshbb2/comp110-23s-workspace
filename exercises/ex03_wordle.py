"""EX03 - Structured Wordle."""

__author__ = "730406136"

SECRET: str = "codes"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
emojified: str = ""

def contains_char(word: str, char: str) -> bool:
    "Determines if char is found at any index of word."
    assert len(char) == 1
    while i < len(word):
        if word[i] == char:
            return True
        else:
            return False
    i = i + 1

