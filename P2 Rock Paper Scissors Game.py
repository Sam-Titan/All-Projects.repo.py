# The purpose of today's program is to make a rock paper scissors game
import random
# paper = 1
# scissors = 2
# rock = 3


def game_start(ans="Start"):
    i = 0
    c = 0
    while True:
        comp_input = random.randint(1, 3)
        player_input = input("Please choose:")
        if player_input == "paper" or player_input == "Paper" or player_input == "scissors" or player_input == "Scissors" or player_input == "rock" or player_input == "Rock":
            print()
        else:
            print("The word in not possible to be played. Please try again")
            continue
        if comp_input == 1:
            if player_input == "paper" or player_input == "Paper":
                print("Computer made the move:Paper")
                print("Paper vs Paper -> Draw")
            elif player_input == "scissors" or player_input == "Scissors":
                print("Computer made the move:Paper")
                print("Scissors vs Paper -> Point to Player")
                i += 1
            else:
                print("Computer made the move:Paper")
                print("Rock vs Paper -> Point to Computer")
                c += 1
        elif comp_input == 2:
            if player_input == "scissors" or player_input == "Scissors":
                print("Computer made the move:Scissors")
                print("Scissors vs Scissors -> Draw")
            elif player_input == "paper" or player_input == "Paper":
                print("Computer made the move:Scissors")
                print("Paper vs Scissors -> Point to Computer")
                c += 1
            else:
                print("Computer made the move:Scissors")
                print("Rock vs Scissors -> Point to Player")
                i += 1
        elif comp_input == 3:
            if player_input == "rock" or player_input == "Rock":
                print("Computer made the move:Rock")
                print("Rock vs Rock -> Draw")
            elif player_input == "scissors" or player_input == "Scissors":
                print("Computer made the move:Rock")
                print("Scissors vs Rock -> Point to Computer")
                c += 1
            else:
                print("Computer made the move:Scissors")
                print("Paper vs Rock -> Point to Player")
                i += 1
        if i == 5:
            print("Scorecard is:\nPlayer Points:", i, "\nComputer Points:", c)
            print("Player wins the game")
            break
        elif c == 5:
            print("Scorecard is:\nPlayer Points:", i, "\nComputer Points:", c)
            print("Computer wins the game")
            break

    if i == 5:
        print("CONGRATULATIONS, YOU WON THE GAME")
    elif c == 5:
        print("YOU LOST, PLEASE TRY AGAIN LATER")
    print("-----GAME OVER-----")


while True:
    game_start()
    break
