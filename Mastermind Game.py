import random
name_1 = input("Please enter your name player 1:")
name_2 = "Player computer"
print("Welcome to the mastermind game", name_1, "and", name_2,)
print(name_1, "You are playing against the computer and hence,\ncomputer picks the number")
comp_rand = str(random.randint(1000, 10000))
user_input = input("Guess the number:")
tries = 0
cur_no = ["", "", "", ""]

# THE PROGRAM STILL NEEDS REFINEMENT AND IS JUST A PROTOTYPE
def neat(a):
    i = 0
    c = 0
    while a > 0:
        if comp_rand[i] == user_input[i]:
            print(user_input[i], end=" ")
            cur_no.insert(c, user_input[i])
            c += 1
            i += 1
            a -= 1
        elif comp_rand[i] == cur_no[c]:
            print(cur_no[c], end=" ")
            a -= 1
            c += 1
            i += 1
        else:
            print("_", end=" ")
            i += 1
            a -= 1
            c += 1


if user_input == "Q":
    print("You are quitting the game")
elif user_input == comp_rand:
    print("Congratulation you guessed it one try", name_1)
    neat(4)
else:
    neat(4)
    tries += 1
while tries > 0:
    while True:
        user_input = input("\nGuess the number:")
        if user_input == "Q":
            print("You are quitting the game")
            break
        else:
            neat(4)
            tries += 1
            break
    if user_input == "Q":
        break
    if user_input == comp_rand:
        print("You have guessed it in", tries, "tries", name_2)
        print("CONGRATULATIONS")
        break
if user_input == "Q":
    print("You have lost", name_1)
else:
    print("You have beat the computer", name_1)
print("----GAME OVER----")
