'''
Hangman Game
'''

import random
import os
from hangman_art import logo, stages
from hangman_words import word_list

def cls():
    ''' Clear Console'''
    os.system('cls' if os.name=='nt' else 'clear')

print(logo)

LIVES = len(stages) - 1

# Choose a random word
chosen_word = random.choice(word_list)


# Create word placeholder to display
display = ['_'] * len(chosen_word)

END_OF_GAME  = False

while not END_OF_GAME:
    GUESS = (input('Guess a Letter: ')).lower()

    cls()

    # check if user entered same letter
    if GUESS in display:
        print(f"You've already guessed {GUESS}")

    # check guessed letter
    for i, letter in enumerate(chosen_word):
        if letter == GUESS:
            display[i] = GUESS

    # check if user is wrong
    if GUESS not in chosen_word:
        print(f'You guessed {GUESS}, That\'s not in the word. You lose a life')
        LIVES = LIVES - 1

    print(display)

    # check if game is ended
    if '_' not in display:
        print('You Won!')
        END_OF_GAME = True
    elif LIVES == 0:
        print('You Lost!')
        END_OF_GAME = True

    print(stages[LIVES])
