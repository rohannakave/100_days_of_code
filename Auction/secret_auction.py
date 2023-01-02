import logo
from os import system

print("Welcome to secret auction program.")
print(logo.logo)

bid_dictionary = {}
flag = 0

while flag == 0:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bid_dictionary.update({name: bid})
    option = input("Are there any other bidders? Type 'yes' or 'no'. ")
    system("cls")
    if option == "no":
        flag = 1

max_bid = max(zip(bid_dictionary.values(), bid_dictionary.keys()))

print(f"The winner is {max_bid[1]} with a bid of ${max_bid[0]}")
