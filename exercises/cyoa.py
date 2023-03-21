"""EX06 - Choose Your Own Adventure."""

__author__ = "730406136"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"

points: int = 0

def main() -> None:
    global points
    greet()
    menu: str = input("Enter 'A' for the number guessing game. Enter 'B' to exit your adventure. Enter 'C' to pause your adventure.: ")
    invalid_input: bool = False
    if menu == 'A':
        random_num()
    if menu == 'B':
        exit_game()
    if menu == 'C':
        i: int = point_count(points)
        print(f"You have {i} points!")
        resume: str = input("Type 'Resume' to unpause your adventure: ")
        if resume == 'Resume':
            random_num()
    else:
        main()
    
def greet() -> None:
    global player
    player = input("Welcome to your adventure! What is your name? ")

def random_num() -> None:
    global points
    turn: int = 1
    win: bool = False
    print(f"=== Turn 1/10 ===")
    from random import randint
    number = randint(1,10)
    print(number)
    guess: int in range(1,10) = input("Guess a number between 1 and 10: ")
    while turn < 10:
        if guess == number:
            win = True
        else:
            print(f"=== Turn {turn + 1}/10 ===")
            guess = input("Try again! Guess a number between 1 and 10: ")
            turn += 1
    if win == True:
        print(f"{GREEN_BOX} Great job! You got it in {turn} turns! {GREEN_BOX}")
    if win == False:
        print(f"{WHITE_BOX} X/10 - Sorry, try again soon! {WHITE_BOX}")
        
def exit_game() -> None:
    global points
    print(f"Goodbye, thanks for playing! Your score is {points} points!")
    again: str = input("Type 'Yes' to start a new adventure: ")
    if again == 'Yes':
        main()
    else:
        exit()

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