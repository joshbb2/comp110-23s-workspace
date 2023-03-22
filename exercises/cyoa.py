"""EX06 - Choose Your Own Adventure."""

__author__ = "730406136"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"

points: int = 0

from random import randint
answer: int = randint(1,10)

def greet() -> None:
    global player
    player = input("Welcome to your adventure! What is your name? ")

def input_guess() -> int:
    global points
    user_guess: int in range(1,11) = input("Guess a number between 1 and 10: ")
    points += 1
    return user_guess

def random_num(guess: int, NUMBER: int) -> bool:
    win: bool = False
    if guess == NUMBER:
        win = True
    return win
        
def exit_game() -> None:
    print(f"Goodbye, thanks for playing! Your score is {points} points!")
    print("Type 'Yes' to start a new adventure. \nType 'No' to exit.")
    again: str = input("Selection: ")
    if again == 'Yes':
        main()
    if again == 'No':
        return None
    while again != 'Yes' or 'No':
        print("Type 'Yes' to start a new adventure. \nType 'No' to exit.")
        again = input("Selection: ")

def point_count(score: int) -> int:
    proceed: str = input(f"{player}, the game has been paused. Type 'Continue' to calculate your score: ")
    if proceed == 'Continue':
        score += 1
    else:
        while proceed != 'Continue':
            proceed = input(f"{player}, type 'Continue' to calculate your score: ")
    return score

def main() -> None:
    global points
    turn: int = 1
    greet()
    print("Enter 'A' for the number guessing game. \nEnter 'B' to exit your adventure. \nEnter 'C' to pause your adventure. ")
    menu: str = input("Selection: ")
    points += 1
    if menu == 'A':
        correct: bool = False
        print(f"=== Turn {turn}/10 ===")
        attempt: int = input_guess()
        turn += 1
        while turn < 11 and not correct:
            print(f"=== Turn {turn}/10 ===")
            attempt = input_guess()
            result = random_num(attempt, answer)
            if result == True:
                correct = True
            else:
                turn += 1
        if correct:
            print(f"{GREEN_BOX} Great job! You won in {turn} turns! {GREEN_BOX}")
        else:
            print(f"{WHITE_BOX} X/10 - Sorry, try again soon! {WHITE_BOX}")
    if menu == 'B':
        exit_game()
    if menu == 'C':
        i = point_count(points)
        view_score: str = input("Type 'Score' to view your score: ")
        if view_score == 'Score':
            i += 1
            print(f"You have {i} points!")
        else:
            while view_score != 'Score':
                view_score = input("Type 'Score' to view your score: ")
        resume: str = input("Type 'Resume' to unpause your adventure: ")
        if resume == 'Resume':
            menu == input("Enter 'A' for the number guessing game. \nEnter 'B' to exit your adventure. \nEnter 'C' to pause your adventure. \nSelection: ")
        while resume != 'Resume':
            resume = input("Type 'Resume' to unpause your adventure: ")

if __name__ == "__main__":
    main()