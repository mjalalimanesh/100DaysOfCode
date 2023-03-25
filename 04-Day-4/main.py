''' 
Randomisation and Python Lists
Play Rock, Paper, Scissors with Computer
'''
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ascii_art = [rock, paper, scissors]

user_choice = int(input("What you choose ? Type 0 for Rock, 1 for paper, or to for scissors.\n"))
computer_choice = random.randint(0, 2)


print("Your Choice:\n")
print(ascii_art[user_choice])
print("Computer Choice:\n")
print(ascii_art[computer_choice])


if user_choice == computer_choice:
    print("It's a draw")
elif user_choice == 0:
    if computer_choice == 2:
        print("You win!")
    else:
        print("You lose!")
elif user_choice == 1:
    if computer_choice == 0:
        print("You win!")
    else:
        print("You lose!")
elif user_choice == 2:
    if computer_choice == 1:
        print("You win!")
    else:
        print("You lose!")
