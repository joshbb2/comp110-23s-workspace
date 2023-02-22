"""EX03 - Structured Wordle."""

__author__ = "730406136"

secret: str = "codes"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word: str, char: str) -> bool:
    "Determines if char is found at any index of word."
    assert len(char) == 1
    i: int = 0
    while i < len(word):
        if word[i] == char:
            return True
        else:
            i += 1
    return False

def emojified(guess: str, secret: str) -> str:
    "Determines if any index of guess is equal to any index of secret."
    assert len(guess) == len(secret)
    j: int = 0
    result: str = ""
    while j < len(secret):
        if guess[j] == secret[j]:
            result += GREEN_BOX
        elif contains_char(secret, guess[j]) == True:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        j += 1
    return (result)

def input_guess(expected_length: int) -> str:
    user: str = input(f"Enter a {expected_length} character word: ")
    while expected_length != len(user):
        user = input(f"That wasn't {expected_length} chars! Try again: ")
    return user

def main() -> None:
    """The entrypoint of the program and main game loop."""
    k: int = 1
    while k <= len(secret):
        print(f"=== Turn {k}/{len(secret)} ===")
        print(emojified(input_guess(len(secret)), secret))
    if input_guess(len(secret)) == secret:
        print(f"You won in {k}/{len(secret)} turns!")
    else:
        k += 1
    print(f"X/{len(secret)} - Sorry, try again tomorrow!")
        


