"""EX06 - Choose Your Own Adventure."""

__author__ = "730406136"

player: str = ""
points: int = 0
turn: int = 1

def greet() -> None:
    global player
    player = input("Welcome to your adventure! What is your name? ")

def input_guess() -> int:
    user_guess: int in range(1,11) = int(input("Guess a number between 1 and 10: "))
    return user_guess

def random_num() -> bool:
    global turn
    correct: bool = False
    print(f"=== Turn {turn}/10 ===")
    from random import randint
    answer: int = randint(1,10)
    guess: int = input_guess()
    turn += 1
    while turn < 11 and not correct:
        print(f"=== Turn {turn}/10 ===")
        if guess == answer:
            correct = True
        else:
            guess = input_guess()
            turn += 1
    return correct
    
def exit_game() -> None:
    print(f"Goodbye, thanks for playing! Your score is {points} points!")
    print("Type 'Yes' to play again. \nType 'No' to exit.")
    again: str = input("Selection: ")
    cont: bool = False
    while cont == False:
        if again == "Yes":
            cont = True
            main()
        if again == "No":
            cont = True
            exit()
        else:
            again = input("Invalid input. Selection: ")

def point_count(score: int) -> int:
    global points
    proceed: str = input(f"{player}, the game has been paused. Type 'Continue' to calculate your score: ")
    if proceed == "Continue":
        points += 1
    else:
        while proceed != "Continue":
            proceed = input(f"{player}, type 'Continue' to calculate your score: ")
    return points

def main() -> None:
    global turn
    global points
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    greet()
    points += 1
    print("Enter 'A' for the number guessing game. \nEnter 'B' to exit your adventure. \nEnter 'C' to pause your adventure. ")
    menu: str = input("Selection: ")
    points += 1
    if menu == "A":
        points += 1
        winner = random_num()
        print(winner)
        if winner:
            print(f"{GREEN_BOX} Great job! You won in {turn} turns! {GREEN_BOX}")
        else:
            print(f"{WHITE_BOX} X/10 - Sorry, try again soon! {WHITE_BOX}")
        points += 1
        exit_game()
    if menu == "B":
        points += 1
        exit_game()
    if menu == "C":
        points += 1
        points = point_count(points)
        view_score: str = input("Type 'Score' to view your score: ")
        if view_score == "Score":
            points += 1
            print(f"You have {points} points!")
        else:
            while view_score != "Score":
                view_score = input("Type 'Score' to view your score: ")
        resume: str = input("Type 'Resume' to unpause your adventure. \nType 'Exit' to exit game. \nSelection: ")
        if resume == "Resume":
            points += 1
            main()
        if resume == "Exit":
            points += 1
            exit()
        while resume != "Resume" or "Exit":
            resume = input("Invalid input. \nType 'Resume' to unpause your adventure. \nType 'Exit' to exit game. \nSelection: ")
    else:
        while menu != "A" or "B" or "C":
            menu = input("Invalid input. \nEnter 'A' for the number guessing game. \nEnter 'B' to exit your adventure. \nEnter 'C' to pause your adventure. \nSelection: ")

if __name__ == "__main__":
    main()