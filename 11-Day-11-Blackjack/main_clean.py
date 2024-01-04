# clean version with the help of the solution and copilot

import os
import random
from art import logo


def deal_card():
    """
    Function to randomly select and return a card from a deck of cards.
    
    Returns:
    int: A randomly selected card from the deck.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """
    Calculates the score of a hand of cards in a blackjack game.

    Parameters:
    cards (list): A list of integers representing the values of the cards in the hand.

    Returns:
    int: The calculated score of the hand.
    """
    score = sum(cards)

    # handle ace
    if (11 in cards) and score > 21:
        score -= 10
    # handle blackjack
    if len(cards) == 2 and score == 21:
        score = 0

    return score


def compare(user_score, computer_score):
    """
    Compare the scores of the user and the computer in a game of Blackjack.

    Args:
        user_score (int): The score of the user.
        computer_score (int): The score of the computer.

    Returns:
        str: The result of the comparison.
    """
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    elif user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    """
    Plays a game of Blackjack.
    """
    print(logo)
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    while user_score != 0 and user_score < 21:
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
        else:
            break

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


is_game_over = False

while not is_game_over:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        os.system('cls')
        play_game()
    else:
        is_game_over = True