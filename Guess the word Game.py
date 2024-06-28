import random

# Guessing the word game
name = input("Enter your user name:")
print("Welcome", name)
print("Best of luck")
words = ["Name", "dost", "girl", "boy", "may", "hope", "find"]
word = random.choice(words)
print("Hint: Names starts with N, d, g, b, m, h, f")
chances = 12
print(word)
guesses = ""
while chances > 0:
    print("Guess the character")
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")

    if word in guesses:
        print("You found the word:", word)
        print("Congratulations,\nYOU WIN")
        break

    guess = input("Guess the Characters:")
    guesses += guess
    for el in word:
        if el in guesses:
            break
        else:
            chances -= 1
            print("The character is wrong.\nYou have", chances, "chances left")
            break
    if chances == 1:
        print("You have one last chance left.\nChoose wisely")

if chances == 0:
    print("YOU LOST")
print("----GAME OVER----")
