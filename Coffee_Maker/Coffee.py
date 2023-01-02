from resource import MENU, resources

resources['Money'] = 0


def check_resources(drink):
    """Check if resources available for ordered drink."""
    required_resources = MENU[drink]['ingredients']
    enough_resources = True
    for resource, amount in required_resources.items():
        if resources.get(resource, 0) < amount:
            enough_resources = False
            print(f"Sorry, There is not enough {resource} available.")
    return enough_resources


def update_resources(drink):
    """Update resources as per ordered drink"""
    required_resources = MENU[drink]['ingredients']
    resources['water'] -= required_resources['water']
    if drink != 'espresso':
        resources['milk'] -= required_resources['milk']
    resources['coffee'] -= required_resources['coffee']
    return


def payment(drink):
    """process payment for the drink"""
    coins = 0
    required_payment = float(MENU[drink]['cost'])
    print("Please insert coins.")
    q = int(input("how many quarters?: "))
    coins += q * 0.25
    d = int(input("how many dimes?: "))
    coins += d * 0.10
    n = int(input("how many nickles?: "))
    coins += n * 0.05
    p = int(input("how many pennies?: "))
    coins += p * 0.01
    if coins < required_payment:
        print("Sorry! Not enough coins. Money refunded")
    elif coins > required_payment:
        resources['Money'] += required_payment
        print(f"Here is your change ${round(coins - required_payment, 2)} and your {drink}. Enjoy!")
    else:
        resources['Money'] += required_payment
        print(f"Here is your {drink}. Enjoy!")


def coffee_maker(inp):
    # When the user enters “report” to the prompt, a report should be generated that shows the current resource values.
    if inp == 'report':
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${resources['Money']}")
    # Check if enough resources are available for the drink.
    else:
        resource_avail = check_resources(inp)
        if resource_avail:
            payment(inp)
            update_resources(inp)


is_machine_on = True
while is_machine_on:
    # Prompt user by asking “ What would you like? (espresso/latte/cappuccino)
    usr_inp = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # Turn off the Coffee Machine by entering “ off ” to the prompt.
    if usr_inp == 'off':
        break
    coffee_maker(usr_inp)
