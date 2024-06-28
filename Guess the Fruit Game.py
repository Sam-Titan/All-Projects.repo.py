import random
fruits = ["apple", "banana", "mango", "strawberry"]
fruit = random.choice(fruits)  # The code does not end even after putting the right answer
# needs to be reviewed again
guess = ""
lst = []
length = len(fruit)
b = length
a = length - 1
while length > 0:
    i = 0
    for el in fruit:
        if el in guess:
            print(el, end="")
        else:
            print("_", end="")

    if fruit == guess:
        print("\nYou win")
        break

    guesses = input("\nEnter a Letter to guess the name of the fruit:")
    while True:
        if guesses == fruit[i]:
            guess += guesses
            break
        elif i == a:
            length -= 1
            print("You have", length, "chances remaining")
            break
        elif guesses != fruit[i]:
            i += 1
            continue
    if length == 0:
        print("You lose")
        break

print("----GAME OVER----")
