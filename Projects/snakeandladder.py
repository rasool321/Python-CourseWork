#players snakes ladders scores dice
import random
import sys
def dice():
    return random.randint(1,7)
def first_player():
    global player1_score
    player1_status=input("want to [C]ontinue or [S]top").upper()
    if player1_status == 'C':
        player1_turn=dice()
        player1_score+=player1_turn
        if player1_score in snakes:
            player1_score=snakes[player1_score]
            print(f"\n{player1}'s turn:\nDice: {player1_turn}\n---Snake bite---\nBoard position: {player1_score}")
        elif player1_score in ladders:
            player1_score=ladders[player1_score]
            print(f"\n{player1}'s turn:\nDice: {player1_turn}\n*****Ladder*****\nBoard position: {player1_score}")
        else:
            print(f"\n{player1}'s turn:\nDice: {player1_turn}\nBoard position: {player1_score}")
    elif player1_status == 'S':
        print(f'\n{player1} quit the game.\n{player2} Won the game!!!')
        sys.exit()

def second_player():
    global player2_score
    player2_status=input("want to [C]ontinue or [S]top").upper()
    if player2_status == 'C':
        player2_turn=dice()
        player2_score+=player2_turn
        if player2_score in snakes:
            player2_score=snakes[player2_score]
            print(f"\n{player2}'s turn:\nDice: {player2_turn}\n---Snake bite---\nBoard position: {player2_score}")
        elif player2_score in ladders:
            player2_score=ladders[player2_score]
            print(f"\n{player2}'s turn:\nDice: {player2_turn}\n*****Ladder*****\nBoard position: {player2_score}")
        else:
            print(f"\n{player2}'s turn:\nDice: {player2_turn}\nBoard position: {player2_score}")
    elif player2_status == 'S':
        print(f'\n{player2} quit the game.\n{player1} Won the game!!!')
        sys.exit()


player1=input("Enter the player name: ")
player2=input("Enter the player name: ")
win_score=100
player1_score=0
player2_score=0

snakes={99:23,81:17,72:64,67:14,56:32,48:12,34:3,25:19,16:9}
ladders={7:19,18:77,23:85,31:44,45:71,54:63,61:94,78:88,89:93}


while player1_score<win_score and player2_score<win_score:
    first_player()
    second_player()
else:
    if player1_score>player2_score:
        print(f"{player1}Wins !!!")
    elif player1_score==player2_score:
        print("Tie...")
    else:
        print(f"{player2} Wins!!")   