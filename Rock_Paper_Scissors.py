import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_options = [rock, paper, scissors]


def game_rule(x, y):
    # x is your choice and y is computer's choice
    if x == y:
        print("Game Draw")
    elif x == 0 and y == 2:
        print("You Won!! 🥳")
    elif x == 1 and y == 0:
        print("You Won!! 🥳")
    elif x == 2 and y == 1:
        print("You Won!! 🥳")
    else:
        print("You Lost 😕")


flag = 0
while flag == 0:
    y_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))
    print(f"You chose :\n{game_options[y_choice]}")
    comp_choice = random.randint(0, 2)
    print(f"Computer chose :\n{game_options[comp_choice]}")
    game_rule(y_choice, comp_choice)
    esc = input("Do you want to play again? Type 'Y' for Yes and 'N' for No.")
    if esc == "Y":
        continue
    else:
        flag = 1

