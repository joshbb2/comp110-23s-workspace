"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730406136"

word: str = input("Enter a 5-character word: ")

if((len(word)) != 5):
    print("Error: Word must contain 5 characters.")
else:
    character: str = input("Enter a single character: ")

if((len(character)) != 1):
    print("Error: Character must be a single character.")
else:
    print("Searching for " + character + " in " + word)

if(character not in word):
    print("No instances of " + character + " in " + word)

x: int = 1

if(character == word[0]):
    print(character + " found at index 0")
    print(x, "instance of " + character + " in " + word)

if(character == word[1]):
    print(character + " found at index 1")
    print(x, "instances of " + character + " in " + word)
        
if(character == word[2]):
    print(word[2] + " found at index 2")
if(character == word[3]):
    print(word[3] + " found at index 3")
if(character == word[4]):
    print(word[4] + " found at index 4")