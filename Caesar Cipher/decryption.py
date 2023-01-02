alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
            , 'w', 'x', 'y', 'z']


def decrypt(enc_text, shift):
    new_text = ""
    for i in enc_text:
        pos = alphabet.index(i)
        new_pos = (pos - shift)
        new_text += alphabet[new_pos]
    return new_text
