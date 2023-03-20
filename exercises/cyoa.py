"""EX06 - Choose Your Own Adventure."""

__author__ = "730406136"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"

points: int = 0

def main() -> None:
    global points
    greet()
    menu: str = input("Enter 'A' for the number guessing game. Enter 'B' to exit your adventure. Enter 'C' to pause your adventure.: ")
    input_menu(menu)
    
def greet() -> None:
    global player
    player = input("Welcome to your adventure! What is your name? ")

def input_menu(selection: str) -> None:
    invalid_input: bool = False
    if selection == "A":
        from random import randint
        answer: int = randint(1,10)
        print(answer)
        print(f"=== Turn 1/10 ===")
        user = input("Guess a number between 1 and 10: ")
        while user != int in range(1,10):
            user = input("Guess a number between 1 and 10: ")
        random_num(user, answer)
    if selection == "B":
        exit_game()
    if selection == "C":
        i: int = point_count(points)
        print(f"You have {i} points!")
        resume: str = input("Type Resume to unpause your adventure: ")
        if resume == "Resume":
            input_menu("A")
    else:
        invalid_input = True
        while invalid_input == True:
            selection = input("Enter A for the number guessing game. Enter B to exit game. Enter C to pause game.: ")


def random_num(guess: int, number: int) -> None:
    global points
    turn: int = 2
    win: bool = False
    while turn <= 10:
        print(f"=== Turn {turn}/10 ===")
        if guess == number:
            win = True
        else:
            turn += 1
            guess = input("Try again! Guess a number between 1 and 10: ")
    if not win:
        print(f"{GREEN_BOX} Great job! You got it in {turn - 1} turns! {GREEN_BOX}")
    else:
        print(f"{WHITE_BOX} X/10 - Sorry, try again soon! {WHITE_BOX}")
    exit_game()

def exit_game() -> None:
    global points
    print(f"Goodbye, thanks for playing! Your score is {points} points!")
    again: str = input("Type 'Yes' to play again: ")
    if again == 'Yes':
        main()
    else:
        exit()

  
def point_count(score: int) -> int:
    score = 0
    proceed: str = input(f"{player}, the game has been paused. Type Continue to view your score: ")
    if proceed == "Continue":
        score += 1
    else:
        while proceed != "Continue":
            proceed = input(f"{player}, type Continue to proceed: ")
    return score

if __name__ == "__main__":
    main()

