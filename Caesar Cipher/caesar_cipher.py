import logo
from caesar import caesar

print(logo.logo)
choice = ""
while choice != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    message = caesar(text, shift, direction)
    print(message)
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.")