alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
            , 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    new_text = ""
    for i in text:
        pos = alphabet.index(i)
        new_pos = (pos + shift) % 26
        new_text += alphabet[new_pos]
    return new_text


