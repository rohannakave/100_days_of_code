def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


options = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

for keys in options:
    print(keys)

chosen_option = input("Pick an mathematical operation from above: ")
cal_function = options[chosen_option]
answer = cal_function(num1, num2)

print(f"{num1} {chosen_option} {num2} = {answer}")