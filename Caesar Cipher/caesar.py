alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
            , 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    new_text = ""
    for i in text:
        if i.isalpha():
            pos = alphabet.index(i)
            if direction == "encode":
                new_pos = (pos + shift) % 26
            elif direction == "decode":
                new_pos = (pos - shift)
            else:
                return "Please enter valid direction."
            new_text += alphabet[new_pos]
        else:
            new_text += i
    return new_text

