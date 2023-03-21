"""EX06 - Choose Your Own Adventure."""

__author__ = "730406136"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"

points: int = 0
turn: int = 1

def main() -> None:
    global points
    global turn
    greet()
    print("Enter 'A' for the number guessing game. \nEnter 'B' to exit your adventure. \nEnter 'C' to pause your adventure. ")
    menu: str = input("Selection: ")
    if menu == 'A':
        RANDOM_ANSWER: int = generate_int()
        attempt1: int = input_guess()
        random_num(attempt1, RANDOM_ANSWER)
    if menu == 'B':
        exit_game()
    if menu == 'C':
        i: int = point_count(points)
        print(f"You have {i} points!")
        resume: str = input("Type 'Resume' to unpause your adventure: ")
        if resume == 'Resume':
            random_num()

def greet() -> None:
    global player
    player = input("Welcome to your adventure! What is your name? ")

def input_guess() -> int:
    global turn
    print(f"=== {turn}/10 ===")
    user_guess: int = input("Guess a number between 1 and 10: ")
    while user_guess != int in range(1,10):
        user_guess = input("Guess a number between 1 and 10: ")
    return user_guess

def generate_int() -> int:
    from random import randint
    ANSWER: int = randint(1,10)
    return ANSWER

def random_num(guess: int, NUMBER: int) -> str:
    global turn
    win: bool = False
    while turn < 10 and not win:
        if guess == NUMBER:
            win = True
        else:
            turn += 1
            guess = input_guess()
    if win:
        print(f"{GREEN_BOX} Great job! You won in {turn} turns! {GREEN_BOX}")
    else:
        print(f"{WHITE_BOX} X/10 - Sorry, try again soon! {WHITE_BOX}")
    exit_game
        
def exit_game() -> None:
    print(f"Goodbye, thanks for playing! Your score is {points} points!")
    again: str = input("Type 'Yes' to start a new adventure: ")
    if again == 'Yes':
        main()
    else:
        while again != 'Yes':
            again = input("Type 'Yes' to start a new adventure: ")

def point_count(score: int) -> int:
    score = 0
    proceed: str = input(f"{player}, the game has been paused. Type 'Continue' to view your score: ")
    if proceed == 'Continue':
        score += 1
    else:
        while proceed != 'Continue':
            proceed = input(f"{player}, type 'Continue' to proceed: ")
    return score

if __name__ == "__main__":
    main()