import random
cur_no = 0
user_input = 0
comp_input = 0
u = 0
c = 0
tot_no = 21
name = input("Please enter you user name:")
print("Welcome to the 21 game", name)
print("Do you want the first turn", name)
choice = input("(Y/N):")
if choice == "Y":
    user_no = int(input("Enter the number between 1 to 4:"))
    print("Current number after the players turn:", user_no)
    user_input += user_no
    cur_no += user_input
    u += 1
else:
    comp_input = random.randint(1, 4)
    cur_no += comp_input
    print("Current number after the computers turn:", cur_no)
    c += 1
while True:
    while True:
        if u >= c:
            comp_input = random.randint(1, 4)
            cur_no += comp_input
            print("Current number after the computers turn:", cur_no)
            c += 1
            break
        else:
            user_no = int(input("Player please enter a number between 1 and 4:"))
            cur_no += user_no
            print("Current number after the players turn:", cur_no)
            u += 1
            break
    if cur_no == 21:
        if u > c:
            print("Player you have lost.\nBest of luck next time")
            break
        elif u <= c:
            print("Player you have won.\nCongratulations")
            break
    elif cur_no > 21:
        if u > c:
            print("Player you have lost.\nBest of luck next time")
            break
        elif u <= c:
            print("Player you have won.\nCongratulations")
            break

print("----GAME OVER----")
