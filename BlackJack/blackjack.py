import random
from logo import logo

cards = ['x', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def computer_turn():
    c = random.choice(cards)
    if c == 'x' and sum(computer_inp) <= 10:
        computer_inp.append(11)
    elif c == 'x' and sum(computer_inp) > 10:
        computer_inp.append(1)
    else:
        computer_inp.append(c)`
    return


def player_turn():
    p = random.choice(cards)
    if p == 'x' and sum(player_input) <= 10:
        player_input.append(11)
    elif p == 'x' and sum(player_input) > 10:
        player_input.append(1)
    else:
        player_input.append(p)
    return


flag = 0

while flag == 0:
    inp = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    print(logo)
    computer_inp = []
    player_input = []
    if inp == 'y':
        computer_turn()
        player_turn()
        player_turn()
        print(f"Your Cards : {player_input}, Current score : {sum(player_input)}")
        print(f"Computer's first card : {computer_inp}")
        while sum(player_input) <= 21:
            inp1 = input("Type 'y' to get another card, type 'n' to pass: ")
            if inp1 == 'y':
                player_turn()
                print(f"Your cards : {player_input}, Current score : {sum(player_input)}")
                print(f"Computer's first card : {computer_inp}")
            else:
                break
        while sum(computer_inp) <= 17:
            if sum(computer_inp) < 17:
                computer_turn()
            else:
                break
        if sum(player_input) > 21:
            print(f"Your cards : {player_input}, Your score : {sum(player_input)}\n"
                  f"Computer's Final cards : {computer_inp}")
            print("You went over 21, You Lost 😓")
            # flag = 1
        elif sum(computer_inp) > 21:
            print(f"Your cards : {player_input}, Your score : {sum(player_input)}\n"
                  f"Computer's Final cards : {computer_inp}")
            print("Computer went over 21, You Won 🥳")
            # flag = 1
        elif sum(player_input) > sum(computer_inp):
            print(f"Your cards : {player_input}, Your score : {sum(player_input)}\n"
                  f"Computer's Final cards : {computer_inp}")
            print("You Won 🥳")
            # flag = 1
        elif sum(player_input) == sum(computer_inp):
            print(f"Your cards : {player_input}, Your score : {sum(player_input)}\n"
                  f"Computer's Final cards : {computer_inp}")
            print("Draw 😕")
            # flag = 1
        else:
            print(f"Your cards : {player_input}, Your score : {sum(player_input)}\n"
                  f"Computer's Final cards : {computer_inp}")
            print("You Lost 😓")
            # flag = 1
    else:
        flag = 1

