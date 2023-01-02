print("Welcome to Treasure Island. Your mission is to find the treasure.")

choice1 = input("You're at a crossroad. Where do you want to go? (Left or Right)")

if choice1 == "Left":
    choice2 = input(
        "You've come to a lake. There is an island in the middle of the lake. Type 'Wait' to wait for a boat. Type "
        "'Swim' to swim across.")
    if choice2 == "Wait":
        choice3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. "
            "Which colour do you choose?")
        if choice3 == "Red":
            print("It's a room full of fire. Game Over")
        elif choice3 == "Blue":
            print("You enter a room of beasts. Game Over.")
        elif choice3 == "Yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. GAME OVER!!")
