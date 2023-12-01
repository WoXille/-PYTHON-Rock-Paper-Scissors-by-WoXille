## Rock Paper Scissors by WoXille - https://github.com/WoXille

import random
choices = ["Rock", "Paper", "Scissors"]
totalround = 5 #Number of rounds ! You can change it !

def computer_choice():
    global computer
    computer = random.choice(choices)

def run(player_score,cpu_score,round):
    try :
        player_choice = choices[int(input("Rock, Paper or Scissors? (1,2 or 3)"))-1]
    except IndexError:
        print("Choose a number between 1,2 and 3")
        return run(player_score,cpu_score,round)
    

    computer_choice()
    if round == totalround :
        if cpu_score < player_score :
            print("The player wins !","Player's score :",player_score,"Computer's score :",cpu_score)
        elif cpu_score > player_score :
            print("The computer wins !","Computer's score :",cpu_score,"Player's score :",player_score)
        else :
            print("It's an equality !")
        return "Game finished"
    else:
        if player_choice == computer :
           print("Tie !")
           return run(player_score,cpu_score,round)
        elif player_choice == "Rock":
            if computer == "Paper":
                print("You lose! Paper covers Rock.")
                return run(player_score,cpu_score+1,round+1)
            print("You win! Rock smashes Scissors.")
            return run(player_score+1,cpu_score,round+1)
        elif player_choice == "Paper":
            if computer == "Scissors":
                print("You lose! Scissors cut Paper")
                return run(player_score,cpu_score+1,round+1)
            print("You win! Paper covers Rock")
            return run(player_score+1,cpu_score,round+1)
        elif player_choice == "Scissors":
            if computer == "Rock":
                print("You lose ! Rock smashes Scissors.")
                return run(player_score,cpu_score+1,round+1)
            print("You win! Scissors cut Paper.")
            return run(player_score+1,cpu_score,round+1)


run(0,0,0)