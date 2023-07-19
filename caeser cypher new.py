n = int(input())
s = input()

# create a list called alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# def the caesar func to encode s
def caesar(start_text, shift_length):
    # call end_text to print out the encoded text
    end_text = ''

    # let shift length is the remainder of shift length / 26 if it is too large
    shift_length = shift_length % 26
    # add spaces as it is not in alphabet
    for letter in start_text:
        if letter not in alphabet:
            end_text += letter
        else:
            # new position is the remainder as it can be higher than 26
            new_position = (shift_length + alphabet.index(letter)) % 26
            end_text += alphabet[new_position]
    print(end_text)

caesar(start_text=s, shift_length=n)