"""
Blackjack Game
"""

import os
import random
from art import logo


def cls():
    ''' Clear Console'''
    os.system('cls' if os.name == 'nt' else 'clear')




cls()
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while play_game == 'y':
    cls()
    print(logo)
    # initialize
    your_cards = random.choices(cards, k=2)
    print(f"\tYour cards: {your_cards}, current score: {sum(your_cards)}")

    dealer_cards = random.choices(cards, k=2)
    print(f"\tComputer's first card: {dealer_cards[0]}")

    while sum(dealer_cards) < 17:
        dealer_cards.append(random.choice(cards))
        if (sum(dealer_cards) > 21) and (11 in dealer_cards):
            dealer_cards[dealer_cards.index(11)] = 1


    HIT = input("Type 'y' to get another card, type 'n' to pass: ")
    OVER = False

    while HIT == 'y':
        your_cards.append(random.choice(cards))

        if (sum(your_cards) > 21) and (11 in your_cards):
            your_cards[your_cards.index(11)] = 1

        if sum(your_cards) < 21:
            print(f"\tYour cards: {your_cards}, current score: {sum(your_cards)}")
            print(f"\tComputer's first card: {dealer_cards[0]}")
            HIT = input("Type 'y' to get another card, type 'n' to pass: ")
        else:
            HIT = 'n'

    if sum(your_cards) > 21:
        RESULT = "You went Over! You LOSE!"
    elif sum(dealer_cards) > 21:
        RESULT = "Computer went Over! You WIN!"
    elif sum(your_cards) > sum(dealer_cards):
        RESULT = "You win"
    elif sum(your_cards) == sum(dealer_cards):
        RESULT = "Draw"
    else:
        RESULT = "You lose"

    """ Print cards state on the table"""
    print(f"\tYour final hand: {your_cards}, final score: {sum(your_cards)}")
    print(f"\tComputer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
    print(RESULT)

    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

