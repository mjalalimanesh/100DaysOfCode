'''
A Caesar cipher, rotation cipher or shift cipher is a simple substitution cipher where the cleartext is shifted a number of times up or down a known alphabet.
'''

from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amount):
    '''
    Encrypt plain_text by shifting alphabet by shift_amount
    '''
    encrypted = ''
    for letter in plain_text:
        ind = alphabet.index(letter) + shift_amount
        if ind >= len(alphabet):
            ind = ind - len(alphabet)
        encrypted = encrypted + alphabet[ind]
    print(f"the encoded text is {encrypted}")


def decrypt(plain_text, shift_amount):
    '''
    Decrypt plain_text by shifting alphabet by shift_amount in reverse 
    '''
    decrypted = ''
    for letter in plain_text:
        ind = alphabet.index(letter) - shift_amount
        decrypted = decrypted + alphabet[ind]
    print(f"the encoded text is {decrypted}")


# combine encrypt and decrypt to a single function
def caesar(plain_text, shift_amount, shift_direction):
    '''
    Encrypt and Decrypt plain_text by shifting alphabet by shift_amount
    '''
    modified_text = ''
    if shift_amount > 26:
        shift_amount = shift_amount % 26
    if shift_direction == 'decode':
        shift_amount = shift_amount * -1
    for letter in plain_text:
        if letter not in alphabet:
            modified_text = modified_text + letter
            continue
        ind = alphabet.index(letter) + shift_amount
        if ind >= len(alphabet):
            ind = ind - len(alphabet)
        modified_text = modified_text + alphabet[ind]
    print(f"the {shift_direction}d text is {modified_text}")


END_THE_GAME = 'no'
while END_THE_GAME == 'no':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    END_THE_GAME = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

print('Goodbye!')
